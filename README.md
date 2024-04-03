# Data-Science-SpaceX-Capstone
This analysis project uses data collected from a copy of the SpaceX API including launch data and data web scraped from a SpaceX launches wikipedia page using the Python library, Beautiful Soup.

The objectives of the analysis were:
* To determine which attributes of distinct launch attempts contributed the most to a successful launch by the SpaceX Falcon 9 launches. A successful launch attempt is deemed successful if the rocket used was able to be recovered (i.e. landing in the ocean) to reduce the total cost of the launch.
* To determine if machine learning models could be constructed given the dataset to accurately predict future rocket launches to be successful in reducing total cost.

The process included:
1. Data Collection from API and web scraped HTML table data from Wikipedia.
2. Data cleaning and wrangling using CSV files and Pandas Dataframe operations (Replacing missing data, converting categorical data to numerical,
  and creating a binary attribute representing successful launch or failure launch using the landing outcome data).
3. Exploratory Data Analysis using SQL (SQLlite) and Python library, MatPlotLib, charts/graphs for visualizing relationships between attributes.
4. Using Folium to create interactive map visualizations showing the launch sites used for Falcon 9 launches.
5. Using Python PyPlot Dash to create an interactive dashboard displaying pie charts representing launch success rates for a user-entered launch site and a scatterplot showing the correlation between a user-entered range of the mass of the rockets in kilograms and the success rate of launches per the selected launch site.
6. A machine learning pipeline was created to predicate if the first stage of the falcon 9 rocket lands successfully. The pipeline featured Logistic Regression, Support Vector Machines, Decision Trees, and K-nearest neighbors.
