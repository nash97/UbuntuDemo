from django.shortcuts import render, redirect
from studentexams.models import *
from datetime import datetime, date
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studentexams.serializers import demoUserRegistrationModelSerializer
import requests
# from studentexams.models import demoUserRegistrationModel


def homepage(request):
    return render(request, 'studentexams/homePage.html')


# Demo User Registration for Student
def demoUserRegistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        package = request.POST['package']

        subject = "Presidency Online Examination - Change Password"
        message = "Hi %s! Please create your new Password here : http://127.0.0.1:8000/changepassword"  % name

        send_mail(
            subject,  # Subject of the email
            message,  # Body or Message of the email
            'karishma.sony.ks@gmail.com',  # from@gmail.com
            [email],  # to@gmail.com
        )

        user = demoUserRegistrationModel.objects.create(name=name, mobile=mobile, email=email,
        package=package, status=1)

        if user:
            return redirect('/login')
        else:
            return render(request, 'studentexams/demoRegister.html')
    else:
        return render(request, 'studentexams/demoRegister.html')



def userRegistration(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        subject = "Presidency Online Examination - Change Password"
        message = "Hi %s! Please create your new Password here : http://127.0.0.1:8000/changepassword"  % firstname

        send_mail(
            subject,  # Subject of the email
            message,  # Body or Message of the email
            'akkirads54321@gmail.com',  # from@gmail.com
            [email],  # to@gmail.com
        )
        # Confirmation message
        # emailMessage = messages.success(request, f'Your account has been created ! Please check your email to create your new password')

        user = userRegistrationModel.objects.create(firstname=firstname, lastname=lastname, username=username,
        email=email, password=password, mobile=mobile, status=1)
        # print(user)
        if user:
            return redirect('/login')
        else:
            return render(request, 'studentexams/register.html')
    else:
        return render(request, 'studentexams/register.html')


# def next(request):
#     return render(request, 'studentexams/check.html')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = userRegistrationModel.objects.filter(email=email, password=password).first()
        if user:
            request.session['email'] = request.POST['email']
            # email = request.session['email']
            # request.session['email'] = user.email
            return redirect('/dashboard')
        else:
            messages.info(request, 'Email OR Password is Incorrect')
            return render(request, 'studentexams/login.html')
    else:
        context = {}
        return render(request, 'studentexams/login.html', context)


def dashboard(request):
    if request.session.has_key('email'):
        email = request.session['email']
        users = userRegistrationModel.objects.all()
        return render(request, 'studentexams/dashboard.html', {'users':users, 'email':request.session['email']})
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


# @login_required(login_url='login')
def updateRecord(request, pk):
    context ={}
    users = get_object_or_404(UserRegistration, id = pk)
    form = UpdateCustomerForm(request.POST or None, instance = users)

    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    context["user"] = form
    return render(request, 'userform/update.html', context)


def createQuestionPaper(request):

    if request.method == 'POST':

        Course = request.POST['Course']
        Subjects = request.POST['Subjects']
        Topics = request.POST['Topics']
        subTopics = request.POST['subTopics']

        createCourse = coursesModel.objects.create(courseName=Course, status=1)
        CourseId = coursesModel.objects.latest('id')
        print(CourseId)

        createSubjects = subjectsModel.objects.create(subjectName=Subjects, course_id_id=CourseId, status=1)
        subjectId = subjectsModel.objects.latest('id')
        print(subjectId)
        # createSections = Section.objects.create(sectionName=Sections, Courses_id_id=CourseId,
        # subject_id_id=subjectId, status=1)
        # sectionsId = Section.objects.latest('id')

        createTopics = topicsModel.objects.create(topicName=Topics, course_id_id=CourseId, subject_id_id=subjectId,
        status=1)
        topicsId = topicsModel.objects.latest('id')

        createSubTopics = subTopicsModel.objects.create(subTopicName=subTopics, course_id_id=CourseId,
        subject_id_id=subjectId, topic_id=topicsId, status=1)
        subTopicsId = subTopicsModel.objects.latest('id')

        return redirect('/createPaper2')
    else:
        return render(request, 'studentexams/createQuestionPaper.html')


def createQuestionPaper2(request):

    if request.method == 'POST':

        CourseId = coursesModel.objects.all().latest('id')
        print(CourseId)
        SubjectsId = subjectsModel.objects.all().latest('id')
        print(SubjectsId)
        topicsId = topicsModel.objects.all().latest('id')
        print(topicsId)
        subTopicsId = subTopicsModel.objects.latest('id')
        print(subTopicsId)
        QuestionTypes = request.POST['QuestionTypes']
        question = request.POST['question']
        Complexity = request.POST['Complexity']
        # mcq1 = request.POST['mcq1']
        # mcq2 = request.POST['mcq2']
        # mcq3 = request.POST['mcq3']
        # mcq4 = request.POST['mcq4']
        #
        # mcqs = mcq1 | mcq2 | mcq3 | mcq4
        createQuestionTypes = questionTypesModel.objects.create(questionType=QuestionTypes,
        course_id=CourseId,subject_id=SubjectsId,topic_id=topicsId, subTopic_id=subTopicsId, status=1)
        queTypeId = questionTypesModel.objects.latest('id')

        print(queTypeId)

        createQuestions = questionsModel.objects.create(Question=question,course_id=CourseId,
        Complexity=Complexity,subject_id=SubjectsId,topic_id=topicsId, subTopic_id=subTopicsId,
        type_id_id=queTypeId  )
        questionsId = questionsModel.objects.latest('id')
        complexityId = questionsModel.objects.latest('id')

        return redirect('/createPaper')
    else:
        return render(request, 'studentexams/createQuestionPaper2.html')


def showQuestionPaper(request):

    # getCourse = coursesModel.objects.select_related('student_id')
    # print(getCourse)
    # getSubject = subjectsModel.objects.select_related('course_id')
    #
    # print(getSubject)
    #
    getcourse = questionsModel.objects.all()
    new =  {'sub':getcourse}
    print(getcourse)
    return render(request, 'studentexams/questionPaper.html', {'sub': getcourse })


    # getSubject = subjectsModel.objects.select_related('course_id')
    # subjects = {'subjects':getSubject}
    # print('///////////')
    # print(subjects)
    # return render(request, 'studentexams/questionPaper.html', subjects)

    # getSection = Section.objects.all()
    # sections = {'sections':getSection}
    # return render(request, 'studentexams/questionPaper.html', sections)

    # getTopic = topicsModel.objects.all()
    # topics = {'topics':getTopic}
    # return render(request, 'studentexams/questionPaper.html', topics)
    #
    # getSubTopic = subTopicsModel.objects.all()
    # subtopics = {'topics':getSubTopic}
    # return render(request, 'studentexams/questionPaper.html', subtopics)



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


def delete(request, pk):
    users = userRegistrationModel.objects.get(id=pk)
    users.delete()
    return redirect('/travellers')


def logout(request):
    del request.session['email']
    return redirect("/login")
