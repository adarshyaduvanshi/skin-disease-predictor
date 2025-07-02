# skin-disease-predictor
AI-powered web app to predict 8+ skin diseases using ResNet50 (TensorFlow) with 50%+ accuracy. Built with Django and HTML/CSS for real-time image-based diagnosis. Fully browser-based, no JS, designed for easy use by non-technical medical staff.
# 🌿 Skin Disease Prediction Web App

An AI-powered web application that predicts skin diseases from uploaded images using a deep learning model built with TensorFlow and integrated into a Django web framework.

## 🚀 Features

- 🔍 **ResNet50-based CNN model** trained on a custom dataset to classify 8+ common skin diseases.
- 💡 **50%+ test accuracy** achieved using image augmentation, dropout, and early stopping.
- 🌐 **Full-stack web app** using Django for backend and HTML/CSS for frontend.
- ⚡ **Real-time prediction** on uploaded images without any client-side JavaScript.
- 🧑‍⚕️ **User-friendly interface** designed for non-technical healthcare workers.

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Django
- HTML5 & CSS3
- Deep Learning


## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/skin-disease-predictor.git
   cd skin-disease-predictor

**Create a virtual environment and install dependencies:**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
**Run database migrations:**
python manage.py migrate
python manage.py runserver
