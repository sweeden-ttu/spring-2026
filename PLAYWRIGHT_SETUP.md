# Playwright Testing Setup

This document describes the Playwright testing setup for the Jekyll site.

## Overview

Playwright tests are configured to run on every push to `main`/`master` branches and on pull requests via GitHub Actions.

## Test Files

### `tests/homepage.spec.js`
Tests for the homepage:
- Page loads successfully
- Page structure is correct
- Course information is displayed
- Navigation links exist
- Meta tags are valid
- CSS styles are loaded

### `tests/courses.spec.js`
Tests for the courses page:
- Page loads successfully
- Course information is displayed
- Links are valid and working

### `tests/theme.spec.js`
Tests for theme functionality:
- Theme CSS is loaded
- Responsive design is present
- Theme structure is correct
- HTML5 structure is valid
- Accessible structure

### `tests/navigation.spec.js`
Tests for navigation:
- Navigation between pages works
- Internal links function correctly
- Navigation state is maintained

## Running Tests Locally

### Prerequisites
```bash
npm install
npx playwright install --with-deps chromium
```

### Run all tests
```bash
npm test
```

### Run tests in headed mode (see browser)
```bash
npm run test:headed
```

### Run tests with UI
```bash
npm run test:ui
```

### Run tests for specific browser
```bash
npx playwright test --project=chromium
npx playwright test --project=firefox
npx playwright test --project=webkit
```

### Run a specific test file
```bash
npx playwright test tests/homepage.spec.js
```

### Debug tests
```bash
npm run test:debug
```

## GitHub Actions Workflow

The workflow (`.github/workflows/test.yml`) runs on:
- Push to `main` or `master` branches
- Pull requests to `main` or `master` branches

### Workflow Steps

1. **Checkout repository**
2. **Set up Ruby** - Installs Ruby 3.3 and caches bundler dependencies
3. **Install Jekyll dependencies** - Runs `bundle install`
4. **Build Jekyll site** - Runs `bundle exec jekyll build`
5. **Set up Node.js** - Installs Node.js 20 and caches npm dependencies
6. **Install npm dependencies** - Runs `npm ci`
7. **Install Playwright browsers** - Installs Chromium with system dependencies
8. **Build site and start server** - Builds and starts Jekyll server
9. **Run Playwright tests** - Executes all tests
10. **Upload test results** - Uploads test reports as artifacts

### Test Results

Test results are available in:
- GitHub Actions workflow summary
- Artifact: `playwright-report/` (retained for 30 days)

## Configuration

### `playwright.config.js`

Key settings:
- **testDir**: `./tests` - Test files directory
- **baseURL**: `http://localhost:4000` - Base URL for tests
- **retries**: 2 on CI, 0 locally
- **workers**: 1 on CI, unlimited locally
- **reporter**: `github` on CI, `html` locally

### Browser Projects

Tests run on multiple browsers/viewports:
- Chromium (Desktop)
- Firefox (Desktop)
- WebKit/Safari (Desktop)
- Mobile Chrome (Pixel 5)
- Mobile Safari (iPhone 12)

## Local Development Server

Playwright automatically starts the Jekyll server before running tests (when not in CI mode):

```javascript
webServer: {
  command: 'bundle exec jekyll serve --host 0.0.0.0 --port 4000',
  url: 'http://localhost:4000',
  reuseExistingServer: !process.env.CI,
  timeout: 120 * 1000,
}
```

If you already have a server running on port 4000, Playwright will reuse it.

## Writing New Tests

Example test structure:

```javascript
const { test, expect } = require('@playwright/test');

test.describe('Feature Name', () => {
  test('should do something', async ({ page }) => {
    await page.goto('/');
    // Your test code here
    await expect(page.locator('selector')).toBeVisible();
  });
});
```

## Best Practices

1. **Use semantic locators** - Prefer `getByRole`, `getByLabel` over CSS selectors
2. **Wait for elements** - Playwright auto-waits, but be explicit when needed
3. **Test user interactions** - Focus on what users do, not implementation details
4. **Keep tests independent** - Each test should work in isolation
5. **Use descriptive test names** - Clear test names help debugging

## Troubleshooting

### Tests fail locally
- Ensure Jekyll server is running: `bundle exec jekyll serve`
- Check that port 4000 is available
- Run `npx playwright install` to ensure browsers are installed

### Tests fail on CI
- Check GitHub Actions logs for specific errors
- Verify Node.js and Ruby versions match local setup
- Ensure all dependencies are in `package.json` and `Gemfile`

### Browser installation issues
```bash
npx playwright install --with-deps chromium
```

## Test Reports

After running tests, view the HTML report:
```bash
npx playwright show-report
```

This opens an interactive report showing:
- Test results
- Screenshots of failures
- Execution timeline
- Video recordings (if enabled)
