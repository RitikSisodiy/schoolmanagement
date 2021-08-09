from django import forms
from .models import classtimings,examtype,staffregister,User
from django.contrib.admin import widgets
from student.models import standard, Class,subject
from schoolmain.models import schoolifo

class classtimingsForm(forms.ModelForm):
    timefrom = forms.TimeField(widget=widgets.AdminTimeWidget)
    timeto = forms.TimeField(widget=widgets.AdminTimeWidget)
    user = forms.ModelChoiceField(queryset = staffregister.objects.all(),label="staff")
    class Meta:
        model = classtimings
        exclude = ('id',)
    def __init__(self, *args, **kwargs):
        super(classtimingsForm, self).__init__(*args, **kwargs)
        initial = kwargs.get("initial", {})
        ini = initial.get('Class')
        if ini is not None:
            self.fields['subject'].queryset = Class.objects.filter(standard=ini)
    def clean_subject(self):
        data = self.cleaned_data['subject']
        return data
class examtypeForm(forms.ModelForm):
    start_date = forms.DateField(widget=widgets.AdminDateWidget)
    end_date = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = examtype
        exclude = ('id',)
    
class standardForm(forms.ModelForm):
    class Meta:
        model = standard
        exclude = ('id',)
    def clean_standard(self):
        standards = self.cleaned_data['standard']
        from student.models import standard
        if standard.objects.filter(standard=standards).exists():
            raise forms.ValidationError("this standard is already exist")
        else:
            standard = standards
            return standard
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ('id',)
    def clean_standard(self):
        standard = self.cleaned_data['standard']
        subject = self.cleaned_data['subject']
        if Class.objects.filter(standard=standard,subject=subject).exists():
            raise forms.ValidationError("this subject is already exist")
        else:
            return standard
   
class subjectForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter if not in subject list'}))
    class Meta:
        model = subject
        exclude = ('id',)
    def clean_subject(self):
        subjects = self.cleaned_data['subject']
        from student.models import subject
        if subject.objects.filter(subject=subjects).exists():
            raise forms.ValidationError("this subject is already exist")
        else:
            subject = subjects
            return subject
class updatestudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
class schoolinfoForm(forms.ModelForm):
    class Meta:
        model = schoolifo
        exclude = ('id',)