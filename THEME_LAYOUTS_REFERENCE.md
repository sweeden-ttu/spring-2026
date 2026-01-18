# Jekyll-TeXt Theme Layouts Reference

This document provides a comprehensive reference for all available layouts in jekyll-TeXt-theme, based on the official documentation: https://kitian616.github.io/jekyll-TeXt-theme/docs/en/layouts

## Layout Hierarchy

```
none
└── base
    └── page
        ├── article
        ├── articles
        │   └── home
        ├── archive
        ├── landing
        └── 404
```

## Available Layouts

### 1. `layout: none`
- **Base**: None
- **Purpose**: Minimal layout, no header/footer
- **Use Case**: Custom pages, embedded content

### 2. `layout: base`
- **Base**: none
- **Purpose**: Base layout with HTML structure
- **Use Case**: Foundation for other layouts

### 3. `layout: page`
- **Base**: base
- **Purpose**: Standard page layout with header/footer
- **Features**: Sidebar support, breadcrumbs, navigation
- **Use Case**: Regular content pages, documentation

**Key Front Matter Options:**
```yaml
---
layout: page
title: Page Title
sidebar:
  nav: navigation-name  # Enable sidebar navigation
full_width: true        # Full-width content
---
```

### 4. `layout: article`
- **Base**: page
- **Purpose**: Article/blog post layout
- **Features**: Article header, author info, tags, date, comments, sharing
- **Use Case**: Blog posts, lecture notes, articles

**Key Front Matter Options:**
```yaml
---
layout: article
title: Article Title
key: unique-article-key
tags:
  - Tag1
  - Tag2
date: 2026-01-15
sidebar:
  nav: navigation-name
article_header:
  actions:
    - text: Button Text
      url: /path/
  type: overlay          # overlay, cover
  height: 50vh          # Custom height
  theme: dark           # dark, light
  background_color: "#333"
  background_image:
    src: /path/to/image.jpg
    gradient: "linear-gradient(...)"
---
```

### 5. `layout: articles`
- **Base**: page
- **Purpose**: List/archive of articles
- **Features**: Article listing, pagination, filters
- **Use Case**: Article archives, blog index

**Key Front Matter Options:**
```yaml
---
layout: articles
title: Article Archive
articles:
  excerpt_type: html    # text, html
  show_info: true       # Show article metadata
  show_readmore: true   # Show read more links
---
```

### 6. `layout: home`
- **Base**: articles
- **Purpose**: Homepage with article listing
- **Features**: Featured posts, recent articles, pagination
- **Use Case**: Blog homepage, main landing page

**Key Front Matter Options:**
```yaml
---
layout: home
title: Home
articles:
  excerpt_type: html
  show_info: true
---
```

### 7. `layout: landing`
- **Base**: page
- **Purpose**: Landing page with hero sections
- **Features**: Hero sections, call-to-action buttons, multiple sections with images
- **Use Case**: Product landing pages, course landing pages

**Key Front Matter Options:**
```yaml
---
layout: landing
title: Landing Page
excerpt: Short description
article_header:
  actions:
    - text: CTA Button
      type: error
      url: /path/
  height: 100vh
  theme: dark
  background_color: "#1a1a1a"
data:
  sections:
    - title: Section Title
      excerpt: Section description
      theme: dark
      background_color: "#333"
      children:
        - title: Card Title
          excerpt: Card description
          actions:
            - text: Button
              url: /path/
          image:
            src: /path/to/image.svg
            style: "max-width: 300px"
            is_row: true
---
```

### 8. `layout: archive`
- **Base**: page
- **Purpose**: Archive/index of posts by date or category
- **Features**: Date grouping, category filtering
- **Use Case**: Post archives, chronological listings

### 9. `layout: 404`
- **Base**: page
- **Purpose**: 404 error page
- **Use Case**: Custom error pages

## Layout-Specific Features

### Article Header (`article_header`)

Available in: `article`, `page`, `landing`

**Types:**
1. **`overlay`**: Text overlays on background image
2. **`cover`**: Image fills header area

**Options:**
- `type`: `overlay`, `cover`
- `height`: `100vh`, `50vh`, custom height
- `theme`: `dark`, `light`
- `background_color`: Hex color code
- `background_image`: Image with optional gradient
- `actions`: Array of CTA buttons

### Sidebar Navigation (`sidebar`)

Available in: `page`, `article`

**Usage:**
```yaml
---
sidebar:
  nav: navigation-name  # Reference from _data/navigation.yml
---
```

The navigation structure must be defined in `_data/navigation.yml`:

```yaml
# In _data/navigation.yml
navigation-name:
  - title: Section 1
    children:
      - title: Item 1
        url: /path/1/
      - title: Item 2
        url: /path/2/
```

## Page Front Matter Options

### Common Options (All Layouts)

```yaml
---
layout: page
title: Page Title
key: unique-page-key        # Required for comments/pageviews
show_title: true            # Show/hide page title
show_date: true             # Show/hide date
show_tags: true             # Show/hide tags
full_width: true            # Full-width content
sidebar:
  nav: navigation-name      # Enable sidebar navigation
---
```

### Article-Specific Options

```yaml
---
layout: article
type: normal                # normal, brief
show_excerpt: true          # Show excerpt
excerpt_type: text          # text, html
show_readmore: true         # Show read more link
show_info: true             # Show article metadata
---
```

## Layout Examples

### Standard Page with Sidebar

```yaml
---
layout: page
title: Course Introduction
permalink: /software-verification/introduction/
sidebar:
  nav: cs-5374-sidebar
---
```

### Article with Hero Header

```yaml
---
layout: article
title: Black Box Testing
key: black-box-testing
tags:
  - Testing
  - Black Box
sidebar:
  nav: cs-5374-sidebar
article_header:
  type: overlay
  height: 50vh
  theme: dark
  background_color: "#E90802"
---
```

### Landing Page

```yaml
---
layout: landing
title: Spring 2026 Coursework
article_header:
  actions:
    - text: View Courses
      type: error
      url: /courses/
  height: 100vh
  theme: dark
data:
  sections:
    - title: Courses
      theme: light
      children:
        - title: Course 1
          excerpt: Description
---
```

## Best Practices

1. **Use `layout: page`** for standard content pages
2. **Use `layout: article`** for blog posts, lecture notes, articles
3. **Use `layout: landing`** for homepage or marketing pages
4. **Use `layout: home`** for blog-style homepages with article listings
5. **Always include `key`** for articles (required for comments/pageviews)
6. **Enable sidebar** for content that needs navigation (`sidebar: { nav: ... }`)
7. **Use `article_header`** for visual impact on article/landing pages

## Navigation Integration

- **Header Navigation**: Defined in `_data/navigation.yml` under `header:` key
- **Sidebar Navigation**: Defined in `_data/navigation.yml` as named structures, referenced in front matter with `sidebar: { nav: structure-name }`

---

**Reference**: https://kitian616.github.io/jekyll-TeXt-theme/docs/en/layouts
