

from django.urls import path
from .views import SkinPredictionView, upload_form_view 

urlpatterns = [
    path('predict-skin-condition/', SkinPredictionView.as_view(), name='predict_skin_condition'),
    path('upload/', upload_form_view, name='upload_form'),
    
]