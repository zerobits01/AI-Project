from django.urls import path, re_path

from ai_solutions import views, consumer


urlpatterns = [
    
    path('hello/', views.SayHello.as_view()),
    path('solve/<str:method>', views.Solver.as_view()),
    
]