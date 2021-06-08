
from selenium import webdriver
from urllib3.poolmanager import PoolManager  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select
import requests
from selenium.webdriver.support.select import Select
print("Website started")  
a=driver=webdriver.Chrome(ChromeDriverManager().install())  
driver.maximize_window()  
#navigate to the url  
print(a.title)
print(a.current_url)
driver.get("https://www.thesparksfoundationsingapore.org/") 
print("\nTest Cases\n")

#Test Case 1:Title
print("Test Case 1:")
if a.title:
    print("Title Exists and Verified: ",a.title)
    print("\n")
else:
    print("Title Not Verified")

#testCase 2:To find logo of the webpage
print("Test case 2:")
try:
    a.find_element_by_xpath('/html/body/div[1]/div/div[1]/h1/a/img').click()
    print("logo is present\n")
    time.sleep(2)
except NoSuchElementException:
    print("No logo present")

#testCase 3:To find NavBar
print("testcase 3:")
try:
    a.find_element_by_class_name("navbar")
    print("Navbar Exists\n")
except NoSuchElementException:
    print("Navbar dosenot Exists")
#testCase 4:Home Button
print("Testcase 4:")
try:
    a.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home Button Exists\n")
except NoSuchElementException:
    print("Home Button Dosenot exists")

#testCase 5:About Us Page
print("TestCase 5:")
try:
    a.find_element_by_link_text('About Us').click()
    time.sleep(2)
    a.find_element_by_link_text('Vision, Mission and Values').click()
    time.sleep(3)
    print("page is visited And exists\n")
except NoSuchElementException:
    print("page doesnot exists")

#testCase 6:policies and code page
print('testcase 6')
try:
    a.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    a.find_element_by_link_text('Policies').click()
    time.sleep(3)
    print("Policies page is verified\n")
except NoSuchElementException:
    print("Policies page is not verified")

#Test case7:Programs Page
print('testcase 7')
try:
    a.find_element_by_link_text('Programs').click()
    time.sleep(3)
    a.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(3)
    print('Student Scholarship Program exist')
    a.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(3)
    print('Student Mentorship Program exists')
    print('proogram page Verified')
    time.sleep(3)
    a.find_element_by_link_text('Workshops').click()
    print('workshop page exists\n')
except NoSuchElementException:
    print('Falied')

#TestCase 8:Links Page:
print('Test Case 8')
try:
    a.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    a.find_element_by_link_text('AI in Education').click()
    time.sleep(3)
    print('Links page verified\n')
except NoSuchElementException:
    print('Links page not verified')

# TestCase 9:Form
print('Test Case 9:')
try:
    a.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    a.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    a.find_element_by_name('Name').send_keys("Sanjeev Kumar Mendegar")
    time.sleep(3)
    a.find_element_by_name('Email').send_keys('msanjeev.2000@gmail.com')
    time.sleep(3)
    select=Select(a.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    a.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]').click()
    time.sleep(3)
    print("form verified\n")
except NoSuchElementException:
    print("form not verified")

# TestCase 10:Contact Us Page
print("TestCase 10:")
try:
    a.find_element_by_link_text('Contact Us').click()
    time.sleep(3)
    b=a.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)
    print(b.text)
    if b.text =="+65-8402-8590, info@thesparksfoundation.sg":
        print('contact Information is verfied')
    else:
        print('contact Information is not verfied')
    print('contact page exits')
except NoSuchElementException:
    print('contact page not verified')

a.close()