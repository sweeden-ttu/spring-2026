// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Homepage', () => {
  test('should load the homepage successfully', async ({ page }) => {
    await page.goto('/');
    
    // Check that the page loaded
    const title = await page.title();
    expect(title).toMatch(/Spring 2026/i);
    
    // Check for main heading or content (check for h1 or main content area)
    const h1 = page.locator('h1').first();
    const heading = page.getByRole('heading', { name: /Spring 2026/i }).first();
    const mainContent = page.getByText(/Welcome to the Spring 2026/i);
    
    // At least one of these should be visible
    const headingVisible = await heading.isVisible().catch(() => false);
    const h1Visible = await h1.isVisible().catch(() => false);
    const contentVisible = await mainContent.isVisible().catch(() => false);
    
    expect(headingVisible || h1Visible || contentVisible).toBeTruthy();
  });

  test('should have correct page structure', async ({ page }) => {
    await page.goto('/');
    
    // Check for HTML structure
    const html = page.locator('html');
    await expect(html).toHaveAttribute('lang', 'en');
    
    // Check for main content area
    const main = page.locator('main').or(page.locator('.main'));
    await expect(main.first()).toBeVisible();
  });

  test('should display course information', async ({ page }) => {
    await page.goto('/');
    
    // Check for Software Verification course
    await expect(page.getByText(/Software Verification and Validation/i)).toBeVisible();
    
    // Check for Cryptography course
    await expect(page.getByText(/Cryptography/i)).toBeVisible();
  });

  test('should have navigation links', async ({ page }) => {
    await page.goto('/');
    
    // Check for links on the page (could be Canvas, course links, etc.)
    const links = page.locator('a[href]');
    const linkCount = await links.count();
    expect(linkCount).toBeGreaterThan(0);
  });

  test('should have valid meta tags', async ({ page }) => {
    await page.goto('/');
    
    // Check for charset
    const charset = page.locator('meta[charset]');
    await expect(charset).toHaveAttribute('charset', 'utf-8');
    
    // Check for viewport
    const viewport = page.locator('meta[name="viewport"]');
    await expect(viewport).toHaveCount(1);
  });

  test('should load CSS styles', async ({ page }) => {
    await page.goto('/');
    
    // Check that CSS link exists in the head (not visible, but present)
    const cssLinks = page.locator('head link[rel="stylesheet"]');
    const cssCount = await cssLinks.count();
    expect(cssCount).toBeGreaterThan(0);
    
    // Check for theme styles (main.css should exist)
    const mainCSS = page.locator('head link[href*="main.css"]');
    const mainCSSCount = await mainCSS.count();
    expect(mainCSSCount).toBeGreaterThan(0);
    
    // Verify CSS file is accessible
    const cssResponse = await page.request.get('/assets/css/main.css');
    expect(cssResponse.ok()).toBeTruthy();
  });
});
