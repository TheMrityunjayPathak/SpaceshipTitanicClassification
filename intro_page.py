#Importing Libraries
import streamlit as st
import pandas as pd

#Reading CSV File
df = pd.read_csv("spaceship_clean.csv")

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

        st.code(f"Different Home Planets are {df["HomePlanet"].unique()}.")

    #Cryo Sleep Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>CryoSleep</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Indicates whether the passenger elected to be put into cryo capsule for the duration of the voyage.</b>',unsafe_allow_html=True)

        st.code(f"Different values for CryoSleep are {df["CryoSleep"].unique()}.")

        st.code(f"0 = No    1 = Yes")

    #Destination Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Destination</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ The planet the passenger will be debarking to.</b>',unsafe_allow_html=True)

        st.code(f"Different Destination Planets are {df["Destination"].unique()}.")

    #VIP Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>VIP</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Whether the passenger has paid for special VIP service during the voyage.</b>',unsafe_allow_html=True)

        st.code(f"Different values for VIP are {df["VIP"].unique()}.")

        st.code(f"0 = No    1 = Yes")

    #RoomService, FoodCourt, ShoppingMall, Spa, VRDeck Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>RoomService, FoodCourt, ShoppingMall, Spa, VRDeck</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Amount the passenger has billed at each of the Spaceship Titanics many luxury amenities.</b>',unsafe_allow_html=True)

        st.code(f"Room Service Amount is between {round(df["RoomService"].min())} to {round(df["RoomService"].max())}.")

        st.code(f"Food Court Amount is between {round(df["FoodCourt"].min())} to {round(df["FoodCourt"].max())}.")

        st.code(f"Shopping Mall Amount is between {round(df["ShoppingMall"].min())} to {round(df["ShoppingMall"].max())}.")

        st.code(f"Spa Amount is between {round(df["Spa"].min())} to {round(df["Spa"].max())}.")

        st.code(f"VRDeck Amount is between {round(df["VRDeck"].min())} to {round(df["VRDeck"].max())}.")

    #Age Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Age</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ The age of the passenger.</b>',unsafe_allow_html=True)

        st.code(f"Age of Passengers is between {round(df["Age"].min())} to {round(df["Age"].max())}.")

    #Transported Section
    st.markdown("<div style='background-color:#48C9B0; padding:10px; border-radius:25px; text-align:center;'><b>Transported</b></div>",unsafe_allow_html=True)

    st.write("")

    with st.expander("Detail View"):

        st.markdown('<b>→ Whether the passenger was transported to another dimension or not.</b>',unsafe_allow_html=True)

        st.code(f"Different values for Transported are {df["Transported"].unique()}.")

        st.code(f"0 = No    1 = Yes")