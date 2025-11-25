# TO PRINT THE ENTIRE TABLE 

#Importing webdriver and By Classes
from selenium import webdriver
from selenium.webdriver.common.by import By

# Opens the URL in Chrome browser
driver=webdriver.Chrome()
driver.get('https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/')

# Locates the table using XPATH
table = driver.find_element(By.XPATH, '//caption[text()="Free Coding Resources"]/ancestor::table')

# Locates the table header
header_row = table.find_element(By.XPATH, './/tr[1]')
headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th')]
print("Headers:", headers)

# Locates the table rows
rows=table.find_elements(By.XPATH,'.//tbody/tr')

# Locates the table data in each column
for row in rows:
    cols=row.find_elements(By.TAG_NAME,'td')
    data=[col.text for col in cols]
    print(data)

# Ends the browser session
driver.quit()
