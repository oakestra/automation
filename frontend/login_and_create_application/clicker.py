#!/usr/bin/python3

# Install selenium & the webdriver via pip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

IP = "http://192.168.178.35/"  # Replace with your IP

APP_NAME = "selenium"
APP_NAMESPACE = "selenium"

SERVICE_NAME = "selenium"
SERVICE_NAMESPACE = "selenium"
SERVICE_PORT_MAPPING = "80:80"
CONTAINER = "docker.io/library/nginx:latest"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def wait():
    driver.implicitly_wait(5)


driver.get(IP)

# login
username_input_field = driver.find_element("xpath", "//input [@id='mat-input-0']")
username_input_field.send_keys("Admin")
pwd_input_field = driver.find_element("xpath", "//input [@id='mat-input-1']")
pwd_input_field.send_keys("Admin")
login_button = driver.find_element("xpath", "//button [span [text()='Sign in']]")
login_button.click()
wait()

# app creation
add_app_button = driver.find_element(
    "xpath", "//button[span[text()[contains(.,'Add Application')]]]"
)
add_app_button.click()

wait()
app_name_input = driver.find_element("xpath", "//input [@id='mat-input-3']")

app_name_input.send_keys(APP_NAME)
app_ns_input = driver.find_element("xpath", "//input [@id='mat-input-4']")
app_ns_input.send_keys(APP_NAMESPACE)
app_add_button = driver.find_element("xpath", "//button [span [text()='Add']]")
app_add_button.click()
wait()

# service creation
select_app_circle = driver.find_element("xpath", "//input [@id='mat-radio-4-input']")
select_app_circle.click()
wait()

create_new_service_button = driver.find_element(
    "xpath", "//button [span [text()[contains(.,'Create new service')]]]"
)
create_new_service_button.click()
wait()

service_ns_input = driver.find_element("xpath", "//input [@id='mat-input-6']")
service_ns_input.send_keys(SERVICE_NAMESPACE)
service_name_input = driver.find_element("xpath", "//input [@id='mat-input-7']")
service_name_input.send_keys(SERVICE_NAME)
service_virtualization_input = driver.find_element("xpath", "//mat-select [@id='mat-select-0']")
service_virtualization_input.click()
wait()

service_virtualization_container_option = driver.find_element(
    "xpath", "//mat-option [@value='container']"
)
service_virtualization_container_option.click()
service_port_input = driver.find_element("xpath", "//input [@id='mat-input-16']")
service_port_input.send_keys(SERVICE_PORT_MAPPING)
service_code_input = driver.find_element("xpath", "//input [@id='mat-input-19']")
service_code_input.send_keys(CONTAINER)
wait()

service_save_button = driver.find_element("xpath", "//button [span [text()='Save']]")
service_save_button.click()
