import { test, expect } from "@playwright/test";

// This file contains a very small Playwright test that demonstrates a basic
// end-to-end (E2E) check for the Playwright website. It shows how to:
//  - navigate to a page,
//  - assert the page title,
//  - interact with page elements (click a link), and
//  - assert the resulting URL after navigation.
//
// The `test` and `expect` helpers are provided by Playwright's test runner.
// The `page` fixture represents a single browser tab / page.
test("homepage loads correctly", async ({ page }) => {
  // Navigate the page to the Playwright homepage URL.
  // This resolves once the page's load event has fired (by default Playwright
  // waits for the load/navigation to finish). If the navigation fails this
  // will reject and the test will fail.
  await page.goto("https://playwright.dev/");

  // Assert that the page title contains the text "Playwright".
  // `toHaveTitle` is an assertion helper that will wait until the condition
  // is true or time out. Using a regex keeps the check flexible.
  await expect(page).toHaveTitle(/Playwright/);

  // Find the link with accessible name "Get started" and click it.
  // `getByRole` queries elements by ARIA role which is robust and accessible.
  // Clicking triggers navigation to the docs section.
  await page.getByRole("link", { name: "Get started" }).click();

  // After the click, assert that the current URL includes '/docs'.
  // `toHaveURL` will wait until the URL matches the provided pattern.
  await expect(page).toHaveURL(/.*docs/);
});
