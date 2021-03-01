from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://45.79.43.178/source_carts/wordpress/wp-login.php")

user_login = driver.find_element_by_id('user_login')
user_login.clear()
user_login.send_keys("admin")

user_pass = driver.find_element_by_id('user_pass')
user_pass.clear()
user_pass.send_keys("123456aA")

btn_submit = driver.find_element_by_id("wp-submit")

ActionChains(driver).click(btn_submit).perform()

display_name = driver.find_element_by_class_name('display-name').text

print(display_name)
driver.close()