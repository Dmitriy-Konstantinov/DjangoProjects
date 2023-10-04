from django import forms
from users.models import User


class UserFilterForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='All users')
