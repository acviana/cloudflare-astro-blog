# Worklog

This file tracks everything attempted during development - what worked and what didn't. Use dates as section headings in **reverse chronological order** (newest first).

## Saturday, January 10, 2026

### Remove Template Example Posts (23:54)

**Cleanup:**
- Deleted `src/data/blog/examples/` directory containing 4 template posts:
  - `example-draft-post.md`
  - `portfolio-website-development.md`
  - `tailwind-typography.md`
  - `terminal-development.md`
- These were part of the AstroPaper theme and not actual blog content

**Result:**
- Cleaner blog directory with only real posts
- Down to 81 actual blog posts (50 from GitHub, 31 from Tumblr)

### Migrate Tumblr Blog Posts (23:40)

**Feature Request:**
- Migrate all posts from old Tumblr blog (theothersideofthescreen-blog.tumblr.com) to Astro blog
- Include post dates, metadata, images, and proper formatting

**Implementation:**
- Created Python migration script `migrate_tumblr.py`:
  - Fetches all posts from Tumblr API with full metadata
  - Converts HTML to Markdown using html2text library
  - Downloads images to `public/assets/tumblr/{post-slug}/`
  - Creates markdown files with naming convention: `YYYY-MM-DD-title.md`
  - Generates proper frontmatter (author, pubDatetime, title, slug, tags, description, originalUrl)
- Installed required dependencies: `html2text` and `requests`
- Ran migration script to process all posts
- Added `tumblr-blog` tag to all 31 migrated posts for easy filtering

**Result:**
- ✅ Successfully migrated 31 posts from 2012 (April - September)
- ✅ All posts in `src/data/blog/` with proper YYYY-MM-DD-title.md naming
- ✅ Images downloaded to `public/assets/tumblr/`
- ✅ Each post includes link back to original Tumblr post
- ✅ All posts tagged with `tumblr-blog` for filtering
- Posts include technical content: Python, Django, astronomy work, academia

**Key Lesson:**
Using the Tumblr API directly is much better than trying to scrape HTML. The API provides proper metadata including timestamps, which can be decoded from post IDs. The html2text library works well for converting Tumblr's HTML to Markdown, though some formatting (like tables) may need manual cleanup.

### Add View Source Link to Footer (23:29)

**Feature Request:**
- Add a link to view the source code on GitHub from the main blog page

**Implementation:**
- Added `sourceCode` configuration to `src/config.ts`:
  - `enabled`: true/false toggle
  - `text`: "View Source"
  - `url`: GitHub repository URL
- Modified `src/components/Footer.astro` to display link after copyright
- Link opens in new tab with security attributes (`target="_blank" rel="noopener noreferrer"`)

**Result:**
- "View Source" link appears in footer: `Copyright © 2026 | All rights reserved. | View Source`
- Links to: https://github.com/acviana/cloudflare-astro-blog
- Appears on all pages site-wide

### Git Remote URL Update (23:26)

**Issue:**
- Git remote was pointing to old repository name `astro-cfworkers-blog`
- GitHub was showing redirect warnings on push

**Solution:**
- Updated remote URL: `git remote set-url origin git@github.com:acviana/cloudflare-astro-blog.git`
- Verified with `git fetch`

### Direct Links to Posts Page (23:25)

**Problem:**
- Even with instant redirect, clicking "Posts" link still triggered a redirect instead of directly loading the page
- Unnecessary redirect when all internal links could point directly to `/posts/page/1`

**Investigation:**
- Found two places linking to `/posts`:
  - `src/components/Header.astro` - Navigation menu "Posts" link
  - `src/pages/index.astro` - "All Posts" button on homepage

**Solution:**
- Updated both links to point directly to `/posts/page/1`
- Kept redirect in `astro.config.ts` as safety for external links/bookmarks
- Now navigation is direct with no redirect delay

**Result:**
- Internal navigation: Direct page load (no redirect)
- External/bookmarks to `/posts`: Instant redirect to `/posts/page/1`

