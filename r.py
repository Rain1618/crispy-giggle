import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

article_num = "4950533"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)


def get_article(article_num):
    url = "https://ccthere.com/article/" + article_num
    driver.get(url)
    element_with_id = driver.find_element(By.ID, "PD"+article_num)

    # Extract the HTML content of the element
    element_html = element_with_id.get_attribute("outerHTML")

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(element_html, 'html.parser')
    return soup.get_text()

def get_user_articles(username):
    url = "https://ccthere.com/user/" + username
    driver.get(url)

#TODO: Instead of printing the text, write it to a file
article = get_article(article_num)
print(article)
with open("article.txt", "w") as f:
    f.write(article)
    
#TODO: Write a function that takes in a URL and writes the article to a file
    
#TODO: Given a username, write a function that scrapes all the articles on their proile and writes them to file(s)

driver.quit()


