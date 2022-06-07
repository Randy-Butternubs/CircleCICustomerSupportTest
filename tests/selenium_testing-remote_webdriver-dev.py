from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserVersion", "74")
    chrome_options.set_capability("platformName", "Windows 10")
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )
    driver.get("https://google.com")

    text = driver.find_element(By.ID, value="text").text
    assert text == ""

    driver.implicitly_wait(0.5)

    button = driver.find_element(by=By.ID, value="button")
    button.click()
    text = driver.find_element(By.ID, value="text").text
    assert text == "Words are CRAAAAZY"

    driver.quit()


test_button()