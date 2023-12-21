import time


def login(driver):
    driver.get("https://play.google.com/console/")

    title = driver.title
    print(title)
    time.sleep(10)
