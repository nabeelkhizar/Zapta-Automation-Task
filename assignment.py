import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//Dell//Downloads//chromedriver.exe")
driver.get("https://stg.zaptatech.com/")
driver.maximize_window()
element = driver.find_element('xpath', '//h4[contains(.,"Midland Apartments")]')
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)
driver.find_element('xpath', '//h4[contains(.,"Midland Apartments")]').click()
time.sleep(3)
#verify that the stay and amenities sections contains the following text
stay_text = driver.find_element(By.XPATH, "//div[@class='col-md-8 left-side']//div[1]//span[1]")
assert stay_text.text == "2 bedrooms"
amenities_text = driver.find_element(By.XPATH, ""//div[@class='col-md-8 left-side']//div[1]//span[1]")
assert amenities_text.text == "4 Guests"
bath_text = driver.find_element(By.XPATH, "//div[@class='col-md-8 left-side']//div[1]//span[1]')
assert bath_text.text == "2 Bath"
wifi_text = driver.find_element(By.XPATH, "//span[normalize-space()='Wifi']")
assert wifi_text.text == "Wifi"
work_area_text = driver.find_element(By.XPATH, "//span[normalize-space()='Work Area']//img[@class='me-3']")
assert work_area_text.text == "Work Area"
full_kitchen_text = driver.find_element(By.XPATH, "//span[normalize-space()='Full Kitchen']")
assert full_kitchen_text.text == "Full kitchen"

timestamp = time.strftime("%H-%M-%S")
driver.save_screenshot("FIRST_" + timestamp + ".png")

#close the browser
driver.close()