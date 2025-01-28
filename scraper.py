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
players_list = [player.text.strip() for player in players if player.text.strip()]  # Remove empty entries

# Step 5: Scrape player salaries
salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')
salaries_list = [salary.text.strip() for salary in salaries if salary.text.strip()]  # Remove empty entries

# Step 6: Ensure both lists have the same length
if len(players_list) != len(salaries_list):
    print(f"Warning: Mismatched lengths. Players: {len(players_list)}, Salaries: {len(salaries_list)}")
    # Trim to the shorter length to avoid misalignment
    min_length = min(len(players_list), len(salaries_list))
    players_list = players_list[:min_length]
    salaries_list = salaries_list[:min_length]

# Step 7: Save the data to a Pandas DataFrame
data = {'Player': players_list, 'Salary': salaries_list}
df = pd.DataFrame(data)

# Step 8: Export the DataFrame to a CSV file with proper formatting
df.to_csv('nba_player_salaries.csv', index=False, quoting=1)  # quoting=1 ensures proper quoting for fields

# Step 9: Quit the driver
driver.quit()

print("Data scraped and saved to 'nba_player_salaries.csv'")
