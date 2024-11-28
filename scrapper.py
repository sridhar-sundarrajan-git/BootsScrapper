
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import time

# Set up the WebDriver (Chrome in this case)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a window)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended in headless mode)
chrome_options.add_argument("--no-sandbox")  # Sometimes needed in headless mode

# Set up the WebDriver (Chrome in this case) with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the webpage
url = "https://www.boots.com/health-pharmacy/medicines-treatments/sleep"
driver.get(url)
driver.maximize_window()

# Wait for the element to be visible (optional, depending on how the page loads)
# Adjust the XPath to match the element you want to interact with.
wait = WebDriverWait(driver, 10)
accept_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
)
accept_button.click()


target_xpath = '//*[@id="hits"]/div/div/div/div[4]/div/div[1]/a'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, target_xpath))
)
product_name = '//*[@id="hits"]/div/div/div/div[4]/div/div[1]/a'
homeLink = wait.until(EC.presence_of_element_located((By.ID, 'widget_breadcrumb')))

productDescription = '//*[@id="contentOmnipresent"]/div'
rating = '//*[@id="estore_pdp_trcol_1"]/div[2]/div/div/button/div[2]'
productPrice = '//*[@id="PDP_productPrice"]'
productNames = wait.until(EC.presence_of_all_elements_located((By.XPATH, product_name)))

for product in productNames:
    product.click()
    driver.save_screenshot('product.png')

    # # driver.execute_script("window.scrollBy(0, 1000);")
    # productDescriptionElement = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, '//*[@id="contentOmnipresent"]/div')))
    # print(productDescriptionElement.text)
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="widget_breadcrumb"]'))
)
    element.click()
    time.sleep(5)

# for productName in productNames:
#     print(productName.text)
#     productName.click()
#     print()
# if isinstance(productNames, list)   # Multiple elements returned
#     for heading in elements:
#         print(heading.text)
# else:  # Single element returned
#     print(elements.text)
# driver.save_screenshot("targetElementDisplayed.png")
# # If the element is found, print the text or any other property
# if element:
#     print(element.text)  # This will print the text inside the <a> tag
# else:
#     print("Element not found.")

# Close the browser window
driver.quit()
