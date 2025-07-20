
Text Summarizer App
This project is a web application that summarizes text using AI. It's built with Python, Streamlit for the user interface, and Hugging Face Transformers for the summarization model.

 eatures
AI-Powered Summaries: Generates concise summaries from long texts.

User-Friendly Interface: Easy to paste text and get a summary.

Adjustable Length: Control summary length with simple sliders.

🚀 Get Started Locally
Clone the repository:

Bash

git clone https://github.com/Anushadhirde/text-summarization-app.git
cd text-summarization-app
Set up a virtual environment:

Bash

python -m venv hf_summarizer_env
# Windows: .\hf_summarizer_env\Scripts\activate
# macOS/Linux: source hf_summarizer_env/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
(The AI model will download the first time you run the app.)

Run the app:

Bash

streamlit run app.py
Your browser will open the app (usually at [http://localhost:8501](http://localhost:8501/)).

