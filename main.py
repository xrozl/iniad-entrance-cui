import subprocess
import time
import platform
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

option: Options = Options()
#option.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)


if not platform.system() == "Darwin":
    print('This script is only for MacOS')
    exit()

def ssid() -> str:
    if platform.system() == "Darwin":
        return subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'", shell=True).decode('utf-8').strip()
    else:
        return None

print(f'SSID: {ssid()}')
if ssid() == "iniad":
    print('INIAD Wifi not connected')
    exit()
else:
    print('INIAD Wifi connected')
    clazz: str = "btn btn-lg btn-info"
    driver.get('https://moocs.iniad.org/')
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/p[2]/a').click()
    time.sleep(2)
    username: str = input('Username: ')
    password: str = input('Password: ')
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[1]/input').send_keys(username)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[2]/input').send_keys(password)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[4]/input').click()
    time.sleep(2)
    if driver.title == "INIAD ID Manager":
        print("Login Failed")
        exit()
    else:
        print("Login Success")
        time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div/form/fieldset/div[2]/div[1]/button[2]').click()
    time.sleep(1)
    driver.get('https://moocs.iniad.org/courses/2022/BOFFICE/00/00')
    time.sleep(2)

