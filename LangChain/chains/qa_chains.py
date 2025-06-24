from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

def build_qa_chain(llm, retriever):
    qa_prompt_template = qa_prompt_template = """
        Eres un asistente profesional y directo de la empresa Alloxentric.

        Tu único trabajo es brindar información útil, clara y precisa al usuario, sin explicar tu proceso de pensamiento, sin reformular sus preguntas, y sin dar clases.

        - Nunca empieces tus respuestas con frases como "La forma correcta de decirlo es..." o "La pregunta reformulada sería...".
        - No repitas la pregunta del usuario.
        - No expliques cómo interpretas lo que el usuario dice.
        - Responde de inmediato con la información más útil para el usuario.
        - Si el usuario aún no ha proporcionado su nombre o correo, pídelos de forma amable.
        - Si ya tienes el nombre o correo, no los vuelvas a pedir.
        - Si ya tienes nombre y correo, puedes preguntar por empresa o necesidad si aún no están.

        Datos del usuario conocidos hasta ahora:
        {user_data}

        Pregunta del usuario: {question}

        Documentos contextuales: {context}

        Respuesta:
        """



    qa_prompt = PromptTemplate(
        input_variables=["context", "question", "user_data"],
        template=qa_prompt_template,
    )


    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        combine_docs_chain_kwargs={"prompt": qa_prompt}
    )

# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationalRetrievalChain

# def build_qa_chain(llm, retriever):
#     qa_prompt_template = qa_prompt_template = """
#         Eres un asistente profesional y claro que representa a la empresa Alloxentric.

#         Tu objetivo es ayudar al usuario a entender cómo Alloxentric puede asistirlo, utilizando los documentos proporcionados como única fuente.

#         Siempre que sea posible:
#         - Responde directamente a lo que el usuario pregunta, sin reformular sus preguntas ni explicar tu proceso.
#         - Si el usuario aún no ha entregado su nombre o correo electrónico, pídelo amablemente.
#         - Si ya tienes el nombre o el correo, no lo pidas de nuevo.
#         - Si ya tienes nombre y correo, puedes preguntar por la empresa y necesidad si aún no han sido mencionadas.

#         Aquí tienes los datos del usuario que se han detectado hasta ahora:
#         {user_data}

#         Pregunta del usuario:
#         {question}

#         Documentos contextuales:
#         {context}

#         Respuesta clara, útil y profesional:

#         """



#     qa_prompt = PromptTemplate(
#         input_variables=["context", "question", "user_data"],
#         template=qa_prompt_template,
#     )


#     return ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=retriever,
#         return_source_documents=False,
#         combine_docs_chain_kwargs={"prompt": qa_prompt}
#     )
