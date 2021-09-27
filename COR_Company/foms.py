from django import forms

from django.contrib.auth.models import User
from COR_Company.models import Company, CompanyUsers


class InviteUserForms(forms.Form):
    users = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super(InviteUserForms, self).__init__(*args, **kwargs)

        owner_users = Company.objects.all().values_list('owner__pk', flat=True)
        invited_users = CompanyUsers.objects.filter(status='S').values_list('id_user__pk', flat=True)
        qs_users = User.objects.filter(is_staff=0)

        users_tuple = (('', '-----'),)
        for user in qs_users:
            # Solo mostrar los usurios que no son propietarios ni han sido invitados
            if user.pk not in owner_users and user.pk not in invited_users:
                users_tuple = users_tuple + ((user.pk, user.get_full_name()),)

        self.fields['users'].choices = users_tuple

