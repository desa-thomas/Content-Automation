from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import requests

import keyboard, time

directory = "C:/Users/desa2/Desktop/ProjectsDigital Marketing Script"

"""
    Checks if the video found on the page is the tik tok loading video, if so it returns false, otherwise true. 
    This function is passed into "wait.until()", the until function calls this on a loop until the function returns true, 
    effectivly waiting until the page loads. 

    parameter: 
        driver - WebDriver passed into the lambda function (webdriver)

    returns: 
        boolean - true if the video is not the tik tok loading animation. 
"""
def checkSrc(driver):
    src = driver.find_element(By.TAG_NAME, "video").get_property("src")
    print("waiting...")
    return src != "https://sf16-website-login.neutral.ttwstatic.com/obj/tiktok_web_login_static/tiktok/webapp/main/webapp-desktop/playback1.mp4"

#Script starts ---------------------------------------------------------------------------------------------

#create webdriver
driver = webdriver.Chrome()

driver.get("https://www.tiktok.com/en")

# wait until the page loads to retrieve video
try: 
    WebDriverWait(driver, 15).until(lambda driver: checkSrc(driver))
    print("video found")

except TimeoutError: 
    print("timed out")


src = driver.find_element(By.TAG_NAME, "video").get_property("src")

#Copy the selenium sessions cookies to a request session to download the mp4 file. 
cookies = driver.get_cookies()
session = requests.Session()
for cookie in cookies: 
    session.cookies.set(cookie['name'], cookie['value'])

file_bytes = session.get(src).content
with open("video.mp4", "wb") as f:
    f.write(file_bytes)
    print("saved video")

driver.quit()

"""
TODO: 
    1. clean up the script, and possibly split up all tasks into functions and have the script just call a main funciton. 
    2. create a dependencies.txt file, and put all the dependencies of the project into it. 
    3. create the LinkedIn posting aspect of the script. 
"""
