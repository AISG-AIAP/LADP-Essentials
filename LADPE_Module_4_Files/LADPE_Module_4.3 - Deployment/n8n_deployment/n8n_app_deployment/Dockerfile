# 1. Start from a small official Python image
FROM python:3.12-slim

# 2. Work inside /app in the container
WORKDIR /app

# 3. Install the Python libraries first (cached between builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of our code (app.py + static/)
COPY . .

# 5. Cloud Run sends traffic to $PORT (8080 by default)
ENV PORT=8080
EXPOSE 8080

# 6. Start the app with gunicorn (a production-grade web server)
#    (JSON format; "sh -c" lets us read the $PORT variable)
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 120 app:app"]
