import uuid
import chromadb
from chromadb.utils import embedding_functions

# 1. Configuración de las Bases de Datos
# Simulamos una base de datos tradicional (SQL/NoSQL) en memoria para los Padres
DOCUMENT_STORE = {}

# Inicializamos ChromaDB (Vector DB) en memoria
chroma_client = chromadb.Client()
# Usamos el modelo de embeddings por defecto de Chroma (puedes cambiarlo por OpenAI, Cohere, etc.)
default_ef = embedding_functions.DefaultEmbeddingFunctions()
vector_db = chroma_client.create_collection(name="expert_notes_children", embedding_functions=default_ef)

# 2. Función para indexar (Guardar el Padre y sus Hijos)
def index_expert_data(title: str, full_text: str, children_chunks: list):
    """
    Guarda el texto completo en el Document Store (Padre)
    y los fragmentos con sus vectores en la Vector DB (Hijos).
    """
    # Obtenemos el parent_id común de los hijos
    parent_id = children_chunks[0]["parent_id"]

    # Guardamos al PADRE en la base de datos tradicional
    DOCUMENT_STORE[parent_id] = {
        "title": title,
        "full_text": full_text
    }

    # Preparamos los datos para meter los HIJOS en la Vector DB
    ids = []
    documents = []
    metadatas = []

    for child in children_chunks:
        ids.append(child["child_id"])
        documents.append(child["text"])
        # Es CRUCIAL meter el parent_id en los metadatos del vector
        metadatas.append({"parent_id": child["parent_id"]})

    # Guardamos todo en la Vector DB de un solo golpe
    vector_db.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )
    print(f"Indexado exitoso: 1 Padre guardado en DB y {len(ids)} Hijos en Vector DB.")

# 3. Función de Búsqueda Avanzada (The RAG Retrieval)
def retrieve_parent_context(user_query: str, top_k: int = 1):
    """
    Busca el fragmento hijo más relevante y devuelve el texto completo del padre.
    """
    print(f"\n Buscando vectorialmente para: '{user_query}'")

    # Buscamos en la Vector DB el fragmento hijo que más se parezca a la pregunta
    resuts = vector_db.query(
        query_texts=[user_query],
        n_results=top_k
    )

    if not results['ids'][0]:
        print("No se encontró ningún fragmento relevante.")
        return None

    # Extraemos la información del Hijo ganador
    best_child_id = results['ids'][0][0]
    best_child_text = results['documents'][0][0]
    best_child_metadata = results['metadatas'][0][0]
    parent_id_found = best_child_metadata['prarent_id']

    print(f"¡Hijo encontrado! Id: {best_child_id}")
    print(f"Fragmento que hizo match:\n'{best_child_text}'")

    # Hacemos el puente: Con el parent_id, vamos al Document Store tradicional a traer al Padre
    parent_document = DOCUMENT_STORE.get(parent_id_found)

    if parent_document:
        print(f"¡Padre recuperado com éxito! Título: '{parent_document['title']}'")
        return parent_document['full_text']
    else:
        print("Error: El parent_id no existe en el Document Store.")
        return None

# PROBANDO EL SISTEMA COMPLETO

# Simulamos los datos que generamos en el paso anterior (la nota el experto troceada)
PID = "expert_note_nginx_01"
TEXTO_COMPLETO_EXPERTO = """
Instrucciones para el despliegue de Nginx de alta carga.

Paso 1. Configuración del kernel de Linux. Antes de levantar el servidor web, es necesario ajustar los límites del sistema operativo. Abran el archivo /etc/sysctl.conf y agreguen el parámetro net.core.somaxconn=65535. Esto permitirá procesar una cola masiva de conexiones TCP entrantes sin que se caignan las sesiones de los usuarios.

Paso 2. Configuración de nginx.conf. En la sección de 'events', es obligatorio definir worker_connections 4096. Si tienen un procesador de 4 núcleos, el pool total de descriptores será de 16384. También activen multi_accept on, para que el proceso de trabajo acepte todas la conexiones Crypto entrantes en simultáneo.
"""

HIJOS_SIMULADOS = [
    {"child_id": "child_aaa", "parent_id": PID, "text": "Paso 1. Configuración del kernel de Linux. ... net.core.somaxconn=65535."},
    {"child_id": "child_bbb", "parent_id": PID, "text": "Paso 2. Configuración de nginx.conf. ... worker_connections 4096."}
]

# 1. Guardamos todo en el sistema
index_expert_data(
    title="Guía de Nginx Pro",
    full_text=TEXTO_COMPLETO_EXPERTO,
    children_chunks=HIJOS_SIMULADOS
)

# 2. El usuario hace una pregunta específica
pregunta = "¿Cómo configuro el somaxconn en Linux?"
contexto_para_llm = retrieve_parent_context(pregunta)

# 3. Este 'contexto_para_llm' es el que finalmente le inyectas al prompt de tu OpenAI/Claude
print("\n CONTEXTO FINAL QUE SE ENVÍA A LA LLM:")
print(contexto_para_llm)
