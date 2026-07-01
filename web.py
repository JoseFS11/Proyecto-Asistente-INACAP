import os
import streamlit as st
from pypdf import PdfReader


@st.cache_data
def leer_reglamentos():
    documentos = []
    carpeta = "Reglamentos"

    if not os.path.isdir(carpeta):
        return documentos

    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(".pdf"):
            ruta = os.path.join(carpeta, archivo)
            try:
                pdf = PdfReader(ruta)
            except Exception:
                continue

            texto_total = ""
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto + "\n"

            documentos.append({
                "archivo": archivo,
                "texto": texto_total
            })

    return documentos


def buscar_respuesta(documentos, pregunta, filtro):
    resultados = []

    palabras_vacias = [
        "que", "qué",
        "cual", "cuál",
        "cuanto", "cuánto",
        "cuanta", "cuánta",
        "como", "cómo",
        "es", "son",
        "la", "las",
        "el", "los",
        "de", "del",
        "un", "una",
        "para", "por",
        "necesito",
        "y", "o", "a", "en", "por", "con"
    ]

    pregunta = (pregunta or "").lower()
    pregunta = pregunta.replace("¿", "")
    pregunta = pregunta.replace("?", "")
    pregunta = pregunta.replace(",", "")
    pregunta = pregunta.replace(".", "")

    terminos = [
        palabra
        for palabra in pregunta.split()
        if palabra not in palabras_vacias
    ]

    if not terminos:
        return resultados

    for documento in documentos:
        if filtro != "Todos" and filtro != documento["archivo"]:
            continue

        fragmentos = [f.strip()
                 for f in documento["texto"].split("\n\n")
                 if len(f.strip()) > 20]
        for fragmento in fragmentos:
            puntaje = 0
            for termino in terminos:
                puntaje += fragmento.lower().count(termino) * 3
                if "nota" in fragmento.lower():
                    puntaje += 5
                if "aprobar" in fragmento.lower():
                    puntaje += 5
                if "aprobación" in fragmento.lower():
                    puntaje += 5

            if any(termino in documento["archivo"].lower() for termino in terminos):
                puntaje += 5

            if puntaje > 0:
                resultados.append({
                    "archivo": documento["archivo"],
                    "texto": fragmento,
                    "puntaje": puntaje
                })

    resultados.sort(key=lambda x: x["puntaje"], reverse=True)
    return resultados


def generar_respuesta(resultado):

    return f"""
De acuerdo con el reglamento {resultado['archivo']},

{resultado['texto']}
"""

if "historial" not in st.session_state:
    st.session_state.historial = []


documentos = leer_reglamentos()

with st.sidebar:
    st.image("logo.png", width=200)
    st.title("📚 INFORMACIÓN")
    st.write(f"Documentos cargados: {len(documentos)}")
    st.subheader("Reglamentos")
    for doc in documentos:
        st.write("📄", doc["archivo"])
    st.divider()
    st.subheader("🕒 Historial")
    for consulta in st.session_state.historial:
        st.write("•", consulta)
    st.markdown("---")
    reglamento_seleccionado = st.selectbox(
        "Buscar en:",
        ["Todos"] + [doc["archivo"] for doc in documentos]
    )

st.title("🎓 Asistente INACAP")
st.write("Consulta información de los reglamentos institucionales.")

pregunta = st.chat_input("¿Qué deseas consultar?")

if pregunta:
        with st.chat_message("user",avatar="👨‍🎓"):
            st.write(pregunta)

        if pregunta not in st.session_state.historial:
            st.session_state.historial.append(pregunta)

        resultados = buscar_respuesta(
            documentos,
            pregunta,
            reglamento_seleccionado
        )
        if resultados:
            mejor_resultado = resultados[0]
            respuesta = generar_respuesta(mejor_resultado)
            
            with st.chat_message("assistant", avatar="🤖"):
                st.write(respuesta)

           #for resultado in resultados[:5]:
               #st.markdown(f"📄 **Fuente:** {resultado['archivo']}")
            #st.write(resultado["texto"])
            #st.markdown("---")
        else:
            st.warning("No encontré información relacionada.")
