from .models import Bcrypt
from rest_framework.authentication import TokenAuthentication


class BcryptTokenAuthentication(TokenAuthentication):

    def get_model(self): 
        if self.model is not None:
            return self.model
        return Bcrypt
