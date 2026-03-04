# Step 1: Start with a Python environment
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4: Copy the rest of your code
COPY . .

# Step 5: Start the app
CMD ["python", "app.py"]