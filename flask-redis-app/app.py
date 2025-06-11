# app.py
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        visits = cache.incr('hits')
    except redis.exceptions.ConnectionError:
        visits = "Redis not available"
    return f"Hello from Docker! You've visited {visits} times."
