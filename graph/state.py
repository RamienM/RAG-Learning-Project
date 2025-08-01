# Define como la información fluye por nuestro grafo.

from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Representa el estado del grafo.

    Atributos:
        question: la pregunta
        generation: generacion/respuesta del LLM
        web_search: si debe usar busqueda
        documents: lista de documento
    """

    question: str
    generation: str
    web_search: bool
    documents: List[str]