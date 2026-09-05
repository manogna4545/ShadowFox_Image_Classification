# 🖼️ Car, Cat & Dog Image Classification using CNN
## Live Demo: https://shadowfoximageclassification-dmu632gab5wbu6c8pnavxx.streamlit.app/
# 🖼️ Car, Cat & Dog Image Classification using CNN

## 📌 Project Overview

This project is an image classification application developed as part of the **ShadowFox Internship – Task 1: Image Classification**.

The application uses a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras** to classify images into three categories:

* 🚗 Car
* 🐱 Cat
* 🐶 Dog

A **Streamlit web application** is integrated with the trained model, allowing users to upload an image and receive a predicted class along with the model's confidence score.

---

## 🌐 Live Demo

**Streamlit Application:**
https://shadowfoximageclassification-dmu632gab5wbu6c8pnavxx.streamlit.app/

The application is deployed using **Streamlit Community Cloud** and can be accessed through a web browser.

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

| Technology                | Purpose                              |
| ------------------------- | ------------------------------------ |
| Python                    | Programming Language                 |
| TensorFlow / Keras        | Deep Learning and CNN Model          |
| NumPy                     | Numerical and Image Array Processing |
| Pillow (PIL)              | Image Processing                     |
| Streamlit                 | Web Application Interface            |
| Google Colab              | Model Training                       |
| GitHub                    | Source Code and Version Control      |
| Streamlit Community Cloud | Application Deployment               |

---

## 📊 Dataset

The model was trained using the **CIFAR-10 dataset**.

CIFAR-10 contains small RGB images with a resolution of **32 × 32 pixels**.

For this project, three classes were selected:

* Automobile → **Car**
* Cat → **Cat**
* Dog → **Dog**

The selected dataset was filtered to create a focused three-class image classification problem.

### Dataset Details

* **Image Type:** RGB
* **Image Size:** 32 × 32 pixels
* **Number of Classes:** 3
* **Classes:** Car, Cat, Dog
* **Training Images Used:** 15,000
* **Testing Images Used:** 3,000

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
```

The model was trained for **10 epochs** using a **batch size of 64**.

---

## 🔄 Image Preprocessing

Before prediction, uploaded images are:

1. Converted to RGB format.
2. Resized to **32 × 32 pixels**.
3. Converted into a NumPy array.
4. Normalized by dividing pixel values by 255.
5. Passed to the trained CNN model.

This ensures that the input format used during prediction matches the preprocessing used during model training.

### Preprocessing Workflow

```text
Uploaded Image
      ↓
Convert to RGB
      ↓
Resize to 32 × 32
      ↓
Convert to NumPy Array
      ↓
Normalize Pixel Values
      ↓
CNN Model
      ↓
Prediction
```

---

## 📈 Model Performance

The trained CNN achieved approximately:

### **Test Accuracy: 80%**

This demonstrates that the model can learn visual patterns from the selected CIFAR-10 classes.

> **Note:** CIFAR-10 images are low-resolution 32 × 32 images. Performance on normal high-resolution real-world photographs may differ because the model was trained on CIFAR-10 images.

---

## 🌐 Streamlit Application

The project includes an interactive **Streamlit web application**.

Users can:

1. Open the web application.
2. Upload a JPG, JPEG, or PNG image.
3. View the uploaded image.
4. Get the predicted class.
5. View the prediction confidence.

### Application Flow

```text
User Uploads Image
        ↓
Image Converted to RGB
        ↓
Image Resized to 32 × 32
        ↓
Pixel Normalization
        ↓
CNN Model Prediction
        ↓
Predicted Class + Confidence
```

### Application Features

* 📤 Image upload
* 🖼️ Uploaded image preview
* 🤖 CNN-based classification
* 📊 Prediction confidence
* 🌐 Web-based interface
* ☁️ Cloud deployment

---

## 📂 Project Structure

```text
ShadowFox_Image_Classification/
│
├── app.py
├── car_cat_dog_classifier.keras
├── requirements.txt
└── README.md
```

### File Description

**app.py**
Contains the Streamlit application and prediction logic.

**car_cat_dog_classifier.keras**
Contains the trained TensorFlow/Keras CNN model.

**requirements.txt**
Contains the Python dependencies required to run the application.

**README.md**
Contains the documentation and information about the project.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manogna4545/ShadowFox_Image_Classification.git
```

### 2. Navigate to the Project Directory

```bash
cd ShadowFox_Image_Classification
```

### 3. Create a Python Virtual Environment

Python 3.12 is recommended for this project.

```bash
py -3.12 -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📋 Requirements

The project uses the following main dependencies:

```text
streamlit
tensorflow==2.20.0
numpy
pillow
```

Python **3.12** is recommended for compatibility with the TensorFlow environment used by this project.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Environment

* **Python:** 3.12
* **TensorFlow:** 2.20.0
* **Streamlit:** Latest compatible version
* **NumPy:** Latest compatible version
* **Pillow:** Latest compatible version

The application is connected to the GitHub repository, allowing updates to the project to be deployed from the repository.

### 🚀 Live Application

https://shadowfoximageclassification-dmu632gab5wbu6c8pnavxx.streamlit.app/

---

## 🔐 Model Input and Prediction

The application accepts:

* `.jpg`
* `.jpeg`
* `.png`

The uploaded image is converted to the required format and processed before being passed to the trained CNN model.

The model returns probabilities for the three classes:

```text
Car
Cat
Dog
```

The class with the highest probability is displayed as the final prediction.

---

## 🚀 Future Improvements

The project can be improved further by:

* Using higher-resolution real-world images.
* Increasing the size and diversity of the dataset.
* Applying data augmentation.
* Using transfer learning models such as MobileNetV2 or EfficientNet.
* Improving classification accuracy.
* Adding prediction probability charts.
* Supporting additional image categories.
* Improving the user interface.
* Adding model performance visualizations.
* Adding more robust real-world image testing.

---

## 🎓 Internship Task

**Program:** ShadowFox Internship
**Task:** Task 1 – Image Classification
**Domain:** Artificial Intelligence / Machine Learning
**Model:** Convolutional Neural Network
**Framework:** TensorFlow / Keras
**Dataset:** CIFAR-10
**Classes:** Car, Cat, Dog
**Interface:** Streamlit
**Deployment:** Streamlit Community Cloud

---

## 💡 Key Learning Outcomes

Through this project, the following concepts were explored:

* Image classification
* Convolutional Neural Networks
* Dataset preprocessing
* Image normalization
* Feature extraction
* Model training and evaluation
* TensorFlow/Keras
* Streamlit application development
* Model deployment
* GitHub version control
* Cloud-based application deployment

---

## 👩‍💻 Author

**Manogna Yara**

Artificial Intelligence & Machine Learning Student

---

## ⭐ Conclusion

This project demonstrates the complete workflow of a basic deep learning image classification system, from dataset preparation and CNN model training to image preprocessing, prediction, web application development, GitHub version control, and cloud deployment.

The project provides a practical foundation for understanding how deep learning models can be integrated into user-friendly applications.

---

## 🔗 Project Links

**GitHub Repository:**
https://github.com/manogna4545/ShadowFox_Image_Classification

**Live Streamlit Application:**
https://shadowfoximageclassification-dmu632gab5wbu6c8pnavxx.streamlit.app/

---

⭐ **If you find this project useful, feel free to explore the repository and try the live application.**
