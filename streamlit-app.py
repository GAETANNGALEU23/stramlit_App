import streamlit as st 
import pandas as pd
import altair as alt 
 
# Charger les données
df = pd.read_csv('Iris.csv', delimiter=';')
 
# Créer un titre
st.title("Mon premier tableau de bord Streamlit")
 
# Afficher les données dans un tableau
# st.table(df) 
st.write(df.head(5))
 
   
