# Technical Challenge 🔍

This repository contains a technical challenge consisting of two exercises that assess web scraping/crawling, data transformation, and reporting skills.

## Exercises

### 1. Web Crawler
- 🕷️ Develop a crawler to extract data from **Booking**.
- 📄 Save at least **200 records** in a **CSV file**.
- ⏳ The crawler should be capable of scraping more data depending on runtime.

### 2. Data Transformation & Reporting
- 🔄 Normalize and transform a given database into structured **CSV files**.
- 📊 Generate specific **reports** based on the transformed data.

## Requirements

To successfully complete this challenge, you need to have the following tools and libraries installed:

### **Programming Language** 💻

- 🐍 **Python 3.13.1** – Ensure you have an updated version for compatibility with required libraries. Probably works with lower versions.

### **Web Crawling - Web Scraping** 🕵️‍♂️ 

- `Scrapy` – For building and managing the web crawler efficiently.
- `scrapy-playwright` - To handle pages that require JavaScript

### **Data Processing** 📖

- `Pandas` – For data manipulation, cleaning, and transformation.

## Setup & Execution
1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Villoh/inatlas-challennge.git
   cd inatlas-challenge
   ```
2. ⚙️ Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. 🎭 Install browsers for playwright
   ```bash
   playwright install
   ```
5. 🕵️‍♂️ Run the crawler:
   ```bash
   cd challenge-1
   scrapy crawl booking_properties
   ```
6. 🔄 Execute the data transformation:
   ```bash
   cd challenge-2
   python main.py
   ```