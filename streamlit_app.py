import streamlit as st

st.title("Cotizaciones - Border Freight")

costo_por_km = 25.3

kilometraje = st.number_input("Ingresa el kilometraje de la ruta:", min_value=1, step=1)

dolares = st.radio("¿Deseas cotizar en dólares?", ("No", "Sí"))

if dolares == "No":
    sugerir_precio = st.radio("¿Tienes algún precio en mente?", ("No", "Sí"))
    if sugerir_precio == "No":
        precio_por_km = st.number_input("Ingresa el precio por kilómetro deseado:", min_value=0.0, step=0.1)
        precio_mxn = precio_por_km * kilometraje
    else:
        precio_mxn = st.number_input("Ingresa el precio deseado:", min_value=0.0, step=0.1)
        precio_por_km = precio_mxn / kilometraje

else:
    sugerir_precio = st.radio("¿Tienes algún precio en mente?", ("No", "Sí"))
    if sugerir_precio == "No":
        precio_por_km = st.number_input("Ingresa el precio por kilómetro deseado:", min_value=0.0, step=0.1)
        precio_mxn = precio_por_km * kilometraje
    else:
        precio_usd = st.number_input("Ingresa el precio deseado:", min_value=0.0, step=0.1)
        tipo_de_cambio = st.number_input("Ingresa el tipo de cambio:", min_value=0.0, step=0.01)
        precio_mxn = precio_usd * tipo_de_cambio
        precio_por_km = precio_mxn / kilometraje

# Calculate profit margin
margen_utilidad = (precio_mxn - (kilometraje * costo_por_km)) / precio_mxn

# Function to determine color
def get_color(margen):
    if margen < 0:
        return "red"
    elif 0 <= margen < 0.35:
        return "yellow"
    else:
        return "green"

# Display results
st.write(f"**El precio total es:** ${precio_mxn:,.2f} MXN")
st.write(f"**El precio por kilómetro es:** ${precio_por_km:,.2f}")

# Apply color styling
color = get_color(margen_utilidad)
st.markdown(f"<p style='color:{color}; font-size:24px; font-weight:bold;'>Utilidad: {margen_utilidad:.2%}</p>", unsafe_allow_html=True)

st.write("---")
