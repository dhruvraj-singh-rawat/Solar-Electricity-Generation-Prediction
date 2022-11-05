# Solar Electricity Generation Prediction


## Objective

*Note*: This work is published in [Advances in Intelligent Systems and Computing](https://link.springer.com/chapter/10.1007/978-981-16-0730-1_28)

Electricity production through PV stations are highly variable and heavily depends upon the solar irradiance at a location and environmental factors. 

The objective of the work is, if the weather can be predicted, then the prediction of solar power is also possible. This would lead to significant reduction in not only greenhouse emissions but also reduction in operating cost of any organization.

**Q: Why Solar Energy ?**

- India, being a tropical country is blessed with 1600-2000 kWh/m2 of solar irradiation and 250-300  sunny days. 
- Solar prices are now within 15% of coal. During 2020 electricity from solar were actually 10% cheaper than domestic coal.
- Commitment of Government of India to reduce its greenhouse gas emissions under the Conference of the Parties (COP) in Paris-France.


## Data Acquisition 

At LNMIIT, the PV Panels used were from Fronius and the image below how the admin dashboard used to looklike. 

![Fronius Dashboard](/Screenshots/Dashboard.png)

Since we didn't had any APIs to automatically fetch the data for each Dates from the portal, following steps were performed to manually fetch it.

![Flowchart](/Screenshots/DataScraping.png ,"Data Scraping")

 
The weather data was fetched from [Weather Underground](https://www.wunderground.com/) using their DEV API. 

