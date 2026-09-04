import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Title
st.title("Car, Cat and Dog Image Classifier")

st.write("Upload an image and the model will predict its class.")

# Load trained model
model = tf.keras.models.load_model("car_cat_dog_classifier.keras")

# Class names
class_names = ["Car", "Cat", "Dog"]

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Display uploaded image
    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize image to CIFAR-10 size
    image = image.resize((32, 32))

    # Convert image to NumPy array
    image_array = np.array(image)

    # Normalize pixel values
    image_array = image_array.astype("float32") / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    prediction = model.predict(image_array, verbose=0)

    # Get predicted class
    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    # Get confidence
    confidence = prediction[0][predicted_index] * 100

    # Display result
    st.success(f"Prediction: {predicted_class}")

    st.write(f"Confidence: {confidence:.2f}%")
