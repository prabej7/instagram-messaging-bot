from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

option = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2  
}
option.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=option)

url = "https://www.instagram.com/"

driver.get(url=url)

your_username = "your_username"
your_password = "your_password"

username = driver.find_element(By.NAME,"username")
time.sleep(2)
username.send_keys(your_username)

password = driver.find_element(By.NAME,"password")
time.sleep(2)
password.send_keys(your_password)

login = driver.find_element(By.CSS_SELECTOR,"._acan._acap._acas._aj1-._ap30")
time.sleep(2)
login.click()

time.sleep(10)
try:
    save = driver.find_element(By.CSS_SELECTOR,"._acan._acap._acas._aj1-._ap30")
except:
    print("Saved not found")
else:
    save.click()

time.sleep(2)

driver.get(url=f"https://www.instagram.com/{your_username}/following/")

try:
    following_btn = WebDriverWait(driver=driver,timeout=10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a')))
except:
    print('Element not found')
else:
    following_btn.click()

following_users = []


try:
    for i in range(1,11):
        if i==11:
            break
        user = WebDriverWait(driver=driver,timeout=10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span')))
        print(user.text)
        following_users.append(user.text)
except:
    print('Following not found')
    time.sleep(100)


driver.get(url="https://www.instagram.com/direct/inbox/")


new_chat = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div')))
new_chat.click()

try:
    username_msg = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))
except:
    print("Element not found!")
else:
    random_user = random.choice(following_users)
    username_msg.send_keys(random_user)

try:
    current_user = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div')))
except:
    print('Element not found!')
else:
    current_user.click() 

try:
    chat = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
except:
    print('Chat button not found!')
else:
    time.sleep(2)
    chat.click()

try:
    msg = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div')))
except:
    print("Input box not found!")
else:
    msg.send_keys("Hello")

try:
    send_btn = WebDriverWait(driver=driver,timeout=2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')))
except:
    print('Send button not found!')
else:
    send_btn.click()
    
time.sleep(5)
driver.close()





