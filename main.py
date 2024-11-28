import streamlit as st
import os

# Placeholder data - replace with your own content

def get_recommended_option(level):
    if 1 <= level <= 3:
        return "Positive Quotes"
    elif 4 <= level <= 6:
        return "Music Recommendations"
    elif 7 <= level <= 8:
        return "Physical Activity"
    else:  # 9 to 10
        return "Talk to a Friend"

def get_image_path(level):
    image_folder = "emotions.png"
    return os.path.join(image_folder)

def main():
    st.title("Mood Support App")

    # Mood level question
    mood_level = st.slider("On a scale of 1-10, how would you rate your mood today?", 1, 10)

    # Display image based on mood level
    image_path = get_image_path(mood_level)
    if os.path.exists(image_path):
        # Create three columns to center the image
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(image_path, caption=f"Mood Level: {mood_level}", use_column_width=True)
    else:
        st.error(f"Image not found: {image_path}")

    # Get recommended option
    recommended_option = get_recommended_option(mood_level)
    st.write(f"Based on your current mood level, we recommend trying the '{recommended_option}' option.")

    # Support options
    st.header("Support Options")
    col1, col2, col3, col4 = st.columns([2,3,2,2])

    with col1:
        if st.button("Positive Quotes"):
            st.switch_page("pages/positive_quotes.py")

    with col2:
        if st.button("Music Recommendations"):
            st.switch_page("pages/music_recommendations.py")

    with col3:
        if st.button("Physical Activity"):
            st.switch_page("pages/physical_activity.py")

    with col4:
        if st.button("Talk to a Friend"):
            st.switch_page("pages/talk_to_friend.py")
            # Here you would implement the logic to connect with a friend or support person

if __name__ == "__main__":
    main()
