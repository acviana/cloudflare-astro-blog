# Worklog

This file tracks everything attempted during development - what worked and what didn't. Use dates as section headings.

## Saturday, January 10, 2026

### Project Initialization (00:24)
- Created initial Astro blog project using Astro Paper template
- Set up for Cloudflare Pages deployment
- Configured Tailwind CSS 4.x
- Created blog content structure in `src/data/blog/`

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

### Route Structure
- Pagination route: `/posts/page/[page]` (not `/posts/[page]`)
- Reason: Prevents route collisions with individual post slugs
- All dynamic routes require `getStaticPaths()` in static mode

### Current Deployment
- Build command: `npm run build`
- Deploy command: `npx wrangler pages deploy dist --project-name=cloudflare-astro-blog --branch=main --commit-dirty=true`
- Live URL: https://cloudflare-astro-blog.pages.dev

### Worklog Creation
- Created this worklog.md file to track development context
- Updated agents.md with documentation for agents on how to use worklog
- Purpose: Help rebuild context efficiently in future sessions

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
