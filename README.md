# Project 3: GeoSpatial Data
Maximiliano Tabó

### Table of Contents:
**1-Intro.**
**2-Goal.**
**3-Data.**
**4-Steps.**
**5-Scoring.**
**6-Visualizations.**



### 1-Intro.
The project is about creating a company in the 'Gaming Industry' with the following structure:
 + 20 Designers
+ 5 UI/UX Engineers
+ 10 Frontend Developers
+ 15 Data Engineers
+ 5 Backend Developers
+ 20 Account Managers
+ 1 Maintenance guy that loves basketball
+ 10 Executives
+ 1 CEO/President.

The starting point is a MongoDB database, that includes more than 18 thousand company with their descriptions.



### 2-Goal.
The Goal is to find the most suitable place to set down our company. For that, we need to dive into the Database and use APIs to enrich the data following the Creteria given:

+ Designers like to go to design talks and share knowledge. 
+ There must be some nearby companies that also do design.
+ 30% of the company staff have at least 1 child.
+ Developers like to be near successful tech startups that have raised at least 1 Million dollars.
+ Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
+ Account managers need to travel a lot.
+ Everyone in the company is between 25 and 40, give them some place to go party.
+ The CEO is vegan.
+ If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
+ The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.





### 3-Data.
In order to run the project the following libraries are needed to be installed:

+ requests
+ folium
+ pandas
+ re
+ os
+ json
+ os
+ seaborn
+ numpy
+ dotenv

### 4-Steps.

Explore the'Companies' file to filter it.
Export it to the Jupyter Notebook.
Set up the Data and do the cleaning, handle missing, incorrect or  not required information, and state Functions to make the work more comfortable.
After dropping the needless columns, proceed to 
drop the rows with missing values that are required, as the coordinates.
Onces the Database is cleant, we have a look to see which cities are the ones with more companies similar to the company we are creating, and chosing one of those. In this case with San Francisco, due to that my cleant Dataframe contains much more companies than the others.
Next, using the APIs with the creteria, we start plotting the map to have an idea where could be the best area for it.
Based on that, we get all the distances between the companies and the places gotten from Foursquare. 

### 5-Scoring.
The scoring was calculated out of the distance from the places, and the number of people envolved in each point of the creteria.

### 6-Visualizations.

####<d> Scoring Plot.<d>_
<img src='/Images/Scoring.png'>





<iframe src='index.html'></iframe>








##### Links and Resources
https://location.foursquare.com/
https://fontawesome.com/
