from django import forms

class CreateNewTask(forms.Form):
    title= forms.CharField(label="Task Title", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description=forms.CharField(label="Task Description", widget=forms.Textarea(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name= forms.CharField(label="Project Title", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
