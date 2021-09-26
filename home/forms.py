from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombres')
    last_name = forms.CharField(max_length=70, required=True, label='Apellidos')
    email = forms.EmailField(max_length=254, label='email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # if email and not validate_structure_email(email):
        #     raise forms.ValidationError("La estructura del correo no es valida", code="email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con el mismo email", code="email")

        return email

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')