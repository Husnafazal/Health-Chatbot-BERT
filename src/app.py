from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Welcome to the Q&A interface. Use the /ask endpoint to ask questions.'

# Define a route for the /ask endpoint
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data['question']
    # Process the question using your model here
    answer = "Placeholder answer"
    return jsonify({'answer': answer})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
