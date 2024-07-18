from selenium import webdriver
from selenium.webdriver.common.by import By
    
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("")

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


driver.quit()