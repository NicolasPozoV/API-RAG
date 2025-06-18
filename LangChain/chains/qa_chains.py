from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

def build_qa_chain(llm, retriever):
    # Prompt para generar la respuesta final basada en documentos
    qa_prompt_template = """
        Eres un asistente experto en la empresa Alloxentric. Solo responde basándote en los documentos proporcionados.
        Si no puedes responder con la información disponible, di: "Lo siento, no tengo información sobre eso."
        Si la respuesta contiene una explicación de por qué no tienes información, cámbiala por: "Lo siento, no tengo información sobre eso."

        Pregunta: {question}

        Documentos contextuales: {context}

        Respuesta útil:
    """


    qa_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=qa_prompt_template,
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        combine_docs_chain_kwargs={"prompt": qa_prompt}
    )


# from langchain.chains import ConversationalRetrievalChain
# from langchain.prompts import PromptTemplate
# from langchain.chains.qa_with_sources import load_qa_with_sources_chain

# def build_qa_chain(llm, retriever):
#     # Prompt para generar la respuesta final basada en documentos
#     qa_prompt_template = """
#         Eres un asistente experto en la empresa Alloxentric. Solo responde basándote en los documentos proporcionados.
#         Si no puedes responder con la información disponible, di: "Lo siento, no tengo información sobre eso".

#         Pregunta: {question}

#         Documentos contextuales: {context}

#         Respuesta útil:
#         """

#     qa_prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template=qa_prompt_template,
#     )

#     # Crear la cadena de recuperación conversacional
#     qa_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=retriever,
#         return_source_documents=False,
#         combine_docs_chain_kwargs={"prompt": qa_prompt}
#     )

#     # Modificar la respuesta del QA Chain
#     def custom_qa_chain(question, chat_history):
#         respuesta = qa_chain.invoke({
#             "question": question,
#             "chat_history": chat_history
#         })

#         # Si la respuesta es demasiado genérica o dice que no se encontró nada, reemplazarla por un mensaje específico
#         if respuesta["answer"] in ["No tengo información sobre eso", "Lo siento, no tengo información sobre eso", "No se encuentra información relevante"]:
#             respuesta["answer"] = "Lo siento, no tengo información sobre eso"
        
#         return respuesta

#     return custom_qa_chain
# # Retornar la cadena personalizada