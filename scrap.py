from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

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

with open('your_file.txt', 'w', encoding='utf-8') as file:
    for paragraph in article:
        # Write the article text to the file
        file.write(paragraph.text)
        #paragraph_text = paragraph.text
        #print(paragraph_text)

print("Article has been written to 'your_file.txt'")

#TODO: Write a function that takes in a URL and writes the article to a file

def write_article_to_file(url, output_file_path):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Get the content of the response
        article_content = response.text

        # Write the content to the specified file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(article_content)

        print(f"Article successfully written to {output_file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from the URL: {e}")

# Example usage
url = "https://example.com"
output_file_path = "output_article.txt"
write_article_to_file(url, output_file_path)
    
#TODO: Given a username, write a function that scrapes all the articles on their proile and writes them to file(s)

def scrape_articles(username):
    # Replace 'https://www.ccthere.com/users/' with the actual URL structure of user profiles on ccthere.com
    user_profile_url = f'https://www.ccthere.com/users/{username}'
    
    # Send a GET request to the user's profile page
    response = requests.get(user_profile_url)
    
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the elements containing articles on the user's profile (adjust based on HTML structure)
        article_elements = soup.find_all('div', class_='article')
        
        # Extract all the article links (urls) on the user page

        # Call write_article_to_file(url, output_file_path) on each article link

driver.quit()
