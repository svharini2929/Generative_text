## Generative Text AI

A web-based text generation application powered by **GPT-2 Large (774M parameters)** from Hugging Face. Users provide a starting sentence, and the AI model generates a coherent, meaningful paragraph continuing from the input.

### Features
- Real-time text generation using GPT-2 Large model
- Clean, modern **teal-themed glassmorphism UI** with animated background glows
- Smart post-processing that removes repetitive text, incomplete sentences, and dialogue artifacts
- Loading state indicator during text generation
- Responsive design for all screen sizes

### Tech Stack
- **Backend:** Python, Flask
- **AI Model:** GPT-2 Large (Hugging Face Transformers)
- **Frontend:** HTML, CSS, JavaScript
- **Styling:** Glassmorphism design with Poppins font

### How It Works
1. User enters a starting sentence (e.g., "The human brain is the most complex organ")
2. The input is sent to the Flask backend via a REST API
3. GPT-2 Large model generates a continuation of the text (up to 200 tokens)
4. Post-processing cleans the output — removes repetition, quotes, and incomplete sentences
5. The generated paragraph is displayed in the UI

### Generation Parameters
- **Temperature (0.6):** Controls randomness — lower values produce more focused output
- **Top-K (40):** Limits vocabulary to top 40 most likely next words
- **Top-P (0.85):** Nucleus sampling for balanced diversity
- **Repetition Penalty (1.8):** Prevents the model from repeating words and phrases
- **No Repeat N-gram (3):** Blocks any 3-word phrase from appearing twice
