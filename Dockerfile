# Use lightweight Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Heroku dynamically assigns this
ENV PORT=$PORT

# Expose Heroku port
EXPOSE $PORT

# Start with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]