
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.find_element_by_name('q').send_keys('Naveen automation')
elements = driver.find_elements_by_xpath("//ul[@class='erkvQe']/li")
print(len(elements))

for ele in elements:
 print(ele.text)
 if ele.text == "naveen automation labs udemy":
   ele.click()
   break
#########################checkbox###########from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
checkboxs = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
for checkbox in checkboxs:
    if checkbox.get_attribute('value') == "blue":


        checkbox.click()

        assert checkbox.is_selected()

##################windohandles############################
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//button[@id ='openwindow']").click()
childwindow = driver.window_handles[1]
driver.maximize_window()

childelemnt=driver.find_element_by_tag_name("//div[@class ='col-sm-6 col-md-8 hidden-xs video-banner']/h3").text
print(childelemnt)
driver.close()
mainwindow = driver.window_handles[0]
mainwindow_element= driver.find_element_by_xpath("//input[@id ='name']").text
print(mainwindow_element)
############################mouse####################################
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


action =ActionChains(driver)
menu = driver.find_element_by_id('mousehover')
action.move_to_element(menu).perform()
Childmenu = driver.find_element_by_link_text('Top')
action.move_to_element(Childmenu).click().perform()
Childmenu1 = driver.find_element_by_link_text('Reload').click()
action.move_to_element(Childmenu).click().perform()

################frames#########################
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
#frame #name#value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_xpath("//body[@id ='tinymce']").clear()
driver.find_element_by_xpath("//body[@id ='tinymce']").send_keys('Hi how are u')
driver.switch_to.default_content()
frametext= driver.find_elements_by_tag_name("h3").text
print(frametext)

##########clicks############################
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
#frame #name#value
action =ActionChains(driver)
menu = driver.find_element_by_xpath("//input[@id ='double-click']")
#action.double_click(menu).perform()
#time.sleep(2)
#alert = driver.switch_to.alert
#print(alert.text)
#alert.accept()
action.context_click(menu).perform()
time.sleep(2)






