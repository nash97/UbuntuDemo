from django.db import models
from multiselectfield import MultiSelectField

# OTP Table
class otpModel(models.Model):
    mobile = models.CharField(max_length=50, blank=False, null=True)
    otp = models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return self.mobile

# Guest Users Model who are not having any Subscription
class guestUsersModel(models.Model):
    # course_id =
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    mobile = models.CharField(max_length=30, blank=False, null=True)

    createdDate = models.DateTimeField(auto_now_add=True)
    deletedDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option, null=True)

    def __str__(self):
        return self.name

# demo user registration model just for checking POST APIs
class demoUserRegistrationModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    mobile = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    package = models.CharField(max_length=30, blank=False, null=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option, null=True)

    def __str__(self):
        return self.name


class userRegistrationModel(models.Model):
    # course_id =
    firstname = models.CharField(max_length=100, blank=False, null=True)
    lastname = models.CharField(max_length=100, blank=False, null=True)
    username = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    password = models.CharField(max_length=200, blank=False, null=True)
    mobile = models.CharField(max_length=30, blank=False, null=True)

    createdDate = models.DateTimeField(auto_now_add=True)
    deletedDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=True)
    loginDateTime = models.DateTimeField(auto_now=True)
    logoutDateTime = models.DateTimeField(auto_now=True)

    categoryOption = ((1, 'Admin'), (2, 'Teacher'), (3, 'Student'), (4, 'Guest'), (5, 'Uploader'))
    userTypes = models.SmallIntegerField(choices=categoryOption, null=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option, null=True)

    def __str__(self):
        return self.firstname

class coursesModel(models.Model):

    options = (('JEE Mains', 'JEE Mains'),('JEE Advance', 'JEE Advance'), ('AIIMS', 'AIIMS'))
    courseName = models.CharField(max_length=100, choices=options, null=True)
    extraCourse = models.CharField(max_length=100, blank=False, null=True)
    # student_id = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    student_id = models.ManyToManyField('userRegistrationModel')

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.id

class subjectsModel(models.Model):

    options = (('Physics', 'Physics'),('Chemistry', 'Chemistry'), ('Maths', 'Maths'))
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subjectName = models.CharField(max_length=200, choices=options, null=True)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.id


class topicsModel(models.Model):
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topicName = models.CharField(max_length=200, null=True, blank=False)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.id


class subTopicsModel(models.Model):
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(topicsModel, max_length=20, null=True, on_delete=models.CASCADE)
    subTopicName = models.CharField(max_length=200, null=True, blank=False)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.id


class questionTypesModel(models.Model):
    options = (('Numerical', 'Numerical'), ('MCQ', 'MCQ'), ('Single MCQ', 'Single MCQ'),
            ('Multiple MCQ', 'Multiple MCQ'))
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(topicsModel, max_length=20, null=True, on_delete=models.CASCADE)
    subTopic_id = models.ForeignKey(subTopicsModel, max_length=20, null=True, on_delete=models.CASCADE)
    questionType = models.CharField(max_length=200, choices=options, null=True)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.id

# Uploading the questions in text format
class questionsModel(models.Model):
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(topicsModel, max_length=200, null=True, on_delete=models.CASCADE)
    subTopic_id = models.ForeignKey(subTopicsModel, max_length=20, null=True, on_delete=models.CASCADE)
    type_id = models.ForeignKey(questionTypesModel, max_length=20, null=True, on_delete=models.CASCADE)
    Question = models.CharField(max_length=1000, blank=False, null=True)

    c1 = models.CharField(max_length=200)
    c2 = models.CharField(max_length=200)
    c3 = models.CharField(max_length=200)
    c4 = models.CharField(max_length=200)

    choice = (('c1','c1'), ('c2','c2'), ('c3','c3'), ('c4','c4'))
    answer = MultiSelectField(choices=choice)

    marks = models.PositiveIntegerField(default=0)

    complexOptions = (('Easy', 'Easy'), ('Average', 'Average'), ('Tough', 'Tough'), ('Very Tough', 'Very Tough'))
    Complexity = models.CharField(max_length=50, choices=complexOptions, null=True)

    def __str__(self):
        return self.Question

