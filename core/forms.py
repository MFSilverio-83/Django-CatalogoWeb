from django import forms
from django.forms.widgets import FileInput

class MultipleFileInput(FileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs['multiple'] = True

class MultiImageUploadForm(forms.Form):
    images = forms.FileField(
        widget=MultipleFileInput(),
        label="Selecionar Imagens"
    )