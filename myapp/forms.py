from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm
from django.contrib.auth.models import User
from myapp.models import otp
from staff.models import staffregister
from student.models import studentregister
# from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class userRegister(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    def __init__(self, *args, **kwargs):
        super(userRegister, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'placeholder':  field.label})
                if type(field.widget) in (forms.PasswordInput,):
                    field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Ths Email addresses is already exist')
        return email
        
class StaffRegister(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StaffRegister, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput,forms.PasswordInput):
                    field.widget = forms.TextInput(attrs={'placeholder':  field.label})
                if type(field.widget) in (forms.PasswordInput,):
                    field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
    class Meta:
        model = staffregister
        exclude = ('user','status','phonestatus')
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = str(phone).replace('+91','')
        phone = str(phone).replace(' ','')
        if phone[0] == '0':
            phone = phone[1:]
        if len(phone)==10:
            return phone
        else:
            raise forms.ValidationError("enter the valid phone number")
class StudentRegister(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(StudentRegister, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput,forms.EmailInput,forms.PasswordInput):
                    field.widget = forms.TextInput(attrs={'placeholder':  field.label})
                if type(field.widget) in (forms.PasswordInput,):
                    field.widget = forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'})
    addmission_date = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = studentregister
        exclude = ('user','status','phonestatus')
        
class loginform(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter the email'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'}),max_length=30)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email=username).exists() is False:
            raise forms.ValidationError("this mail is not registered")
        else:
            return username
class otpform(forms.Form):
    otp = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Enter the OTP'}))
    