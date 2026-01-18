# Development Guide: Running and Debugging the Jekyll Site

This guide provides step-by-step instructions for running and debugging the Spring 2026 Jekyll site locally.

## Prerequisites

Before running the site, ensure you have:

1. **Ruby 3.3+** installed
2. **Bundler** installed (`gem install bundler`)
3. **Node.js 20+** (for Playwright tests, optional)
4. **Python 3.x** (for lecture page generation scripts, optional)

## Quick Start

### 1. Install Dependencies

```bash
# Install Ruby dependencies
bundle install

# Install Node.js dependencies (for tests)
npm install
```

### 2. Build the Site

```bash
# Build Jekyll site
bundle exec jekyll build

# Or build with verbose output for debugging
bundle exec jekyll build --verbose
```

### 3. Run Development Server

```bash
# Start Jekyll development server
bundle exec jekyll serve

# Or with specific options
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload
```

The site will be available at: **http://localhost:4000**

## Running the Site

### Basic Server

```bash
bundle exec jekyll serve
```

**Features:**
- Serves at `http://localhost:4000`
- Auto-regenerates on file changes
- Shows build errors in terminal

### Development Server with Live Reload

```bash
bundle exec jekyll serve --livereload
```

**Features:**
- Auto-refreshes browser on changes
- Better for active development

### Production Build

```bash
# Build for production
JEKYLL_ENV=production bundle exec jekyll build

# Then serve the built site
bundle exec jekyll serve --no-watch --destination _site
```

## Debugging Common Issues

### Issue 1: Bundle Install Errors

**Symptoms:**
- `Could not find compatible versions`
- Dependency conflicts

**Solutions:**

```bash
# Update bundler
gem update bundler

# Clear bundle cache
bundle clean --force

# Remove Gemfile.lock and reinstall
rm Gemfile.lock
bundle install
```

### Issue 2: Theme Not Loading

**Symptoms:**
- Site appears unstyled
- Missing theme components

**Solutions:**

```bash
# Verify theme is installed
bundle list | grep jekyll-text-theme

# Rebuild theme dependency
bundle update jekyll-text-theme

# Check _config.yml has theme setting
grep -i theme _config.yml
```

**Check:**
- `_config.yml` contains `theme: jekyll-text-theme`
- Theme path in `Gemfile` is correct
- Bundle includes theme gem

### Issue 3: CSS Not Loading

**Symptoms:**
- No styles applied
- CSS file 404 errors

**Solutions:**

```bash
# Check main.scss exists
ls -la assets/css/main.scss

# Rebuild CSS
bundle exec jekyll build --verbose

# Check generated CSS
ls -la _site/assets/css/main.css
```

**Check:**
- `assets/css/main.scss` exists
- No conflicting `assets/css/main.css` file
- Sass compilation succeeds

### Issue 4: Build Errors

**Symptoms:**
- Build fails with errors
- Missing files or references

**Debug Steps:**

```bash
# Build with trace for detailed errors
bundle exec jekyll build --trace

# Check for Liquid errors
bundle exec jekyll build --verbose 2>&1 | grep -i error

# Validate YAML files
bundle exec jekyll build --verbose 2>&1 | grep -i yaml
```

**Common Causes:**
- Invalid YAML syntax
- Missing front matter
- Broken Liquid templates
- Missing data files

### Issue 5: Page Not Found (404)

**Symptoms:**
- Pages return 404
- Links broken

**Debug Steps:**

```bash
# Check if page exists
find _pages -name "*.md" | grep page-name

# Check permalink in front matter
grep -r "permalink" _pages/

# Verify build includes page
ls -la _site/path/to/page/
```

**Check:**
- Page file exists in `_pages/` or root
- Front matter has correct `permalink`
- `_config.yml` includes `_pages` directory

### Issue 6: Data Files Not Loading

**Symptoms:**
- YAML data not accessible
- `site.data` empty or missing

**Debug Steps:**

```bash
# Check data file exists
find . -name "*.yaml" -path "*/_data/*"

# Validate YAML syntax
ruby -e "require 'yaml'; YAML.load_file('path/to/file.yaml')"

# Check data in build
bundle exec jekyll build --verbose 2>&1 | grep -i data
```

**Check:**
- Data files in `_data/` directories
- YAML syntax is valid
- File names match references in templates

## Development Workflow

### Typical Development Session

```bash
# 1. Start development server
bundle exec jekyll serve --livereload

# 2. Make changes to files
# - Edit markdown files
# - Modify templates
# - Update configuration

# 3. Check for errors in terminal
# - Build errors appear immediately
# - Fix issues as they appear

# 4. Verify in browser
# - Visit http://localhost:4000
# - Check all pages load correctly
```

