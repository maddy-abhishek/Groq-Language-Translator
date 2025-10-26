import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# --- Prompt Template ---
# We create a specific prompt for translation.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert language translator. You must translate the user's text into the target language provided. Do not add any extra commentary, greetings, or explanations. Just provide the translated text directly."),
        ("user", "Translate the following text to {target_language}:\n\n{text_to_translate}")
    ]
)

# --- Streamlit UI ---
st.title('Groq Language Translator ⚡')

input_text = st.text_area("Text to Translate", height=150)
target_language = st.text_input("Translate to (e.g., 'French', 'Spanish', 'Japanese')")

if st.button("Translate"):
    # Check if the API key is loaded
    if not os.getenv("GROQ_API_KEY"):
        st.error("GROQ_API_KEY not found. Please create a .env file and add it.")
    elif input_text and target_language:
        try:
            # --- LLM and Chain ---
            llm = ChatGroq(model_name="llama-3.1-8b-instant")
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser

            with st.spinner(f"Translating to {target_language}..."):
                # Invoke the chain with the user's input
                response = chain.invoke({
                    "text_to_translate": input_text,
                    "target_language": target_language
                })
                
                st.write("### Translation:")
                st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both text to translate and a target language.")

