# model.py
import pickle
import logging

# ----------------- Configure Logging -----------------
logging.basicConfig(filename='model.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Loading pickle files...")

# ----------------- Load Pickled Data -----------------
try:
    with open("pickle_files/cleaned_data.pkl", "rb") as f:
        df = pickle.load(f)
    logging.info("Loaded cleaned_data.pkl successfully.")
except Exception as e:
    logging.error(f"Error loading cleaned_data.pkl: {e}")

try:
    with open("pickle_files/user_final_rating.pkl", "rb") as f:
        user_final_rating_df = pickle.load(f)
    logging.info("Loaded user_final_rating.pkl successfully.")
except Exception as e:
    logging.error(f"Error loading user_final_rating.pkl: {e}")

try:
    with open("pickle_files/sentiment_xgb_model.pkl", "rb") as f:
        sentiment_model = pickle.load(f)
    logging.info("Loaded sentiment_xgb_model.pkl successfully.")
except Exception as e:
    logging.error(f"Error loading sentiment_xgb_model.pkl: {e}")

try:
    with open("pickle_files/tfidf_vectorizer.pkl", "rb") as f:
        tfidf_vectorizer = pickle.load(f)
    logging.info("Loaded tfidf_vectorizer.pkl successfully.")
except Exception as e:
    logging.error(f"Error loading tfidf_vectorizer.pkl: {e}")

# ----------------- Sentiment Scoring -----------------
def get_product_sentiment_score(product_name):
    """Returns average positive sentiment probability for all reviews of a product."""
    product_reviews = df[df['name'] == product_name]['cleaned_review'].dropna()
    if product_reviews.empty:
        logging.warning(f"No reviews found for product: {product_name}")
        return 0
    X = tfidf_vectorizer.transform(product_reviews)
    probs = sentiment_model.predict_proba(X)
    positive_probs = probs[:, -1]
    return positive_probs.mean()

def rerank_by_sentiment(top_products, top_n=5):
    """Re-ranks products by average positive sentiment."""
    product_scores = []
    for product in top_products.index:
        score = get_product_sentiment_score(product)
        product_scores.append((product, score))
    product_scores = sorted(product_scores, key=lambda x: x[1], reverse=True)
    return product_scores[:top_n]

# ----------------- Final Recommendation Function -----------------
def get_product_recommendations(username, top_n=20, sentiment_top_n=5):
    """
    Returns top N recommendations re-ranked by sentiment.
    Handles missing usernames gracefully.
    """
    if username not in user_final_rating_df.index:
        logging.warning(f"Username '{username}' not found")
        return {"error": f"Username '{username}' not found"}
    
    logging.info(f"Generating recommendations for user: {username}")
    top_n_recommendations = user_final_rating_df.loc[username].sort_values(ascending=False)[:top_n]
    top_5_sentiment_recommendations = rerank_by_sentiment(top_n_recommendations, top_n=sentiment_top_n)
    
    recommendations = []
    for product, score in top_5_sentiment_recommendations:
        product_row = df[df['name'] == product].iloc[0]
        recommendations.append({
            "product": product,
            "brand": product_row.get('brand', 'N/A'),
            "recommendation": round(score * 100, 2)
        })
    return {"username": username, "recommendations": recommendations}
