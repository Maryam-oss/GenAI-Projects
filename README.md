# 🤖 Generative AI Projects


## 📌 Project Overview

This repository contains 4 practical projects completed.
Each task focuses on real-world applications of Large Language Models (LLMs), including deployment, fine-tuning, retrieval systems, and speech-based AI pipelines.

---

## ⚙️ Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3
* Unsloth
* QLoRA (4-bit Quantization)
* FAISS
* Sentence Transformers
* OpenAI Whisper
* Google Colab

---

# 📂 Project Structure

```
GenAI-Internship-Tasks/
│
├── Task1_Streamlit/
├── Task2_Finetuning/
├── Task3_RAG/
├── Task4_Speech/
```

---

# 🔹 Task 1: Streamlit + Ollama LLM Interface

### 📖 Description

A web-based chatbot application built using Streamlit that connects to a locally running LLM (Llama 3) using Ollama.

### ⚡ Features

* User input text box
* AI-generated responses
* Conversation history
* Reset button
* Runs completely locally (no cloud)

### 🔄 How It Works

1. User enters a query
2. Streamlit sends request to Ollama API
3. Ollama runs Llama 3 locally
4. Response is displayed in UI

### ▶️ How to Run

```bash
python -m pip install streamlit requests
python -m streamlit run Task1_app.py
```

---

# 🔹 Task 2: Medical Fine-tuning (QLoRA with Unsloth)

### 📖 Description

Fine-tuned a Llama 3 model on a medical dataset using QLoRA (4-bit quantization) for efficient training.

### ⚡ Key Concepts

* QLoRA (Low memory fine-tuning)
* Adapter-based training
* Domain-specific learning

### 🔄 Workflow

1. Load quantized model
2. Add LoRA adapters
3. Prepare dataset
4. Train model
5. Save adapter

### 💡 Output Example

Model can answer medical questions like:

* Symptoms of diseases
* Treatments
* Clinical explanations

---

# 🔹 Task 3: RAG (Retrieval-Augmented Generation)

### 📖 Description

Built a system where the model retrieves relevant documents before generating answers.

### ⚡ Features

* Document-based answering
* Reduced hallucination
* More accurate responses

### 🔄 Workflow

1. Convert documents → embeddings
2. Store in FAISS
3. Retrieve top relevant docs
4. Send context to LLM
5. Generate answer

---

# 🔹 Task 4: Speech-to-Reasoning Pipeline

### 📖 Description

An end-to-end pipeline that converts speech into text using Whisper and generates answers using an LLM.

### ⚡ Features

* Speech input → text
* AI reasoning
* End-to-end pipeline

### 🔄 Workflow

1. Audio input
2. Whisper transcription
3. Send text to LLM
4. Generate response

---

# 🚀 Key Learnings

* Running LLMs locally using Ollama
* Efficient fine-tuning using QLoRA
* Building RAG systems for accuracy
* Using Whisper for speech recognition
* Combining multiple AI systems into pipelines

---

# ✅ Conclusion

This project demonstrates practical implementation of modern Generative AI techniques including chatbot development, model fine-tuning, retrieval-based systems, and multimodal AI pipelines.

---

# 📌 Note

All tasks are implemented using open-source tools and are optimized to run on local systems or free cloud platforms like Google Colab.
