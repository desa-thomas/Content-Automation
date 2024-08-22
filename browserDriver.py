from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import requests
import time
import pathlib

def checkSrc(driver: webdriver.Chrome) -> bool:
    """
    Checks if the video found on the page is not the tik tok loading video. 

    ### Parameters
        driver : webdriver.Chrome
            - WebDriver passed into the lambda function (webdriver)

    ### Returns
        boolean : bool
            - true if the video is not the tik tok loading animation. 
    """ 

    src = driver.find_element(By.TAG_NAME, "video").get_property("src")
    print("waiting...")
    
    # Returns true when the video is not the loading animation
    return src != "https://sf16-website-login.neutral.ttwstatic.com/obj/tiktok_web_login_static/tiktok/webapp/main/webapp-desktop/playback1.mp4"


def scrape_video(driver: webdriver.Chrome): 
    """
    Scrapes first Tiktok video from user's for you page (must be logged in on driver). Saves video to "video.mp4"

    ### parameters
        driver : webdriver.Chrome
            - chrome webdriver doing the scraper
    ### returns
        nothing
    """
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
        f.close()
    
    return 


#---------------------------------------------------------------------------------------
#script
directory = pathlib.Path().absolute()

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument(f"--user-data-dir={directory}\\userdata")

#create webdriver
driver = webdriver.Chrome(options = chrome_options)

scrape_video(driver)

driver.quit()

"""
TODO: 
    1. clean up the script, and possibly split up all tasks into functions and have the script just call a main funciton. 
    2. create a dependencies.txt file, and put all the dependencies of the project into it. 
    3. create the LinkedIn posting aspect of the script. 
"""
