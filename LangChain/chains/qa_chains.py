from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

def build_qa_chain(llm, retriever):
    # Prompt para generar la respuesta final basada en documentos
    qa_prompt_template = """
Eres un asistente experto en la empresa Alloxentric. Solo responde basándote en los documentos proporcionados.
Si no puedes responder con la información disponible, di: "Lo siento, no tengo información sobre eso".

Pregunta: {question}

Documentos contextuales:
{context}

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
