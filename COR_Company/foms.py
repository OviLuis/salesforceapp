from django import forms

from django.contrib.auth.models import User
from COR_Company.models import Company


class InviteUserForms(forms.Form):
    users = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super(InviteUserForms, self).__init__(*args, **kwargs)

        owner_users = Company.objects.all().values_list('owner__pk', flat=True)
        qs_users = User.objects.all()

        users_tuple = (('', '-----'),)
        for user in qs_users:
            users_tuple = users_tuple + ((user.pk, user.get_full_name()),)

        self.fields['users'].choices = users_tuple

