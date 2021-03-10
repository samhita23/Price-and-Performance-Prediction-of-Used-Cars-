# Price-prediction for Used Cars
## Introduction
In the financial field price prediction is an important forecast for buyers and sellers. The hypothesis of this project focuses on predicting the price and performance of used cars. An e-commerce platform 'Cars24' is the best marketplace containing elaborated details of used cars by primarily showing the price quotes. So studying the features that influence the price is a complex and challenging task as it relies on data hidden patterns and market trends. In this project various Machine learning algorithms will be analyzed and evaluated for accurate statistical results. Hence predicting the price for these used cars helps business to set the budget margins and customer satisfaction. 
### Project Goal
	Data Collection - The data is fabricated from scratch to gain deeper insights on the pricing strategies. Accordingly, the details of used cars are collected from Cars24 website. All the features are scrapped and around 42,000 data points are obtained. 
	Data Cleaning - Data depicts both numerical & categorical information. In which the three main columns pricing, model and rating are analyzed and the empty values in these three columns have been removed by reaching to 32,481 data points. Also missing values in some columns like transmission and insurance are replaced with NULL. Further, some words in each row of a feature are removed and standardized. 
	Data Visualization - Price distribution is visualized against each columns into bar charts, pie chart and interactive charts using Seaborn, matplotlib and plotly libraries. 
	Model -Regression techniques are used to make the prediction and accuracies of models are compared. 
	Interactive Dashboard - The output is imported to Tableau and picturize different worksheets for best selling at different locations. Also making it interactive for customer to select a car based on estimated price and rating.
#### Data Overview
The Data is scrapped from cars24 website using beautifulsoup and is saved as .csv file. Effort is put to fetch the data as it took around 10 hours to pull the links and corresponding features for each car. Finally 14 Columns and 32,000 rows have been saved and examined.
Cars24website--> Scraping using beautifulsoup library --> Fetch the url links for each car --> Extract features --> Save it as .csv files.
##### Data Cleaning 
1) Spliting the columns names
2) Removing the currency symbol in price column
3) Removing words like kilometers, transmission, insurance in KM, Transmission and insurance type columns
4) Rating is given as 4 out of 5 , 4.2 out of 5 etc. So out of 5 is removed in each row.
5) Missing vaules is relpaced with Nan (code is wriiten to check the lengh as 8 and if not present it changes to Nan)
###### Data Visulization 
1) Univarariate visulization plots
(i) Count of price
(ii)Count of City
(iii)Count of cCar Models
(iv) Count of Insurance types
2)Bivariate vizulization graphs 
(i) Price vs City
(ii) Price vs Kilometers
(iii) Price vs Insurance type
(iv) Prive vs transmission
(v) Price vs year of purchase
3) Mutlivariate Graphs
(i) Prive vs city and car model
(ii) Transmission vs pice vs year of purchase
(iii) Pai plots for Price, rating, kilometers and year of purchase
(iv) Correlation matrix and other ploty interactive plots. 
######## Data Preprocessing
Feature transforms
Categorical to numerical 
preparing data to split for train and test 
Model selection and results review.


