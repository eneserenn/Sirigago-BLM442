from django.urls import path

from user import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('orders/', views.orders, name='orders'),
    path('mycomments/', views.mycomment, name='mycomment'),
    path('orderdelete/<int:id>', views.orderdelete, name='orderdelete'),
    path('commentdelete/<int:id>', views.commentdelete, name='commentdelete'),

    # path('addcomment/<int:id>',views.addcomment,name='addcomment')
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
 
]