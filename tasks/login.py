import time


async def login(page):
    await page.goto("https://play.google.com/console/login", waitUntil='domcontentloaded')
    email_input = await page.querySelector('input[type="email"]')
    await email_input.type('this.dhiraj@gmail.com')
    await page.keyboard.press('Enter')

    time.sleep(10)
