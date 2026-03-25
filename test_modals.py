from playwright.sync_api import sync_playwright

def verify_feature(page):
    # Print all console errors
    page.on("console", lambda msg: print(f"Browser Console: {msg.type} {msg.text}"))
    page.on("pageerror", lambda err: print(f"Browser Page Error: {err.message}"))

    page.goto("http://localhost:3000/index.html")
    page.wait_for_timeout(2000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            verify_feature(page)
        finally:
            context.close()
            browser.close()
