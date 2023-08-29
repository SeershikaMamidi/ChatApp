from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [     
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/&lt;int:sender&gt;/&lt;int:receiver&gt;/', views.message_view, name='chat'),  
    path('api/messages/&lt;int:sender&gt;/&lt;int:receiver&gt;/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('register/', views.register_view, name='register')
]