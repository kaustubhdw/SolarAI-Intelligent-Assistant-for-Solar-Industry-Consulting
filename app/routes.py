from flask import Blueprint, request, jsonify
from app.utils import get_ai_response

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Solar Industry AI Assistant API. Use the /ask endpoint to ask questions."})

@main.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    answer = get_ai_response(question)
    return jsonify({"answer": answer})
