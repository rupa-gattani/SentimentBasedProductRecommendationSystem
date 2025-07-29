# Sentiment-Based Product Recommendation System

An end-to-end recommendation engine designed for an e-commerce platform (Ebuss) that intelligently combines collaborative filtering with sentiment analysis to deliver personalized product recommendations. This system aims to enhance user experience by suggesting products based on historical user preferences and the sentiment extracted from product reviews.

This project was developed as part of a machine learning engineering task focused on improving product recommendation accuracy and relevance for e-commerce users.

---

## ✨ Features

* **User-Based Collaborative Filtering:** Generates initial top-N product recommendations by identifying users with similar preferences.
* **Sentiment Analysis for Re-ranking:** Utilizes an **XGBoost** classifier trained on **TF-IDF** features to analyze product review sentiments, re-ranking the initial recommendations to prioritize products with more positive feedback.
* **Flask Web Application:** Provides a clean, responsive, and intuitive user interface built with Bootstrap for easy interaction.
* **Heroku Deployment:** The application is publicly accessible, allowing for easy demonstration and usage.
* **Comprehensive Logging:** Implements logging mechanisms for tracking application usage, performance monitoring, and debugging purposes.

---

## 🚀 Project Workflow

The development of this recommendation system followed a structured machine learning engineering workflow:

1.  **Data Preprocessing:**
    * Cleaned and preprocessed raw product review data.
    * Generated sentiment labels from product ratings to serve as the ground truth for sentiment model training.

2.  **Sentiment Model Development:**
    * Extracted features using **TF-IDF Vectorizer** from preprocessed reviews.
    * Trained and evaluated multiple machine learning models including Logistic Regression, Random Forest, and XGBoost.
    * **XGBoost** was selected as the final sentiment classifier due to its superior performance.

3.  **Recommendation Engine Implementation:**
    * Developed the core recommendation logic using **user-based collaborative filtering**.
    * Integrated the trained sentiment model to re-rank the initial recommendations, promoting products with higher positive sentiment scores.

4.  **Deployment:**
    * Created a **Flask** web interface to allow users to interact with the recommendation system.
    * Successfully deployed the application on **Heroku** for public access and scalability.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Machine Learning Models:** XGBoost, Scikit-learn
* **Feature Extraction:** TF-IDF Vectorizer
* **Frontend:** HTML, Bootstrap 5
* **Deployment:** Heroku (Gunicorn)
* **Data Storage:** Pickle files (hosted externally for lightweight deployment)

---

## 📂 Project Structure

```bash
Sentiment_Based_Product_Recommendation_System/
│
├── app.py                  # Main Flask application
├── model.py                # Core logic for recommendations & sentiment re-ranking
├── requirements.txt        # Project dependencies
├── Procfile                # Heroku deployment configuration
├── .python-version         # Specifies Python version for Heroku
├── templates/
│   └── index.html          # Frontend UI for the web application
├── README.md               # Project documentation
└── (pickle_files & dataset hosted externally) # Note: Large data files are external

## ⚙️ Setup Instructions
Follow these steps to get the project up and running on your local machine.

1.  Clone Repository:
   git clone [https://github.com/your-username/sentiment-recommendation.git](https://github.com/your-username/sentiment-recommendation.git)
   cd sentiment-recommendation

2.  Create Virtual Environment
   It is highly recommended to use a virtual environment to manage dependencies.
   python -m venv venv
   venv\Scripts\activate

3.  Install Dependencies
   Once your virtual environment is active, install the required packages:
   pip install -r requirements.txt

4. Run Locally
   After installing dependencies, you can run the Flask application:
   python app.py

Open your web browser and visit: http://127.0.0.1:5000

## ☁️ Heroku Deployment
This project is set up for easy deployment to Heroku.

1.  Login & Create App
     Ensure you have the Heroku CLI installed and logged in.
     heroku login
     heroku create your-app-name # Replace 'your-app-name' with a unique name

2.  Push Code
     Commit your changes and push them to the Heroku remote:
     git add .
     git commit -m "Initial commit for Heroku deployment"
     git push heroku main

3.  Open App
     Once the deployment is complete, open your application in the browser:
     heroku open

##💡 Usage

* Navigate to the deployed web application (or run it locally).
* Enter an existing username in the provided input field.
* Click the "Get Recommendations" button.
* The system will display the top 5 product recommendations, re-ranked based on the positive sentiment extracted from their reviews.
