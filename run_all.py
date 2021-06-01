from  selenium import webdriver


driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

print(driver.current_url)


driver.implicitly_wait(5)

driver.quit()










