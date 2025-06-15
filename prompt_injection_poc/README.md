# Prompt Injection PoC

## Setup
1. `pip install -r requirements.txt`
2. `python app.py`
3. Test endpoints:
   - `curl -X POST -H 'Content-Type: application/json' -d '{"prompt": "Hello"}' http://localhost:5000/attack`
   - `curl -X POST -H 'Content-Type: application/json' -d '{"prompt": "Hello"}' http://localhost:5000/safe`

## Description
Demonstrates a prompt-injection attack and a simple sanitizer.
