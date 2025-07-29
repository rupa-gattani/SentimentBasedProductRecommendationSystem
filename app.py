from flask import Flask, render_template, request
from model import get_product_recommendations


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    username = ""   # Initialize first
    recommendations = []
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        result = get_product_recommendations(username)
        if "error" in result:
            error_message = result["error"]
        else:
            recommendations = result["recommendations"]
    return render_template('index.html', recommendations=recommendations, error_message=error_message,username=username)

if __name__ == '__main__':
    app.run(debug=True)

    