# selenium_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By

Example: Initialize WebDriver and navigate to a page
driver = webdriver.Chrome()
# Make sure you have the ChromeDriver in your PATH
driver = webdriver.Firefox()
#driver.get("https://www.example.com")

# Example action
print("Page title is:", driver.title)

# Close the browser
driver.quit()






