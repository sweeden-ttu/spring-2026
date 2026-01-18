// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Courses Page', () => {
  test('should load courses page successfully', async ({ page }) => {
    await page.goto('/courses/');
    
    // Check that the page loaded
    await expect(page).toHaveTitle(/Courses/i);
    
    // Check for courses content
    const content = page.locator('body');
    await expect(content).toBeVisible();
  });

  test('should display course information', async ({ page }) => {
    await page.goto('/courses/');
    
    // Check for course names
    await expect(page.getByText(/Software Verification/i).or(
      page.getByText(/CS-5374/i)
    ).first()).toBeVisible();
    
    await expect(page.getByText(/Cryptography/i).or(
      page.getByText(/CS-6343/i)
    ).first()).toBeVisible();
  });

  test('should have valid links', async ({ page }) => {
    await page.goto('/courses/');
    
    // Check that links exist
    const links = page.getByRole('link');
    const linkCount = await links.count();
    expect(linkCount).toBeGreaterThan(0);
    
    // Check for Canvas links
    const canvasLinks = page.getByRole('link', { name: /Canvas/i });
    const canvasCount = await canvasLinks.count();
    expect(canvasCount).toBeGreaterThan(0);
  });
});