### Posts Index Redirect Improvement (23:09)

**Problem:**
- `/posts` showed "Redirecting from /posts/ to /posts/page/1" message for 2 seconds before redirecting
- User reported seeing the redirect message which felt like a hack

**Investigation:**
- Checked Astro routing documentation (https://docs.astro.build/en/guides/routing/#redirects)
- Original implementation used `return Astro.redirect()` in `/posts/index.astro`
- For static builds, Astro generates HTML files with meta refresh tags by default
- The 2-second delay (`content="2;url=..."`) was Astro's default for dynamic redirects

**What Didn't Work:**
- Dynamic redirect with `Astro.redirect()` in page file - causes visible redirect message with delay

**Solution That Worked:**
- Removed `src/pages/posts/index.astro` file
- Added configured redirect in `astro.config.ts`: `redirects: { "/posts": "/posts/page/1" }`
- Configured redirects use instant redirect (`content="0;url=..."`) instead of 2-second delay
- This is the **standard Astro pattern** for static site redirects, not a hack

**Key Lesson:**
For static sites, use configured redirects in `astro.config.ts` instead of dynamic `Astro.redirect()` calls. Configured redirects are instant and cleaner. The meta refresh HTML is standard for static sites - when deployed to production, Cloudflare Pages may handle these differently with proper 301/302 responses.

### Worklog Creation
- Created this worklog.md file to track development context
- Updated agents.md with documentation for agents on how to use worklog
- Purpose: Help rebuild context efficiently in future sessions

### Current Deployment
- Build command: `npm run build`
- Deploy command: `npx wrangler pages deploy dist --project-name=cloudflare-astro-blog --branch=main --commit-dirty=true`
- Live URL: https://cloudflare-astro-blog.pages.dev

### Route Structure
- Pagination route: `/posts/page/[page]` (not `/posts/[page]`)
- Reason: Prevents route collisions with individual post slugs
- All dynamic routes require `getStaticPaths()` in static mode

### Documentation Enhancement (06:27)
- Created comprehensive `agents.md` file documenting:
  - Project structure and architecture
  - Static vs SSR decision and rationale
  - Routing patterns and pagination structure
  - LaTeX support implementation
  - Search functionality (client-side)
  - Deployment procedures
  - Links to official documentation
  - Troubleshooting guide

**Why This Matters:**
During initial setup, we configured for SSR based on assumptions, leading to 500 errors. The documentation now emphasizes checking official docs first to avoid similar issues.

### SSR to Static Site Migration (01:09)

**Problem Encountered:**
- Initial SSR configuration (`output: "server"`) with Cloudflare adapter caused 500 errors in production
- Root cause: Large content collection bundles (924KB) exceeded Cloudflare Workers limits
- Missing Node.js compatibility configuration

**What Didn't Work:**
- SSR mode with Cloudflare adapter for blog with many posts
- Large content collections in Workers runtime
- Attempting to deploy without proper nodejs_compat flags

**Solution That Worked:**
- Switched to static site generation (`output: "static"`)
- Removed Cloudflare adapter (not needed for static builds)
- Added `getStaticPaths()` to all dynamic routes:
  - `/posts/[slug].astro`
  - `/posts/page/[page].astro`
  - `/tags/[tag]/[...page].astro`
- Created `wrangler.toml` with:
  - `nodejs_compat` compatibility flag (for future SSR if needed)
  - SESSION KV namespace binding
  - Project configuration for Cloudflare Pages
- Added Vite SSR externals for Node.js modules in `astro.config.ts`

**Key Lesson:**
Static site generation is the recommended approach for blogs on Cloudflare Pages. Consult official Cloudflare and Astro documentation before choosing SSR vs static - assumptions can lead to deployment issues.

### Project Initialization (00:24)
- Created initial Astro blog project using Astro Paper template
- Set up for Cloudflare Pages deployment
- Configured Tailwind CSS 4.x
- Created blog content structure in `src/data/blog/`
