from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

# demo user registration model

User = settings.AUTH_USER_MODEL

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

    status_option = ((1, 'Active'), (0, 'In-Active'))
    status = models.SmallIntegerField(choices=status_option, null=True)

    def __str__(self):
        return self.firstname

class coursesModel(models.Model):

    options = (('JEE Mains', 'JEE Mains'),('JEE Advance', 'JEE Advance'), ('AIIMS', 'AIIMS'))
    courseName = models.CharField(max_length=100, choices=options, null=True)
    extraCourse = models.CharField(max_length=100, blank=False, null=True)
    student_id = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)

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
    imageQuestion = models.ImageField(upload_to='questions/')

    img1 = models.ImageField(upload_to='questions/')
    img2 = models.ImageField(upload_to='questions/')
    img3 = models.ImageField(upload_to='questions/')
    img4 = models.ImageField(upload_to='questions/')
    choice = (('img1','img1'),('img2','img2'),('img3','img3'),('img4','img4'))
    answer = MultiSelectField(choices=choice)

    marks = models.PositiveIntegerField(default=0)

    complexOptions = (('Easy', 'Easy'), ('Average', 'Average'), ('Tough', 'Tough'), ('Very Tough', 'Very Tough'))
    Complexity = models.CharField(max_length=50, choices=complexOptions, null=True)

    class Meta:
        db_table = "imageQuestionsModel"

    def __int__(self):
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



class goldQuerySet(models.QuerySet):
    def smaller_than(self, size):
        return self.filter(amount__lt=size)

class goldPlanModel(models.Model):
    student_id = models.ForeignKey(userRegistrationModel, max_length=20, null=True, on_delete=models.CASCADE)
    gold_id = models.ForeignKey(subscriptionDetailsModel, max_length=20, null=True,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    objects = goldQuerySet.as_manager()
