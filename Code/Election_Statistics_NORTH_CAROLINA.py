from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
from warnings import filterwarnings
from os import system
filterwarnings('ignore')

# WebDriver Chrome
driver = webdriver.Chrome()

# Target URL
driver.get("https://www.cnn.com/election/2020/results/state/north-carolina/president")
driver.maximize_window()
right_arrow_image_source:str = "yaWdodCIgZD0iTTkuOTUyIDUuOTk0SDEuMzk1YS41OTUuNTk1IDAgMSAxIDAtMS4xOWg4LjU1N2wtMy4yMTgtMy4xOWEuNTkyLjU5MiAwIDAgMSAwLS44NC42MDYuNjA2IDAgMCAxIC44NDkgMGw0LjI0MiA0LjIwNWEuNTkzLjU5MyAwIDAgMSAwIC44NDJsLTQuMjQyIDQuMjA1YS42MDYuNjA2IDAgMCAxLS44NSAwIC41OTMuNTkzIDAgMCAxIDAtLjg0MWwzLjIyLTMuMTl6Ii8+CiAgICA8L2RlZnM+CiAgICA8ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEgMSkiPgogICAgICAgIDx1c2UgZmlsbD0iIzRENEQ0RCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNSA3KSIgeGxpbms6aHJlZj0iI2EtYXJyb3ctcmlnaHQiLz4KICAgICAgICA8Y2lyY2xlIGN4PSIxMi41IiBjeT0iMTIuNSIgcj0iMTIuNSIgc3Ryb2tlPSIjNEQ0RDREIi8+CiAgICA8L2c+Cjwvc3ZnPgo="
while True:
    system('cls')
    driver.refresh()
    sleep(1)
    page:str = driver.find_element(By.XPATH, "/html/body").text
    sleep(1)
    while True:
        try:
            # Locate all arrow buttons (left and right)
            arrow_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.paginationstyles__Arrow-sc-58lau4-1.kxnBsH img'))
            )

            # Loop through the buttons and find the right arrow by comparing its src attribute
            right_arrow_button = None
            for arrow_button in arrow_buttons:
                # Check if the current button's image source matches the right arrow image
                if right_arrow_image_source[:20] in arrow_button.get_attribute("src"):
                    right_arrow_button = arrow_button
                    break

            # If the right arrow is found, click the button
            if right_arrow_button:
                right_arrow_button.click()
                page += driver.find_element(By.XPATH, "/html/body").text
            else:
                break

        except:
            break
    system('cls')
    extraction_time = datetime.now()
    if(extraction_time.month>=11 and extraction_time.day>=10 and extraction_time.hour>=23 and extraction_time.minute>=59):
        break
    lines:list[str] = page.split('\n')
    del page
    inside_county_numbers:bool = False
    with open('State_Details/North_Carolina/CNN_Text.txt','a') as file:
        file.write(f"UPDATE DATETIME: {extraction_time}\n")
        for line in lines:
            if("county result" in line.lower()):
                inside_county_numbers:bool = True
            if("Not all candidates are listed" in line):
                inside_county_numbers:bool = False
            if(inside_county_numbers):
                file.write(f"{line}\n")
        file.write('\n-----------------------------------------------------------------------------------------------------------\n')
    system('cls')