# ChatBot conversacional de ventas Alloxentric - Implementación con LangChain, Weaviate y MongoDB

## Introducción

Este proyecto implementa un chatbot interactivo para la empresa **Alloxentric**, diseñado para responder preguntas sobre sus servicios y agendar citas. Utiliza **LangChain** para la integración de un modelo de lenguaje, junto con una base de datos **MongoDB** para almacenar la información del usuario y de las conversaciones, y **Weaviate** como cliente de recuperación de información para consultas más detalladas.

La principal funcionalidad del chatbot es ofrecer asistencia en tiempo real, respondiendo a las preguntas de los usuarios y proporcionando la opción de agendar citas. Si el chatbot no tiene información específica sobre una consulta, ofrece la posibilidad de agendar una cita para una consulta más profunda.

### Integrantes del Proyecto

* **Aranza Sue Díaz Tobar**
* **Nicolás Armando Pozo Villagrán**
* **Javier Alonso Nanco Becerra**
* **Josefa Isadora González Rocha**

## Estructura del Proyecto

El script principal del proyecto está compuesto por varias dependencias y módulos que permiten interactuar con la base de datos, cargar y almacenar información del usuario, integrar el modelo de lenguaje, y realizar la gestión de las citas.

### Principales Componentes

1. **[LangChain](./LangChain/Readme.md)**: LangChain es la biblioteca que se utiliza para hacer todo el esqueleto del bot. Conectara toda la tecnologia responsable de construir la cadena de preguntas y respuestas y mantener la concistencia de estas. Principalmente integrando un modelo de Groq para generar la experiencia mas completa de Groq.

2. **[weaviate_local](./weaviate_local/Readme.md)**: Se usa Weaviate como base para la recuperación de información. Weaviate es una base de datos vectorial que permite almacenar y recuperar información de forma eficiente, lo que facilita las consultas semánticas y el uso de embeddings (representaciones vectoriales de las palabras) para obtener respuestas relevantes y precisas.

3. **[MongoDB](./LangChain/db/README.md)**: MongoDB se usa como base de datos para almacenar los datos de los usuarios, como su nombre, correo electrónico y número de teléfono, así como el historial de las conversaciones con el chatbot.

### Funcionamiento General

El chatbot interactúa con el usuario a través de un ciclo de preguntas y respuestas. En cada interacción, el chatbot:

* Responde a las consultas del usuario utilizando LangChain, respondiendo de forma natural gracias a la integración de un modelo LLM
* La información de Alloxentric se encuentra en una base de datos Vectorial.
* Constantemente se ofrece la posibilidad de agendar una cita. Al momento de solicitarla se le pide al usuario información para realizar el agendamiento (nombre, teléfono, correo).
* Guarda la información de la conversación y los datos del usuario en la base de datos MongoDB.

# Instalación

## Instalación de Weaviate

### Paso 1: Instalación del Cliente de Weaviate

Para comenzar, necesitamos instalar el cliente de Weaviate en tu entorno de desarrollo. Ejecuta el siguiente comando para instalar la última versión:

```bash
%pip install -U weaviate-client
```

### Paso 2: Instalación de Dependencias Adicionales

A continuación, instala PyMuPDF, que nos ayudará a extraer texto de archivos PDF:

```bash
%pip install weaviate-client PyMuPDF
```

### Paso 3: Configuración de Weaviate para Almacenar PDFs

En este paso, creamos una colección en Weaviate para almacenar los textos extraídos de los archivos PDF. El siguiente código se conecta a Weaviate, crea la colección `PdfPage` y carga los [textos extraídos de los PDFs](./weaviate_local/4.%20Cargar%20PdfPage.ipynb)

### Requisitos de Docker

Para que Weaviate funcione correctamente, es necesario tener Docker corriendo en tu máquina. Si no tienes Docker instalado, puedes seguir los siguientes pasos:

1. **Instalar Docker Desktop**: Se recomienda utilizar Docker Desktop, ya que facilita la configuración y ejecución de contenedores. Puedes descargarlo e instalarlo desde [aquí](https://www.docker.com/products/docker-desktop). Aunque cabe aclarar que se permiten alternativas.

2. **Iniciar Docker Compose**: Después de instalar Docker, asegúrate de que Docker Compose esté funcionando. Ejecuta el siguiente comando para levantar los servicios de Weaviate en contenedores Docker:

   ```bash
   docker-compose up
   ```

> **Nota**: Asegúrate de tener configurado Docker Desktop en modo `Windows Subsystem for Linux (WSL2)` si usas Windows para evitar problemas de compatibilidad y ademas que al momento de correr el comando te encuentres en la carpeta [weaviate_local](./weaviate_local/).

### Documentación Detallada

Para más detalles sobre cómo configurar y usar Weaviate, consulta el [README más detallado aquí](./weaviate_local/Readme.md).

### Comando de Salida

Para salir de la conversación, el usuario puede escribir "salir", lo que terminará el ciclo de preguntas y respuestas y almacenará la conversación. El archivo que contiene los comandos para salir se encuentar en [respuestas_salidas.py](./LangChain/config/respuestas_salida.py)
