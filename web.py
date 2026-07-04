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
                    texto_total += texto + "\n\n"

            documentos.append({
                "archivo": archivo,
                "texto": texto_total
            })

    return documentos


def buscar_respuesta(documentos, pregunta, filtro):
    resultados = []

    palabras_vacias = [
        "que", "qué", "cual", "cuál", "cuanto", "cuánto", "cuanta", "cuánta",
        "como", "cómo", "es", "son", "la", "las", "el", "los", "de", "del",
        "un", "una", "para", "por", "necesito", "y", "o", "a", "en", "con"
    ]

    pregunta = (pregunta or "").lower()
    pregunta = pregunta.replace("¿", "").replace("?", "").replace(",", "").replace(".", "")

    terminos = [p for p in pregunta.split() if p not in palabras_vacias]

    if not terminos:
        return resultados

    sinonimos = {
        "aprobar": ["aprobacion", "aprobación", "aprobado"],
        "nota": ["calificacion", "calificación"],
        "asistencia": ["inasistencia"],
        "docente": ["profesor", "académico"],
        "beca": ["beneficio"]
    }

    for documento in documentos:
        if filtro != "Todos" and filtro != documento["archivo"]:
            continue

        fragmentos = [
            f.strip()
            for f in documento["texto"].split("\n\n")
            if len(f.strip()) > 50
        ]

        for fragmento in fragmentos:
            if any(x in fragmento.upper() for x in ["REGLAMENTO ACADÉMICO", "TÍTULO I", "NORMAS GENERALES"]):
                continue

            lower_fragmento = fragmento.lower()
            terminos_expandido = terminos.copy()
            
            for termino in terminos:
                if termino in sinonimos:
                    terminos_expandido.extend(sinonimos[termino])
            
            terminos_expandido = list(set(terminos_expandido))

            puntaje = 0
            coincidencias = 0

            for termino in terminos_expandido:
                cantidad = lower_fragmento.count(termino)
                if cantidad > 0:
                    coincidencias += 1
                puntaje += cantidad * 3

            puntaje += coincidencias * 15

            if any(termino in documento["archivo"].lower() for termino in terminos_expandido):
                puntaje += 10

            if puntaje > 0:
                pos = -1
                for termino in terminos:
                    pos = lower_fragmento.find(termino)
                    if pos != -1:
                        break

                if pos != -1:
                    inicio = max(0, pos - 150)
                    fin = min(len(fragmento), pos + 500)
                    extracto = fragmento[inicio:fin]
                else:
                    extracto = fragmento[:400]

                resultados.append({
                    "archivo": documento["archivo"],
                    "texto": extracto,
                    "puntaje": puntaje
                })

    resultados.sort(key=lambda x: x["puntaje"], reverse=True)
    return resultados


def generar_respuesta(resultado):
    texto = resultado["texto"].replace("\n", " ").strip()
    return f"""
De acuerdo con el reglamento {resultado['archivo']},

{texto}
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
