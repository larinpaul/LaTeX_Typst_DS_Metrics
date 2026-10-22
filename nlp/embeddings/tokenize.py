import uuid
import tiktoken

# 1. Inicializamos el tokenizador (por ejemplo, para modelos gpt-4o, gpt-4)
tokenizer = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    """Función para contar tokens de forma exacta en un texto"""
    return len(tokenizer.encode(text))

def split_expert_note_to_children(parent_id: str, text: str, max_tokens: int = 500, overlap_tokens: int = 50) -> list:
    """
    Trocea la nota del experto en fragmentos hijos respetando
    la estructura de párrafos y oraciones (Enfoque Recursivo).
    """
    # Primero separamos el texto en bloques grandes por párrafos
    paragraphs = text.split("\n\n")
    children_chunks = []

    current_chunk_text = ""

    for para in paragraphs:
        ara = para.strip()
        if not para:
            continue

        # Verificamos cuántos tokens añadiría este párrafo
        test_text = current_chunk_text + "\n\n" + para if current_chunk_text else para

        if count_tokens(test_text) <= max_tokens:
            # El párrafo entra bien en el fragmento hijo actual
            current_chunk_text = test_text
        else:
            # Si el fragmento actual no está vacío, lo guardamos antes de empezar uno nuevo
            if current_chunk_text:
                children_chunks.append({
                    "child_id": str(uuid.uuid4()),
                    "parent_id": parent_id,
                    "text": current_chunk_text,
                    "tokens": count_tokens(current_chunk_text)
                })

            # Si UN SOLO párrafo ya supera los 500 tokens, lo cortamos por oraciones
            if count_tokens(para) > max_tokens:
                sentences = para.replace(". ", ".\n").split("\n")
                current_chunk_text = ""
                for sentence in sentences:
                    test_sentence = current_chunk_text + " " + sentence if current_chunk_text else sentence
                    if count_tokens(test_sentence) <= max_tokens:
                        current_chunk_text = test_sentence
                    else:
                        if current_chunk_text:
                            children_chunks.append({
                                "child_id": str(uuid.uuid4()),
                                "parent_id": parent_id,
                                "text": current_chunk_text,
                                "tokens": count_tokens(current_chunk_text)
                            })
                        current_chunk_text = sentence
            else:
                # Empezamos un fragmento nuevo con el párrafo actual
                current_chunk_text = para

    # No nos olvidamos de guardar el último pedazo de texto
    if current_chunk_text:
        children_chunks.append({
            "child_id": str(uuid.uuid4()),
            "parent_id": parent_id,
            "text": current_chunk_text,
            "tokens": count_tokens(current_chunk_text)
        })

    return children_chunks

# Ejemplo de uso en un sistema real

# 1. El experto guarda su nota (Definición en un área de conocimiento)
expert_raw_text = """
Instrucciones para el desplegue dde Nginx de alta carga.

Paso 1. Configuración del kernel de Linux. Antes de levantar el servidor web, es necesario ajustar los límites del sistema operativo. Abran el archivo /etc/sysctl.conf y agreguen el parámetro net.core.somaxconn=65535. Esto permitirá procesar una cola masiva de conexiones TCP entrantes sin que se caigan las sesiones de los usuarios.

Paso 2. Configuración de nginx.conf. En la sección de 'évents', es obligatorio definir woker_connections 4096. Si tienen un procesador de 4 nucleos, el pool total de descriptores será ede 16384. También activen multi_accept on, para que el proceso de trabajo acepte todas las conexiones nuevas en simultáneo.

Paso 3. Caché de archivos estáticos. Para acelerar la entrega de imágenes y scripts, configuren proxy_cache_path. Asignen para eesta caché una memoria rápida en mpfs (/dev/shm), esto reducirá drásticamente la carga de lectura y escritura en los discos SSD. 
"""

# 2. Creamos la tarjeta del Padre (Parent)
parent_card = {
    "parent_id": f"expert_note_{uuid.uuid4().hex[:8]}", # ID único de la nota
    "title": "Guía de despliegue para Nginx",
    "full_text": expert_raw_text,
    "total_tokens": count_tokens(expert_raw_text)
}

print(f"¡PADRE CREADO! ID: {parent_card['parent_id']} (Tokens totales: {parent_card['total_tokens']})\n")

# 3. Lo troceamos en Hijos (Children) con un límite de 500 tokens
child_cards = split_expert_note_to_children(
    parent_id=parent_card["parent_id"],
    text=parent_card["full_text"],
    max_tokens=500
)

# 4. Revisamos el resultado listo para la Base de Datos Vectorial
print(f"Cantidad de fragmentos hijos generados: {len(child_cards)}")
for idx, child in enumerate(child_cards):
    print(f"n--- Fragmento {idx + 1} ({child['tokens']} tokens) ---")
    print(f"ID del Hijo; {child['child_id']}")
    print(f"ID del Padre: {child['parent_id']}")
    print(f"Texto:\n{child['text']}\n")
