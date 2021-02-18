from django.contrib import admin
from studentexams.models import *

# Register your models here.
class otpModelAdmin(admin.ModelAdmin):
    list_display = ['mobile', 'otp']
admin.site.register(otpModel, otpModelAdmin)


class demoUserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'package', 'status']
admin.site.register(demoUserRegistrationModel, demoUserRegistrationModelAdmin)


class userRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'username', 'email', 'password', 'mobile', 'userTypes',
                    'createdDate', 'deletedDate', 'updatedDate', 'loginDateTime', 'logoutDateTime', 'status', ]
admin.site.register(userRegistrationModel, userRegistrationModelAdmin)


class guestUsersModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'createdDate', 'deletedDate', 'updatedDate', 'status', ]
admin.site.register(guestUsersModel, guestUsersModelAdmin)


class courseReferenceModelAdmin(admin.ModelAdmin):
    list_display = ['courseType', 'status']
admin.site.register(courseReferenceModel, courseReferenceModelAdmin)


class subscriptionModelAdmin(admin.ModelAdmin):
    list_display = ['userId', 'courseType', 'createdDate', 'deletedDate', 'status']
admin.site.register(subscriptionModel, subscriptionModelAdmin)


class subscriptionDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['badges', 'userId', 'courseType', 'subscriptionStartDate', 'subscriptionEndDate', 'status']
admin.site.register(subscriptionDetailsModel, subscriptionDetailsModelAdmin)


class CoursePlanModelAdmin(admin.ModelAdmin):
    list_display = ['availableCourse', 'attemptedCourse', 'createdPlan', 'updatedPlan', 'status']
admin.site.register(CoursePlanModel, CoursePlanModelAdmin)


class studentResultModelAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'subject_id', 'marks', 'exam_date', 'createdResult', 'updatedResult', 'status']
admin.site.register(studentResultModel, studentResultModelAdmin)


# Creating Exams Paper
class coursesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'courseName', 'extraCourse', 'status', ]
admin.site.register(coursesModel, coursesModelAdmin)


class subjectsModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subjectName', 'status']
admin.site.register(subjectsModel, subjectsModelAdmin)


class topicsModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject_id', 'topicName', 'status']
admin.site.register(topicsModel, topicsModelAdmin)


class subTopicsModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject_id', 'topic_id', 'subTopicName', 'status']
admin.site.register(subTopicsModel, subTopicsModelAdmin)


class questionTypesModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject_id', 'topic_id', 'subTopic_id', 'questionType', 'status']
admin.site.register(questionTypesModel, questionTypesModelAdmin)


class questionsModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject_id', 'topic_id','subTopic_id', 'type_id', 'Question', 'c1', 'c2', 'c3', 'c4', 'marks', 'answer', 'Complexity']
admin.site.register(questionsModel, questionsModelAdmin)


class imageQuestionsModelAdmin(admin.ModelAdmin):
    list_display = ['topic_id', 'type_id', 'imageQuestion', 'img1', 'img2', 'img3', 'img4', 'marks', 'answer', 'Complexity']
admin.site.register(imageQuestionsModel, imageQuestionsModelAdmin)


# Register Content Models for uploading Pdf and Videos
class guestUsersContentModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject_id', 'topic_id', 'subTopic_id', 'createdDate', 'deletedDate', 'updatedDate', 'title', 'file', 'description']
admin.site.register(guestUsersContentModel, guestUsersContentModelAdmin)

class registeredUsersContentModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'course_id', 'subject_id', 'topic_id', 'subTopic_id', 'createdDate', 'deletedDate', 'updatedDate', 'title', 'file', 'amount', 'description']
admin.site.register(registeredUsersContentModel, registeredUsersContentModelAdmin)


#
