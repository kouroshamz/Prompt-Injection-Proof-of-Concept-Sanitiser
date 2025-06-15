from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from sanitizer import sanitize
app = Flask(__name__)
# Load small GPT-2 model
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')
model.eval()
@app.route('/attack', methods=['POST'])
def attack():
    data = request.get_json()
    prompt = data.get('prompt', '')
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': text})
@app.route('/safe', methods=['POST'])
def safe():
    data = request.get_json()
    prompt = data.get('prompt', '')
    clean_prompt = sanitize(prompt)
    inputs = tokenizer.encode(clean_prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'sanitized_prompt': clean_prompt, 'response': text})
if __name__ == '__main__':
    app.run(debug=True)
