#Importing Libraries
import streamlit as st
import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
import pickle

#Reading CSV File
df = pd.read_csv("spaceship_clean.csv")

df_is_vip = df[df["VIP"]==1]
df_not_vip = df[df["VIP"]==0]

df_is_vip_upsample = resample(df_is_vip, n_samples=len(df_not_vip), random_state=1234)

final_df = pd.concat([df_not_vip,df_is_vip_upsample])

#Loading Models in App
with open('model_svm.pkl', 'rb') as f:
    svm = pickle.load(f)

with open('model_rf.pkl', 'rb') as f:
    rf = pickle.load(f)

#Setting Page Configuration
st.set_page_config(page_title="Spaceship Titanic Classification",page_icon="🛰️",layout="centered")

#Home Page Function
def intro_page():
    #Title
    st.markdown("<h1 style='text-align:center;'>Spaceship Titanic Classification</h1>",unsafe_allow_html=True)

    #Problem Statement Section
    st.markdown("<div style='background-color:#EC7063; padding:10px; border-radius:25px; text-align:center;'><b>Problem Description</b></div>",unsafe_allow_html=True)

    st.write("")

    st.markdown("<div style='background-color:#CACFD2; padding:10px; border-radius:15px; text-align:left;'>Welcome to the Year 2912, where your Data Science Skills are needed to solve a Cosmic Mystery. We've received a transmission from four lightyears away and things aren't looking good.<br><br>The Spaceship Titanic was an interstellar passenger liner launched a month ago. With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.<br><br>While rounding Alpha Centauri en route to its first destination—the torrid 55 Cancri E—the unwary Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud. Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!<br><br>To help rescue crews and retrieve the lost passengers, you are challenged to predict which passengers were transported by the anomaly using records recovered from the spaceships damaged computer system.</div>",unsafe_allow_html=True)

    st.write("")
    
    #Dataset Description Section
    st.markdown("<div style='background-color:#EC7063; padding:10px; border-radius:25px; text-align:center;'><b>Dataset Description</b></div>",unsafe_allow_html=True)

    st.write("")

    st.markdown("<div style='background-color:#CACFD2; padding:10px; border-radius:15px; text-align:left;'>In this problem your task is to predict whether a passenger was transported to an alternate dimension during the Spaceship Titanic's collision with the spacetime anomaly.<br><br>To help you make these predictions, you're given a set of personal records recovered from the ship's damaged computer system.</div>",unsafe_allow_html=True)
    
    st.write("")

    #Buttons Section
    col1, col2, col3 = st.columns(3)

    #Download Dataset Button
    with col1:
        @st.cache_data
        def convert_df(my_df):
            return my_df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download Dataset",
            data=csv,
            file_name='spaceship.csv',
            mime='text/csv',
            use_container_width=True
        )

    #View Notebook Button
    with col2:
        st.link_button(label="View Notebook",url="https://www.kaggle.com/code/themrityunjaypathak/spaceship-titanic-classification",use_container_width=True)

    #View Repository Button
    with col3:
        st.link_button(label="View Repository",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification",use_container_width=True)

    #Show Dataset Toogle
    data = st.toggle(label="Show Dataset")

    if data:
        st.dataframe(df,hide_index=True,use_container_width=True)

    #Column Description Section
    st.markdown("<div style='background-color:#EC7063; padding:10px; border-radius:25px; text-align:center;'><b>Columns Description</b></div>",unsafe_allow_html=True)

    st.write("")
    
    #Home Planet Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>HomePlanet</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ The planet the passenger departed from, typically their planet of permanent residence.<b>',unsafe_allow_html=True)

        st.write(f"Different Home Planets are {df['HomePlanet'].unique()}.")

    #Cryo Sleep Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>CryoSleep</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Indicates whether the passenger elected to be put into cryo capsule for the duration of the voyage.</b>',unsafe_allow_html=True)

        st.write(f"Different values for CryoSleep are {df['CryoSleep'].unique()}.")

        st.write(f"0 = No    1 = Yes")

    #Destination Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Destination</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ The planet the passenger will be debarking to.</b>',unsafe_allow_html=True)

        st.write(f"Different Destination Planets are {df['Destination'].unique()}.")

    #VIP Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>VIP</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Whether the passenger has paid for special VIP service during the voyage.</b>',unsafe_allow_html=True)

        st.write(f"Different values for VIP are {df['VIP'].unique()}.")

        st.write(f"0 = No    1 = Yes")

    #RoomService, FoodCourt, ShoppingMall, Spa, VRDeck Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>RoomService, FoodCourt, ShoppingMall, Spa, VRDeck</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Amount the passenger has billed at each of the Spaceship Titanics many luxury amenities.</b>',unsafe_allow_html=True)

        st.write(f"Room Service Amount is between {round(df['RoomService'].min())} to {round(df['RoomService'].max())}.")

        st.write(f"Food Court Amount is between {round(df['FoodCourt'].min())} to {round(df['FoodCourt'].max())}.")

        st.write(f"Shopping Mall Amount is between {round(df['ShoppingMall'].min())} to {round(df['ShoppingMall'].max())}.")

        st.write(f"Spa Amount is between {round(df['Spa'].min())} to {round(df['Spa'].max())}.")

        st.write(f"VRDeck Amount is between {round(df['VRDeck'].min())} to {round(df['VRDeck'].max())}.")

    #Age Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Age</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ The age of the passenger.</b>',unsafe_allow_html=True)

        st.write(f"Age of Passengers is between {round(df['Age'].min())} to {round(df['Age'].max())}.")

    #Transported Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Transported</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Whether the passenger was transported to another dimension or not.</b>',unsafe_allow_html=True)

        st.write(f"Different values for Transported are {df['Transported'].unique()}.")

        st.write(f"0 = No    1 = Yes")

#Web Application Section
def web_app():
    #Title
    st.markdown("<div style='background-color:#219C90; border-radius:50px; align-items:center; justify-content: center;'><h1 style='text-align:center; color:white;'>Spaceship Titanic Classification</h1></div>",unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:center; color:black;'>Find out If a Passenger was Transported to an Alternate Dimension</h4>",unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    #Image
    with col1:
        #Prediction
        models = st.selectbox(label="Select any Model",placeholder="Choose any Model",options=["Support Vector Machine","Random Forest"],index=None)
        st.write("")
        st.image("spaceship.png",use_column_width=True)

    #Feature Inputs
    with col2:
        home_planet = st.selectbox(label="Select the Home Planet", options=final_df["HomePlanet"].unique(),placeholder="Choose the Home Planet",index=None)

        destination = st.selectbox(label="Select the Destination Planet",options=final_df["Destination"].unique(),placeholder="Choose the Destination Planet",index=None)

        col4, col5 = st.columns(2)
        with col4:
            cryo_sleep = st.radio(label="Did they elected for CryoSleep?",options=["Yes","No"],index=None)
            if cryo_sleep == "Yes":
                cryo_sleep = 1
            else:
                cryo_sleep = 0
        with col5:
            vip = st.radio(label="Did they paid for VIP Service?",options=["Yes","No"],index=None)
            if vip == "Yes":
                vip = 1
            else:
                vip = 0

        age = st.slider(label="Select the Age of the Passenger",min_value=1,max_value=80,step=1)

    #Feature Inputs
    with col3:
        #Data Standardization
        subset_cols = ["RoomService","FoodCourt","ShoppingMall","Spa","VRDeck"]

        subset_df = final_df[subset_cols]

        scaler = StandardScaler()

        scaler.fit(subset_df)

        scaled_values = scaler.transform(subset_df)

        final_df[subset_cols] = scaled_values

        #Standardized Selection Box
        room_service = st.selectbox(label="Select the Room Service Amount",options=final_df[subset_cols[0]].round(4),placeholder="Select the Amount...",index=None,help="These inputs are Standardized by using StandardScaler")

        food_court = st.selectbox(label="Select the Food Cort Amount Spend",options=final_df[subset_cols[1]].round(4),placeholder="Select the Amount...",index=None,help="These inputs are Standardized by using StandardScaler")

        spa = st.selectbox(label="Select the Spa Service Amount Spend",options=final_df[subset_cols[2]].round(4),placeholder="Select the Amount...",index=None,help="These inputs are Standardized by using StandardScaler")

        vr_deck = st.selectbox(label="Select the VRDeck Amount Spend",options=final_df[subset_cols[3]].round(4),placeholder="Select the Amount...",index=None,help="These inputs are Standardized by using StandardScaler")

        shopping_mall = st.selectbox(label="Select the Shopping Amount Spend",options=final_df[subset_cols[4]].round(4),placeholder="Select the Amount...",index=None,help="These inputs are Standardized by using StandardScaler")

    #Prediction Button
    with col3:
        pred = st.button("Predict",use_container_width=True)

    #Data Preprocessing
    data1 = {"CryoSleep":[cryo_sleep],"Age":[age],"VIP":[vip],"HomePlanet":[home_planet],"Destination":[destination]}

    data2 = {"RoomService":[room_service],"FoodCourt":[food_court],"ShoppingMall":[shopping_mall],"Spa":[spa],"VRDeck":[vr_deck]}

    df1 = pd.DataFrame(data1)

    df2 = pd.DataFrame(data2)

    #Dummy Variable
    dummy_home = pd.get_dummies(df1["HomePlanet"],dtype=int)
    home_df = pd.DataFrame(dummy_home)
    new1_df = pd.concat([df1,home_df],axis="columns")

    dummy_dest = pd.get_dummies(new1_df["Destination"],dtype=int)
    dest_df = pd.DataFrame(dummy_dest)
    new2_df = pd.concat([new1_df,dest_df],axis="columns")

    new2_df.drop(["HomePlanet","Destination"],axis="columns",inplace=True)

    model_features = ['CryoSleep', 'Age', 'VIP', 'Earth', 'Europa', 'Mars',
       '55 Cancri e', 'PSO J318.5-22', 'TRAPPIST-1e']
    
    for features in model_features:
        if features not in new2_df.columns:
            new2_df[features] = 0
    
    new2_df = new2_df[model_features]

    #Concatenating Both the DataFrames
    df3 = pd.concat([new2_df,df2],axis="columns")

    #Prediction
    if models == "Support Vector Machine":
        if pred:
            if any([cryo_sleep is None, age is None, vip is None, home_planet is None, destination is None, room_service is None, shopping_mall is None, vr_deck is None, spa is None, food_court is None, models is None]):
                st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
            else:
                prediction = svm.predict(df3)
                if prediction == 1:
                    st.success(f"Passenger has been Transported to an Alternate Dimension", icon="✅")
                else:
                    st.error(f"Passenger has not been Transported to an Alternate Dimension", icon="❌")   
    else:
        if pred:
            if any([cryo_sleep is None, age is None, vip is None, home_planet is None, destination is None, room_service is None, shopping_mall is None, vr_deck is None, spa is None, food_court is None, models is None]):
                st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
            else:
                prediction = rf.predict(df3)
                if prediction == 1:
                    st.success(f"Passenger has been Transported to an Alternate Dimension", icon="✅")
                else:
                    st.error(f"Passenger has not been Transported to an Alternate Dimension", icon="❌")  

#Sidebar Section
st.sidebar.markdown("<h1 style='text-align:center;'>Hi 👋, Welcome to the App</h1>",unsafe_allow_html=True)    

st.sidebar.image("logo.png",caption="Spaceship Titanic Classification",use_column_width=True)

st.sidebar.markdown("<div style='text-align:center; font-size:x-large;'><b>Select any Page</b></div>",unsafe_allow_html=True) 

pages = st.sidebar.selectbox(label="",options=["Home Page","Web Application"],index=0)

if pages == "Home Page":
    intro_page()
else:
    web_app()

#Contributions Section
st.sidebar.markdown("<h1 style='text-align:center;'>Contributions</h1>",unsafe_allow_html=True)    

st.sidebar.link_button(label="Star",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification",use_container_width=True)

st.sidebar.link_button(label="Fork",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/fork",use_container_width=True)

st.sidebar.link_button(label="Download",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/archive/HEAD.zip",use_container_width=True)

st.sidebar.markdown("<h1 style='text-align:center;'>Thanks 👏 for Visiting!</h1>",unsafe_allow_html=True)    
