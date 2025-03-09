from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()  # Ensure you have chromedriver installed

# Open the Demoblaze website
driver.get("https://www.demoblaze.com")
time.sleep(3)

# "Laptops" section
laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_link.click()
time.sleep(3)

laptop_data = []

while True:
    # Find all laptop items
    items = driver.find_elements(By.CLASS_NAME, "card-title")
    prices = driver.find_elements(By.CLASS_NAME, "card-text")

    for i in range(len(items)):
        name = items[i].text
        price = prices[i].text

        items[i].click()
        time.sleep(2)

        description = driver.find_element(By.ID, "more-information").text

        # Store data
        laptop_data.append({
            "name": name,
            "price": price,
            "description": description
        })

        driver.back()
        time.sleep(2)

    # Try to click "Next" button
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)
    except:
        break

# Save data to JSON
with open("laptops.json", "w") as file:
    json.dump(laptop_data, file, indent=4)

driver.quit()

print("Laptop data scraped and saved to laptops.json!")
