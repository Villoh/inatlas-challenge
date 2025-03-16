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

## Crawler Class Documentation

### `__init__` Method

#### Parameters

| Argument    | Type        | Default         | Description                                                                                   |
|-------------|------------|----------------|---------------------------------------------------------------------------------------------------|
| `search_keyword`   | str        | `"Spain"`       | The keyword to search for hotels.                                                             |
| `checkin`      | datetime  | `datetime.now()` | The date and time to check in.                                                                  |
| `checkout`     | datetime  | `datetime.now() + timedelta(days=1)` | The date and time to check out.                                                                |
| `group_adults`   | int        | `1`              | The number of adults in the reservation.                                                         |
| `group_children` | int        | `0`              | The number of children in the reservation.                                                       |
| `max_results`    | int        | `200`            | The maximum number of results to extract from Booking.                                             |

#### Usage

To use the `__init__` method and set specific parameters, you can call it with the desired arguments using `-a`. For example:

```bash
scrapy crawl -a search_keyword="Paris" -a checkin="2024-01-15T14:30" -a checkout="2024-01-17T14:30" -a group_adults=2 -a group_children=1
```

This command will initialize the class with the specified search parameters and additional options. You can customize any of these arguments based on your requirements.