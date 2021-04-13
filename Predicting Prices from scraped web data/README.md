# Predicting tomato prices from web-scraped data

The project focuses on programming a web scraper to extract data in a csv format and
consequently modeling an ML program to predict prices of Tomatoes.

## Description

URL scraped : https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=30-Jun-2020&DateTo=30-Jun-2020&Fr_Date=30-Jun-2020&To_Date=30-Jun-2020&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--

The URL given above contains prices of various commodities across different states of India. I developed
a web scraper that can download tabular information for Tomato prices in Karnataka from Jan-01-
2015 to Feb-01-2021. 

After obtaining the CSV file, I then developed an XGB model to predict Modal Price for different locations.

## Getting Started

### Dependencies

* Selenium, webdriver-manager
* Conventional data science libraries like numpy, pandas, train_test_split, GridSearchCV, etc.

### Executing program

* The web scraper was run locally as selenium requires a web browser in order to scrape data.
* The XGB model was trained on Colab after uploading Agr

## Authors

Contributors names and contact info

Ishan Rai - [@ishan-rai](https://www.linkedin.com/in/ishan-rai/)
