import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from loguru import logger
import os

DATA_PATH = os.path.join("app", "data", "change_history.csv")


def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except Exception as e:
        logger.error(f"Error loading history data: {e}")
        return pd.DataFrame()


def find_similar_changes(new_description, top_n=3):
    df = load_data()

    if df.empty:
        return []

    try:
        texts = df["description"].tolist() + [new_description]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(texts)

        similarity = cosine_similarity(vectors[-1], vectors[:-1])[0]

        top_indices = similarity.argsort()[-top_n:][::-1]

        results = []
        for idx in top_indices:
            row = df.iloc[idx]
            results.append({
                "description": row["description"],
                "risk": row["risk_level"],
                "issues": row["issues"],
                "score": float(similarity[idx])   # 🔥 confidence score
            })

        return results

    except Exception as e:
        logger.error(f"Similarity error: {e}")
        return []