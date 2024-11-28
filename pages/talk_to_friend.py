import streamlit as st
from openai import OpenAI

# OpenAI Client
client = OpenAI(api_key='up_CpZjdAyzHNZSbSTAQWVqYuJGgQNJW', base_url='https://api.upstage.ai/v1/solar')

# Streamlit page configuration
st.set_page_config(page_title='Chat with me 😊', layout='wide')
st.title("Chat with me 😊")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'system', 'content': 'You are a helpful friend that someone can depend on and want to chat with, you provides positive, optimistic, uplifting, and motivational suggestions and advices filled with wisdom, encouragement and hope to uplift and inspire people.'}
    ]

def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="solar-pro",
        messages=st.session_state.messages + [{'role': 'user', 'content': prompt}],
        temperature=0.7,
        max_tokens=200
    )
    
    return response.choices[0].message.content

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message['role']):
        st.write(message['content'])

# Chat input
user_input = st.chat_input("I am waiting to hear from you 😊")

if user_input:
    if user_input.lower() in ['quit', 'exit', 'escape', 'out', 'ex']:
        st.session_state.messages = [st.session_state.messages[0]]  # Keep only the system message
        st.success("Thanks for chatting with me!")
    else:
        # Add user message to chat history
        st.session_state.messages.append({'role': 'user', 'content': user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        
        # Generate bot response
        response = generate_response(user_input)
        
        # Add bot response to chat history
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        
        # Display bot response
        with st.chat_message("assistant"):
            st.write(response)

# No rerun needed