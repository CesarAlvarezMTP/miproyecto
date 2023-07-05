from selenium import webdriver

driver = webdriver.Chrome('C:/Users/cesar.alvarez/workspaces/test-lab/chromedriver.exe')

try:
    driver.get('https://www.google.com')
    accept_button = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('temperatura en Madrid')
    search_box.submit()


    result_element = driver.find_element_by_id('wob_tm')
    temperatura = int(result_element.text)


    if temperatura > 30:
        print("Alto")
    else:
        print("No tan alto")

finally:
  time.sleep(5)
  driver.close()
  driver.quit()