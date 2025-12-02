CardSnark.cc 💳
> "Stop Being a Sucker."
> The only credit card site that isn't boring as hell. We read the fine print so you don't have to.
> 
🚀 Project Overview
This is a static site built with Jekyll and styled with Tailwind CSS.
Unlike traditional Jekyll themes (like Minima), this project uses a custom "Design Engine" built on the Tailwind CDN, making it lightweight, responsive, and incredibly easy to edit.
Live Site: https://cardsnark.cc
🛠️ Tech Stack
 * Core: Jekyll 4.x
 * Styling: Tailwind CSS (via CDN - no build step required)
 * Icons: Heroicons (SVGs)
 * Fonts: Inter (Body) & Merriweather (Headers)
 * SEO: Jekyll SEO Tag & Sitemap plugins
⚡ Quick Start (Local Development)
1. Prerequisites
You need Ruby and Bundler installed on your machine.
2. Install Dependencies
Run this command in the root folder to install Jekyll and the plugins:
bundle install

3. Run the Server
Start the local server to preview your site:
bundle exec jekyll serve

Your site will be live at: http://localhost:4000
📂 Project Structure
_layouts/
 * default.html: The master template. Loads Tailwind, Fonts, and Analytics.
 * post.html: The blog post template. Includes "Prose" styling for readability and the "Related Posts" grid.
 * page.html: For static pages (About, Privacy, Terms).
_includes/
 * header.html: The responsive Mega Menu navigation.
 * footer.html: The dark-mode footer with the Beehiiv newsletter integration.
 * card-comparison.html: The reusable table component for comparing credit cards.
 * social-share.html: The floating share buttons (Twitter, Facebook, Reddit).
_posts/
 * Contains all reviews and articles.
 * Naming Convention: YYYY-MM-DD-title.md
assets/
 * images/: Stores all card images and logos.
 * css/style.scss: (Empty) kept only to prevent Jekyll 404 errors. All real styling is handled by Tailwind classes in HTML.
🔧 Utility Scripts
fix_posts.py
A Python script included in the root folder. Run this if your YAML Front Matter gets messy (e.g., double quotes or duplicate categories).
python fix_posts.py

🚀 Deployment
This site is configured for GitHub Pages.
 * Push your changes to the main branch.
 * GitHub Actions will automatically build and deploy the site.
 * The _config.yml file handles the Sitemap generation automatically.
📝 License
© CardSnark. All rights reserved.
Not financial advice. Just common sense.
