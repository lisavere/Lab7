from selenium import webdriver
import os 
link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
driver.get(link)

input1 = driver.find_element_by_name('firstname')
input1.send_keys("Елизавета")
input2 = driver.find_element_by_name('lastname')
input2.send_keys("Верепекина")
input3 = driver.find_element_by_name('email')
input3.send_keys("verepekinaelizabeth@yandex.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt') 

option3 = driver.find_element_by_tag_name('button')
option3.submit()