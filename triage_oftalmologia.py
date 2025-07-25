import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Triage Oftalmológico", layout="centered")

# Función para reiniciar (refrescar) la app
def reiniciar():
    st.experimental_rerun()

# Título y descripción
st.title("👁️ Triage Oftalmológico")
st.markdown("Aplicación para triage inicial realizado para personal de enfermería sin formación oftalmológica.")

# Datos personales antes de empezar
st.header("📝 Datos del paciente")
nombre = st.text_input("Nombre y apellido")
dni = st.text_input("DNI")
edad = st.number_input("Edad", min_value=0, max_value=120, step=1)

st.divider()

if nombre and dni and edad > 0:
    st.header("🟠 PASO 1: Emergencias Oftalmológicas")

    trauma = st.radio("¿Tuvo un traumatismo con elemento punzo-cortante?", 
                      ["No", 
                       "Sí: proyectil, alambre, metal mientras martillaba", 
                       "Sí: esquirla de amoladora"])

    quimico = st.radio("¿Le cayó un producto químico en el ojo?", 
                       ["No", 
                        "Sí, una gota", 
                        "Sí, gran cantidad (chorro o baldazo)"])

    dolor = st.radio("¿Tiene el ojo rojo doloroso con dolor de cabeza y ganas de vomitar?", 
                     ["No", 
                      "Sí", 
                      "Solo dolor leve, sin náuseas ni vómitos"])

    politrauma = st.radio("¿Tiene múltiples golpes (politraumatismo)?", 
                          ["No", 
                           "Sí"])

    # Lógica Paso 1
    codigo_paso1 = None
    if trauma == "Sí: proyectil, alambre, metal mientras martillaba":
        codigo_paso1 = "🟡 CÓDIGO AMARILLO= Espera de 20 minutos"
    elif quimico == "Sí, gran cantidad (chorro o baldazo)":
        codigo_paso1 = "🟡 CÓDIGO AMARILLO=  Espera de 20 minutos"
    elif dolor == "Sí":
        codigo_paso1 = "🟡 CÓDIGO AMARILLO=  Espera de 20 minutos"
    elif politrauma == "Sí":
        codigo_paso1 = "🔺 Evaluar primero por emergentólogo"
    elif trauma == "Sí: esquirla de amoladora" or quimico == "Sí, una gota" or dolor == "Solo dolor leve, sin náuseas ni vómitos":
        codigo_paso1 = "🟢 CÓDIGO VERDE= Espera de 1 a 2 horas"

    if codigo_paso1:
        st.subheader(f"Resultado Paso 1: {codigo_paso1}")

    st.divider()

    if codigo_paso1 in ["🟢 CÓDIGO VERDE= Espera de 1 a 2 horas", None]:
        st.header("🟢 PASO 2: Síntomas frecuentes")

        st.markdown("Si **NO hay síntomas de alarma en el Paso 1**, pasar al paso 2.")

        sintomas = st.multiselect("¿Qué síntomas presenta el paciente?", [
            "Ojo rojo doloroso",
            "Secreción o legaña",
            "Picazón o ardor ocular",
            "Hinchazón del párpado (como orzuelo)",
            "Pérdida de visión de menos de 72 hs",
            "Manchas negras, telarañas o mosquitas"
            "Derrame"
            "Sensacion de cuerpo extraño o arenilla"
        ])

        dias = st.slider("¿Hace cuántos días tiene el problema?", 0, 30, 1)

        codigo_paso2 = None
        if sintomas:
            if dias <= 3:
                codigo_paso2 = "🟢 CÓDIGO VERDE= Espera de 1 a 2 horas"
            else:
                codigo_paso2 = "📅 DERIVAR A CONSULTORIO (patología crónica)"

        if sintomas:
            st.subheader(f"Resultado Paso 2: {codigo_paso2}")

        st.divider()

        st.header("📋 PASO 3: ¿No presenta síntomas agudos?")

        st.markdown("""
        Si el paciente no presenta ninguno de los síntomas anteriores, y viene por:

        - Control de anteojos
        - Control de fondo de ojo sin síntomas
        - Molestias visuales de larga data

        ➡️ **Debe ser derivado directamente a consultorio** (no requiere atención por guardia).
        Recuerde completar el formulario con honestidad, el correcto funcionamiento del sistema de triage contribuye a mejorar la calidad de atención priorizando a los pacientes mas graves y cuidando los recursos del sistema publico de atencion. 
        """)

    # Firma digital enfermero y fecha/hora
    st.divider()
    st.write("---")
    st.markdown("**Firma digital del enfermero:**")
    enfermero = st.text_input("Nombre del enfermero que realiza el triage")

    if enfermero:
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        st.markdown(f"**Enfermero:** {enfermero}  \n**Fecha y hora de atención:** {fecha_hora}")

    st.write("---")

    # Botón para reiniciar todo
    if st.button("🔄 Reiniciar triage"):
        reiniciar()

else:
    st.warning("Por favor, complete todos los datos personales para continuar.")
