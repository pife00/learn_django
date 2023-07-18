from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    # Otras rutas...
    path('new/',views.new, name="new"),
    path('<int:pk>/', views.details, name='details'),
]