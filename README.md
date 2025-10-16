## Spaceship Titanic Classification
- Welcome to the year 2912. We've received a transmission from four lightyears away and things aren't looking good.
- The Spaceship Titanic was an interstellar passenger liner launched a month ago.
- With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.
- While rounding Alpha Centauri on its route the Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud.
- Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!
- To help rescue the lost passengers, you are challenged to predict which passengers were transported by the anomaly using records recovered from the spaceship’s damaged computer system.
- Help save them and change history!

<hr>

## Dataset
- To help make these predictions, we have a set of records recovered from the ship's damaged computer system.
- **Link to the Dataset :** [Spaceship Titanic Dataset](https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv)

<hr>

## Problem Statement
- To predict whether a passenger was transported to an alternate dimension during the spaceship collision or not.
- To make these predictions, we have a set of records recovered from the ship's damaged computer system.

<hr>

## Streamlit Application
- For my project, I have created a streamlit web app for classifying passenger's in a user friendly way.
- The web app is multi-pages, means you can navigate to different pages through dropdown menu in the sidebar.
    - First Page is home page, which contains the problem statement and information about the dataset.
    - Second Page is web application page, which contains the web application itself used to classify passengers.
- It also contains a contribution section in the sidebar.

**Link to the Application :** [Application](https://spaceship-titanic-classification.streamlit.app/)

<a href="https://spaceship-titanic-classification.streamlit.app/"><img title="Application" src="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/649c907b-7c72-4bfa-9b78-584acec1cc22"></a>

<hr>

## Setting up the Enviroment
Jupyter Notebook is required for this project and you can install and set it up in the terminal.
- Install the Notebook
```
pip install notebook
```
- Run the Notebook
```
jupyter notebook
```

<hr>

## Libraries required for the Project
**NumPy**
- Go to the terminal and run this code
```
pip install numpy
```
**Pandas**
- Go to the terminal and run this code
```
pip install pandas
```
**Matplotlib**
- Go to the terminal and run this code
```
pip install matplotlib
```
**Seaborn**
- Go to the terminal and run this code
```
pip install seaborn
```
**Sklearn**
- Go to the terminal and run this code
```
pip install scikit-learn
```

<hr>

## Getting Started
- Clone this repository to your local machine by using the following command :
```
git clone https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification.git
```

<hr>

## Steps involved in the Project

**Data Cleaning**
- First of all I dropped some unnecessary columns from the dataset like name, passengerId, cabin.
- Then I found nan values in age column which I filled with median of age by fillna() method.
- Then I counted the maximum occuring category for vip, destination, homeplanet and cryosleep column.
- And used them to fill the nan values present in those columns.
- After that I converted transported column to 'int' DataType.
- And finally I dropped all the nan values from RoomService, FoodCourt, ShoppingMall, Spa and VRDeck column.

**Data Visualization**
- Number of Passengers Transported vs Not Transpoprted to their Planets.

<img src="https://github.com/user-attachments/assets/d0a7c482-b630-4a2e-8311-4d66dd0abbac">

- Number of Passengers in their HomePlanet.

<img src="https://github.com/user-attachments/assets/563ffba9-0d6b-4be9-9d5b-f4cd09fe90ce">

- Number of Passengers opted for VIP Service.
  
<img src="https://github.com/user-attachments/assets/7eeab33d-ff99-4cac-b068-a0721a7cacc6">

- Number of Passengers going to their Destinations.

<img src="https://github.com/user-attachments/assets/bc9e6f66-26fe-439a-878b-02f4726d85a0">

**Dummy Variable**
- I created dummy variables for homeplanet and destination column.
- And stored them into their individual DataFrame and then concatenated them into the orignal DataFrame.
- Finally i dropped the original homeplanet and destination column as it is of no use now.

**Data Standardization**
- I used StandardScaler to scale the data into a particular range instead of random values.
- RoomService, FoodCourt, ShoppingMall, Spa and VRDeck column needed standardization.
- Then I dropped the unscaled columns and concatenated the scaled DataFrame into the orignal DataFrame.

**Model Creation**
- I started by creating dependent and independent variables (X, y).
- Then I split the data into traning and testing set by using train_test_split.
- Then I fit the data on support vector classifier and random forest classifier.
- Then I evaluated both the models using classification report and confusion matrix.
- After that I used k-fold cross validation for further testing the robustness of the models.
- So I cheked mean cross_val_score of both svc and rfc to select the best overall model.

## Conclusion
- Trained classification models for classifying if a passenger was transported to an alternate dimension or not.
- Used Random Forest Classifier and SVC to classify the passengers, achieving an accuracy of 78% and 76% respectively.
- Validated the models with k-fold cross-validation.
- Revealing Random Forest's superior robustness with a mean cross-val-score of 77.5% compared to 77.4% of SVC.
- Lastly, I created a web application by using Streamlit.

<div align='left'>
  
**[`^        Scroll to Top       ^`](#spaceship-titanic-classification)**

</div>
