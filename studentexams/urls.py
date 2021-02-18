from django.urls import path
from studentexams import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'), # Index Page

# **********************************  Registration of Users  **********************************
    path('demoregister/', views.demoUserRegistration, name='register'),
    path('register/', views.userRegistration, name='register'),
    path('login/', views.userLogin, name='userLogin'),
    path('logout/', views.logoutUser, name="logout"),
    # path('dashboard/', views.dashboard, name='dashboard'),


# *********************  Landing Page Urls for different Users after Login  ********************
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('teacherDashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('studentDashboard/', views.studentDashboard, name='studentDashboard'),
    path('guestDashboard/', views.guestDashboard, name='guestDashboard'),
    path('demodashboard/', views.demodashboard, name='dashboard'),


# ************************************  Super Admin Dashboard  *********************************



# *************************************  Teacher Dashboard  ************************************



# *************************************  Student Dashboard  *************************************
    path('studentProfile/', views.studentProfile, name='studentDashboard'),
    path('studentResult/', views.studentResult, name='studentDashboard'),

    # urls for users
# *************************************  Users Profile  ************************************
    path('update/<str:pk>', views.updateRecord, name='update'),
    path('delete/<str:pk>', views.deleteRecord, name='delete'),
    # path('createpassword/', views.createPassword, name='createpassword'),


# **************************************  Question Paper  ************************************
    path('createImagePaper/', views.createImageQuestionPaper, name='createImageQuestionPaper'),
    path('showImagePaper/', views.showImageQuestionPaper, name='showImageQuestionPaper'),
    # path('createImagePaper2/', views.createImageQuestionPaper2, name='createImageQuestionPaper'),
    path('createPaper/', views.createQuestionPaper, name='createQuestionPaper'),
    path('createPaper2/', views.createQuestionPaper2, name='createQuestionPaper2'),
    path('showPaper/', views.showQuestionPaper, name='showQuestionPaper'),


# *************************************  Creating Content  *************************************
    path('createDemoContent/', views.createDemoContent, name='createDemoContent'),
    path('createMainContent/', views.createMainContent, name='createMainContent'),
    path('demoContent/', views.demoContent, name='demoContent'),
    path('mainContent/', views.mainContent, name='mainContent'),

# **************************************  Creating OTP  *************************************
    path('registerotp/', views.registerOTP, name='registerotp'),

]

# **************************************  Working with Media Files  **************************
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
