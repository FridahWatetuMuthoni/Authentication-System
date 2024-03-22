from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser

# accounts.serializers.py


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    date_of_birth = serializers.DateField(required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    address = serializers.CharField(required=False)
    gender = serializers.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        self.cleaned_data['age'] = self.validated_data.get('age', None)
        self.cleaned_data['date_of_birth'] = self.validated_data.get('date_of_birth', None)
        self.cleaned_data['phone_number'] = self.validated_data.get('phone_number', None)
        self.cleaned_data['address'] = self.validated_data.get('address', None)
        self.cleaned_data['gender'] = self.validated_data.get('gender', None)
        self.cleaned_data['first_name'] = self.validated_data.get('first_name', '')
        self.cleaned_data['last_name'] = self.validated_data.get('last_name', '')
        return self.cleaned_data

    def save(self, request):
        user = super(CustomRegisterSerializer, self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.validated_data.get('age', None)
        user.date_of_birth = self.validated_data.get('date_of_birth', None)
        user.phone_number= self.validated_data.get('phone_number', None)
        user.address = self.validated_data.get('address', None)
        user.gender = self.validated_data.get('gender', None)
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('email','username' 'password1','password2', 'first_name', 'last_name','age', 'date_of_birth', 'phone_number', 'address', 'gender')
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

