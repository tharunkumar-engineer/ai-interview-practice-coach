from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-question", methods=["POST"])
def generate_question():
    role = request.json.get("role")
    return jsonify({
        "question": f"Explain OOPS concepts relevant to a {role} role."
    })

@app.route("/evaluate-answer", methods=["POST"])
def evaluate_answer():
    return jsonify({
        "result": """Score: 7/10
Feedback:
- Answer is clear but lacks examples
- Could explain with real-world use cases
Improved Answer:
OOPS concepts like encapsulation, inheritance, polymorphism, and abstraction help in writing reusable and maintainable code."""
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

