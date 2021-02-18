from rest_framework import serializers
from studentexams.models import demoUserRegistrationModel
# from django.contrib.auth.models import User


class demoUserRegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = demoUserRegistrationModel
        fields = "__all__"


# class activityPeriodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = activityPeriod
#         fields = "__all__"
