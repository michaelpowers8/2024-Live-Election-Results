from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
from warnings import filterwarnings
from pandas import DataFrame
from os import system
from re import search
filterwarnings('ignore')

# WebDriver Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
county_names:list[str] = []
county_results:dict[str,DataFrame] = {}
columns:list[str] = ['Leading_Candidate','Vote_Percent_Leader','Vote_Count_Leader','Trailing_Candidate',
                    'Vote_Percent_Trailer','Vote_Count_Trailer','Reported_Percent']
first_iteration:bool = True

# Target URL
driver.get("https://www.cnn.com/election/2020/results/state/nevada/president")
driver.maximize_window()
right_arrow_image_source:str = "yaWdodCIgZD0iTTkuOTUyIDUuOTk0SDEuMzk1YS41OTUuNTk1IDAgMSAxIDAtMS4xOWg4LjU1N2wtMy4yMTgtMy4xOWEuNTkyLjU5MiAwIDAgMSAwLS44NC42MDYuNjA2IDAgMCAxIC44NDkgMGw0LjI0MiA0LjIwNWEuNTkzLjU5MyAwIDAgMSAwIC44NDJsLTQuMjQyIDQuMjA1YS42MDYuNjA2IDAgMCAxLS44NSAwIC41OTMuNTkzIDAgMCAxIDAtLjg0MWwzLjIyLTMuMTl6Ii8+CiAgICA8L2RlZnM+CiAgICA8ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEgMSkiPgogICAgICAgIDx1c2UgZmlsbD0iIzRENEQ0RCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNSA3KSIgeGxpbms6aHJlZj0iI2EtYXJyb3ctcmlnaHQiLz4KICAgICAgICA8Y2lyY2xlIGN4PSIxMi41IiBjeT0iMTIuNSIgcj0iMTIuNSIgc3Ryb2tlPSIjNEQ0RDREIi8+CiAgICA8L2c+Cjwvc3ZnPgo="
while True:
    system('cls')
    driver.refresh()
    page:str = driver.find_element(By.XPATH, "/html/body").text
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
    final_lines:list[str] = []
    current_county:str = ""
    current_row:list = ['None']*len(columns)
    for line in lines:
        if("county result" in line.lower()):
            inside_county_numbers:bool = True
        if("Not all candidates are listed" in line):
            inside_county_numbers:bool = False
        if(inside_county_numbers):
            final_lines.append(line)
    for line in range(len(final_lines)):
        if("Nevada County" in final_lines[line]):
            pass
        elif("County" in final_lines[line]):
            current_county:str = final_lines[line][:final_lines[line].index('County')]
            county_results[current_county] = DataFrame(data=None,columns=columns)
        elif("Candidate % Vote" in final_lines[line]):
            extraction_time = datetime.now()
            current_row[0] = 'Trump' if 'T' in final_lines[line+1] else 'Harris'
            current_row[1] = final_lines[line+2].replace('%','').replace(',','')
            current_row[2] = final_lines[line+3].replace('%','').replace(',','')
            current_row[3] = 'Trump' if 'T' in final_lines[line+4] else 'Harris'
            current_row[4] = final_lines[line+5].replace('%','').replace(',','')
            current_row[5] = final_lines[line+6].replace('%','').replace(',','')
            current_row[6] = search(r"[0-9]{1,}",final_lines[line+7]).group()
            county_results[current_county].loc[extraction_time] = current_row
            current_row:list = ['None']*len(columns)
            
    if(first_iteration):
        first_iteration:bool = False
        for key,item in county_results.items():
            file_name:str = f'{key.replace(" ","_")}_County.csv'
            item.to_csv(f'State_Details/Nevada/{file_name.replace("__","_")}',index=True,mode='a',header=True)
        first_iteration:bool = False
    else:
        for key,item in county_results.items():
            file_name:str = f'{key.replace(" ","_")}_County.csv'
            item.to_csv(f'State_Details/Nevada/{file_name.replace("__","_")}',index=True,mode='a',header=False)
    system('cls')
    
columns:list[str] = ['Leading_Candidate','Vote_Percent_Leader','Vote_Count_Leader','Trailing_Candidate',
                    'Vote_Percent_Trailer','Vote_Count_Trailer','Reported_Percent']