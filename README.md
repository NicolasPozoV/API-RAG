# 🤖 ChatBot conversacional de ventas Alloxentric - Implementación con LangChain, Weaviate y MongoDB

## 📚 Introducción

Este proyecto implementa un chatbot interactivo para la empresa **Alloxentric**, diseñado para responder preguntas sobre sus servicios y agendar citas. Utiliza **LangChain** para la integración de un modelo de lenguaje, junto con una base de datos **MongoDB** para almacenar la información del usuario y de las conversaciones, y **Weaviate** como cliente de recuperación de información para consultas más detalladas.

La principal funcionalidad del chatbot es ofrecer asistencia en tiempo real, respondiendo a las preguntas de los usuarios y proporcionando la opción de agendar citas. Si el chatbot no tiene información específica sobre una consulta, ofrece la posibilidad de agendar una cita para una consulta más profunda.

### Integrantes del Proyecto

* **Aranza Sue Díaz Tobar**
* **Nicolás Armando Pozo Villagrán**
* **Javier Alonso Nanco Becerra**
* **Josefa Isadora González Rocha**

## 🛠️ Estructura del Proyecto

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

# 📥 Instalación

## 📦 Instalación de Weaviate

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

## 🔗 Instalación LangChain

### Paso 1: Configuración de la API Key de Groq

Para usar LangChain con el modelo Groq, primero necesitas obtener una **API Key** de Groq. Esta clave es necesaria para interactuar con los servicios de Groq.

1. **Obten la API Key de Groq**:

   * Regístrate en [Groq](https://www.groq.com/).
   * Obtén tu clave API desde el panel de control de la cuenta de Groq.

2. **Configura la API Key**:

   * Crea un archivo `.env` en el directorio [LangChain](./LangChain/).
   * Añade la siguiente línea al archivo `.env`, reemplazando `YOUR_API_KEY` con la clave que obtuviste de Groq:

   ```
   GROQ_API_KEY=YOUR_API_KEY
   ```

   **Importante**: Este archivo debe estar en el mismo directorio que el script [chatbot.py](./LangChain/chatbot.py) para poder acceder a la clave correctamente.

### Paso 2: Instalación de las Dependencias

A continuación, instala las dependencias necesarias para que el proyecto funcione correctamente. Estas dependencias se encuentran en el archivo `requirements.txt`.

Para instalar las dependencias, simplemente ejecuta el siguiente comando en tu terminal:

   ```bash
   pip install -r requirements.txt
   ```

   Esto instalará **LangChain**, **Weaviate Client** y **OpenAI**, junto con cualquier otra librería necesaria que esté listada en el archivo `requirements.txt`.

### Documentación Detallada

Para más detalles sobre cómo configurar y usar el chatbot, consulta el [README más detallado aquí](./LangChain/Readme.md).

## 📍 Instalación de MongoDB de manera local (Opcional)

Para que tu proyecto funcione correctamente con MongoDB, necesitas instalar y configurar MongoDB de manera local en tu máquina. Sigue estos pasos para instalar MongoDB en tu entorno local.

### Paso 1: Descargar e Instalar MongoDB

1. **Descargar MongoDB**:

   * Dirígete a la página oficial de descargas de MongoDB: [MongoDB Download Center](https://www.mongodb.com/try/download/community).
   * Selecciona la versión más reciente de **MongoDB Community Server** para tu sistema operativo (Windows, macOS o Linux) y descarga el instalador correspondiente.

2. **Instalar MongoDB**:

En caso de no tener acceso a una base de datos no relacional se puede correr de manera local:

   * Sigue las instrucciones de instalación para tu sistema operativo. Asegúrate de seleccionar la opción para instalar MongoDB como un servicio, lo que te permitirá ejecutar MongoDB en segundo plano sin tener que iniciar el servidor manualmente cada vez.
   * Para **Windows**, asegúrate de agregar MongoDB al **PATH** durante la instalación para facilitar su ejecución desde la línea de comandos.
   * Para **macOS y Linux**, la instalación puede realizarse a través de **Homebrew** (macOS) o con el paquete `.tar.gz` o `.deb` disponible en la página de descargas.

### Paso 2: Iniciar MongoDB

Una vez que MongoDB esté instalado en tu máquina, debes iniciar el servidor de MongoDB para que esté listo para recibir conexiones.

* **En Windows**, abre una terminal (CMD o PowerShell) y ejecuta:

  ```bash
  mongod
  ```

  Esto iniciará el servidor de MongoDB en el puerto predeterminado `27017`.

* **En macOS/Linux**, si usas **Homebrew** en macOS, puedes iniciar MongoDB con:

  ```bash
  brew services start mongodb-community@5.0
  ```

  O simplemente ejecutando:

  ```bash
  mongod
  ```

  Esto también iniciará el servidor en el puerto predeterminado `27017`.


### Comando de Salida

Para salir de la conversación, el usuario puede escribir "salir", lo que terminará el ciclo de preguntas y respuestas y almacenará la conversación. El archivo que contiene los comandos para salir se encuentar en [respuestas_salidas.py](./LangChain/config/respuestas_salida.py)
