# 🖼️ Car, Cat & Dog Image Classification using CNN
## Live Demo: https://shadowfoximageclassification-dmu632gab5wbu6c8pnavxx.streamlit.app/
## 📌 Project Overview

This project is an image classification application developed as part of the **ShadowFox Internship – Task 1: Image Classification**.

The application uses a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras** to classify images into three categories:

- 🚗 Car
- 🐱 Cat
- 🐶 Dog

A **Streamlit web application** is integrated with the trained model, allowing users to upload an image and receive a predicted class along with the model's confidence score.

---

## 🎯 Objective

The main objective of this project is to develop a practical image classification system that can:

1. Process image data.
2. Train a CNN-based deep learning model.
3. Classify images into multiple categories.
4. Display predictions through a simple web interface.
5. Provide prediction confidence to the user.
6. Deploy the application for online access.

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| TensorFlow / Keras | Deep learning and CNN model |
| NumPy | Numerical and image array processing |
| Pillow (PIL) | Image processing |
| Streamlit | Web application interface |
| Google Colab | Model training |
| GitHub | Source code and project version control |
| Streamlit Community Cloud | Application deployment |

---

## 📊 Dataset

The model was trained using the **CIFAR-10 dataset**.

CIFAR-10 contains small RGB images with a resolution of **32 × 32 pixels**.

For this project, three classes were selected:

- Automobile → **Car**
- Cat → **Cat**
- Dog → **Dog**

The selected dataset was filtered to create a focused three-class classification problem.

### Dataset Details

- Image type: RGB
- Image size: 32 × 32 pixels
- Number of classes: 3
- Classes: Car, Cat, Dog
- Training images used: 15,000
- Testing images used: 3,000

---

## 🏗️ Model Architecture

A **Convolutional Neural Network (CNN)** was used for image classification.

The general workflow is:

```text
Input Image
     ↓
Image Preprocessing
     ↓
Convolutional Layers
     ↓
Pooling Layers
     ↓
Feature Extraction
     ↓
Fully Connected Layers
     ↓
Softmax Classification
     ↓
Car / Cat / Dog
