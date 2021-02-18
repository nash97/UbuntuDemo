from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from studentexams.models import *
from studentexams.forms import UpdateUserRegistrationForm
from datetime import datetime, date
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

# working with serializers and DRF
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from studentexams.serializers import demoUserRegistrationModelSerializer
# from studentexams.models import demoUserRegistrationModel
import requests
import json
# Working with OTP
import random
from itertools import islice


def homepage(request):
    return render(request, 'studentexams/homePage.html')

# Inserting OTPs in Database
def registerOTP(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        otps = []
        for i in range(1000):
            otp = random.randint(100000, 999999)
            otp_obj = otpModel(mobile=mobile, otp=otp)
            otps.append(otp_obj)

        batch_size = 50
        while True:
            batch = list(islice(otps, batch_size))
            print(batch)
            if not batch:
                break
            otpModel.objects.bulk_create(batch, batch_size)
            del otps[0:batch_size]
        if otp:
            messages.info(request, 'OTP is saved!!!')
            content = {}
            return render(request, 'studentexams/otp.html', content)

    else:
        return render(request, 'studentexams/otp.html')


# Demo User Registration for Student
@api_view(['GET','POST'])
def demoUserRegistration(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # mobile = request.POST['mobile']
        # email = request.POST['email']
        # package = request.POST['package']

        jsondata = ' { "name": "Nashit", "mobile": 8965985689, "email": "nashit@gmail.com", "package": "JEE Advanced"} '
        decodejson = json.loads(jsondata)
        name = decodejson['name']
        mobile = decodejson['mobile']
        email = decodejson['email']
        package = decodejson['package']

        # print(decodejson)

        user = demoUserRegistrationModel.objects.create(name=name, mobile=mobile, email=email, package=package, status=1)
        # print(user)

        if user:
            return redirect('/login')
        else:
            return render(request, 'studentexams/demoRegister.html')
    else:
        return render(request, 'studentexams/demoRegister.html')


# API for fetching record from the database in JSON format
@api_view(['GET','POST'])
def demodashboard(request):
    users = demoUserRegistrationModel.objects.all()
    print(users)

    userSerializer =  demoUserRegistrationModelSerializer(users, many=True)

    resultModel = userSerializer.data
    return Response(resultModel)


@api_view(['GET','POST'])
def resultApi(request):
    resultapi = requests.get('http://127.0.0.1:8000/demodashboard/')
    jsonobj = resultapi.json()
    return render(request, 'studentexams/index.html', {"usermodel": jsonobj})


def userRegistration(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        # subject = "Presidency Online Examination - Change Password"
        # message = "Hi %s! Please create your new Password here : http://127.0.0.1:8000/changepassword"  % firstname
        #
        # send_mail(
        #     subject,  # Subject of the email
        #     message,  # Body or Message of the email
        #     'akkirads54321@gmail.com',  # from@gmail.com
        #     [email],  # to@gmail.com
        # )
        # Confirmation message
        # emailMessage = messages.success(request, f'Your account has been created ! Please check your email to create your new password')

        if userRegistrationModel.objects.filter(firstname=firstname, username=username, email=email, mobile=mobile).exists():
            messages.info(request, 'Duplication is not allowed!!!')
            return render(request, 'studentexams/register.html')
        else:
            user = userRegistrationModel.objects.create(firstname=firstname, lastname=lastname, username=username,
            email=email, password=password, mobile=mobile, status=1)
            # print(user)
            if user:
                return redirect('/login')
            else:
                return render(request, 'studentexams/register.html')
    else:
        context = {}
        return render(request, 'studentexams/register.html', context)


# def next(request):
#     return render(request, 'studentexams/check.html')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = userRegistrationModel.objects.filter(email=email, password=password).latest('id')
        print(user.userTypes)
        if user:
            request.session['firstname'] = user.firstname
            request.session['email'] = request.POST['email']
            # Access permissions for different Users
            if user.userTypes == 1:
                print(user.userTypes)
                return redirect('/adminDashboard')
            elif user.userTypes == 2:
                return redirect('/teacherDashboard')
            elif user.userTypes == 3:
                return redirect('/studentDashboard')
            else:
                return redirect('/guestDashboard')
            # End Access permissions for different Users
        else:
            messages.info(request, 'Email OR Password is Incorrect')
            return render(request, 'studentexams/login.html')
    else:
        context = {}
        return render(request, 'studentexams/login.html', context)


# Different Dashboard for different Users
@login_required(login_url='/login')
def adminDashboard(request):
    if request.session.has_key('firstname'):
        firstname = request.session['firstname']
        users = userRegistrationModel.objects.filter(firstname=firstname)
        return render(request, 'studentexams/superAdminDashboard.html', {'users':users, 'firstname':request.session['firstname']})
    else:
        return redirect('/login')


@login_required(login_url='login')
def teacherDashboard(request):
    if request.session.has_key('firstname'):
        firstname = request.session['firstname']
        users = userRegistrationModel.objects.filter(firstname=firstname)
        return render(request, 'studentexams/teacherDashboard.html', {'users':users, 'firstname':request.session['firstname']})
    else:
        return redirect('/login')


@login_required(login_url='login')
def studentDashboard(request):
    if request.session.has_key('firstname'):
        firstname = request.session['firstname']
        users = userRegistrationModel.objects.filter(firstname=firstname)
        course = coursesModel.objects.filter(id=20)
        return render(request, 'studentexams/studentDashboard.html', {'users':users, 'course':course, 'firstname':request.session['firstname']})
    else:
        return redirect('/login')


@login_required(login_url='login')
def studentProfile(request):
    if request.session.has_key('firstname'):
        return render(request, 'studentexams/studentProfile.html')
    else:
        return redirect('/login')


@login_required(login_url='login')
def studentResult(request):
    if request.session.has_key('firstname'):
        return render(request, 'studentexams/studentResult.html')
    else:
        return redirect('/login')


@login_required(login_url='login')
def guestDashboard(request):
    if request.session.has_key('firstname'):
        firstname = request.session['firstname']
        users = userRegistrationModel.objects.filter(firstname=firstname)
        return render(request, 'studentexams/guestDashboard.html')
    else:
        return redirect('/login')

# Main Dashboard
@login_required(login_url='login')
def dashboard(request):
    if request.session.has_key('firstname'):
        firstname = request.session['firstname']
        users = userRegistrationModel.objects.filter(firstname=firstname)
        course = coursesModel.objects.filter(id=20)
        return render(request, 'studentexams/studentDashboard.html', {'users':users, 'course':course, 'firstname':request.session['firstname']})
    else:
        return redirect('/login')

        # currentDate = datetime.now().replace(microsecond=0)
        # newDate = currentDate.strftime("%Y-%m-%d %H:%M:%S") #str
        # currentDate = date.today()
        # users = subscriptionDetailsModel.objects.all()
        # # print(users.subEndDate)
        # if users:
        #     return render(request, 'studentexams/dashboard.html')
        #     # subscriptionStartDate = users.subscriptionStartDate
        #     # if subscriptionEndDate <= subscriptionStartDate:
        #     #     messages.info(request, "Your subscription has been expired...!")
        #     #     # return HttpResponse(messages.add_message(request, messages.INFO, 'Your subscription has been expired...!'))
        #     # else:
        #     #     messages.info(request, "You can access this course!!!")
        #         # return HttpResponse(messages.add_message(request, messages.INFO, 'You can access this course!!!'))
        # else:
        #     return render(request, 'studentexams/dashboard.html')


@login_required(login_url='login')
def updateRecord(request, pk):
    context ={}
    users = get_object_or_404(userRegistrationModel, id = pk)
    form = UpdateUserRegistrationForm(request.POST or None, instance = users)

    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    context["user"] = form
    return render(request, 'studentexams/userUpdate.html', context)


def createImageQuestionPaper(request):

    if request.method == 'POST':
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        # answer = request.POST['answer']
        answer = request.POST.getlist('answer[]')

        createImageQuestion = imageQuestionsModel.objects.create(imageQuestion=question,
        img1=option1, img2=option2, img3=option3, img4=option4, answer=answer)
        print(dir('createImageQuestion'))

        return redirect('/showImagePaper')
    else:
        return render(request, 'studentexams/createImageQuestionPaper.html')


@login_required(login_url='login')
def showImageQuestionPaper(request):
    getImageQuestions = imageQuestionsModel.objects.all()
    # imgQuestions =  {'question':getImageQuestions}
    return render(request, 'studentexams/imageQuestionPaper.html', {'getImageQuestions': getImageQuestions})


def createQuestionPaper(request):

    if request.method == 'POST':

        Course = request.POST['Course']
        Subjects = request.POST['Subjects']
        Topics = request.POST['Topics']
        subTopics = request.POST['subTopics']
        QuestionTypes = request.POST['QuestionTypes']
        Complexity = request.POST['QuestionComplexity']
        questionMarks = request.POST['nmarks']
        question = request.POST['question']


        createCourse = coursesModel.objects.create(courseName=Course, status=1)
        CourseId = coursesModel.objects.latest('id')
        print(int(CourseId))

        createSubjects = subjectsModel.objects.create(subjectName=Subjects, course_id_id=CourseId, status=1)
        subjectId = subjectsModel.objects.latest('id')

        # createSections = Section.objects.create(sectionName=Sections, Courses_id_id=CourseId,
        # subject_id_id=subjectId, status=1)
        # sectionsId = Section.objects.latest('id')

        createTopics = topicsModel.objects.create(topicName=Topics, course_id_id=CourseId, subject_id_id=subjectId,
        status=1)
        topicsId = topicsModel.objects.latest('id')

        createSubTopics = subTopicsModel.objects.create(subTopicName=subTopics, course_id_id=CourseId,
        subject_id_id=subjectId, topic_id=topicsId, status=1)
        subTopicsId = subTopicsModel.objects.latest('id')


        createQuestionTypes = questionTypesModel.objects.create(questionType=QuestionTypes,
        course_id=CourseId,subject_id=subjectId,topic_id=topicsId, subTopic_id=subTopicsId, status=1)
        queTypeId = questionTypesModel.objects.latest('id')

        createQuestions = questionsModel.objects.create(Question=question,course_id=CourseId,
        Complexity=Complexity,subject_id=subjectId,topic_id=topicsId, subTopic_id=subTopicsId,
        type_id_id=queTypeId, marks=questionMarks)
        # questionsId = questionsModel.objects.latest('id')

        return redirect('/showPaper')
    else:
        return render(request, 'studentexams/createQuestionPaper.html')


def createQuestionPaper2(request):

    if request.method == 'POST':

        CourseId = coursesModel.objects.all().latest('id')  # Karishma Code
        SubjectsId = subjectsModel.objects.all().latest('id')  # Karishma Code
        topicsId = topicsModel.objects.all().latest('id')
        subTopicsId = subTopicsModel.objects.latest('id')

        QuestionTypes = request.POST['QuestionTypes']
        question = request.POST['question']
        Complexity = request.POST['Complexity']
        # mcq = request.POST['answer']

        # createQuestionTypes = questionTypesModel.objects.create(questionType=QuestionTypes, topic_id=topicsId,
        # Karishma
        createQuestionTypes = questionTypesModel.objects.create(questionType=QuestionTypes,
        course_id=CourseId,subject_id=SubjectsId,topic_id=topicsId, subTopic_id=subTopicsId, status=1)
        queTypeId = questionTypesModel.objects.latest('id')

        # createQuestions = questionsModel.objects.create(Question=question, topic_id_id=topicsId,
        # Karishma
        createQuestions = questionsModel.objects.create(Question=question,course_id=CourseId,
        Complexity=Complexity,subject_id=SubjectsId,topic_id=topicsId, subTopic_id=subTopicsId,
        type_id_id=queTypeId)
        questionsId = questionsModel.objects.latest('id')
        # Karishma Code
        complexityId = questionsModel.objects.latest('id')

        return redirect('/createPaper')
    else:
        return render(request, 'studentexams/createQuestionPaper2.html')

# Akhilesh(OLD)
# def showQuestionPaper(request):
#     getCourse = coursesModel.objects.all()
#     Courses = {'Courses':getCourse}
#     return render(request, 'studentexams/questionPaper.html', Courses)
#
#     getSubject = subjectsModel.objects.all()
#     subjects = {'subjects':getSubject}
#     return render(request, 'studentexams/questionPaper.html', subjects)
#
#     getSection = Section.objects.all()
#     sections = {'sections':getSection}
#     return render(request, 'studentexams/questionPaper.html', sections)
#
#     getTopic = topicsModel.objects.all()
#     topics = {'topics':getTopic}
#     return render(request, 'studentexams/questionPaper.html', topics)


# Karishma Code
@login_required(login_url='login')
def showQuestionPaper(request):

    # getCourse = coursesModel.objects.select_related('student_id')
    # getSubject = subjectsModel.objects.select_related('course_id')

    getQuestions = questionsModel.objects.all()
    question =  {'question':getQuestions}
    return render(request, 'studentexams/questionPaper.html', {'question': getQuestions })


def createDemoContent(request):
    if request.method == 'POST':

        CourseId = coursesModel.objects.all().latest('id')  # Karishma Code
        SubjectsId = subjectsModel.objects.all().latest('id')  # Karishma Code
        topicsId = topicsModel.objects.all().latest('id')
        subTopicsId = subTopicsModel.objects.latest('id')

        Course = request.POST['Course']
        Subjects = request.POST['Subjects']
        Topics = request.POST['Topics']
        subTopics = request.POST['subTopics']
        title = request.POST['title']
        pdf = request.POST['pdf']
        video = request.POST['video']

        createDemoContent = guestUsersContentModel.objects.create(course_id=CourseId,
        subject_id=SubjectsId, topic_id=topicsId, subTopic_id=subTopicsId, title=title,
        video=video, status=1)

        return redirect('/demoContent')
    else:
        return render(request, 'studentexams/createDemoContent.html')


def createMainContent(request):
    if request.method == 'POST':

        CourseId = coursesModel.objects.all().latest('id')  # Karishma Code
        SubjectsId = subjectsModel.objects.all().latest('id')  # Karishma Code
        topicsId = topicsModel.objects.all().latest('id')
        subTopicsId = subTopicsModel.objects.latest('id')

        QuestionTypes = request.POST['QuestionTypes']
        question = request.POST['question']
        Complexity = request.POST['Complexity']

        createDemoContent = questionTypesModel.objects.create(questionType=QuestionTypes,
        course_id=CourseId,subject_id=SubjectsId,topic_id=topicsId, subTopic_id=subTopicsId, status=1)

        return redirect('/mainContent')
    else:
        return render(request, 'studentexams/createMainContent.html')


def demoContent(request):
    return render(request, 'studentexams/demoContent.html')

def mainContent(request):
    return render(request, 'studentexams/mainContent.html')


@login_required(login_url='login')
def deleteRecord(request, pk):
    if request.session.has_key('email'):
        users = userRegistrationModel.objects.get(id=pk)
        users.delete()
        return redirect('/studentDashboard')
    else:
        return redirect('/login')


def logoutUser(request):
    del request.session['firstname']
    return redirect("/login")
