from django import forms

class SignInForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

class CreatePost(forms.Form):
	title = forms.CharField(required=True)
	content = forms.CharField(widget=forms.widgets.Textarea(),required=True)

class EditPost(forms.Form):
	title = forms.CharField(required=True)
	content = forms.CharField(widget=forms.widgets.Textarea(),required=True)
    