# 🎓 Asistente INACAP

Este proyecto consiste en la creación de un asistente documental desarrollado en Python y Streamlit para consultar información contenida en reglamentos institucionales en formato PDF para poder solucionar consultas de los estudiantes sobre asistencia, notas, biblioteca, etc.

El sistema permite cargar automáticamente reglamentos, buscar información relevante mediante palabras clave o preguntas simples, y responder al usuario utilizando una interfaz conversacional inspirada en sistemas de Recuperación Aumentada por Generación (RAG).

---

## Características

- Lectura automática de archivos PDF.
- Carga dinámica de reglamentos desde una carpeta local.
- Interfaz web desarrollada con Streamlit.
- Historial de consultas.
- Filtrado por reglamento.
- Ranking básico de relevancia.
- Recuperación de información basada en palabras clave.
- Respuesta contextual basada en el contenido encontrado.
- Diseño personalizado con identidad visual INACAP.

---

## Arquitectura General

```text
Reglamentos PDF
        │
        ▼
Extracción de texto
        │
        ▼
Fragmentación del contenido
        │
        ▼
Procesamiento de consulta
        │
        ▼
Recuperación de información
        │
        ▼
Ranking por relevancia
        │
        ▼
Generación de respuesta
        │
        ▼
Interfaz Streamlit

---


## Estructura del proyecto

```text
ASISTENTE INACAP
│
├── Reglamentos
│   ├── academico.pdf
│   ├── beca_apoyo_INACAP.pdf
│   ├── bibliotecas.pdf
│   ├── docentes.pdf
│   ├── educacion_continua.pdf
│   ├── medidas_disciplinarias.pdf
│   ├── practicas.pdf
│   └── uso_de_talleres.pdf
│
├── app_respaldo.py
├── logo.png
├── README.md
├── web.py
└── .gitignore

---

## Tecnologías Utilizadas

- Python: Lenguaje principal utilizado para el desarrollo del sistema.
- Streamlit: utilizado para construir la interfaz web.
- PyPDF: Biblioteca utilizada para extraer texto desde documentos PDF.

---

## Instalación

- Clonar el repositorio: git clone URL_DEL_REPOSITORIO
- Acceder a la carpeta: cd "ASISTENTE INACAP"
- Instalar dependencias: 
  - pip install streamlit
  - pip install pypdf

---

## Ejecución

- Ejecutar la aplicación: streamlit run web.py
- Luego acceder al navegador: http://localhost:8501

---

## Funcionamiento

- Lectura de Reglamentos: El sistema recorre automáticamente la carpeta: Reglamentos/ y extrae el contenido de todos los archivos PDF disponibles.
- Procesamiento de Consulta: Las consultas del usuario son normalizadas para eliminar signos de puntuación y palabras irrelevantes.
- Ejemplo: ¿Cuál es la nota mínima para aprobar?
- Se transforma en: nota minima aprobar
- Recuperación de Información: El sistema busca coincidencias dentro de los reglamentos utilizando palabras clave relevantes.
- Ranking: Cada fragmento obtiene un puntaje según la cantidad de coincidencias encontradas. Posteriormente los resultados se ordenan para mostrar primero la información más relevante.
- Generación de Respuesta: La información encontrada es formateada y presentada al usuario mediante una interfaz conversacional.

---

## Conceptos Aplicados

Durante el desarrollo se aplicaron conceptos relacionados con:
- Procesamiento básico de texto.
- Recuperación de información.
- Ranking por relevancia.
- Programación modular.
- Interfaces web.
- Manejo de archivos PDF.
- Principios de arquitectura RAG.

---

## Mejoras Futuras

- Integración con modelos de IA.
- Exportación de respuestas.
- Despliegue en servidor institucional.

---