### Before Committing

```bash
# 1. Build site successfully
bundle exec jekyll build

# 2. Run tests (if available)
npm test

# 3. Check for warnings
bundle exec jekyll build 2>&1 | grep -i warning

# 4. Validate HTML (optional)
bundle exec htmlproofer _site --disable-external
```

## Debugging Tools

### Jekyll Debug Output

```bash
# Verbose build output
bundle exec jekyll build --verbose

# Trace for full stack traces
bundle exec jekyll build --trace

# Show all files being processed
bundle exec jekyll build --verbose 2>&1 | grep -i "processing\|reading"
```

### Check Generated Site

```bash
# List generated files
find _site -type f | head -20

# Check specific page
cat _site/index.html | head -50

# Verify CSS generation
ls -lh _site/assets/css/main.css
```

### Inspect Configuration

```bash
# Show effective configuration
bundle exec jekyll build --verbose 2>&1 | grep -i "configuration"

# Check theme configuration
grep -A 5 "Theme Config" _site/*.html 2>/dev/null | head -10
```

## Common Debugging Commands

### Check Dependencies

```bash
# List installed gems
bundle list

# Check Jekyll version
bundle exec jekyll --version

# Verify theme
bundle exec jekyll info
```

### Clean Build

```bash
# Remove build artifacts
rm -rf _site .jekyll-cache

# Fresh build
bundle exec jekyll build
```

### Validate Files

```bash
# Check YAML syntax
for file in $(find . -name "*.yaml" -o -name "*.yml"); do
  ruby -e "require 'yaml'; YAML.load_file('$file')" 2>&1 && echo "✓ $file"
done

# Check Markdown files
find _pages -name "*.md" | while read f; do
  grep -q "^---" "$f" && echo "✓ $f" || echo "✗ $f (missing front matter)"
done
```

## Testing

### Run Integration Tests

```bash
# Run Jekyll build tests
./test_integration.sh

# Run Playwright tests (requires server running)
npm test

# Run specific test
npx playwright test tests/homepage.spec.js
```

### Manual Testing Checklist

- [ ] Homepage loads correctly
- [ ] Navigation links work
- [ ] CSS styles apply properly
- [ ] All pages are accessible
- [ ] Images and assets load
- [ ] No console errors in browser
- [ ] Responsive design works

## Troubleshooting Guide

### Problem: Server Won't Start

**Check:**
```bash
# Port in use?
lsof -i :4000

# Kill existing Jekyll process
pkill -f jekyll

# Check Ruby version
ruby --version
```

### Problem: Theme Not Applied

**Check:**
```bash
# Verify theme in config
grep theme _config.yml

# Check Gemfile
grep jekyll-text-theme Gemfile

# Reinstall theme
bundle update jekyll-text-theme
```

### Problem: Build Takes Too Long

**Solutions:**
```bash
# Use incremental build
bundle exec jekyll build --incremental

# Exclude large directories
# Add to _config.yml exclude list
```

## Getting Help

### Log Files

- **Build log**: Check terminal output
- **Jekyll cache**: `.jekyll-cache/`
- **Generated site**: `_site/`

### Useful Commands Summary

```bash
# Quick commands
bundle exec jekyll serve              # Start server
bundle exec jekyll build --trace      # Build with errors
bundle install                        # Update dependencies
bundle exec jekyll clean              # Clean build artifacts
```

### Debug Checklist

When debugging issues:

1. ✅ Check Ruby version (`ruby --version`)
2. ✅ Verify dependencies installed (`bundle list`)
3. ✅ Build with verbose output (`--verbose --trace`)
4. ✅ Check file paths and names
5. ✅ Validate YAML syntax
6. ✅ Verify front matter format
7. ✅ Check _config.yml settings
8. ✅ Review generated _site/ directory

## Performance Tips

### Faster Builds

```bash
# Use incremental builds
bundle exec jekyll serve --incremental

# Limit files processed (development)
# Add to _config.yml exclude patterns
```

### Optimize Development

```bash
# Disable plugins in development
# Comment out in _config.yml plugins list

# Use Jekyll's watch mode
bundle exec jekyll serve --watch
```

---

**Next Steps**: See [THEME_INSTALLATION.md](THEME_INSTALLATION.md) for theme-specific setup and [PLAYWRIGHT_SETUP.md](PLAYWRIGHT_SETUP.md) for testing setup.
