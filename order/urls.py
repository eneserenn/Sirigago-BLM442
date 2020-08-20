from django.urls import path

from order import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('reservations/<int:id>',views.Reserve,name='reservations'),
    
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
 
]