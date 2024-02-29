from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
import time
from dotenv import load_dotenv
import os


# 디스코드 웹훅 URL
load_dotenv()
webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

# 확인할 사이트 URL
TARGET_URL = "https://kloa.gg/merchant"

driver = webdriver.Chrome() 
driver.get(TARGET_URL)
time.sleep(2)

#서버선택
element = driver.find_element(By.ID, "headlessui-combobox-input-:r2:")
element.click()

time.sleep(0.5)
#루페온
lupeon_element = driver.find_element(By.XPATH, "//span[text()='루페온']")
lupeon_element.click()

time.sleep(0.5)
div_text = driver.find_element(By.CSS_SELECTOR, 'div.mb-\\[30px\\]').text


def send_discord_message(webhook_url, message):
    
    data = {
        "content": message
    }
    response = requests.post(webhook_url, data=json.dumps(data),
                             headers={"Content-Type": "application/json"})
    
    if response.status_code != 204:
        raise ValueError(f"Request to discord returned an error {response.status_code}, the response is:\n{response.text}")

def check_strings(main_str, sub_strs):
    for sub_str in sub_strs:
        if sub_str in main_str:
            discord_send_message = f"{datetime.now().strftime('%H:%M')} {sub_str} 출현"
            send_discord_message(webhook_url, discord_send_message)
        else:
            print(f"'{sub_str}' 없음")
            
sub_strs = ["웨이", "아만", "아제나","바훈"]


check_strings(div_text, sub_strs)