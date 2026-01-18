# Jekyll-TeXt Theme Guide

This document provides layout and design guidelines for working with the jekyll-TeXt-theme (from `sweeden-ttu/jekyll-TeXt-theme`) in this site.

## Theme Configuration

The theme is configured in `_config.yml` using `remote_theme`:

```yaml
remote_theme: sweeden-ttu/jekyll-TeXt-theme
text_skin: default
highlight_theme: tomorrow
```

### Available Skins

The `text_skin` setting controls the overall color scheme. Available options:
- `default` - Light theme with blue accents (currently used)
- `dark` - Dark theme with good contrast
- `forest` - Green-tinted theme
- `ocean` - Blue-tinted theme
- `chocolate` - Brown/warm theme
- `orange` - Orange-tinted theme

### Oracle-Inspired Color Scheme

The site uses an **Oracle-inspired color palette** for visual design:

#### Primary Colors
- **Oracle Red**: `#F80000` - Primary accent color, hero backgrounds, CTAs
- **Black**: `#000000` - Primary backgrounds, text on light sections
- **White**: `#FFFFFF` - Primary text on dark backgrounds, light section backgrounds

#### Secondary Colors
- **Dark Gray**: `#333333` - Alternate section backgrounds
- **Medium Gray**: `#666666` - Secondary text and accents
- **Light Gray**: `#CCCCCC` - Subtle backgrounds
- **Very Light Gray**: `#F5F5F5` - Light section backgrounds

#### Social Media Colors
- **Facebook Blue**: `#1877F2` - Facebook button
- **Instagram Gradient**: `#E4405F` (primary), `#C13584` (hover), `#A52C6A` (active)
- **LinkedIn Blue**: `#0077B5` - LinkedIn button
- **GitHub Dark**: `#24292E` - GitHub button

#### Usage Guidelines

**Oracle Red (`#F80000`):**
- Use for hero section backgrounds
- Primary call-to-action buttons
- Key highlights and accents
- Navigation active states
- Important alerts and notifications

**Black (`#000000`):**
- Dark section backgrounds
- Primary text on light backgrounds
- High-contrast elements
- Footer backgrounds (optional)

**White (`#FFFFFF`):**
- Primary text on Oracle Red or Black backgrounds
- Light section backgrounds
- Cards and containers
- Navigation text on dark backgrounds

**Grays:**
- Use for subtle backgrounds (`#F5F5F5`, `#CCCCCC`)
- Secondary text and metadata (`#666666`)
- Section alternation (`#333333`)

#### Color Application Examples

```yaml
# Hero Section (index.html)
article_header:
  theme: dark
  background_color: "#F80000"  # Oracle Red

# Dark Section
- theme: dark
  background_color: "#000000"  # Black

# Light Section
- theme: light
  background_color: "#F5F5F5"  # Very Light Gray
```

#### Custom CSS Variables

Oracle colors are defined in `assets/css/custom.scss`:
```scss
$oracle-red: #F80000;
$oracle-black: #000000;
$oracle-white: #FFFFFF;
$oracle-gray: #333333;
```

These can be referenced in custom stylesheets.

### Code Highlighting Themes

The `highlight_theme` setting controls syntax highlighting for code blocks:
- `default` - Default highlighting
- `tomorrow` - Tomorrow theme (currently used)
- `tomorrow-night` - Dark tomorrow theme
- `tomorrow-night-eighties` - Retro dark theme
- `tomorrow-night-blue` - Blue-tinted dark theme
- `tomorrow-night-bright` - Bright dark theme

## Page Layouts

### Home Page (`layout: home`)

The home/landing page should use `layout: home`. This layout:
- Displays site title and description
- Shows featured content or posts
- Provides navigation to main sections

**Example front matter:**
```yaml
---
layout: home
title: Spring 2026 Coursework
permalink: /
---
```

**Location:** `_pages/index.md` (with `permalink: /`)

### Standard Pages (`layout: page`)

Regular content pages use `layout: page`:
- Clean, readable layout
- Sidebar navigation (if configured)
- Breadcrumbs

**Example front matter:**
```yaml
---
layout: page
title: Courses
permalink: /courses/
---
```

**Location:** `_pages/*.md` files

### Post Layout (`layout: post`)

For blog posts or lecture notes using the `_posts/` directory:
- Date and metadata display
- Author information
- Comments and sharing (if enabled)

**Example front matter:**
```yaml
---
layout: post
title: "Lecture 1: Introduction"
date: 2026-01-15
categories: [lectures, software-verification]
tags: [introduction, testing]
---
```

**Naming convention:** `YYYY-MM-DD-title.md` in `_posts/` directory

### Course Layout (`layout: course`)

Custom layout for course pages (preserved from original site structure):
- Course-specific metadata
- Lecture listings
- Course materials

**Example front matter:**
```yaml
---
layout: course
title: "Software Verification and Validation"
permalink: /courses/software-verification/
---
```

