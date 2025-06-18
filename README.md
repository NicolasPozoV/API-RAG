# ChatBot Alloxentric - Implementación con LangChain y Weaviate

## Introducción

Este proyecto implementa un chatbot interactivo para la empresa **Alloxentric**, diseñado para responder preguntas sobre sus servicios y agendar citas. Utiliza **LangChain** para la integración de un modelo de lenguaje, junto con una base de datos **MongoDB** para almacenar la información del usuario y de las conversaciones, y **Weaviate** como cliente de recuperación de información para consultas más detalladas.

La principal funcionalidad del chatbot es ofrecer asistencia en tiempo real, respondiendo a las preguntas de los usuarios y proporcionando la opción de agendar citas. Si el chatbot no tiene información específica sobre una consulta, ofrece la posibilidad de agendar una cita para una consulta más profunda.

### Integrantes del Proyecto

* **Aranza Sue Díaz Tovar**
* **Nicolás Armando Pozo Villagrán**
* **Javier Alonso Nanco Becerra**
* **Josefa Isadora González Rocha**

---

Ahora, la introducción incluye a todos los miembros del equipo, dándoles el reconocimiento correspondiente.

---

## Estructura del Proyecto

El script principal del proyecto está compuesto por varias dependencias y módulos que permiten interactuar con la base de datos, cargar y almacenar información del usuario, integrar el modelo de lenguaje, y realizar la gestión de las citas.

### Principales Componentes

1. **LangChain**: LangChain es una biblioteca de Python diseñada para facilitar el uso de modelos de lenguaje en aplicaciones de múltiples etapas. Este proyecto hace uso de LangChain para construir una cadena de preguntas y respuestas (QA), integrando el modelo Groq para generar respuestas a las preguntas de los usuarios y crear una experiencia de conversación fluida.

2. **Weaviate**: Se usa Weaviate como base para la recuperación de información. Weaviate es una base de datos vectorial que permite almacenar y recuperar información de forma eficiente, lo que facilita las consultas semánticas y el uso de embeddings (representaciones vectoriales de las palabras) para obtener respuestas relevantes y precisas.

3. **MongoDB**: MongoDB se usa como base de datos para almacenar los datos de los usuarios, como su nombre, correo electrónico y número de teléfono, así como el historial de las conversaciones con el chatbot.

---

## Instalación y Dependencias

1. **Instalar las dependencias necesarias**:

2. **Configurar la base de datos MongoDB**:

3. **Weaviate**: 

---

### Funcionamiento General

El chatbot interactúa con el usuario a través de un ciclo de preguntas y respuestas. En cada interacción, el chatbot:

* Responde a las consultas del usuario utilizando LangChain, respondiendo de forma natural gracias a la integración de un modelo LLM
* La información de Alloxentric se encuentra en una base de datos Vectorial.
* Constantemente se ofrece la posibilidad de agendar una cita. Al momento de solicitarla se le pide al usuario información para realizar el agendamiento (nombre, teléfono, correo).
* Guarda la información de la conversación y los datos del usuario en la base de datos MongoDB.


### Comando de Salida

Para salir de la conversación, el usuario puede escribir "salir", lo que terminará el ciclo de preguntas y respuestas y almacenará la conversación. El archivo que contiene los comandos para salir se encuentar en [respuestas_salidas.py](./LangChain/config/respuestas_salida.py)
