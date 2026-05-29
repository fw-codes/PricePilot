# PricePilot-E-commerce Product Scraper using Selenium

PricePilot is a Python-based web automation tool that scrapes product details from e-commerce websites (currently Amazon) and organizes them into a structured Excel file for easy comparison.

It automates repetitive manual tasks like searching products, scrolling listings, extracting data, and filtering out sponsored ads.

---

## 📌 Features

- 🔍 Automated product search on Amazon
- 🤖 Browser automation using Selenium
- 📄 Extracts product details:
  - Product Name
  - Price
  - Rating
  - Product Link
- 🚫 Skips sponsored advertisements
- 📊 Exports clean data into Excel file
- 🔗 Clickable product links in Excel
- 📐 Auto-formatted Excel output

---

## 🛠️ Tech Stack

- Python
- Selenium
- Pandas
- OpenPyXL

---

## ⚙️ How It Works

1. Opens Chrome browser automatically
2. Navigates to Amazon
3. Searches for user-defined product
4. Scrolls and loads product listings
5. Extracts product information
6. Filters out ads
7. Saves data into Excel file

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
