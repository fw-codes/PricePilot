from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

service = Service("chromedriver-win64/chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")
search_query = input("Enter product to search: ")
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.amazon.in")
print("Opened Amazon successfully!")
time.sleep(2)

#Product search
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_query)
search_box.submit()
time.sleep(5)

# Scrolling...
driver.execute_script("window.scrollBy(0, 3000);")
time.sleep(3)


products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
print("Total products found:", len(products))

data = []

for p in products:
    try:
        #ads
        p.find_element(By.XPATH, ".//span[contains(text(),'Sponsored')]")
        continue
    except:
        pass

    #title 
    try:
        title = p.find_element(By.XPATH, ".//a//h2").text
    except:
        title = None

    # price
    try:
        price = p.find_element(By.XPATH, ".//span[@class='a-price']").text
        price = price.replace("\n", ".").replace("₹", "").strip()
    except:
        price = None
           
    #rating
    try:
        rating = p.find_element(By.XPATH, ".//span[contains(@class,'a-icon-alt')]").get_attribute("innerHTML")
        rating = rating.split(" ")[0]
    except:
        rating = None    
    #LINK
    try:
        link = p.find_element(By.XPATH, ".//a").get_attribute("href")
    except:
        link = None     

    if title and price:
        data.append({
            "Product Name": title,
            "Price (INR)": price,
            "Rating": rating,

            "Link": link
        })



df = pd.DataFrame(data)

with pd.ExcelWriter("product_prices.xlsx", engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='products')

    worksheet = writer.sheets['products']

    #MAKING WIDer
    worksheet.column_dimensions['A'].width = 50
    worksheet.column_dimensions['B'].width = 15
    worksheet.column_dimensions['C'].width = 10
    worksheet.column_dimensions['D'].width = 20

    #links as open product
    for row in range(2, len(df) + 2):
        cell = worksheet[f'D{row}']
        url = cell.value
        cell.value = "Open Product"
        cell.hyperlink = url
        cell.style = "Hyperlink"
print("File saved at:", os.getcwd())    #location where the excel file issaved 

#print(df.head())
print(f"Saved {len(df)} products to 'product_prices.xlsx'")
driver.quit()
