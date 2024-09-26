from django import forms

class UserForm(forms.Form):
    # if django not provide a attribute that we can use that html attribute by using widget
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Enter FUll Name','style':'width:300px'}
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder':'Enter email'}
    ))

    user_dob = forms.DateField(label='Date of Birth',widget=forms.TextInput(
        attrs={'type':'date'}
    ))
