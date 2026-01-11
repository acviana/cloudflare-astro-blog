# acviana.com

Personal blog built with Astro and the AstroPaper theme, deployed on Cloudflare Pages.

**Live Site**: [acviana.com](https://acviana.com)

This is a minimal, responsive, accessible and SEO-friendly Astro blog featuring technical writing, LaTeX math support, and client-side search.

## About This Project

This blog uses the [AstroPaper theme](https://github.com/satnaing/astro-paper) with customizations for:
- Static site generation optimized for Cloudflare Pages
- LaTeX/KaTeX math rendering with custom color schemes
- Client-side fuzzy search
- Markdown blog posts with frontmatter

For detailed documentation about the architecture and development process, see:
- `agents.md` - Project structure, configuration, and deployment guide
- `worklog.md` - Development history and lessons learned

## 🔥 Features

- [x] type-safe markdown
- [x] super fast performance
- [x] accessible (Keyboard/VoiceOver)
- [x] responsive (mobile ~ desktops)
- [x] SEO-friendly
- [x] light & dark mode
- [x] fuzzy search
- [x] draft posts & pagination
- [x] sitemap & rss feed
- [x] followed best practices
- [x] highly customizable
- [x] dynamic OG image generation for blog posts [#15](https://github.com/satnaing/astro-paper/pull/15) ([Blog Post](https://astro-paper.pages.dev/posts/dynamic-og-image-generation-in-astropaper-blog-posts/))

_Note: I've tested screen-reader accessibility of AstroPaper using **VoiceOver** on Mac and **TalkBack** on Android. I couldn't test all other screen-readers out there. However, accessibility enhancements in AstroPaper should be working fine on others as well._

## 🚀 Project Structure

Inside of AstroPaper, you'll see the following folders and files:

```bash
/
├── public/
│   ├── assets/
|   ├── pagefind/ # auto-generated when build
│   └── favicon.svg
│   └── astropaper-og.jpg
│   └── favicon.svg
│   └── toggle-theme.js
├── src/
│   ├── assets/
│   │   └── icons/
│   │   └── images/
│   ├── components/
│   ├── data/
│   │   └── blog/
│   │       └── some-blog-posts.md
│   ├── layouts/
│   └── pages/
│   └── styles/
│   └── utils/
│   └── config.ts
│   └── constants.ts
│   └── content.config.ts
└── astro.config.ts
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

Any static assets, like images, can be placed in the `public/` directory.

All blog posts are stored in `src/data/blog` directory.

## 📖 Documentation

Documentation can be read in two formats\_ _markdown_ & _blog post_.

- Configuration - [markdown](src/data/blog/how-to-configure-astropaper-theme.md) | [blog post](https://astro-paper.pages.dev/posts/how-to-configure-astropaper-theme/)
- Add Posts - [markdown](src/data/blog/adding-new-post.md) | [blog post](https://astro-paper.pages.dev/posts/adding-new-posts-in-astropaper-theme/)
- Customize Color Schemes - [markdown](src/data/blog/customizing-astropaper-theme-color-schemes.md) | [blog post](https://astro-paper.pages.dev/posts/customizing-astropaper-theme-color-schemes/)
- Predefined Color Schemes - [markdown](src/data/blog/predefined-color-schemes.md) | [blog post](https://astro-paper.pages.dev/posts/predefined-color-schemes/)

## 💻 Tech Stack

**Main Framework** - [Astro 5.x](https://astro.build/) (Static Site Generation)  
**Type Checking** - [TypeScript](https://www.typescriptlang.org/)  
**Styling** - [TailwindCSS 4.x](https://tailwindcss.com/)  
**Math Rendering** - [KaTeX](https://katex.org/) via remark-math and rehype-katex  
**Search** - [FuseJS](https://fusejs.io/) (Client-side)  
**Icons** - [Tablers](https://tabler-icons.io/)  
**Deployment** - [Cloudflare Pages](https://pages.cloudflare.com/)  
**Code Formatting** - [Prettier](https://prettier.io/)  
**Linting** - [ESLint](https://eslint.org)

## 👨🏻‍💻 Development

### Local Development

```bash
# Install dependencies
npm install

# Start dev server at localhost:4321
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Deployment to Cloudflare Pages

```bash
# Build the site
npm run build

# Deploy to Cloudflare Pages
npx wrangler pages deploy dist --project-name=cloudflare-astro-blog --branch=main --commit-dirty=true
```

See `agents.md` for detailed deployment instructions including initial setup and custom domain configuration.

## Google Site Verification (optional)

You can easily add your [Google Site Verification HTML tag](https://support.google.com/webmasters/answer/9008080#meta_tag_verification&zippy=%2Chtml-tag) in AstroPaper using an environment variable. This step is optional. If you don't add the following environment variable, the google-site-verification tag won't appear in the HTML `<head>` section.

```bash
# in your environment variable file (.env)
PUBLIC_GOOGLE_SITE_VERIFICATION=your-google-site-verification-value
```

> See [this discussion](https://github.com/satnaing/astro-paper/discussions/334#discussioncomment-10139247) for adding AstroPaper to the Google Search Console.

## 🧞 Commands

All commands are run from the root of the project:

| Command              | Action                                              |
| :------------------- | :-------------------------------------------------- |
| `npm install`        | Installs dependencies                               |
| `npm run dev`        | Starts local dev server at `localhost:4321`         |
| `npm run build`      | Build production site to `./dist/`                  |
| `npm run preview`    | Preview build locally before deploying              |
| `npm run format`     | Format code with Prettier                           |
| `npm run sync`       | Generate TypeScript types for Astro modules         |
| `npm run lint`       | Lint with ESLint                                    |

## 📜 License

Licensed under the MIT License, Copyright © 2025

---

Built with the [AstroPaper theme](https://github.com/satnaing/astro-paper) by [Sat Naing](https://satnaing.dev).
