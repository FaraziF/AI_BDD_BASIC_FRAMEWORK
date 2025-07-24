from playwright.sync_api import Playwright, Browser, Page


class CustomContext:
    page: Page  # is the browser tab or screen you interact with.
    browser: Browser  # is the overall browser application you’ve opened.
    playwright: Playwright  # is the engine that controls the browser and helps r
