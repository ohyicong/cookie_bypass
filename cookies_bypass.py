#selenium libraries
from selenium import webdriver
import os
import getpass
import time

options = webdriver.ChromeOptions()

#Find your google cookie directory
path_to_chrome_cookie="user-data-dir=C:\\Users\\OHyic\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(path_to_chrome_cookie) #Path to your chrome profile
driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe", options=options)

#go to the website that you want to bypass
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

time.sleep(30)
#dont forget to close your driver, as chrome cookie can only work on one thread.
driver.close()













