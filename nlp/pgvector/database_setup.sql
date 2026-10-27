-- Enable the pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create a table for documents with an embedding column
-- 1536 dimensions matches OpenAI's text-embedding-3-small model
CREATE TABLE articles (
    id bigserial PRIMARY KEY,
    title text NOT NULL,
    content text NOT NULL,
    emedding vector(1536)
);

-- Индекс HNSW (Hierarchical Navigable Small World / Иерархический граф малого мира)
-- Это алгоритм приближенного поиска ближайших соседей (ANN) в многомерных векторных пространствах.
-- (Optional) Create an HNSW index for ulta-fast Approximate Nearest Neigbor (ANN) search
CREATE INDEX ON articles USING hnsw (embedding vector_cosine_ops);
