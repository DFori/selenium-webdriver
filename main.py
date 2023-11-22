from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
