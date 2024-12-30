from datetime import datetime

from django.conf import settings
from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from account.models import CustomToken


class CustomTokenAuthentication(TokenAuthentication):
    model = CustomToken
    keyword = "Bearer"

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.filter().select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        utc_now = datetime.now()
        if token.created.replace(tzinfo=None) < utc_now - settings.TOKEN_EXPIRATION_TIME:
            raise exceptions.AuthenticationFailed('Token has expired')

        # if not token.user.is_active or token.user.deleted:
        #    raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return [token.user, token]
