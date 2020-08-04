import base64
from datetime import datetime

from django.conf import settings

from .models import AuthToken
from .http import post
from .mpesautils import get_token


def register_c2b_url():
    """
    Register the c2b_url
    :return:
    """
    url = f"{settings.MPESA_URL}/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" %
               AuthToken.objects.get_token("c2b")}
    body = {
        "ShortCode":settings.C2B_SHORT_CODE,
        "ResponseType":settings.C2B_RESPONSE_TYPE,
        "ConfirmationURL":settings.C2B_CONFIRMATION_URL,
        "ValidationURL":settings.C2B_VALIDATE_URL,
    }
    response = post(url=url, headers=headers, data=body)
    return response.json()


def process_online_checkout(
    msisdn: int,
    amount: int,
    account_reference: str,
    transaction_desc: str,
    is_paybil=True,
):
    """
    Handle the online checkout
    :param msisdn:
    :param amount:
    :param account_reference:
    :param transaction_desc:
    :param is_paybil: If set to False it means we are make a till transaction
    :return:
    """
    transaction_type = "CustomerPayBillOnline"
    if is_paybil:
      transaction_type = "CustomerBuyGoodsOnline"
    

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    data_to_encode = settings.C2B_ONLINE_SHORT_CODE + \
        settings.C2B_ONLINE_PASSKEY+timestamp
    online_password = base64.b64encode(data_to_encode.encode())
    password = online_password.decode('utf-8')


    api_url = f"{settings.MPESA_URL}/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" %
               AuthToken.objects.get_token("c2b")}
    request = {
        "BusinessShortCode": settings.C2B_ONLINE_SHORT_CODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": transaction_type,
        "Amount": str(amount),
        # replace with your phone number to get stk push
        "PartyA": str(msisdn),
        "PartyB": settings.C2B_ONLINE_SHORT_CODE,
        # replace with your phone number to get stk push
        "PhoneNumber": str(msisdn),
        "CallBackURL": settings.C2B_ONLINE_CHECKOUT_CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }


   
    response = post(url=api_url, headers=headers, data=request)
    return response.json()
