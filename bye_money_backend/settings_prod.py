import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'garciaprog$default',   # o nome do banco que você criou
        'USER': 'garciaprog',           # seu username no PythonAnywhere
        'PASSWORD': os.getenv('PASSWORD_MYSQL', ''),        # senha que você escolheu
        'HOST': 'garciaprog.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
