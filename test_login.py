from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    expect(page.get_by_text("Dashboard")).to_be_visible()
