# Install dependencies (cached if requirements.txt hasn't changed)
FROM python:3.8 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
FROM python:3.8

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY . .

EXPOSE 80

CMD ["python", "run.py"]
