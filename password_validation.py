import re
from django.core.exceptions import (
    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
)
from django.utils.translation import ugettext as _, ungettext


class IsEntireAlphaPasswordValidator(object):
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                _("This password is entirely alpha."),
                code='password_entirely_alpha',
            )

    def get_help_text(self):
        return _("Your password can't be entirely alpha.")


def hasUpperCaseAlpha(password):
    pattern = re.compile('[A-Z]+')
    match = pattern.findall(password)
    if len(match) > 0 :
        return True
    else:
        return False


class hasUpperCasePasswordValidator(object):
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):

        if not hasUpperCaseAlpha(password) :
            raise ValidationError(
                _("This password must have a upper-case alpha."),
                code='password_no_upper_case_alpha',
            )
    def get_help_text(self):
        return _("Your password must have at least a upper-case alpha.")

def haslowerCaseAlpha(password):
    pattern = re.compile('[a-z]+')
    match = pattern.findall(password)
    if len(match) > 0 :
        return True
    else:
        return False

class haslowerCasePasswordValidator(object):
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):

        if not haslowerCaseAlpha(password) :
            raise ValidationError(
                _("This password must have a lower-case alpha."),
                code='password_no_lower_case_alpha',
            )
    def get_help_text(self):
        return _("Your password must have at least a lower-case alpha.")


def hasNumberAlpha(password):
    pattern = re.compile('[0-9]+')
    match = pattern.findall(password)
    if len(match) > 0 :
        return True
    else:
        return False

class hasNumberPasswordValidator(object):
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):

        if not hasNumberAlpha(password) :
            raise ValidationError(
                _("This password must have at least a number."),
                code='password_no_number',
            )
    def get_help_text(self):
        return _("Your password must have at least a number.")
