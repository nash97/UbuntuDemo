from django.urls import path
from studentexams import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # urls for registering and log users
    path('demoregister/', views.demoUserRegistration, name='register'),
    path('register/', views.userRegistration, name='register'),
    path('login/', views.userLogin, name='userLogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('logout/', views.logoutUser, name="logout"),
    # urls for users
    # path('update/<str:pk>', views.updateRecord, name='update'),
    # path('delete/<str:pk>', views.deleteRecord, name='delete'),

    # path('createpassword/', views.createPassword, name='createpassword'),

    # path('next/', views.next, name='next'),
    
    path('demodashboard/', views.demodashboard, name='dashboard'),
    path('createPaper/', views.createQuestionPaper, name='createQuestionPaper'),
    path('createPaper2/', views.createQuestionPaper2, name='createQuestionPaper2'),
    path('showPaper/', views.showQuestionPaper, name='showQuestionPaper'),

]
