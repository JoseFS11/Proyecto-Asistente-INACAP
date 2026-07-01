# 🎓 Asistente INACAP

## Descripción

El siguiente proyecto surge a raiz de las constantes consultas a docentes y administrativos por temas de notas, asistencia, becas, etc. En base a esto se desarrollo un asistente documental orientado a la consulta de reglamentos institucionales de INACAP, los cuales traen todas las respuestas que los alumnos necesitan.

La aplicación fue desarrollada utilizando **Python** y **Streamlit**, permitiendo buscar información dentro de distintos reglamentos en formato PDF mediante una interfaz conversacional inspirada en los principios de los sistemas **RAG (Retrieval Augmented Generation)**.

---

## Características

- Lectura automática de archivos PDF.
- Carga dinámica de reglamentos.
- Interfaz web desarrollada con Streamlit.
- Historial de consultas.
- Filtrado por reglamentos específicos.
- Ranking básico de relevancia.
- Recuperación de información mediante palabras clave.
- Generación de respuestas contextualizadas.
- Diseño institucional con logo INACAP.

---

## Arquitectura General

```text
Reglamentos PDF
        │
        ▼
Extracción de texto
        │
        ▼
Procesamiento de contenido
        │
        ▼
Fragmentación de información
        │
        ▼
Procesamiento de consultas
        │
        ▼
Búsqueda de coincidencias
        │
        ▼
Ranking por relevancia
        │
        ▼
Generación de respuesta
        │
        ▼
Interfaz Web Streamlit
```

---

## Flujo de funcionamiento

El sistema ejecuta los siguientes pasos:

1. Cargar automáticamente todos los reglamentos disponibles.
2. Extraer el contenido de cada documento PDF.
3. Procesar la consulta realizada por el usuario.
4. Identificar términos relevantes.
5. Buscar coincidencias dentro de los reglamentos.
6. Calcular relevancia de los resultados encontrados.
7. Seleccionar la información más útil.
8. Generar una respuesta contextualizada.
9. Mostrar la respuesta mediante una interfaz conversacional.

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
```

---

# Archivos principales

### `web.py`

Archivo principal del proyecto.

Contiene:

- Interfaz Streamlit.
- Lectura de consultas.
- Historial de preguntas.
- Presentación de respuestas.
- Gestión de filtros y reglamentos.

---

### `Reglamentos/`

Carpeta que almacena todos los documentos PDF utilizados por el asistente.

Los archivos son cargados automáticamente al iniciar la aplicación.

---

### `logo.png`

Imagen institucional utilizada dentro de la interfaz gráfica.

---

### `app_respaldo.py`

Versión inicial del proyecto desarrollada en consola.

Se conserva como referencia del proceso de evolución del sistema.

---

## Tecnologías utilizadas

### `Python`

Lenguaje principal utilizado para el desarrollo del sistema.

### `Streamlit`

Framework utilizado para construir la interfaz web.

### `PyPDF`

Biblioteca utilizada para extraer texto desde documentos PDF.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Acceder a la carpeta

```bash
cd "ASISTENTE INACAP"
```

### 3. Instalar dependencias

```bash
pip install streamlit
pip install pypdf
```

---

## Ejecución

Ejecutar la aplicación:

```bash
streamlit run web.py
```

Luego abrir:

```text
http://localhost:8501
```

---

## Conceptos aplicados

Durante el desarrollo se trabajó con:

- Programación modular.
- Manejo de archivos PDF.
- Procesamiento de texto.
- Recuperación de información.
- Ranking de relevancia.
- Interfaces web.
- Arquitectura inspirada en RAG.
- Desarrollo de asistentes documentales.

---

## Mejoras futuras

- Integración con modelos de IA.
- Búsqueda semántica.
- Respuestas más precisas.
- Exportación de resultados.
- Implementación de autenticación.
- Publicación en servidor institucional.

---

## Autor

**José Solda Huenante**

Proyecto académico desarrollado para la consulta automatizada de reglamentos institucionales mediante técnicas de recuperación documental y principios RAG.
``
