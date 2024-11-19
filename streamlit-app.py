import streamlit as st 
import pandas as pd
import altair as alt 
 
# Charger les données
df = pd.read_csv('Iris.csv', delimiter=';')
 
# Créer un titre
st.title("Mon premier tableau de bord Streamlit")
 
# Afficher les données dans un tableau
# st.table(df)

#creer un char Altair
chart = alt.Chart(df).mark_bar().encode( x='SepalLength' , y='SepalWidth')

#Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True) 

chart = alt.Chart(df).mark_point().encode(x='SepalLength' , y='PetalLength')
#Afficher le chart sur Streamlit
st.altair_char(chart, use_container_width=True)

#st.write(df.head(5))
 
   
