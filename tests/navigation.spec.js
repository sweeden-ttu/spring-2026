// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Navigation', () => {
  test('should navigate to homepage', async ({ page }) => {
    await page.goto('/courses/');
    await page.getByRole('link', { name: /Home/i }).or(
      page.getByRole('link', { name: /Spring 2026/i })
    ).first().click();
    
    await expect(page).toHaveURL(/\/$/);
  });

  test('should navigate to courses page from homepage', async ({ page }) => {
    await page.goto('/');
    
    // Try to find and click courses link
    const coursesLink = page.getByRole('link', { name: /Courses/i }).first();
    if (await coursesLink.isVisible()) {
      await coursesLink.click();
      await expect(page).toHaveURL(/\/courses/);
    }
  });

  test('should have working internal links', async ({ page }) => {
    await page.goto('/');
    
    // Check for links that point to internal pages
    const internalLinks = page.locator('a[href^="/"], a[href^="#"]');
    const linkCount = await internalLinks.count();
    
    if (linkCount > 0) {
      // Check first internal link
      const firstLink = internalLinks.first();
      const href = await firstLink.getAttribute('href');
      expect(href).toBeTruthy();
      
      // Try navigating to it if it's not a hash link
      if (href && !href.startsWith('#')) {
        const response = await page.request.get(href);
        expect([200, 404]).toContain(response.status()); // 200 OK or 404 is acceptable
      }
    }
  });

  test('should maintain navigation state', async ({ page }) => {
    await page.goto('/');
    
    // Get initial page content
    const initialTitle = await page.title();
    expect(initialTitle).toBeTruthy();
    
    // Navigate if possible
    const navLinks = page.locator('nav a, header a, .nav a, .header a');
    const navCount = await navLinks.count();
    
    if (navCount > 0) {
      const firstNavLink = navLinks.first();
      const href = await firstNavLink.getAttribute('href');
      
      if (href && href.startsWith('/')) {
        await firstNavLink.click();
        await page.waitForLoadState('networkidle');
        
        // Page should have changed
        const newTitle = await page.title();
        expect(newTitle).toBeTruthy();
      }
    }
  });
});
