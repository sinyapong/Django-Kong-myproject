from django.urls import path
from personal import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('form/', views.form, name="form"),
    path('edit/<personal_id>', views.edit, name="edit"),
    path('delete/<personal_id>',views.delete, name='delete'),
]