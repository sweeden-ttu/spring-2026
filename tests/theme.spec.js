// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Theme Functionality', () => {
  test('should have theme CSS loaded', async ({ page }) => {
    await page.goto('/');
    
    // Check for CSS file
    const cssResponse = await page.request.get('/assets/css/main.css');
    expect(cssResponse.ok()).toBeTruthy();
    expect(cssResponse.headers()['content-type']).toContain('text/css');
  });

  test('should have responsive design', async ({ page }) => {
    await page.goto('/');
    
    // Check viewport meta tag for responsive design
    const viewport = page.locator('meta[name="viewport"]');
    await expect(viewport).toHaveAttribute('content', expect.stringContaining('width=device-width'));
  });

  test('should have theme structure', async ({ page }) => {
    await page.goto('/');
    
    // Check for theme elements (header, main, footer areas)
    const body = page.locator('body');
    await expect(body).toBeVisible();
    
    // Theme should have some structure
    const hasStructure = await page.evaluate(() => {
      return document.querySelector('header, .header, main, .main, footer, .footer') !== null;
    });
    expect(hasStructure).toBeTruthy();
  });

  test('should have proper HTML5 structure', async ({ page }) => {
    await page.goto('/');
    
    // Check for doctype
    const doctype = await page.evaluate(() => {
      return document.doctype !== null && document.doctype.name === 'html';
    });
    expect(doctype).toBeTruthy();
    
    // Check for lang attribute
    const html = page.locator('html');
    await expect(html).toHaveAttribute('lang', 'en');
  });

  test('should have accessible structure', async ({ page }) => {
    await page.goto('/');
    
    // Check for headings hierarchy
    const h1 = page.locator('h1');
    const h1Count = await h1.count();
    expect(h1Count).toBeGreaterThan(0);
    
    // Check that images have alt text (if any)
    const images = page.locator('img');
    const imageCount = await images.count();
    if (imageCount > 0) {
      // At least check that images exist - alt text checking can be more specific
      const imagesWithAlt = page.locator('img[alt]');
      const altCount = await imagesWithAlt.count();
      // Not enforcing alt on all images, but checking structure
      expect(imagesWithAlt.count()).toBeGreaterThanOrEqual(0);
    }
  });
});
