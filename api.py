from fastapi import FastAPI
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = FastAPI()

# --------------------
# Load artifacts
# --------------------
new_df = pickle.load(open("recommender/new_df.pkl", "rb"))
embeddings = pickle.load(open("recommender/embeddings.pkl", "rb"))

index = faiss.read_index("recommender/course.index")

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------
# Recommendation logic
# --------------------
def recommend(course_name):

    course_index = new_df[
        new_df["course_name"].str.contains(course_name, case=False, na=False)
    ].index[0]

    query_vector = model.encode(
        [new_df.iloc[course_index]["tags"]]
    ).astype("float32")

    distances, indices = index.search(query_vector, 6)

    results = []
    for i in indices[0]:
        results.append({
            "course_name": new_df.iloc[i]["course_name"],
            "course_url": new_df.iloc[i]["course_url"]
        })

    return results


# --------------------
# API Endpoint
# --------------------
@app.get("/")
def home():
    return {"message": "Course Recommendation API is running 🚀"}


@app.get("/recommend")
def get_recommendations(course: str):
    return {
        "input": course,
        "recommendations": recommend(course)
    }


#import os

#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(
        #app,
        #host="0.0.0.0",
        #port=int(os.environ.get("PORT", 8000))
    #)