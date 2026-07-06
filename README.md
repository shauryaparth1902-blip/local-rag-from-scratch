
# Local RAG Pipeline 🧠

A fully local, framework-free Retrieval-Augmented Generation (RAG) architecture built entirely from scratch in Python. 

Unlike most modern AI projects that rely on heavy abstraction libraries like LangChain, this project handles raw vector embeddings, calculates cosine similarity using pure Python math, and feeds the optimal context window into a local LLM. It is designed to be lightweight, fast, and 100% private.

## ✨ Features
* **Zero-Framework Architecture:** No LangChain, no LlamaIndex. Just pure Python and raw math.
* **100% Local & Private:** Runs entirely on your own hardware using Ollama. No API keys, no cloud data leaks.
* **Custom Vector Search:** Uses custom-written cosine similarity algorithms to calculate the mathematical distance between concepts.
* **Dynamic Context Injection:** Retrieves the most mathematically relevant text chunks and dynamically constructs a prompt for the AI.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **LLM Engine:** Ollama
* **Generation Model:** Microsoft Phi-3 (`phi3`)
* **Embedding Model:** Nomic Embed Text (`nomic-embed-text`)

## 🚀 Getting Started

### Prerequisites
1. Install [Ollama](https://ollama.com/).
2. Pull the required models by running these commands in your terminal:
   ```bash
   ollama run phi3
   ollama pull nomic-embed-text
