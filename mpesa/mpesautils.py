from django.conf import settings
from .http import get
from requests.auth import HTTPBasicAuth
import json
def get_token(type):
    """
    fetch a new token
    :param: type: whether we are fetching token for B2C or C2B
    :return: JSON
    """
    url = f'{settings.MPESA_URL}/oauth/v1/generate?grant_type=client_credentials'
    if type.lower() == "c2b":
        response=get(url=url,
        auth=HTTPBasicAuth(settings.MPESA_C2B_ACCESS_KEY, settings.MPESA_C2B_CONSUMER_SECRET))

        mpesa_access_token = json.loads(response.text)

    return mpesa_access_token


