import undetected_chromedriver as uc
#By = uc.selenium.webdriver.common.by.By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait = uc.selenium.webdriver.support.ui.WebDriverWait
EC = uc.selenium.webdriver.support.expected_conditions

opts = uc.selenium.webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = uc.Chrome(chrome_options=opts)

def google_signin(email, password):
    driver.get("https://google.com")

    #d=driver.find_element(By.XPATH, "//a[contains(., 'https://accounts.google.com')]")
    login_button=driver.find_element(By.XPATH, "//a[contains(@href, 'https://accounts.google.com')]")
    login_button.click()

    input_email=driver.find_element(By.XPATH, "//input[contains(@type, 'email')]")
    input_email.send_keys(email)

    button_next=driver.find_element(By.XPATH, "//button[contains(., 'Avançar')]")
    button_next.click()

    password_xpath = "//input[contains(@type, 'password')]"
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))

    input_password=driver.find_element(By.XPATH, password_xpath)
    input_password.click()
    input_password.send_keys(password)

    button_next=driver.find_element(By.XPATH, "//button[contains(., 'Avançar')]")
    button_next.click()


