from django import forms


class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'checkbox-select'
