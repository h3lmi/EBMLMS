from django import forms

class AdminCreationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
