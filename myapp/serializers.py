from rest_framework import serializers
from. models import Advisor, User, Userlogin, Advisorbook

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id','Advisor_Name', 'Advisor_Photo_URL')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Name', 'Email','Password')

class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlogin
        fields = ('Email','Password')


class AdvisorbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisorbook
        fields = "__all__"
        #fields = ('Booking_time')

