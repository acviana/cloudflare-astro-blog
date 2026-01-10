# Cloudflare Astro Blog

This is an Astro blog using the Astro Paper template, configured for deployment to Cloudflare Workers (SSR mode).

## Project Structure

- **Framework**: Astro 5.x with SSR (Server-Side Rendering)
- **Template**: Astro Paper theme
- **Deployment**: Cloudflare Workers via `@astrojs/cloudflare` adapter
- **Styling**: Tailwind CSS 4.x
- **Content**: Markdown blog posts in `src/data/blog/`

## Key Configuration

### Content Collections
- Blog posts are stored in `src/data/blog/*.md`
- Schema defined in `src/content.config.ts`
- Posts require: `author`, `pubDatetime`, `title`, `slug`, `draft`, `tags`, `description`

### Routing (SSR Mode)
- Individual posts: `/posts/[slug].astro` → `/posts/{slug}`
- Paginated list: `/posts/page/[page].astro` → `/posts/page/1`, `/posts/page/2`, etc.
- Posts index: `/posts/index.astro` → redirects to `/posts/page/1`
- Tags: `/tags/[tag]/[...page].astro` → `/tags/{tag}/1`, `/tags/{tag}/2`, etc.

**Important**: The pagination route is at `/posts/page/[page]` (not `/posts/[page]`) to avoid route collisions with post slugs.

### LaTeX Support
- Uses `remark-math` and `rehype-katex`
- KaTeX CSS loaded from CDN in `src/layouts/Layout.astro`
- Custom color overrides in `src/styles/global.css` for better readability

### Search
- Client-side search at `/search`
- Filters posts by title and tags using data attributes
- No build-time indexing (Pagefind removed for SSR compatibility)

## Important Notes

### SSR vs Static
This project uses SSR mode (`output: "server"`), which means:
- Pages are rendered on-demand, not pre-built
- `getStaticPaths()` is not used in dynamic routes
- Pagination and post routing is handled dynamically at runtime

### Cloudflare Workers Limitations
- No dynamic OG image generation (requires Node.js native modules)
- No sharp for image optimization at runtime
- `imageService: "noop"` configured in `astro.config.ts`

### Frontmatter Format
Posts migrated from Next.js blog use this frontmatter:
```yaml
---
author: acv
pubDatetime: 2024-01-01T00:00:00.000Z
title: Post Title
slug: 2024-01-01-post-title
draft: false
tags:
  - tag1
  - tag2
description: Post description
---
```

## Development

```bash
npm run dev    # Start dev server
npm run build  # Build for production
npm run preview # Preview production build
```

## Deployment

Deploy to Cloudflare Workers:
```bash
wrangler login
wrangler deploy
```

## Recent Changes

1. **Route Structure**: Moved pagination from `/posts/[page]` to `/posts/page/[page]` to prevent route collisions
2. **Search**: Implemented client-side search replacing Pagefind
3. **LaTeX**: Added color overrides for better visibility
4. **SSR Conversion**: Converted all dynamic routes from static to SSR mode
5. **Card Component**: Updated to pass through data attributes for search functionality

## Configuration Files

- `astro.config.ts` - Astro configuration with Cloudflare adapter
- `src/content.config.ts` - Content collection schema
- `src/config.ts` - Site configuration (SITE object)
- `src/styles/global.css` - Global styles including KaTeX overrides
- `transform-frontmatter.js` - Script used for migrating blog posts (one-time use)
