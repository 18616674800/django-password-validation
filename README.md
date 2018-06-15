# django-password-validation


#step 1 copy the password_validation.py to your application


#step 2 change the AUTH_PASSWORD_VALIDATORS in setting.py


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'yourappnames.password_validation.IsEntireAlphaPasswordValidator',
    },
    {
        'NAME': 'yourappnames.password_validation.hasUpperCasePasswordValidator',
    },
    {
        'NAME': 'yourappnames.password_validation.haslowerCasePasswordValidator',
    },
    {
        'NAME': 'yourappnames.password_validation.hasNumberPasswordValidator',
    },
]
