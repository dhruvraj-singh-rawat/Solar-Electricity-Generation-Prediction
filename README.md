# Solar Electricity Generation Prediction


## Objective

*Note*: This work is published in [Advances in Intelligent Systems and Computing](https://link.springer.com/chapter/10.1007/978-981-16-0730-1_28)

Electricity production through PV stations are highly variable and heavily depends upon the solar irradiance at a location and environmental factors. 

The objective of the work is, if the weather can be predicted, then the prediction of solar power generation is also possible. This would lead to significant reduction in not only greenhouse emissions but also reduction in operating cost of any organization. In this work, data from LNMIIT PV station were used for analysis. 

- Location of different PV Stations at LNMIIT 
![Map](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/map.png)


**Q: Why Solar Energy ?**

- India, being a tropical country is blessed with 1600-2000 kWh/m2 of solar irradiation and 250-300  sunny days. 
- Solar prices are now within 15% of coal. During 2020 electricity from solar were actually 10% cheaper than domestic coal.
- Commitment of Government of India to reduce its greenhouse gas emissions under the Conference of the Parties (COP) in Paris-France.


## Data Acquisition 

At LNMIIT, the PV Panels used were from Fronius and the image below how the admin dashboard used to looklike. 

![Fronius Dashboard](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/Dashboard.png)

Since we didn't had any APIs to automatically fetch the data for each Dates from the portal, following steps were performed to manually fetch it.

![Data Scraping](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/DataScraping.png)

 
The weather data was fetched from [Weather Underground](https://www.wunderground.com/) using their DEV API. 

## Data Prepossessing

1. Weather information was available at 30 minutes interval whereas solar production was available in 5 min. Dropped all values in between values.
2. Turned all ‘None’ and ‘NaN values to 0. 
3. Removed values that belongs to time other than from 6AM-6PM as in other timings no sunlight is present


![Pre-Prossessing](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/Prepossessing.png)

## Dataset Information 

![Dataset-Information](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/dataset.png)

## Data Analysis

Theoretically, the solar power is proportional to the irradiance. We are claiming that solar power is also proportional to the local weather. 
To prove it, we need to find the correlation between **produced power** and the **weather**.

![Pre-Prossessing](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/Correlation.png)

## Model Performance 

- Regression problems R2 score is widely used as an indicator for quality of prediction. It represents quality of fit of the regression line. Hence R2 in this paper score has been used as evaluation metric.
- Best parameters were selected using GridSearchCV

![Model-Performance](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/ModelPerformance.png)


## Results 

Following results were generated using Random Forest ( Best Performing Model ) 

- On a Random Day
![Random-Day](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/randomDay.png)

- On randomly selected 200 Data-Points
![Sample-Points](https://github.com/dhruvraj-singh-rawat/Solar-Electricity-Generation-Prediction/blob/master/%20Screenshots/randomPoints.png)

In this work, I tried to develop mechanism to forecast solar power in LNMIIT campus which has multiple solar station. After overcoming with nuances with the quality of data, developed mechanism to identify and eliminate outliers. I applied various regression mechanism to forecast solar power and found that **Random Forest Regressor** gave the best results.






