from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

username = "put your instagram id"
password = "put your instagram password" 

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def login_to_instagram():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)
    
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(5)

def scrape_hashtag_posts(tag):
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(5)

    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
    
    print(f"\n📌 Trending Posts for #{tag}:\n")
    for link in post_links:
        print("🔗", link.get_attribute("href"))

login_to_instagram()
scrape_hashtag_posts("reels")
driver.quit()
