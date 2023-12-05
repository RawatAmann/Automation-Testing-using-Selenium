from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(10)

# for login page
login=driver.find_element(By.ID,"ap_email")
login.send_keys("amanrawat135790@gmail.com")
time.sleep(2)
submit=driver.find_element(By.ID,"continue")
submit.click()
time.sleep(5)


# for password page
passw=driver.find_element(By.ID,"ap_password")
passw.send_keys("merimataji1")
time.sleep(5)
sign=driver.find_element(By.ID,"signInSubmit")
sign.click()
time.sleep(100)