import asyncio

from pyppeteer import launch

from tasks.login import login


async def main():
    browser = await launch(headless=False)
    page = (await browser.pages())[-1]
    try:
        await login(page)
    finally:
        await browser.close()


print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Done...")
