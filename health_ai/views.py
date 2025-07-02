
from django.shortcuts import render
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
MODEL_PATH = os.path.join(settings.BASE_DIR, 'health_ai', 'ml_models', 'best_skin_disease_model.h5')
skin_disease_model = None 

try:

    if os.path.exists(MODEL_PATH):
        skin_disease_model = load_model(MODEL_PATH)
        print("Skin disease model loaded successfully!")
    else:
        print(f"Error: Model file not found at {MODEL_PATH}")
        print("Please ensure 'best_skin_disease_model.h5' is in health_ai/ml_models/")
except Exception as e:
    print(f"An unexpected error occurred while loading the skin disease model: {e}")
    print("Please check your TensorFlow installation and model file integrity.")

IMG_WIDTH, IMG_HEIGHT = 224, 224 
CLASS_LABELS = [
    'BA- cellulitis',
    'BA-impetigo',
    'FU-athlete-foot',
    'FU-nail-fungus',
    'FU-ringworm',
    'PA-cutaneous-larva-migrans',
    'VI-chickenpox',
    'VI-shingles'
]
NUM_CLASSES = len(CLASS_LABELS)


class SkinPredictionView(APIView):
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        
        if skin_disease_model is None:
            return Response({
                'error': 'AI model is not available. Server configuration error.',
                'details': 'Model file might be missing or failed to load. Check server console for errors during startup.'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

      
        if 'image' not in request.FILES:
            return Response({'error': 'No image file was provided in the request. Please upload an image with the key "image".'},
                            status=status.HTTP_400_BAD_REQUEST)

        image_file = request.FILES['image']

        try:
            img = Image.open(image_file).convert('RGB')
           
            img = img.resize((IMG_WIDTH, IMG_HEIGHT))

            img_array = image.img_to_array(img)
            
            img_array = np.expand_dims(img_array, axis=0)
           
            img_array /= 255.0

            predictions = skin_disease_model.predict(img_array)
            
            predicted_class_index = np.argmax(predictions[0])
            
            confidence = float(np.max(predictions[0]) * 100) 

            
            predicted_label = CLASS_LABELS[predicted_class_index]

           
            response_data = {
                'prediction': predicted_label,
                'confidence': f"{confidence:.2f}%",
          
                'disclaimer': 'This is an AI-generated preliminary assessment and not a definitive medical diagnosis. Always consult a qualified healthcare professional for accurate diagnosis and treatment.',
                
                'all_confidences': {CLASS_LABELS[i]: f"{float(predictions[0][i]*100):.2f}%" for i in range(NUM_CLASSES)}
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
           
            print(f"Error during image processing or prediction: {str(e)}")
            return Response({
                'error': f'An internal server error occurred while processing your image.',
                'details': str(e) 
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def upload_form_view(request):
    """
    Renders the HTML form for uploading skin images.
    """
    return render(request, 'upload_form.html')