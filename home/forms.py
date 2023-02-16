from django import forms
from .models import Agent

class AgentForm(forms.ModelForm):
    name = forms.CharField(label="name", required=True)

    class Meta:
        model = Agent
        fields = ["name",] #改造できるものを記述
