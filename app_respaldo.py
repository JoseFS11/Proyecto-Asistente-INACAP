
import os
from pypdf import PdfReader


def leer_reglamentos():
    texto_total = ""

    if not os.path.isdir("Reglamentos"):
        print("No se encontró la carpeta 'Reglamentos'.")
        return texto_total

    for archivo in os.listdir("Reglamentos"):
        if archivo.lower().endswith(".pdf"):
            ruta = os.path.join("Reglamentos", archivo)
            pdf = PdfReader(ruta)

            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto + "\n"

    return texto_total


def buscar_respuesta(reglamentos, pregunta):
    encontrado = False

    for linea in reglamentos.split("\n"):
        if pregunta.lower() in linea.lower():
            print("\nResultado encontrado:")
            print(linea)
            encontrado = True

    if not encontrado:
        print("\nNo encontré información relacionada.")


def main():
    reglamentos = leer_reglamentos()
    while True:
        pregunta = input("\n¿Qué deseas consultar? (o escribe 'salir' para terminar): ")
        if pregunta.lower() == "salir":
            print("Programa finalizado.")
            break
        buscar_respuesta(reglamentos, pregunta)


if __name__ == "__main__":
    main()
