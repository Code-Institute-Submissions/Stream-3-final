from models import User

class EmailAuth(object):
    def authenticate(self, email=None, password=None, allownopassword=False):
        try:
            user = User.objects.get(email=email)
            if allownopassword:
                return user
            else:
                if user.is_active == False:
                    return None
                else:
                    if user.check_password(password):
                        return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None