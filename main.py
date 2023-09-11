import os
import openai
import streamlit as st
from langchain.document_loaders import DirectoryLoader

# Streamlit settings
st.set_page_config(page_title='Langchain LLM Chatbot')

# Sidebar
st.sidebar.title('OpenAI API Key')
api_key = st.sidebar.text_input('Enter your OpenAI API key', value='', type='password')

# Check if API key is entered
if api_key:
    # Set the OpenAI API key
    openai.api_key = api_key

    # Load custom data using Langchain DirectoryLoader
    loader = DirectoryLoader("data/")
    docs = loader.load()

    # Chatbot settings
    model = 'gpt-3.5-turbo'
    messages = [{'role': 'system', 'content': 'You are chatting with an AI assistant.'}]

    # User input
    user_input = st.text_input('Enter your message')

    if user_input:
        messages.append({'role': 'user', 'content': user_input})

        # Generate response from the model
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=150,
        )

        # Display the model's message
        st.write(response['choices'][0]['message']['content'])
else:
    st.warning('Please enter your OpenAI API key in the sidebar.')