# Uploading the questions in image format
class imageQuestionsModel(models.Model):
    topic_id = models.ForeignKey(topicsModel, max_length=200, null=True, on_delete=models.CASCADE)
    type_id = models.ForeignKey(questionTypesModel, max_length=200, null=True, on_delete=models.CASCADE)
    imageQuestion = models.ImageField(upload_to='media/')

    img1 = models.ImageField(upload_to='media/')
    img2 = models.ImageField(upload_to='media/')
    img3 = models.ImageField(upload_to='media/')
    img4 = models.ImageField(upload_to='media/')
    choice = (('img1','img1'),('img2','img2'),('img3','img3'),('img4','img4'))
    answer = MultiSelectField(choices=choice)

    marks = models.PositiveIntegerField(default=0)

    complexOptions = (('Easy', 'Easy'), ('Average', 'Average'), ('Tough', 'Tough'), ('Very Tough', 'Very Tough'))
    Complexity = models.CharField(max_length=50, choices=complexOptions, null=True)

    class Meta:
        db_table = "imageQuestionsModel"

    def __str__(self):
        return self.imageQuestion

class courseReferenceModel(models.Model):
    options = (('TimeBased', 'TimeBased'),('AttemptBased', 'AttemptBased'))
    courseType = models.CharField(max_length=100, choices=options, blank=False, null=True)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __str__(self):
        return self.courseType

class subscriptionModel(models.Model):
    userId = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    courseType = models.ForeignKey(courseReferenceModel, max_length=20, null=True, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    deletedDate = models.DateTimeField(auto_now=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.status

class subscriptionDetailsModel(models.Model):
    options = (('Silver', 'Silver'),('Gold', 'Gold'), ('Platinum', 'Platinum'))
    badges = models.CharField(max_length=100, choices=options, blank=False, null=True)
    userId = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    courseType = models.ForeignKey(courseReferenceModel, max_length=200, null=True, on_delete=models.CASCADE)
    subscriptionStartDate = models.DateField(auto_now_add=True)
    subscriptionEndDate = models.DateField(auto_now=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option)

    def __str__(self):
        return self.badges

class CoursePlanModel(models.Model):
    availableCourse = models.CharField(max_length=100, blank=False, null=True)
    attemptedCourse = models.CharField(max_length=100, blank=False, null=True)
    createdPlan = models.DateField(auto_now_add=True)
    updatedPlan = models.DateField(auto_now=True)

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option)

    def __str__(self):
        return self.availableCourse

# For storing the result of the student and finding accuracy
class studentResultModel(models.Model):
    student_id = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    # Subject = models.OneToManyField(subjectsModel, blank=True)
    marks = models.PositiveIntegerField(null=True)
    exam_date = models.DateTimeField()

    createdResult = models.DateField(auto_now_add=True)
    updatedResult = models.DateField(auto_now=True)

    status_option = ((1, 'Existed'), (0, 'Deleted'))
    status = models.SmallIntegerField(choices=status_option)

    def __int__(self):
        return self.marks


# Content Model for pdf and video for Demo Users
class guestUsersContentModel(models.Model):
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(topicsModel, max_length=200, null=True, on_delete=models.CASCADE)
    subTopic_id = models.ForeignKey(subTopicsModel, max_length=20, null=True, on_delete=models.CASCADE)

    createdDate = models.DateTimeField(auto_now_add=True)
    deletedDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='content/')

    # This max_digits must be greater than or equal to decimal_places.
    description = models.TextField(blank=True, null=True)


# Content Model for pdf and video for Registerd Users
class registeredUsersContentModel(models.Model):
    user_id = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    course_id = models.ForeignKey(coursesModel, max_length=20, null=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectsModel, max_length=20, null=True, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(topicsModel, max_length=200, null=True, on_delete=models.CASCADE)
    subTopic_id = models.ForeignKey(subTopicsModel, max_length=20, null=True, on_delete=models.CASCADE)

    createdDate = models.DateTimeField(auto_now_add=True)
    deletedDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='content/')

    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    description = models.TextField(blank=True, null=True)
