## Spaceship Titanic Classification

Hello Everyone,

Here is My Classification Project based on Predicting which Passenger is transported to an Alternate Dimension.

## Dataset

I used Spaceship Titanic Dataset which is uploaded by Kaggle on their Website in Competition Menu.

**Link to the Dataset :** [Spaceship Titanic Dataset](https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv)

## Problem Statement

- To predict whether a passenger was transported to an alternate dimension during the Spaceship collision with the spacetime anomaly.
  
- To make these predictions, we have a set of personal records recovered from the ship's damaged computer system.

## Streamlit Web App

- For my Spaceship Titanic Classification Project, I have created a Streamlit Web App for Finding out If a Passenger was Transported to an Alternate Dimensionin or not.

- This Web App allows you to classify the Passengers based on some Features and Criteria and Predict Whether They were transported or not.

- This Web App is Multi-Pages, means you can navigate to different pages through dropdown menu in Sidebar.

  - First Page is Home Page, which contains all information about the Problem Statement and Dataset.
 
  - Second Page is Web Application Page, which contains the interactive web application itself used to classify Passengers.

- It also contains a Contribution Section in the Sidebar, which lets you contribute to the project by Giving Stars, Forking the Repository and Download ZIP File of the Entire Project.

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

- Go to Terminal and run this Code
```
pip install pandas
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install pandas
```

**Matplotlib**

- Go to Terminal and run this Code
```
pip install matplotlib
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install matplotlib
```

**Seaborn**

- Go to Terminal and run this Code
```
pip install seaborn
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install seaborn
```

**Sklearn**

- Go to Terminal and run this Code
```
pip install scikit-learn
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install scikit-learn
```

## Getting Started

- Clone the repository to your local machine using the following command :
```
git clone https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification.git
```

## Steps involved in the Project

**Data Cleaning**

- First of all I dropped the Text Column and Some Unnecessary Column from our Dataset i.e Name, PassengerId, Cabin.

- Then I found NaN Values in Age Column which I filled with Median of Age by fillna(df["Age"].median()) Method.

- Then I count the Maximum Occuring Element from VIP, Destination, HomePlanet, CryoSleep Column and used them to fill the NaN Values present in those Columns.

- After that I converted Transported Column to int DataType.

- Then I dropped all NaN Values from RoomService, FoodCourt, ShoppingMall, Spa, VRDeck Column.

**Data Visualization**

- I used CountPlot to visualize all Categorical Variables from the Dataset by using sns.countplot() Method.

- Number of Passengers Transported vs Not Transpoprted to their Planets

![__results___69_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/18b89805-1522-4d61-84e1-ce4c783c0267)

- Number of Passengers with their respective HomePlanet

![__results___71_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/537abe8d-2021-4744-8e8a-0eba692664a6)

- Number of Passengers opted for VIP Service

![__results___73_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/f1108956-32d3-4d4d-b6e6-87b23e463c95)

- Number of Passengers with their respective Destinations

![__results___75_1](https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/assets/123563634/23e3a915-48d5-427f-b64e-b9cc47045030)


**Dummy Variable**

- I created Dummy Variable for HomePlanet and Destination Column and stored them into their individual DataFrame and then concatenated them into our Orignal DataFrame.

- Then I dropped the HomePlanet and Destination Column as it is of no use now.

**Data Standardization**

- I used StandardScaler to scale the Data to a Particular Interval of Values instead of Random Values.

- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck Column are the Columns which get Standardized and then I Stored them into ScaledValues DataFrame.

- Then I dropped the Unscaled Columns and concatenated the Scaled Column DataFrame into our Orignal DataFrame.

**Imbalance Data**

- After that I found that VIP Column is highly imbalance which can reduce our Model Accuracy.

- So I divided our DataFrame into 2 Parts based on People who opted for VIP Service or Not.

- Then I upscaled the VIP People to Non VIP People as Number of VIP People is much lesser than Number of Non VIP People.

- Then I used sns.countplot(x="VIP",data=df4) to verify that both the Values are evenly Balanced.

**Model Creation**

- Firstly I have definied Dependent and Independent Variables for our Traning and Testing.

- Then I splitted data into Traning and Testing by using Train Test Split.

- Then I fit the Model with X_train and y_train on Support Vector Machine and Random Forest Classifier and checked the Score.

- After that I used KFold Cross Validation for further improving the Accuracy of our Model.

- So I cheked Mean Cross_Val_Score of both SVM and Random Forest Classifier for Best Score.

## Conclusion

- Implemented Random Forest and SVM Model to achieve a score of 88% and 83% respectively.

- Validated the Random Forest Model with a mean cross_val_score of 88% and demonstrated its superior robustness compared to SVM with a mean cross_val_score of 81%.

<div align='right'>
  
**[`^        Scroll to Top       ^`](#spaceship-titanic-classification)**

</div>
