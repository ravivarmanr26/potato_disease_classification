import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Potato Disease Classification",
    layout="wide",
    page_icon="🥔"
)

# Load the potato disease classification model
potato_disease_model = tf.keras.models.load_model("1.keras")

CLASS_NAMES = ['Early Blight', 'Late Blight', 'Healthy']

# Add content to your Streamlit app
st.title('Potato Disease Classification')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Preprocess the image
    img = Image.open(uploaded_file)
    img = img.resize((256, 256))  # Resize the image to match model input size
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Make prediction
    predictions = potato_disease_model.predict(img_array)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    # Display prediction
    st.markdown(f"<div class='predicted-class'>Predicted Class: {predicted_class}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='confidence'>Confidence: {confidence:.2f}</div>", unsafe_allow_html=True)

    # Display the uploaded image with the specified CSS class
    st.image(img, caption='Uploaded Image', width=500)

