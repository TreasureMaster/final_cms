from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .context_registry import ContextRegistry

# ------------------------------ Context Helpers ----------------------------- #

@ContextRegistry.register(url_name='login')
class LoginFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = layout.Layout(
            layout.Field('username', css_class='w-50'),
            layout.Field('password', css_class='w-50'),
        )
        # self.formset_error_title = 'Login errors'
        self.form_show_errors = False
        self.add_input(layout.Submit('submit', _('Submit')))


@ContextRegistry.register(url_name='password_reset')
class PasswordResetFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = layout.Layout(
            layout.Field('email', css_class='w-75'),
        )
        self.add_input(layout.Submit('reset', _('Reset')))


@ContextRegistry.register(url_name='password_reset_confirm')
class PasswordSetAfterResetFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = layout.Layout(
            layout.Field('new_password1', css_class='w-75'),
            layout.Field('new_password2', css_class='w-75'),
        )
        self.add_input(layout.Submit('change password', _('Change password')))


@ContextRegistry.register(url_name='password_change')
class PasswordChangeFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = layout.Layout(
            layout.Field('old_password', css_class='w-75'),
            layout.Field('new_password1', css_class='w-75'),
            layout.Field('new_password2', css_class='w-75'),
        )
        self.add_input(layout.Submit('change password', _('Change password')))


# ------------------------------- Form Helpers ------------------------------- #

class SignupFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        """Create Bootstrap form widgets"""
        super().__init__(*args, **kwargs)

        self.form_method = 'POST'
        # self.form_show_errors = False
        self.layout = layout.Layout(
            layout.Field('username', css_class='w-75'),
            layout.Field('email', css_class='w-75'),
            layout.Field('password1', css_class='w-75'),
            layout.Field('password2', css_class='w-75'),
            bootstrap.FormActions(layout.Submit('register', _('Register'))),
        )


class SenderFormHelper(FormHelper):
    """."""
    def __init__(self, *args, **kwargs):
        """Create Bootstrap form widgets"""
        super().__init__(*args, **kwargs)

        self.form_method = 'POST'
        # self.form_show_errors = False
        self.layout = layout.Layout(
            layout.Field('name', css_class='w-100'),
            layout.Field('email', css_class='w-100'),
            layout.Field('subject', css_class='w-100'),
            layout.Field('text', css_class='w-100'),
            bootstrap.FormActions(layout.Submit('register', _('Отправить'))),
        )
