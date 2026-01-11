# Cloudflare Astro Blog

This is an Astro blog using the Astro Paper template, configured for deployment to Cloudflare Pages as a static site.

## Project Structure

- **Framework**: Astro 5.x with static site generation
- **Template**: Astro Paper theme
- **Deployment**: Cloudflare Pages (static)
- **Styling**: Tailwind CSS 4.x
- **Content**: Markdown blog posts in `src/data/blog/`

## Key Configuration

### Content Collections
- Blog posts are stored in `src/data/blog/*.md`
- Schema defined in `src/content.config.ts`
- Posts require: `author`, `pubDatetime`, `title`, `slug`, `draft`, `tags`, `description`

### Routing (Static Mode)
- Individual posts: `/posts/[slug].astro` → `/posts/{slug}` (uses `getStaticPaths()`)
- Paginated list: `/posts/page/[page].astro` → `/posts/page/1`, `/posts/page/2`, etc. (uses `getStaticPaths()`)
- Posts index: `/posts` → instant redirect to `/posts/page/1` (configured in `astro.config.ts`)
- Tags: `/tags/[tag]/[...page].astro` → `/tags/{tag}/1`, `/tags/{tag}/2`, etc. (uses `getStaticPaths()`)

**Important**: 
- The pagination route is at `/posts/page/[page]` (not `/posts/[page]`) to avoid route collisions with post slugs
- All dynamic routes require `getStaticPaths()` for static builds
- Redirects use configured redirects in `astro.config.ts` for instant, standard behavior

### LaTeX Support
- Uses `remark-math` and `rehype-katex`
- KaTeX CSS loaded from CDN in `src/layouts/Layout.astro`
- Custom color overrides in `src/styles/global.css` for better readability

### Search
- Client-side search at `/search`
- Filters posts by title and tags using data attributes
- No build-time indexing (Pagefind removed for SSR compatibility)

## Important Notes

### Static Site Generation
This project uses static site generation (`output: "static"`), which means:
- All pages are pre-built at build time
- All dynamic routes require `getStaticPaths()` functions
- No server-side rendering or Workers required

### Why Static Instead of SSR?
Initially configured for SSR with Cloudflare Workers, but switched to static because:
- Simpler deployment (no Workers runtime configuration needed)
- Better performance (pre-built HTML)
- No need for `nodejs_compat` flag or Node.js module handling
- Blog content doesn't require on-demand rendering
- Avoids Worker bundle size limits with large content collections

### Cloudflare Pages Configuration
- `wrangler.toml` includes `nodejs_compat` flag and SESSION KV binding (for future SSR if needed)
- Currently deployed as static site, so these settings are not actively used
- `astro.config.ts` includes Vite SSR externals for Node.js modules (not used in static mode)

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

### Initial Setup
```bash
# Login to Cloudflare (interactive OAuth)
npx wrangler login

# Create the Pages project (one-time)
npx wrangler pages project create cloudflare-astro-blog --production-branch=main

# Optional: Create SESSION KV namespace for future SSR features
npx wrangler kv namespace create "SESSION"
```

### Deploy to Cloudflare Pages
```bash
# Build the site
npm run build

# Deploy to Cloudflare Pages
npx wrangler pages deploy dist --project-name=cloudflare-astro-blog --branch=main --commit-dirty=true
```

### Wrangler Configuration
The `wrangler.toml` file includes:
- `nodejs_compat` compatibility flag (for future SSR support)
- SESSION KV namespace binding (not used in static mode)
- Project name and compatibility date

### Custom Domain Setup
1. Add custom domain in Cloudflare dashboard: Workers & Pages → cloudflare-astro-blog → Custom domains
2. Update DNS records at your domain registrar to point to Cloudflare Pages
3. Remove domain from previous hosting provider (e.g., Vercel)

Current deployment: https://cloudflare-astro-blog.pages.dev

## Documentation for Agents

### Required Workflow Rules

**CRITICAL**: Follow these rules for ALL changes to the project:

1. **Always Update Worklog**:
   - Update `worklog.md` for every significant change, feature, or fix
   - Add entries at the TOP (reverse chronological order)
   - Include problem, investigation, solution, and results

2. **Always Ask Before Committing**:
   - NEVER commit without explicit user approval
   - Show what files changed and summarize the changes
   - Ask: "Should I commit these changes?"

3. **Always Ask About Documentation**:
   - Before committing, ask: "Should I update the worklog and agents.md file?"
   - Even if you think it's obvious, ask first

4. **Always Ask Before Deploying**:
   - NEVER run `npm run build` or `wrangler pages deploy` without user approval
   - Ask: "Should I deploy to Cloudflare Pages?"
   - Wait for explicit confirmation

