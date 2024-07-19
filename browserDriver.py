from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from functions import *

import time

#TO DO
"""
    Grabbing content from tiktok

    1. Make Tik tok account with the express purpose of generating the kind of content we care about/want to repost

    2. Grab first video's (found on fyp) src link

    3. Download video

    -- Post content steps --

    4. delete video

    5. Repeat steps x amount per day

"""


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

#create webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(40)

driver.get("https://www.tiktok.com/en")

# wait until the page loads to retrieve video
try: 
    WebDriverWait(driver, 15).until(lambda driver: checkSrc(driver))
    print("video found")

except TimeoutError: 
    print("timed out")

#download video
src = driver.find_element(By.TAG_NAME, "video").get_property("src")
print(src)
driver.get(src)

time.sleep(10)

driver.quit()