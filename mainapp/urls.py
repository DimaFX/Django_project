from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.HelloView.as_view()),
    path('<int:number>/', views.funk),
    
]
