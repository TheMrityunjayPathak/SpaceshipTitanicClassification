  ## Spaceship Titanic Classification

Welcome to the year 2912. We've received a transmission from four lightyears away and things aren't looking good.

The Spaceship Titanic was an interstellar passenger liner launched a month ago.

With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.

While rounding Alpha Centauri on its route the Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud.

Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!

To help rescue the lost passengers, you are challenged to predict which passengers were transported by the anomaly using records recovered from the spaceship’s damaged computer system.

Help save them and change history!

## Dataset

To help make these predictions, we have a set of records recovered from the ship's damaged computer system.

**Link to the Dataset :** [Spaceship Titanic Dataset](https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv)

## Problem Statement

- To predict whether a passenger was transported to an alternate dimension during the spaceship collision with the spacetime anomaly.
  
- To make these predictions, we have a set of personal records recovered from the ship's damaged computer system.

## Streamlit Web App

- For my project, I have created a streamlit web app for finding out if a passenger was transported to an alternate dimensionin or not.

- This web app is multi-pages, means you can navigate to different pages through dropdown menu in the sidebar.

  - First Page is home page, which contains the problem statement and information about the dataset.
 
  - Second Page is web application page, which contains the web application itself used to classify passengers.

- It also contains a contribution section in the sidebar, which lets you contribute to the project by Giving Stars, Forking the Repository and Download ZIP file of the entire Project.

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

## Getting Started

- Clone this repository to your local machine by using the following command :
```
git clone https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification.git
```

## Steps involved in the Project

**Data Cleaning**

- First of all I dropped some unnecessary column from the dataset like Name, PassengerId, Cabin.

- Then I found nan values in age column which I filled with median of age by fillna() method.

- Then I count the maximum occuring category from VIP, Destination, HomePlanet, CryoSleep column.

- And used them to fill the nan values present in those columns.

- After that I transformed Transported column to 'int' DataType.

- Then I dropped all the nan values from RoomService, FoodCourt, ShoppingMall, Spa, VRDeck column.

**Data Visualization**

- I used countplot() to visualize all the categorical features from the dataset.

- Number of passengers transported vs not transpoprted to their planets.

![__results___69_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/18b89805-1522-4d61-84e1-ce4c783c0267)

- Number of passengers with their respective HomePlanet.

![__results___71_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/537abe8d-2021-4744-8e8a-0eba692664a6)

- Number of passengers opted for VIP service.

![__results___73_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/f1108956-32d3-4d4d-b6e6-87b23e463c95)

- Number of passengers with their respective destinations.

![__results___75_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/23e3a915-48d5-427f-b64e-b9cc47045030)


**Dummy Variable**

- I created dummy variables for HomePlanet and Destination column.

- Stored them into their individual DataFrame and then concatenated them into the orignal DataFrame.

- Then I dropped the HomePlanet and Destination column as it is of no use now.

**Data Standardization**

- I used StandardScaler to scale the data to a particular range instead of random values.

- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck column are the columns which get standardized and then I stored them into a DataFrame.

- Then I dropped the unscaled columns and concatenated the scaled DataFrame into the orignal DataFrame.

**Imbalance Data**

- After that I found that VIP column is highly imbalance which can make the model baised to the majority class.

- So I divided the data into 2 parts based on people who opted for VIP service or not.

- Then I upscaled the VIP people to non VIP people because number of VIP people is much lesser than the number of non VIP people (VIP <<< Non-VIP).

- Then I used sns.countplot() to verify that both the categories are evenly balanced.

**Model Creation**

- I started by defining dependent and independent variables (X, y).

- Then I split the data into traning and testing set by using train_test_split.

- Then I fit the data on support vector machine and random forest classifier and checked the score.

- After that I used k-fold_cross_validation for further testing the robustness of the models.

- So I cheked mean cross_val_score of both svm and random forest classifier to select the best model.

## Conclusion

- Trained machine learning models for classifying if a passenger was transported to an alternate dimension or not.
  
- Used Random Forest and SVM to classify the passengers, achieving an accuracy of 88% and 83% respectively.
  
- Validated the models with k-fold cross-validation.

- Revealing Random Forest's superior robustness with a mean cross-val-score of 88% compared to 81% of SVM.
  
- Lastly, I created a web application by using Streamlit.

<div align='left'>
  
**[`^        Scroll to Top       ^`](#spaceship-titanic-classification)**

</div>
