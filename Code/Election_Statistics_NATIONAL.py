from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
from re import search
from pandas import DataFrame
from os import system
from warnings import filterwarnings
filterwarnings('ignore')

# WebDriver Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut",
            "District Of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", 
            "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", 
            "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", 
            "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
            "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", 
            "Washington", "Wisconsin", "West Virginia", "Wyoming"]

results:dict[str,DataFrame] = {}
for state in state_names:
    results[state] = DataFrame(data=None,columns=['Leading_Candidate','Vote_Percent_Leader','Vote_Count_Leader','Trailing_Candidate',
                                                'Vote_Percent_Trailer','Vote_Count_Trailer','Reported_Percent'])

# Target URL
driver.get("https://www.cnn.com/election/2020/results/president")
driver.maximize_window()

while True:
    driver.refresh()
    while True:
        try:
            show_more_button = driver.find_element(By.CLASS_NAME, "house-nationalsstyles__FullRaceDetails-sc-10qfp1h-7")
            driver.execute_script("arguments[0].click();", show_more_button)
            sleep(1)  # wait for the content to load
        except Exception as e:
            break
    
    # Printing the whole body text
    page = driver.find_element(By.XPATH, "/html/body").text
    extraction_time = datetime.now()
    if(extraction_time.month>=11 and extraction_time.day>=10 and extraction_time.hour>=8 and extraction_time.minute>=0):
        break
    lines = page.split('\n')
    del page
    state_results_found:bool = False
    current_state:str = 'None'
    current_state_found:bool = False
    current_state_leading_candidate:str = 'None'
    current_state_leading_candidate_vote_percent:float = 0
    current_state_leading_candidate_vote_count:int = 0
    current_state_trailing_candidate:str = 'None'
    current_state_trailing_candidate_vote_percent:float = 0
    current_state_trailing_candidate_vote_count:int = 0
    current_state_reported_percent:float = 0
    for line in range(len(lines)):
        if(not(state_results_found)):
            if('STATE RESULTS' in lines[line]):
                state_results_found = True
        if(state_results_found):
            if(not(current_state_found)):
                for state in state_names:
                    if(state in lines[line]):
                        current_state = state
                        current_state_found = True
            if('Candidate % Votes' in lines[line]):
                current_state_leading_candidate = lines[line+1]
                if('trump' in current_state_leading_candidate.lower()):
                    current_state_trailing_candidate = 'Harris'
                else:
                    current_state_trailing_candidate = 'Trump'
            if(
                (current_state_trailing_candidate_vote_percent==0)and 
                (not(current_state_leading_candidate_vote_percent==0))and  
                (search(r"[0-9]{1,}",lines[line]))and
                ('%' in lines[line])
                ):
                current_state_trailing_candidate_vote_percent = float(lines[line].replace('%',''))
            if(
                (current_state_leading_candidate_vote_percent==0)and 
                (search(r"[0-9]{1,}",lines[line]))and
                ('%' in lines[line])
                ):
                current_state_leading_candidate_vote_percent = float(lines[line].replace('%',''))
            if(
                (current_state_trailing_candidate_vote_count==0)and 
                (not(current_state_leading_candidate_vote_count==0))and 
                (search(r'\d+(?:,\d+)?',lines[line]))and
                (not('%' in lines[line]))and
                (not('.' in lines[line]))and
                (not(':' in lines[line]))and
                (not('Elect' in lines[line]))and
                (not(search(r"[A-Za-z]{1,}",lines[line])))
                ):
                current_state_trailing_candidate_vote_count = int(lines[line].replace(',',''))
            if(
                (current_state_trailing_candidate_vote_count==0)and 
                (current_state_leading_candidate_vote_count==0)and 
                (search(r'\d+(?:,\d+)?',lines[line]))and
                (not('%' in lines[line]))and
                (not('.' in lines[line]))and
                (not(':' in lines[line]))and
                (not('Elect' in lines[line]))and
                (not(search(r"[A-Za-z]{1,}",lines[line])))
                ):
                current_state_leading_candidate_vote_count = int(lines[line].replace(',',''))
            if('Est.'in lines[line]):
                current_state_reported_percent = int(search(r"[0-9]{1,}",lines[line]).group())
                results[current_state].loc[extraction_time] = [current_state_leading_candidate,current_state_leading_candidate_vote_percent,
                                                            current_state_leading_candidate_vote_count,current_state_trailing_candidate,
                                                            current_state_trailing_candidate_vote_percent,current_state_trailing_candidate_vote_count,
                                                            current_state_reported_percent]
                if(True):
                    current_state_found = False
                    current_state_leading_candidate = 'None'
                    current_state_leading_candidate_vote_percent = 0
                    current_state_leading_candidate_vote_count = 0
                    current_state_trailing_candidate = 'None'
                    current_state_trailing_candidate_vote_percent = 0
                    current_state_trailing_candidate_vote_count = 0
                    current_state_reported_percent = 0
            if(
                ('Not all candidates are listed' in lines[line])or
                ('All times ET' in lines[line])
              ):
                break

    for key,item in results.items():
        item.to_csv(f"State_Summary_Results/{key}_Results.csv")