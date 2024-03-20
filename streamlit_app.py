#Importing Libraries
import streamlit as st
import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
import pickle
from intro_page import intro_page

#Reading CSV File
df = pd.read_csv("spaceship_clean.csv")

df_is_vip = df[df["VIP"]==1]
df_not_vip = df[df["VIP"]==0]

df_is_vip_upsample = resample(df_is_vip, n_samples=len(df_not_vip), random_state=1234)

final_df = pd.concat([df_not_vip,df_is_vip_upsample])

#Loading Models in App
with open('model_rf.pkl', 'rb') as f:
    rf = pickle.load(f)

with open('model_svm.pkl', 'rb') as f:
    svm = pickle.load(f)

#Setting Page Configuration
st.set_page_config(page_title="Spaceship Titanic Classification",page_icon="🛰️",layout="centered")

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
        room_service = st.selectbox(label="Select the Room Service Amount",options=final_df[subset_cols[0]].round(4),placeholder="Select the Amount...",index=None)

        food_court = st.selectbox(label="Select the Food Cort Amount Spend",options=final_df[subset_cols[1]].round(4),placeholder="Select the Amount...",index=None)

        spa = st.selectbox(label="Select the Spa Service Amount Spend",options=final_df[subset_cols[2]].round(4),placeholder="Select the Amount...",index=None)

        vr_deck = st.selectbox(label="Select the VRDeck Amount Spend",options=final_df[subset_cols[3]].round(4),placeholder="Select the Amount...",index=None)

        shopping_mall = st.selectbox(label="Select the Shopping Amount Spend",options=final_df[subset_cols[4]].round(4),placeholder="Select the Amount...",index=None)

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
                prediction_svm = svm.predict(df3)
                if prediction_svm == 1:
                    st.success(f"Passenger has been Transported to an Alternate Dimension", icon="✅")
                else:
                    st.error(f"Passenger has not been Transported to an Alternate Dimension", icon="❌")   
    else:
        if pred:
            if any([cryo_sleep is None, age is None, vip is None, home_planet is None, destination is None, room_service is None, shopping_mall is None, vr_deck is None, spa is None, food_court is None, models is None]):
                st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
            else:
                prediction_rf = rf.predict(df3)
                if prediction_rf == 1:
                    st.success(f"Passenger has been Transported to an Alternate Dimension", icon="✅")
                else:
                    st.error(f"Passenger has not been Transported to an Alternate Dimension", icon="❌")  

#Sidebar Section
st.sidebar.markdown("<h1 style='text-align:center;'>Hi 👋, Welcome to the App</h1>",unsafe_allow_html=True)    

st.sidebar.image("logo.png",caption="Spaceship Titanic Classification",use_column_width=True)

st.sidebar.markdown("<div style='text-align:center; font-size:x-large;'><b>Select any Page</b></div>",unsafe_allow_html=True)    

page = st.sidebar.selectbox("", ["Home Page", "Web Application"])

#Display the Selected Page Content
if page == "Home Page":
    intro_page()
if page == "Web Application":
    web_app()

#Contributions Section
st.sidebar.markdown("<h1 style='text-align:center;'>Contributions</h1>",unsafe_allow_html=True)    

st.sidebar.link_button(label="Star",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification",use_container_width=True)

st.sidebar.link_button(label="Fork",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/fork",use_container_width=True)

st.sidebar.link_button(label="Download",url="https://github.com/TheMrityunjayPathak/SpaceshipTitanicClassification/archive/HEAD.zip",use_container_width=True)

st.sidebar.markdown("<h1 style='text-align:center;'>Thanks 👏 for Visiting!</h1>",unsafe_allow_html=True)    