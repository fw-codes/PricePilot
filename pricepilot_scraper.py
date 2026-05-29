from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

service = Service(r"C:\Users\FAARIAH WASEEM\Desktop\chromedriver-win64\chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in")
print("Opened Amazon successfully!")
time.sleep(2)

# Search product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("HP Laptop")
search_box.submit()
time.sleep(5)

# Scroll down to load more products
driver.execute_script("window.scrollBy(0, 2000);")
time.sleep(3)

# Find all product containers
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
print("Total products found:", len(products))

data = []

for p in products:
    try:
        # Skip ads
        p.find_element(By.XPATH, ".//span[contains(text(),'Sponsored')]")
        continue
    except:
        pass

    # Extract title
    try:
        title = p.find_element(By.XPATH, ".//h2//span").text
    except:
        title = None

    # Extract price (handles multiple formats)
    try:
        price = p.find_element(By.XPATH, ".//span[@class='a-price']").text
        price = price.replace("\n", ".").replace("₹", "").replace(",", "").strip()
    except:
        price = None

    if title and price:
        data.append({
            "Product Name": title,
            "Price (INR)": price
        })

# Save to Excel
df = pd.DataFrame(data)
df.to_excel("amazon_prices.xlsx", index=False)

print(f"✅ Saved {len(df)} products to 'amazon_prices.xlsx'")
driver.quit()