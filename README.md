  ## Spaceship Titanic Classification

Hello Everyone,

Here is my classification project based on predicting whether a passenger is transported to an alternate dimension or not.

## Dataset

I used Spaceship Titanic Dataset which is uploaded by Kaggle on their website in competition menu.

**Link to the Dataset :** [Spaceship Titanic Dataset](https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv)

## Problem Statement

- To predict whether a passenger was transported to an alternate dimension during the Spaceship collision with the spacetime anomaly.
  
- To make these predictions, we have a set of personal records recovered from the ship's damaged computer system.

## Streamlit Web App

- For my project, I have created a streamlit web app for finding out if a passenger was transported to an alternate dimensionin or not.

- This web app is multi-pages, means you can navigate to different pages through dropdown menu in the sidebar.

  - First Page is home page, which contains the problem statement and information about the dataset.
 
  - Second Page is web application page, which contains the web application itself used to classify passengers.

- It also contains a contribution section in the sidebar, which lets you contribute to the project by Giving Stars, Forking the Repository and Download ZIP File of the entire Project.

**Link to the Web App :** [Spaceship Titanic App](https://spaceship-titanic-classification.streamlit.app/)

<a href="https://spaceship-titanic-classification.streamlit.app/"><img src="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/649c907b-7c72-4bfa-9b78-584acec1cc22"/></a>

## Table of Contents

- [Setting up the Enviroment](#setting-up-the-enviroment)
- [Libraries required for the Project](#libraries-required-for-the-project)
- [Getting started with Repository](#getting-started)
- [Steps involved in the Project](#steps-involved-in-the-project)
- [Conclusion](#conclusion)

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

## Libraries required for the Project

**Pandas**

- Go to the terminal and run this code
```
pip install pandas
```

- Go to Jupyter Notebook and run this code from a cell
```
!pip install pandas
```

**Matplotlib**

- Go to the terminal and run this code
```
pip install matplotlib
```

- Go to Jupyter Notebook and run this code from a cell
```
!pip install matplotlib
```

**Seaborn**

- Go to the terminal and run this code
```
pip install seaborn
```

- Go to Jupyter Notebook and run this code from a cell
```
!pip install seaborn
```

**Sklearn**

- Go to the terminal and run this code
```
pip install scikit-learn
```

- Go to Jupyter Notebook and run this code from a cell
```
!pip install scikit-learn
```

## Getting Started

- Clone this repository to your local machine by using the following command :
```
git clone https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification.git
```

## Steps involved in the Project

**Data Cleaning**

- First of all I dropped some unnecessary column from our dataset i.e Name, PassengerId, Cabin.

- Then I found nan values in age column which I filled with median of age by fillna() method.

- Then I count the maximum occuring element from VIP, Destination, HomePlanet, CryoSleep column and used them to fill the nan values present in those columns.

- After that I transformed Transported column to **'int'** DataType.

- Then I dropped all the nan values from RoomService, FoodCourt, ShoppingMall, Spa, VRDeck column.

**Data Visualization**

- I used countplot() to visualize all the categorical variables from the dataset by using sns.countplot() method.

- Number of passengers transported vs not transpoprted to their Planets

![__results___69_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/18b89805-1522-4d61-84e1-ce4c783c0267)

- Number of passengers with their respective HomePlanet

![__results___71_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/537abe8d-2021-4744-8e8a-0eba692664a6)

- Number of passengers opted for VIP service

![__results___73_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/f1108956-32d3-4d4d-b6e6-87b23e463c95)

- Number of passengers with their respective destinations

![__results___75_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/23e3a915-48d5-427f-b64e-b9cc47045030)


**Dummy Variable**

- I created dummy variables for HomePlanet and Destination column and stored them into their individual DataFrame and then concatenated them into our orignal DataFrame.

- Then I dropped the HomePlanet and Destination Column as it is of no use now.

**Data Standardization**

- I used StandardScaler to scale the data to a particular scale instead of random values.

- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck column are the columns which get standardized and then I stored them into a DataFrame.

- Then I dropped the unscaled columns and concatenated the scaled DataFrame into our orignal DataFrame.

**Imbalance Data**

- After that I found that VIP column is highly imbalance which can reduce our model accuracy.

- So I divided our DataFrame into 2 parts based on people who opted for VIP service or not.

- Then I upscaled the VIP people to non VIP people as number of VIP people is much lesser than the number of non VIP people.

- Then I used sns.countplot() to verify that both the values are evenly balanced.

**Model Creation**

- Firstly I have definied dependent and independent variables for our traning and testing.

- Then I splitted the data into traning and testing set by using train_test_split.

- Then I fit the model with X_train and y_train on support vector machine and random forest classifier and checked the score.

- After that I used kfold_cross_validation for further testing the accuracy of our model.

- So I cheked mean cross_val_score of both svm and random forest classifier for best score.

## Conclusion

- Implemented random forest classifier and svm model to achieve an accuracy score of 88% and 83% respectively.

- Validated random forest with a mean cross_val_score of 88% and demonstrated its superior robustness compared to svm with a mean cross_val_score of 81%.

<div align='left'>
  
**[`^        Scroll to Top       ^`](#spaceship-titanic-classification)**

</div>
