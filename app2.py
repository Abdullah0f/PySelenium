from selenium import webdriver
import info

browser = webdriver.Chrome()
browser.get("https://eserve.psau.edu.sa/ku/init")
signin_link = browser.find_element_by_id("j_id_id7:login5")
signin_link.click()
username = browser.find_element_by_id("username")
username.send_keys(info.username2)
password = browser.find_element_by_id("password")
password.send_keys(info.password2)
password.submit()
