# Rocky Top Rock Website

This repository contains the static HTML and CSS files for the **Rocky Top Rock** website.  
The site is designed to generate leads for rock, gravel and dump‑truck delivery services, using a rugged yet approachable brand style.  
It includes a homepage and dedicated landing pages for rock &amp; aggregate supply, dump‑truck delivery, and landscaping services.

## Features

- **Mobile‑first responsive layout** using HTML5 and CSS3.
- **Consistent brand colors** (orange, charcoal, stone gray and white) and typography.
- **Optimized logo** and images for faster load times.
- **Clear calls‑to‑action** on every page to encourage inquiries.
- **Semantic markup** with descriptive meta tags for better SEO and accessibility.

## Structure

The project is organized as follows:

- `index.html` – Homepage with hero section, services overview, trust indicators, testimonials, and call‑to‑action.
- `rock-aggregate.html` – Landing page for rock &amp; aggregate supply.
- `dump-truck-delivery.html` – Landing page for dump‑truck delivery service.
- `landscaping.html` – Landing page for landscaping and property projects.
- `style.css` – Shared styles across all pages.
- `assets/` – Contains the Rocky Top Rock logo assets. `logo.png` is the original multi‑variant logo pack, `logo_small.png` is a downscaled version of that pack, and `logo_header.png` is a cropped single horizontal logo used in the site header.

## Deployment

This is a static site with no build step. It can be hosted on any static file server.
To deploy on **Vercel**, select **Import Project**, choose this repository and deploy with the **Static** preset.  
The default branch is **main**, and the site will be available at your Vercel‑generated URL.

## Font privacy

Montserrat is served from `assets/fonts/` on this site's own origin. All six HTML
entry points use the same local stylesheet. The original four weights (400, 500,
600 and 700), five language subsets and `font-display: swap` are unchanged.
The WOFF2 files are the unmodified Montserrat v31 assets used by the previous
stylesheet. No font service is contacted by the visitor or during deployment.

The SIL Open Font License and copyright notices are included in
`assets/fonts/OFL.txt`. Upstream: https://github.com/google/fonts/tree/main/ofl/montserrat.

Run the offline font regression checks with `python -m unittest discover -s tests`.
These checks cover font delivery, not overall privacy-law compliance or unrelated
services such as analytics, contact forms or embedded content.
