# Step 1: Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 2: Set up WebDriver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 3: Open the website to scrape data
driver.get('https://hoopshype.com/salaries/players/')

# Step 4: Scrape player names
players = driver.find_elements(By.XPATH, '//td[@class="name"]')
players_list = [player.text for player in players]

# Step 5: Scrape player salaries
salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')
salaries_list = [salary.text for salary in salaries]

# Step 6: Save the data to a Pandas DataFrame
data = {'Player': players_list, 'Salary': salaries_list}
df = pd.DataFrame(data)

# Step 7: Export the DataFrame to a CSV file   
df.to_csv('nba_player_salaries.csv', index=False)

# Step 8: Quit the driver
driver.quit()

print("Data scraped and saved to 'nba_player_salaries.csv'")