## Directory Structure

```
spring-2026/
├── _config.yml              # Theme configuration
├── _pages/                  # Site pages (index, courses, etc.)
│   ├── index.md            # Home page (layout: home)
│   └── courses.md          # Courses listing (layout: page)
├── _posts/                  # Blog posts/lectures (optional)
│   └── YYYY-MM-DD-title.md
├── _layouts/                # Custom layouts (override theme)
│   └── course.html          # Custom course layout
├── _includes/               # Reusable components (override theme)
├── assets/                  # Static assets (CSS, images, JS)
│   └── css/
│       └── main.css
└── [course-name]/           # Course directories
    ├── _data/              # Course YAML data
    └── _lectures/          # Lecture materials
```

## Design Guidelines

### 1. Typography & Spacing

- The theme provides consistent typography using a carefully designed font stack
- Headings use proper hierarchy (H1 → H6)
- Paragraph spacing is handled by the theme automatically
- Use standard Markdown for formatting

### 2. Code Blocks

Code blocks automatically use the `highlight_theme` from `_config.yml`:

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

For inline code, use single backticks: `code`

### 3. Images

Place images in `assets/images/` and reference them:

```markdown
![Alt text](/assets/images/example.png)
```

Or use relative paths:
```markdown
![Alt text]({{ '/assets/images/example.png' | relative_url }})
```

### 4. Navigation

Navigation is configured in `_config.yml` via `nav_lists`:

```yaml
nav_lists:
  - title: Home
    url: /
  - title: Courses
    url: /courses/
```

The theme will automatically generate navigation menus from this configuration.

### 5. Front Matter Best Practices

Always include at minimum:
- `layout` - Which layout to use
- `title` - Page title

Optional but recommended:
- `permalink` - Custom URL (useful for pages in `_pages/`)
- `description` - Meta description
- `date` - For posts, controls sorting

Example:
```yaml
---
layout: page
title: "My Page Title"
permalink: /my-page/
description: "A description of this page"
---
```

### 6. Math & Diagrams

The theme supports:
- **MathJax**: For mathematical notation (enabled in `_config.yml`)
  ```markdown
  $E = mc^2$ (inline math)

  $$
  \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
  $$ (block math)
  ```

- **Mermaid**: For diagrams (enabled in `_config.yml`)
  ````markdown
  ```mermaid
  graph TD
      A[Start] --> B[Process]
      B --> C[End]
  ```
  ````

- **Charts**: Chart.js support (enabled in `_config.yml`)

### 7. Content Organization

#### Posts Directory (`_posts/`)

For lecture notes or blog posts:
- Use `YYYY-MM-DD-title.md` naming
- Use `layout: post`
- Front matter should include `date`, `title`, and optionally `categories`, `tags`
- Use `<!--more-->` to control excerpt on home/archive pages

#### Pages Directory (`_pages/`)

For static content pages:
- Use descriptive filenames: `courses.md`, `about.md`
- Use `layout: page` or `layout: home` (for index)
- Set `permalink` if you want a custom URL

#### Collections

Course pages use the `courses` collection:
- Defined in `_config.yml`
- Each course has its own directory
- Can have custom front matter defaults

## Theme Features

### Pagination

Posts can be paginated. Configured in `_config.yml`:
```yaml
paginate: 10
paginate_path: "/page:num"
```

### SEO

The theme integrates with `jekyll-seo-tag` for automatic SEO:
- Meta descriptions
- Open Graph tags
- Twitter cards

### Social Links

Configure social links in `_config.yml`:
```yaml
social:
  github: username
  twitter: handle
  linkedin: profile
```

### Comments & Sharing

Can be configured in `_config.yml` (currently disabled):
```yaml
comments:
  provider: disqus  # or gitalk, valine, etc.
sharing:
  provider: addtoany
```

## Customization

### Overriding Theme Layouts

To customize a layout, copy it from the theme and modify:
1. Create `_layouts/[layout-name].html` in your site
2. Jekyll will use your version instead of the theme's

### Custom CSS

Add custom styles to `assets/css/main.css`. These will load after the theme's CSS.

### Custom Includes

Similar to layouts, create `_includes/[component-name].html` to override theme includes.

## Reference Links

- **Theme Repository**: https://github.com/sweeden-ttu/jekyll-TeXt-theme
- **Theme Documentation**: https://kitian616.github.io/jekyll-TeXt-theme/
- **Example Posts**: https://github.com/sweeden-ttu/jekyll-TeXt-theme/tree/master/docs/_posts

## Quick Reference

| Task | Location | Layout |
|------|----------|--------|
| Home page | `_pages/index.md` | `home` |
| Static pages | `_pages/*.md` | `page` |
| Blog posts | `_posts/YYYY-MM-DD-*.md` | `post` |
| Course pages | `[course-name]/README.md` | `course` |
| Custom CSS | `assets/css/main.css` | N/A |
| Custom layouts | `_layouts/*.html` | N/A |
