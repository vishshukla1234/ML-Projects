# 🪩 Vibe Matcher – AI-Powered Fashion Recommender

## 🧠 Overview
**Vibe Matcher** is a prototype recommendation system that matches a user's *vibe query* (like “cozy weekend” or “energetic urban chic”) with the top fashion products that fit that mood.  
It uses **Sentence Transformers** and **cosine similarity** to understand the semantic meaning of both user queries and product descriptions — making it a simple yet powerful *AI-powered recommender system*.

---

## 🎯 Objective
Build a mini recommendation notebook that:
- Takes a **vibe-based query** (e.g., “luxurious occasion”).
- Embeds product descriptions using **sentence-transformers**.
- Finds and ranks the **top 3 most semantically similar items** using **cosine similarity**.
- Evaluates performance with latency and similarity metrics.

---

## 🧩 Workflow

### 1. **Data Preparation**
Created a small dataset of 10 mock fashion products with:
- `name`, `desc`, and `vibes` tags  
- Each representing distinct moods: *energetic urban chic*, *cozy weekend*, and *luxurious occasion*.

### 2. **Embeddings**
Used the `SentenceTransformer` model (`all-mpnet-base-v2` or `all-MiniLM-L6-v2`) to generate high-dimensional embeddings for product texts and user queries.

### 3. **Vector Search**
Calculated cosine similarity between the query vector and all product vectors:
```python
cosine_similarity([query_emb], product_embs)

### 4. **Evaluation**

Ran 3 test queries:

energetic urban chic

cozy weekend

luxurious occasion

Logged metrics like:

Top similarity score

Whether score > threshold (good match)

Query latency using timeit

Calculated accuracy = fraction of queries with a "good match" (> 0.6)
