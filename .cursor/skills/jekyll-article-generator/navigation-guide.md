# Navigation Configuration Guide

Complete guide to configuring navigation in jekyll-TeXt-theme articles.

## Overview

The jekyll-TeXt-theme uses `_data/navigation.yml` to define navigation structures. Navigation is separated into:

1. **Header Navigation**: Main site menu (top navigation bar)
2. **Sidebar Navigation**: Contextual navigation for articles and pages

## Header Navigation

### Structure

Header navigation is defined under the `header` key:

```yaml
header:
  - title: Home
    url: /
  - title: Docs
    url: /docs/en/quick-start
    key: docs  # Optional: unique identifier
```

### Options

- **`title`**: Single language title (string)
- **`titles`**: Multi-language titles (object with locale keys)
- **`url`**: Relative or absolute URL
- **`key`**: Optional unique identifier

### Multi-language Support

```yaml
header:
  - titles:
      en: Archive
      zh: 归档
      zh-Hans: 归档
      zh-Hant: 歸檔
    url: /archive.html
```

### External Links

```yaml
header:
  - title: GitHub
    url: https://github.com/username/repo
```

## Sidebar Navigation

### Structure

Sidebar navigation uses named navigation structures:

```yaml
docs-en:
  - title: Start
    children:
      - title: Quick Start
        url: /docs/en/quick-start
      - title: Structure
        url: /docs/en/structure
  - title: Customization
    children:
      - title: Configuration
        url: /docs/en/configuration
      - title: Navigation
        url: /docs/en/navigation
```

### Using in Articles

Reference the navigation structure in article front matter:

```yaml
---
layout: article
title: Article Title
sidebar:
  nav: docs-en  # Name of navigation structure
---
```

### Hierarchical Structure

Sidebar navigation supports multiple levels:

```yaml
course-topics:
  - title: Fundamentals
    children:
      - title: Introduction
        url: /topics/intro/
      - title: Basics
        url: /topics/basics/
  - title: Advanced
    children:
      - title: Advanced Topics
        url: /topics/advanced/
```

## Best Practices

### 1. Organize by Topic

Group related articles under parent categories:

```yaml
testing-methods:
  - title: Black Box Testing
    children:
      - title: Equivalence Partitioning
        url: /topics/black-box/equivalence/
      - title: Boundary Value Analysis
        url: /topics/black-box/boundary/
```

### 2. Use Consistent URLs

Maintain consistent permalink patterns:

```yaml
/software-verification/topics/01-introduction-vv/
/software-verification/topics/02-adequacy-criterion/
/software-verification/topics/03-student-presentation/
```

### 3. Logical Grouping

Group articles logically by:
- Topic or subject matter
- Course or course section
- Difficulty level
- Content type

### 4. Update Navigation When Creating Articles

When generating new articles:
1. Determine which navigation structure it belongs to
2. Add to appropriate `children` array
3. Reference in article front matter with `sidebar: { nav: structure-name }`

## Complete Example

```yaml
# _data/navigation.yml

header:
  - title: Home
    url: /
  - title: Software Verification
    url: /software-verification/introduction/
  - title: Topics
    url: /software-verification/introduction/

course-topics:
  - title: Introduction
    children:
      - title: Introduction to V&V
        url: /software-verification/topics/01-introduction-vv/
      - title: Adequacy Criterion
        url: /software-verification/topics/02-adequacy-criterion/
  - title: Testing Methods
    children:
      - title: Black Box Testing
        url: /software-verification/topics/04-black-box-testing/
      - title: White Box Testing
        url: /software-verification/topics/05-white-box-testing/
```

## Integration with Article Generation

When the article generator creates new articles:

1. **Check existing navigation**: Review `_data/navigation.yml` for appropriate structure
2. **Determine placement**: Decide where article fits in navigation hierarchy
3. **Update navigation file**: Add article to appropriate navigation structure
4. **Add sidebar reference**: Include `sidebar: { nav: structure-name }` in front matter
5. **Maintain consistency**: Follow existing URL patterns and grouping logic

## Troubleshooting

### Navigation Not Showing

- Verify `_data/navigation.yml` exists and is valid YAML
- Check that navigation structure name matches `sidebar.nav` in front matter
- Ensure URLs in navigation match article permalinks

### Invalid YAML

- Validate YAML syntax using online validator or `ruby -e "require 'yaml'; YAML.load_file('_data/navigation.yml')"`
- Check indentation (use spaces, not tabs)
- Verify array/list syntax

### Links Not Working

- Use relative URLs (e.g., `/path/to/page/`) not absolute (e.g., `http://domain.com/path`)
- Ensure permalinks in articles match URLs in navigation
- Verify trailing slashes are consistent

---

**Reference**: See https://github.com/sweeden-ttu/jekyll-TeXt-theme/blob/master/docs/_data/navigation.yml for complete examples.
