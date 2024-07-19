from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from functions import *

import time

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
driver.implicitly_wait(40)

driver.get("https://www.tiktok.com/en")

# wait until the page loads to retrieve video
try: 
    WebDriverWait(driver, 15).until(lambda driver: checkSrc(driver))
    print("video found")

except TimeoutError: 
    print("timed out")


src = driver.find_element(By.TAG_NAME, "video").get_property("src")
print(src)
driver.get(src)

#TO DO: got the videos src link, now need to download it from the driver since "requests" library is getting 403

time.sleep(10)

driver.quit()