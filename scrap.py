from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://ccthere.com/article/4950533"

driver = webdriver.Chrome()
driver.get(url)

# #Press on button to expand the article
# button = driver.find_elements(By.XPATH, '//button[text()="一展到底"]') #SEraching by XPATH returns a list. You need to iterate through list to get the element
# for b in button:
#     b.click()

#Get the text of the article
article = driver.find_elements(By.XPATH, "//article") 

for paragraph in article:
    print(paragraph.text)

#TODO: Instead of printing the text, write it to a file

    
#TODO: Write a function that takes in a URL and writes the article to a file
    
#TODO: Given a username, write a function that scrapes all the articles on their proile and writes them to file(s)

driver.quit()
