from webbrowser import get
from django.contrib.auth import  get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailAuth(ModelBackend):
    @classmethod
    def authenticate(self,email=None,password=None,**kwargs):
        if email==None or password == None:
            return None 
        User = get_user_model()

        try :
            user = User.objects.get(email=email)
        except User.DoesNotExist:
           return None
        if user.check_password(password):
            return user
        return None
