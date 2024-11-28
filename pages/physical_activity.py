import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="9a70a7b82dd84c8cb2e8c43a156be3c7",  # Replace with your actual API key
    base_url="https://api.aimlapi.com",  # Replace with the correct base URL if needed
)

# Streamlit page title
st.title("Mood-based Exercise Recommendations")

# User input: Ask the user how they feel
user_feeling = st.text_input("How are you feeling right now?", placeholder="e.g., tired, stressed, happy...")

# When the user submits their feeling, generate an exercise recommendation using the model
if user_feeling:
    with st.spinner("Generating exercise recommendation..."):
        # Send the user's feeling to the OpenAI model
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a fitness coach and a doctor . Based on the user's current mood, suggest a suitable exercise in one sentence. and write them in bullet"
                },
                {
                    "role": "user",
                    "content": f"I am feeling {user_feeling}. What exercise should I do?"
                },
            ],
        )
        
        # Get the model's response
        message = response.choices[0].message.content
        
        # Display the exercise recommendation
        st.write(f"Based on how you're feeling, here's an exercise suggestion for you: {message}")
