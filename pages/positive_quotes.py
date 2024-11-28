# Import necessary libraries
from openai import OpenAI
import streamlit as st

# Initialize OpenAI Client
client = OpenAI(api_key='2051e9263e2e4f0e9afb23afe4a654fa', base_url='https://api.aimlapi.com/')

# Define the system prompt
system_prompt = (
    'You are a helpful assistant that provides positive, optimistic, uplifting, '
    'and motivational quotes filled with wisdom, encouragement, and hope to uplift and inspire people.'
)

def generate_positive_quote(feeling):
    # Create a personalized user prompt based on the user's input
    user_prompt = f'Give me a positive quote that can help someone who feels {feeling}.'
    
    # Create messages for the API request
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ]

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=100
    )

    # Extract and return the quote from the response
    return response.choices[0].message.content


 
   # Set up the Streamlit page
st.title('✨ Positive Quote Generator ✨')
    
st.markdown("Welcome to the Positive Quote Generator! Click the button below to receive an uplifting message.")
    # Input field for the user to describe how they feel
feeling = st.text_input('How do you feel today?', '')

    # Generate and display a quote when the button is clicked
if st.button('Get Positive Quote'):
        if feeling:
            quote = generate_positive_quote(feeling)
            st.success(quote)
        else:
            st.error('Please enter how you feel.')

