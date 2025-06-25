from langchain.prompts import PromptTemplate

def build_extractor_chain(llm):
    prompt = PromptTemplate(
        input_variables=["chat_history"],
            # template="""\nExtrae del siguiente historial los datos del usuario si están disponibles.\nDevuelve en JSON estrictamente este formato:\n\n{{\n  \"nombre\": \"\",\n  \"empresa\": \"\",\n  \"necesidad\": \"\",\n  \"correo\": \"\"\n}}\n\nHistorial:\n{chat_history}\n"""
            # Añadimos idioma ahora en template
            template="""\nExtrae del siguiente historial los datos del usuario si están disponibles (idioma es el idioma del input del usuario de la pregunta, si buscas la empresa Alloxentric NUNCA será la empresa).\nDevuelve en JSON estrictamente este formato:\n\n{{\n  \"nombre\": \"\",\n  \"empresa\": \"\",\n  \"necesidad\": \"\",\n  \"correo\": \"\",\n  \"idioma\": \"\"\n}}\n\nHistorial:\n{chat_history}\n""" 
        )
    return prompt | llm
