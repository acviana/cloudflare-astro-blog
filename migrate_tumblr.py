#!/usr/bin/env python3
"""
Migrate Tumblr posts to Astro blog format.

This script:
1. Fetches all posts from Tumblr API
2. Downloads images to public/assets/tumblr/
3. Converts HTML to Markdown
4. Creates markdown files with YYYY-MM-DD-title.md naming
5. Adds proper frontmatter
"""

import requests
import json
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import html2text

# Configuration
TUMBLR_BLOG = "theothersideofthescreen-blog.tumblr.com"
TUMBLR_API_KEY = "fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
OUTPUT_DIR = Path("src/data/blog")
IMAGES_DIR = Path("public/assets/tumblr")

# Create directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Setup HTML to Markdown converter
h2t = html2text.HTML2Text()
h2t.body_width = 0  # Don't wrap lines
h2t.ignore_links = False
h2t.ignore_images = False


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text.strip("-")


def download_image(url, post_slug):
    """Download image and return local path."""
    try:
        # Parse URL to get filename
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)

        # Create post-specific directory
        post_image_dir = IMAGES_DIR / post_slug
        post_image_dir.mkdir(parents=True, exist_ok=True)

        # Download image
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Save image
        image_path = post_image_dir / filename
        with open(image_path, "wb") as f:
            f.write(response.content)

        # Return path relative to public/
        return f"/assets/tumblr/{post_slug}/{filename}"
    except Exception as e:
        print(f"  Warning: Failed to download image {url}: {e}")
        return url  # Return original URL if download fails


def process_content(content, post_slug):
    """Convert HTML to Markdown and download images."""
    if not content:
        return ""

    # Download images and replace URLs
    img_pattern = r'<img[^>]+src="([^"]+)"[^>]*>'
    images = re.findall(img_pattern, content)

    for img_url in images:
        if img_url.startswith("http"):
            local_path = download_image(img_url, post_slug)
            content = content.replace(img_url, local_path)

    # Convert HTML to Markdown
    markdown = h2t.handle(content)

    # Clean up excessive newlines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    return markdown.strip()


def extract_tags(post):
    """Extract tags from post."""
    tags = post.get("tags", [])
    # Add post type as a tag if not already present
    post_type = post.get("type", "")
    if post_type and post_type not in tags:
        tags.append(post_type)
    return tags


def create_markdown_file(post):
    """Create markdown file for a single post."""
    # Get post metadata
    post_id = post.get("id")
    timestamp = post.get("timestamp")
    post_type = post.get("type", "text")
    slug = post.get("slug", "")
    title = post.get("title", post.get("summary", f"Post {post_id}"))

    # Convert timestamp to datetime
    dt = datetime.fromtimestamp(timestamp)
    date_str = dt.strftime("%Y-%m-%d")

    # Create filename slug
    file_slug = slugify(slug or title)
    if not file_slug:
        file_slug = f"post-{post_id}"

    filename = f"{date_str}-{file_slug}.md"
    filepath = OUTPUT_DIR / filename

    # Skip if file already exists
    if filepath.exists():
        print(f"  Skipping {filename} (already exists)")
        return

    print(f"  Creating {filename}")

    # Extract content based on post type
    content = ""
    if post_type == "text":
        content = post.get("body", "")
    elif post_type == "photo":
        # Get caption
        content = post.get("caption", "")
        # Add photos
        photos = post.get("photos", [])
        for photo in photos:
            original_size = photo.get("original_size", {})
            photo_url = original_size.get("url", "")
            if photo_url:
                local_path = download_image(photo_url, file_slug)
                content = f"![Photo]({local_path})\n\n" + content
    elif post_type == "link":
        url = post.get("url", "")
        description = post.get("description", "")
        content = f"[{title}]({url})\n\n{description}"
    elif post_type == "quote":
        text = post.get("text", "")
        source = post.get("source", "")
        content = f"> {text}\n\n{source}"
    else:
        # Fallback to any available body content
        content = post.get("body", post.get("caption", post.get("description", "")))

    # Process content (convert to markdown, download images)
    markdown_content = process_content(content, file_slug)

    # Get tags
    tags = extract_tags(post)

    # Get post URL
    post_url = post.get("post_url", "")

    # Create frontmatter
    title_escaped = title.replace('"', '\\"')
    desc_text = post.get("summary", title)[:200]
    desc_escaped = desc_text.replace('"', '\\"')
    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    frontmatter = f"""---
author: acv
pubDatetime: {dt.isoformat()}
title: "{title_escaped}"
slug: {file_slug}
featured: false
draft: false
tags:
{tags_yaml}
description: "{desc_escaped}"
originalUrl: {post_url}
---

"""

    # Write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(markdown_content)


def fetch_all_posts():
    """Fetch all posts from Tumblr API."""
    base_url = f"https://api.tumblr.com/v2/blog/{TUMBLR_BLOG}/posts"
    all_posts = []
    offset = 0
    limit = 20

    print(f"Fetching posts from {TUMBLR_BLOG}...")

    while True:
        params = {
            "api_key": TUMBLR_API_KEY,
            "limit": limit,
            "offset": offset,
            "npf": "false",  # Use legacy format for easier parsing
        }

        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        posts = data.get("response", {}).get("posts", [])

        if not posts:
            break

        all_posts.extend(posts)
        print(f"  Fetched {len(all_posts)} posts so far...")

        offset += limit

    print(f"Total posts fetched: {len(all_posts)}")
    return all_posts


def main():
    """Main migration function."""
    print("Starting Tumblr migration...")
    print()

    # Fetch all posts
    posts = fetch_all_posts()
    print()

    # Process each post
    print("Creating markdown files...")
    for i, post in enumerate(posts, 1):
        print(f"[{i}/{len(posts)}]", end=" ")
        try:
            create_markdown_file(post)
        except Exception as e:
            post_id = post.get("id", "unknown")
            print(f"  ERROR: Failed to process post {post_id}: {e}")

    print()
    print("Migration complete!")
    print(f"  Created files in: {OUTPUT_DIR}")
    print(f"  Downloaded images to: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