### Worklog
The `worklog.md` file contains a **reverse chronological** log of development work (newest entries first):
- **Purpose**: Track what was tried, what worked, and what didn't work
- **Format**: Organized by date (section headings in reverse chronological order), with subsections for different features/issues
- **Usage**: Agents should **prepend** new entries to the top of each date section when:
  - Attempting new approaches or solutions
  - Discovering bugs and their fixes
  - Encountering blockers or limitations
  - Making configuration changes
  - Learning lessons that would help future context rebuilding
- **Detail Level**: Include enough context to understand the problem and solution, but avoid sensitive data
- **Public**: Assume this file is publicly visible - no API keys, SSH keys, or credentials
- **Important**: Add new entries at the TOP (most recent first) so the latest work is immediately visible

### Context Rebuilding
When resuming work on this project, read:
1. This `agents.md` file for project overview and architecture
2. `worklog.md` for recent development history and lessons learned
3. Relevant source files based on the task at hand

## Recent Changes

1. **Cloudflare Pages Deployment**: Configured for static site generation and deployed to Cloudflare Pages
2. **Static Site Mode**: Switched from SSR (`output: "server"`) to static (`output: "static"`)
3. **Dynamic Routes**: Added `getStaticPaths()` to all dynamic routes for static builds
4. **Wrangler Setup**: Created `wrangler.toml` with Pages configuration and KV namespace
5. **Route Structure**: Pagination at `/posts/page/[page]` to prevent route collisions
6. **Search**: Client-side search implementation
7. **LaTeX**: Added color overrides for better visibility
8. **Card Component**: Updated to pass through data attributes for search functionality
9. **Worklog**: Created `worklog.md` for tracking development attempts and solutions
10. **Redirects**: Using configured redirects in `astro.config.ts` for instant, standard behavior (not file-based redirects)

## Configuration Files

- `astro.config.ts` - Astro configuration (static mode, configured redirects, Vite SSR externals for future SSR)
- `wrangler.toml` - Cloudflare Pages configuration with nodejs_compat flag and KV binding
- `src/content.config.ts` - Content collection schema
- `src/config.ts` - Site configuration (SITE object)
- `src/styles/global.css` - Global styles including KaTeX overrides
- `transform-frontmatter.js` - Script used for migrating blog posts (one-time use)
- `worklog.md` - Development log tracking what was tried (successful and failed attempts)

## Documentation References

**IMPORTANT**: Before making major changes to deployment configuration, routing, or framework setup, always consult the official documentation:

### Official Documentation
- **Cloudflare Pages**: https://developers.cloudflare.com/pages/
  - Framework guide for Astro: https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/
  - Functions configuration: https://developers.cloudflare.com/pages/functions/wrangler-configuration/
  - Node.js compatibility: https://developers.cloudflare.com/workers/runtime-apis/nodejs/

- **Astro**: https://docs.astro.build/
  - Cloudflare adapter: https://docs.astro.build/en/guides/integrations-guide/cloudflare/
  - Deployment guide: https://docs.astro.build/en/guides/deploy/cloudflare/
  - Static vs SSR: https://docs.astro.build/en/guides/on-demand-rendering/

- **Astro Paper Theme**: https://github.com/satnaing/astro-paper
  - Theme documentation and customization guide

### Why This Matters
During this project's setup, we initially configured for SSR mode based on assumptions, which led to 500 errors due to:
- Large content collection bundles exceeding Worker limits
- Missing Node.js compatibility configuration
- Incorrect understanding of Cloudflare Pages vs Workers deployment

Checking the official Cloudflare and Astro documentation revealed that **static site generation** is the recommended approach for blogs on Cloudflare Pages, avoiding these issues entirely.

## Troubleshooting

### If switching back to SSR mode
If you need to switch back to SSR (`output: "server"`):
1. Uncomment the Cloudflare adapter in `astro.config.ts`
2. Remove `getStaticPaths()` from dynamic routes (they'll use on-demand rendering)
3. Ensure `wrangler.toml` has `nodejs_compat` flag and `pages_build_output_dir = "./dist"`
4. Deploy with `npx wrangler pages deploy dist`

Note: SSR mode had issues with large content collections (924KB bundle) causing 500 errors on Cloudflare Workers.

### Common Issues
- **500 errors on Cloudflare**: Usually means Worker bundle too large or missing Node.js compatibility
- **Missing pages after deploy**: Check that `getStaticPaths()` returns all required paths
- **Build errors**: Ensure all dynamic routes have `getStaticPaths()` in static mode
