# Python Chatbot Learning Series

A step-by-step guide to building chatbots with Python, from the simplest rule-based bot to a full RAG (Retrieval-Augmented Generation) chatbot. Each phase has its own Flask web app.

## Phases

| # | Type | Folder | Key Concepts |
|---|------|--------|--------------|
| 1 | Rule-Based | `01_rule_based/` | Keywords, if/else logic |
| 2 | Pattern Matching | `02_pattern_matching/` | Regex, NLTK, intents |
| 3 | ML-Based | `03_ml_based/` | TF-IDF, intent classification |
| 4 | LLM-Powered | `04_llm_powered/` | Claude API, conversation memory |
| 5 | RAG Chatbot | `05_rag_chatbot/` | Embeddings, vector search, RAG |

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Run a chatbot (e.g. Phase 1)
cd 01_rule_based
python app.py
# Open http://localhost:5000
```

## Phase-by-Phase Guide

### Phase 1 — Rule-Based Chatbot
The simplest chatbot. Checks for keywords in the user's message and returns pre-written responses.
- No ML, no external APIs
- Fast and predictable
- Limited to what you explicitly program

```bash
cd 01_rule_based && python app.py
```

### Phase 2 — Pattern Matching Chatbot *(coming soon)*
Uses regex patterns and NLTK for more flexible intent detection.

### Phase 3 — ML-Based Chatbot *(coming soon)*
Trains a TF-IDF + Naive Bayes classifier to detect user intent.

### Phase 4 — LLM-Powered Chatbot *(coming soon)*
Connects to the Claude API for intelligent, context-aware responses with memory.

### Phase 5 — RAG Chatbot *(coming soon)*
Lets the bot answer questions about your own documents using vector search.

## Project Structure

```
Chatbot/
├── 01_rule_based/
│   └── app.py
├── 02_pattern_matching/
│   └── app.py
├── 03_ml_based/
│   └── app.py
├── 04_llm_powered/
│   └── app.py
├── 05_rag_chatbot/
│   └── app.py
├── shared/
│   └── templates/
│       └── chat.html       # Shared chat UI
├── requirements.txt
└── README.md
```
