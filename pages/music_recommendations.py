import streamlit as st
from transformers import pipeline
import scipy.io.wavfile
from openai import OpenAI
import time
import numpy as np

# Initialize the OpenAI client
client = OpenAI(
    api_key="a99ae8e15f1e439a935b5e1cf2005c8b",
    base_url="https://api.aimlapi.com",
)

# Streamlit app layout
st.title("Mood-based Music Generator")

# Ask the user for their feeling and preferred music style via Streamlit inputs
user_feeling = st.text_input("How are you feeling right now?", value="feeling down")
music_style = st.text_input("What music style do you prefer?", value="pop")

# Button to trigger music generation
if st.button("Generate Music"):
    with st.spinner("Generating music, please wait..."):
        # Send the feeling and music style to the OpenAI model
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a musical assistant that, based on a user's feeling, can describe it as a musical instrument. Provide a short one-sentence response."
                },
                {
                    "role": "user",
                    "content": f"I am feeling {user_feeling}. Can you make me happy with a {music_style} style of music?"
                },
            ],
        )

        message = response.choices[0].message.content
        st.write(f"Assistant: {message}")

        # Load the synthesizer model for music generation
        synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

        # Simulate a short wait to represent loading time for music generation
        time.sleep(2)

        # Generate the music using the synthesizer model based on the message
        music = synthesiser(message, forward_params={"do_sample": True, "guidance_scale": 1})

        # Save the generated audio to a file
        audio_filename = "musicgen_out.wav"
        scipy.io.wavfile.write(audio_filename, rate=music["sampling_rate"], data=np.array(music["audio"]))

        st.success("Music has been generated!")

        # Play the generated audio in Streamlit
        st.audio(audio_filename)
