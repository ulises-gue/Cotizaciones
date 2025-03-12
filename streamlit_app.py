import streamlit as st

st.title("Cotizaciones - Border Freight")

#Este es el costo por kilometro que usaremos para el caluculo de rentabilidad de ruta
costo_por_km = 25.3

#La primer variable que necesitamos sabe es el kilometraje de la ruta
st.number_input("Ingerese el kilometraje de la Ruta: ", min_value = 1, step = 1)
#Despues se pregunta si qusiera cotizar en dolares
st.radio("Cotizar en USD?", ("No","Si"))

if dolares == "No":
    sugerir_precio = st.radio("¿Tienes algún precio en mente?", ("No", "Sí"))
    if sugerir_precio == "No":
        precio_por_km = st.number_input("Ingresa el precio por kilómetro deseado:", min_value=0.0, step=0.1)
        precio_mxn = precio_por_km * kilometraje
        margen_utilidad = (precio_mxn - (kilometraje * costo_por_km)) / precio_mxn
        
        st.write(f"**El precio total es:** ${precio_mxn:,.2f} MXN")
        st.write(f"**La utilidad es:** {margen_utilidad:.2%}")
    
    else:
        precio_mxn = st.number_input("Ingresa el precio deseado:", min_value=0.0, step=0.1)
        precio_por_km = precio_mxn / kilometraje
        margen_utilidad = (precio_mxn - (kilometraje * costo_por_km)) / precio_mxn
        
        st.write(f"**El precio por kilómetro es:** ${precio_por_km:,.2f}")
        st.write(f"**La utilidad es:** {margen_utilidad:.2%}")

else:
    sugerir_precio = st.radio("¿Tienes algún precio en mente?", ("No", "Sí"))
    if sugerir_precio == "No":
        precio_por_km = st.number_input("Ingresa el precio por kilómetro deseado:", min_value=0.0, step=0.1)
        precio_mxn = precio_por_km * kilometraje
        tipo_de_cambio = st.number_input("Ingresa el tipo de cambio:", min_value=0.0, step=0.01)
        precio_usd = precio_mxn / tipo_de_cambio
        margen_utilidad = (precio_mxn - (kilometraje * costo_por_km)) / precio_mxn
        
        st.write(f"**El precio total es:** ${precio_usd:,.2f} USD")
        st.write(f"**La utilidad es:** {margen_utilidad:.2%}")
    
    else:
        precio_usd = st.number_input("Ingresa el precio deseado:", min_value=0.0, step=0.1)
        tipo_de_cambio = st.number_input("Ingresa el tipo de cambio:", min_value=0.0, step=0.01)
        precio_mxn = precio_usd * tipo_de_cambio
        precio_por_km = precio_mxn / kilometraje
        margen_utilidad = (precio_mxn - (kilometraje * costo_por_km)) / precio_mxn
        
        st.write(f"**El precio por kilómetro es:** ${precio_por_km:,.2f}")
        st.write(f"**La utilidad es:** {margen_utilidad:.2%}")

st.write("---")
st.write("💡 *Desarrollado para facilitar cotizaciones de rutas de transporte.*")

                             


