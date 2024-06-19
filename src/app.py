from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy model processing function
def get_answer(context, question):
    if question == "What are Surgical Site Infections (SSIs)?":
        return "Surgical Site Infections (SSIs) are infections that occur after surgery in the part of the body where the surgery took place."
    elif question == "What are the common causes of SSIs?":
        return "Common causes of SSIs include bacteria entering the wound during surgery, contaminated surgical instruments, and poor post-operative care."
    elif question == "How can SSIs be prevented?":
        return "SSIs can be prevented by maintaining proper hygiene, using sterile techniques, and monitoring symptoms."
    elif question == "What are the symptoms of SSIs?":
        return "Symptoms of SSIs include redness, swelling, pain at the surgical site, and sometimes fever."
    elif question == "How are SSIs treated?":
        return "SSIs are treated with antibiotics, drainage of the infected area, and proper wound care."
    else:
        return "Question not recognized."

@app.route('/answer', methods=['POST'])
def get_answer_route():
    data = request.get_json()
    context = data.get('context')
    question = data.get('question')
    
    answer = get_answer(context, question)
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
