from django.urls import path
from . import views

urlpatterns = [
    path('', views.maketest, name = "maketest"),
    path('exam',views.exampage, name = "exampage"),
    path('studentpage', views.student, name="student"),
]