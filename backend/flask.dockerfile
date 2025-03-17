# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 


# Copy all backend files
COPY . ./

# Expose the Flask application port
EXPOSE 4000

# Set environment variables
ENV FLASK_APP=/app/app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=4000
ENV DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
ENV FLASK_DEBUG=1

# Run Flask application
CMD ["watchmedo", "auto-restart", "--pattern=*.py", "--recursive", "--", "flask", "run", "--host=0.0.0.0", "--port=4000"]
