from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Submit
from crispy_forms.bootstrap import FormActions


class LoginForm(forms.Form):
    '''Form for user login'''

    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
    )

    helper = FormHelper()
    helper.form_id = 'login-form'
    helper.layout = Layout(
        Row('username', css_class="mb-2"),
        Row('password', css_class="mb-2"),
        FormActions(
            Submit('login', 'Log in', css_class="mt-2"),
        )
    )


class SignupForm(forms.Form):
    '''Form for user signup'''

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Username',
                'autocomplete': 'username',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'autocomplete': 'password',
            }
        )
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'autocomplete': 'password'
            }
        )
    )

    userEmail = forms.EmailField(
        label="User Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'autocomplete': 'email'
            }
        ),
    )

    helper = FormHelper()
    helper.form_id = 'signup-form'
    helper.layout = Layout(
        Row('username', css_class='mb-2'),
        Row('password', css_class='mb-2'),
        Row('password_confirm', css_class='mb-2'),
        Row('userEmail', css_class='mb-2'),
        FormActions(
            Submit('signup', 'Sign up', css_class="btn-primary"),
            css_class='mt-3'
        )
    )
