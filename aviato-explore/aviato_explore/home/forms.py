from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from home.models import Person
from home.models import Message

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'password', 'age', 'weight', 'height', 'health_problems')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('user', 'message', 'response')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send Message'))