# event_finder_app/forms.py
from django import forms

class EventSearchForm(forms.Form):
    location = forms.CharField(label='Location', max_length=100)
    interests = forms.ChoiceField(label='Interests', choices=[
        ('music', 'Music'),
        ('tech', 'Tech'),
        ('sports', 'Sports'),
    ])
