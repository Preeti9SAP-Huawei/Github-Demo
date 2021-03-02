from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()
#Click on dropdown
dropdown= driver.find_element(By.ID, 'searchDropdownBox')
book = Select(dropdown)
#select 'book' option from dropdown
book.select_by_visible_text('Books')
#click on search button
driver.find_element_by_id('nav-search-submit-button').click()
#Scroll the page
driver.execute_script("window.scrollBy(0,1000)","")
#select english language and click
#menu = driver.find_element_by_xpath("//div[@id ='s-refinements']/div[2]/ul[1]/li[1]/span/a").click()
driver.find_element_by_xpath("//span[contains(text(),'English') and @class ='a-size-base a-color-base']").click()




#extract the tittle
Title = driver.find_element_by_partial_link_text("How To Stop Worrying & Start Living").text
#print the title
print(Title)






