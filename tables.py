from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.freecodecamp.org/news/html-tables-table-tutorial-with-css-example-code/')


table = driver.find_element(By.XPATH, '//caption[text()="Free Coding Resources"]/ancestor::table')

header_row = table.find_element(By.XPATH, './/tr[1]')
headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th')]
print("Headers:", headers)

rows=table.find_elements(By.XPATH,'.//tbody/tr')


for row in rows:

    cols=row.find_elements(By.TAG_NAME,'td')
    data=[col.text for col in cols]
    print(data)
driver.quit()