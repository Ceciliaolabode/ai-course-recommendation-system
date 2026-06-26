# 🎓 AI Course Recommendation System

A semantic course recommendation system powered by **Sentence Transformers** and **FAISS**, exposed via **FastAPI** and ready for production use.

---

## 🚀 Features

- 🔍 Semantic search using transformer embeddings
- ⚡ Fast similarity search using FAISS
- 🌐 REST API built with FastAPI
- 🧠 NLP-powered tagging system
- 📊 Course recommendation engine

---

## 🧠 Tech Stack

- Python
- Sentence Transformers (MiniLM)
- FAISS
- FastAPI
- Pandas
- Streamlit (optional frontend)

---

## ⚙️ How it works

1. Course descriptions are converted into embeddings
2. FAISS stores vector representations
3. User input is embedded using transformer model
4. Nearest neighbors are retrieved using vector search

---

## 🚀 Run the API

```bash
uvicorn api:app --reload

http://127.0.0.1:8000/docs

Example API call: /recommend?course=Finance for Managers


📷 Architecture

User → FastAPI → SentenceTransformer → FAISS → Recommendations

👩🏽‍💻 Author

Cecilia Olabode







Kindly find above an updated version.
# 🎓 AI Course Recommendation System

An NLP-powered content-based recommendation system that recommends similar online courses based on course descriptions, difficulty level, and skills.

Built using **Python**, **Natural Language Processing (NLP)**, **Scikit-learn**, and **Streamlit**.

---

## 📌 Project Overview

This project uses Natural Language Processing techniques to analyze course information and recommend similar courses to users.

Instead of relying on user ratings or purchase history, the system compares the textual content of courses to identify those that are most alike.

---

## 🚀 Features

* NLP-based content recommendation
* Text preprocessing and cleaning
* Feature engineering using a `tags` column
* Tokenization and stemming
* Text vectorization using CountVectorizer
* Cosine similarity for course matching
* Interactive Streamlit web application
* Fast recommendations using serialized model files (`pickle`)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

---

## 🧠 Machine Learning Pipeline

1. Load the Coursera dataset
2. Clean and preprocess textual data
3. Create a combined `tags` feature from:

   * Course Name
   * Difficulty Level
   * Course Description
   * Skills
4. Perform stemming using NLTK PorterStemmer
5. Convert text into numerical vectors using CountVectorizer
6. Compute cosine similarity between courses
7. Recommend the most similar courses
8. Save model artifacts using Pickle
9. Serve recommendations through a Streamlit interface

---

## 📂 Project Structure

```text
Course-Recommendation-System/
│
├── app.py
├── README.md
├── requirements.txt
├── recommender/
│   ├── similarity.pkl
│   ├── course_list.pkl
│   └── Coursera.csv.zip
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/course-recommendation-system.git
```

Navigate into the project:

```bash
cd course-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

The application allows users to:

* Select a course from a dropdown
* Click the **Recommend** button
* View six similar courses with clickable links

---

## 🔮 Future Improvements

* Semantic search using sentence embeddings
* Transformer-based recommendations (BERT/Sentence Transformers)
* Personalized recommendations based on user preferences
* Course filtering by category or difficulty
* Cloud deployment
* REST API using FastAPI

---

## 📚 Concepts Demonstrated

* Data preprocessing
* Text cleaning
* Feature engineering
* Tokenization
* Stemming
* Bag of Words
* CountVectorizer
* Cosine similarity
* Recommendation systems
* Model serialization
* Streamlit deployment

---

## 👩‍💻 Author

**Cecilia Olabode**

AI/ML Engineer | AI Automation Specialist | Software Engineer

Passionate about Artificial Intelligence, NLP, AI for Healthcare, AI Security, and building intelligent solutions for Africa.
