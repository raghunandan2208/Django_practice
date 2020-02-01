from django import forms
from jobsapp.models import IndiaJobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = IndiaJobs
        fields = '__all__'
