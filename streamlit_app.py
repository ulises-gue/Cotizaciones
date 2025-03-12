import streamlit as st

st.title("Cotizaciones - Border Freight")

#Este es el costo por kilometro que usaremos para el caluculo de rentabilidad de ruta
costo_por_km = 25.3

#La primer variable que necesitamos sabe es el kilometraje de la ruta
st.number_input("Ingerese el kilometraje de la Ruta: ", min_value = 1, step = 1)
#Despues se pregunta si qusiera cotizar en dolares
st.radio("Cotizar en USD?", ("No,"Si"))

                             


