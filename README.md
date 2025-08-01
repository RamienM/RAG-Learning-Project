# 🚀 Proyecto basado en "Building Agentic RAG with LangGraph"

Este repositorio sigue paso a paso el artículo publicado en [Plain English](https://ai.plainenglish.io/building-agentic-rag-with-langgraph-mastering-adaptive-rag-for-production-c2c4578c836a), donde se explica cómo construir un sistema Agentic RAG (Retrieval-Augmented Generation) utilizando LangGraph.

## 📚 Propósito

El objetivo principal de este proyecto es **aprender y entender en profundidad cómo funciona LangGraph** y cómo construir un flujo de trabajo **RAG adaptativo orientado a producción**. Todo el código y los experimentos realizados tienen un fin **educativo y exploratorio**.

## 🛠️ Instalación y uso
> **Versión recomendada de Python:** `Python 3.10+`  
> Se recomienda utilizar [Anaconda](https://anaconda.org/anaconda/python) para facilitar la gestión del entorno.

### Instrucciones de configuración

1. Instala las dependencias requeridas:  
   ```bash
   pip install -r requirements.txt
   ```

2. Configura tus variables de entorno creando un archivo .env en la raíz del proyecto. Puedes usar el archivo de ejemplo .env.sample como plantilla

3. Creación de la base de datos vectorizada
    ```bash
   python ingestion.py
   ```

4. Ejecución del programa principal
    ```bash
    python main.py
    ```