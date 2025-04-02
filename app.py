from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
import os

app = Flask(__name__)

# Securely fetch API key from environment variable
groq_api_key = "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"
# Ensure it's set in your environment
if not groq_api_key: 
    raise ValueError("Groq API key is missing. Set it as an environment variable.")

# Initialize Groq model
groq_model = ChatGroq(api_key="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", model_name="mixtral-8x7b-32768")

@app.route('/', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')  # Handle missing 'message' key safely

        if not user_message:
            return jsonify({'error': 'Message is required'}), 400  # Return HTTP 400 for missing input

        # Get AI response from Groq
        response = groq_model.chat(messages=[{"role": "user", "content": user_message}])
        
        # Check response format (Debugging)
        print("Groq API Response:", response)

        ai_response = response.get('message', {}).get('content', 'Error: Invalid response format')

        return jsonify({'response': ai_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Handle errors gracefully

@app.route('/affirmation', methods=['GET'])
def affirmation():
    try:
        prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed."
        response = groq_model.chat(messages=[{"role": "user", "content": prompt}])

        affirmation = response.get('message', {}).get('content', 'Error: Invalid response format')

        return jsonify({'affirmation': affirmation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/meditation', methods=['GET'])
def meditation():
    try:
        prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
        response = groq_model.chat(messages=[{"role": "user", "content": prompt}])

        meditation_guide = response.get('message', {}).get('content', 'Error: Invalid response format')

        return jsonify({'meditation': meditation_guide})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
