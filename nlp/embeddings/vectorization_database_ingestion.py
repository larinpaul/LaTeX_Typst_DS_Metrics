# Step 3: Vectorization & Database Ingestion

# When inserting the data into your vector database
# (e.g., Pinecone, Weaviate, or Qdrant)
# target the structured summary for your vector generation,
# rather than the raw chunk

import openai
from qdrant_client import QdrantClient

# 1. The generated card text from your LLM pipeline
card_markdown = """
# Vector DB Quantization
**Context:** Storing billions of high-dimensional vectros in memory is financially unsustainable.
**Key Takeways:**
- Scalar Quantization (SQ) maps floats to int8, cutting memory by 75%.
- Product Quantization (PQ) splits vectors into subvectors, cutting memory by 97%.
**Technical Tags:** [Databases, DevOps, Quantization]
"""

# 2. Embed the highly dense card text
response = openai.Embedding.create(
    input=card_markdown,
    model="text-embedding-3-small"
)
vector = response['data'][0]['embedding']

# 3. Store in Vector DB
client = QdrantClient(url="https://localhost:6333")
client.upsert(
    collection_name="knowledge_cards",
    points=[
        {
            "id": 1,
            "vector": vector,
            "payload": {
                "uid_card_html": card_markdown, # User for immediate front-end rendering
                "parent_doc_id": "doc_84920", # Reference to full-text file
                "tags": ["Databases", "Quantization"] # Filterable metadata
            }
        }
    ]
)
