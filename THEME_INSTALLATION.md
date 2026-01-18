# Jekyll TeXt Theme Installation & Testing Guide

This document provides step-by-step instructions for installing and testing the jekyll-TeXt-theme on this site.

## Installation Summary

The theme has been successfully installed as a local gem to avoid SSL certificate issues with remote theme downloads.

### Step-by-Step Installation Process

#### 1. Build the Theme Gem
```bash
cd ../jekyll-text-theme
gem build jekyll-text-theme.gemspec
# Output: jekyll-text-theme-2.2.6.gem
```

#### 2. Configure Gemfile
Added the theme as a local path dependency:
```ruby
gem "jekyll-text-theme", path: "../jekyll-text-theme"
```

#### 3. Install Dependencies
```bash
bundle install
```

#### 4. Configure _config.yml
- Changed from `remote_theme: sweeden-ttu/jekyll-TeXt-theme` to `theme: jekyll-text-theme`
- Removed `jekyll-remote-theme` from plugins
- Added theme-specific configuration (`text_skin`, `highlight_theme`)

#### 5. Create Required Theme Files
- Created `assets/css/main.scss` with theme imports
- Removed conflicting `assets/css/main.css`
- Created `index.html` in root with `layout: home`

#### 6. Fix File Conflicts
- Removed `_pages/index.md` to avoid conflict with root `index.html`
- Updated `_config.yml` exclude patterns

## Theme Configuration

### _config.yml Settings
```yaml
theme: jekyll-text-theme
text_skin: default
highlight_theme: tomorrow
```

### Required Files Structure
```
spring-2026/
├── index.html              # Homepage (layout: home)
├── assets/
│   └── css/
│       └── main.scss       # Theme stylesheet
├── _pages/
│   └── courses.md          # Courses page
└── _config.yml             # Theme configuration
```

## Testing

### Build Test
```bash
bundle exec jekyll build
```
**Result**: ✓ Build succeeds with theme applied

### Integration Tests
Run the integration test script:
```bash
./test_integration.sh
```

#### Test Coverage
1. ✓ Build completes successfully
2. ✓ Homepage (`index.html`) exists
3. ✓ CSS file (`main.css`) generated
4. ✓ Theme CSS contains styling
5. ✓ Homepage has content
6. ✓ Homepage uses theme layout
7. ✓ Navigation structure present
8. ✓ Courses page exists
9. ✓ Theme components loaded
10. ✓ HTML structure valid
11. ✓ Metadata present
12. ✓ Theme configured correctly

**All 12 tests passed!**

### Manual Testing
```bash
# Start the development server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Troubleshooting

### Issue: SSL Certificate Errors
**Solution**: Use local gem path instead of `remote_theme`

### Issue: CSS Conflicts
**Solution**: Remove `assets/css/main.css` and create `assets/css/main.scss`

### Issue: Index File Conflicts
**Solution**: Use `index.html` in root, not `_pages/index.md`

### Issue: Dependency Resolution
**Solution**: Explicitly add `jemoji` to Gemfile:
```ruby
gem "jemoji", "~> 0.8"
```

## Theme Customization

### Changing Skin
Edit `_config.yml`:
```yaml
text_skin: dark  # Options: default, dark, forest, ocean, chocolate, orange
```

### Changing Code Highlighting
Edit `_config.yml`:
```yaml
highlight_theme: tomorrow-night  # Options: tomorrow, tomorrow-night, etc.
```

### Custom Styles
Create or edit `_sass/custom.scss` in your site (theme will import it automatically).

## Reference Files

- `THEME_GUIDE.md` - Comprehensive theme usage guide
- `test_integration.sh` - Automated integration test script
- `_config.yml` - Site and theme configuration
- `Gemfile` - Ruby dependencies including theme

## Status

✅ **Theme Installed**: jekyll-text-theme 2.2.6 (local gem)
✅ **Build Status**: Passing
✅ **Integration Tests**: 12/12 passed
✅ **Site Structure**: Valid
