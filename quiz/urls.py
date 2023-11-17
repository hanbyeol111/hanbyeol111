from django.urls import path
from .views import randomQuiz

urlpatterns = [
    path("<int:id>/", randomQuiz),
]