# Language Translator Chatbot

This Python script builds a simple web application using Streamlit that functions as a language translator, powered by the Groq API. It creates a user interface with a title, a text area for input, and a field to specify the target language. When the "Translate" button is clicked, the code checks for a valid 'GROQ_API_KEY', then uses a langchain prompt template to instruct the 'llama-3.1-8b-instant' model (via ChatGroq) to translate the user's text into the desired language, finally displaying the translated text on the screen.

## How to run??

1. Create virtual environment

```bash
python -m venv venv
```

2. Activate venv

```bash
venv\Scripts\activate.bat
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run Streamlit app

```bash
streamlit run app.py
```