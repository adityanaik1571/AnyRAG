# AnyRAG

> Bring your own LLM. Bring your own embeddings.

AnyRAG is a modular Retrieval-Augmented Generation (RAG) framework built in Python. The goal of the project is to provide a clean architecture where language models, embedding models, vector databases, and document loaders can be swapped without changing the overall pipeline.

The project is being built as a long-term GenAI engineering project with an emphasis on maintainability, extensibility, and software engineering best practices rather than a one-off demo.

---

## Current Features

- PDF document ingestion
- Recursive text chunking
- Local embedding generation using BAAI/bge-small-en-v1.5
- ChromaDB vector storage
- Semantic similarity search
- Semantic instruction interpretation
- Dynamic prompt construction
- Groq LLM integration
- Structured logging
- Provider abstraction using factories

---

## Architecture

### Document Ingestion

```text
PDF
 │
 ▼
Loader
 │
 ▼
Splitter
 │
 ▼
Embeddings
 │
 ▼
Vector Store
```

### Query Flow

```text
User Input
      │
      ▼
Instruction Interpreter
      │
      ▼
Structured Instruction
      │
      ▼
Vector Retrieval
      │
      ▼
Prompt Builder
      │
      ▼
LLM
      │
      ▼
Response
```

---

## Project Structure

```text
AnyRAG/
│
├── config/
├── core/
├── data/
├── logs/
├── services/
│   ├── embeddings/
│   ├── llm/
│   ├── loaders/
│   ├── rag/
│   ├── reasoning/
│   ├── splitters/
│   └── vectorstores/
│
├── main.py
└── requirements.txt
```

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| AI Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | BAAI/bge-small-en-v1.5 |
| LLM | Groq (Llama 3.3 70B) |
| PDF Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |

---

## Design Goals

This project is built around a few core principles:

- Keep components modular and replaceable.
- Avoid coupling business logic to a specific AI provider.
- Build features behind abstractions instead of concrete implementations.
- Separate document ingestion, retrieval, reasoning, and generation into independent layers.
- Make it easy to extend the framework with new providers and capabilities.

---

## Roadmap

### Core Engine

- [x] Project architecture
- [x] Configuration management
- [x] Logging
- [x] PDF ingestion
- [x] Text splitting
- [x] Embedding abstraction
- [x] Vector store abstraction
- [x] ChromaDB integration
- [x] Semantic instruction interpreter
- [x] Prompt builder
- [x] End-to-end RAG pipeline

### Next

- [ ] Structured query response
- [ ] Source citations
- [ ] Multiple document support
- [ ] Metadata filtering
- [ ] Chat history
- [ ] Gradio interface
- [ ] FastAPI backend
- [ ] Docker support
- [ ] Additional LLM providers
- [ ] Additional embedding providers
- [ ] Additional vector databases

---

## Project Vision

AnyRAG started as a document question-answering project but is gradually evolving into a provider-agnostic RAG framework.

The long-term goal is to support multiple document types, interchangeable AI providers, different retrieval strategies, and richer reasoning workflows while keeping the core architecture unchanged.