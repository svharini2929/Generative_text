from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

print("Loading GPT-2 Large model... (this may take a few minutes)")
generator = pipeline("text-generation", model="gpt2-large")
print("Model loaded!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data["prompt"]

    output = generator(
        prompt,
        max_new_tokens=200,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.6,
        top_k=40,
        top_p=0.85,
        repetition_penalty=1.8,
        no_repeat_ngram_size=3,
        truncation=True
    )
    result = output[0]["generated_text"]

    # Remove the original prompt from the output
    generated = result[len(prompt):].strip()

    # Clean up: remove incomplete sentences and dialogue/quotes
    generated = generated.replace('"', '').replace('"', '').replace('"', '')
    sentences = generated.split(".")
    clean_sentences = []
    for s in sentences:
        s = s.strip()
        if s and "--" not in s and "says" not in s and "said" not in s:
            clean_sentences.append(s)
    if clean_sentences:
        generated = ". ".join(clean_sentences) + "."

    return jsonify({"result": generated})

if __name__ == "__main__":
    app.run(debug=True)
