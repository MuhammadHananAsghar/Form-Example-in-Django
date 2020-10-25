from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    url = forms.URLField(initial='http://')
    day = forms.DateField()
    choice = forms.TypedChoiceField()
    datetime = forms.DateTimeField()
    dec = forms.DecimalField()
    file = forms.FileField()
    image = forms.ImageField()
    multiple = forms.MultipleChoiceField()
    time = forms.TimeField()
    cc_myself = forms.BooleanField(required=False)