from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from .tasks import send_mail_task



def getAccessToken(request):
    consumer_key = 'DvHHHSpxWxv5I7yjXsdJHYrvGPuWnezR'
    consumer_secret = 'BkaY1BhdCX9FGx39'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return validated_mpesa_access_token


def lipa_na_mpesa_online(request):
   
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254711521508,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254711521508,  # replace with your phone number to get stk push
        "CallBackURL": "http://5ccd97aff471.ngrok.io/c2b/confirmation",
        "AccountReference": "shop with us",
        "TransactionDesc": "Testing stk push"
    }
  
    response = requests.post(api_url, json=request, headers=headers)
    register_urls(request)
    return HttpResponse(response)


@csrf_exempt
def register_urls(request):
    #cel=add.apply_async((4,4),queue="sum",retry=True)
    #cel1=cel.get()
    #cel12=cel.ready()
    
    #print(cel12)
    return HttpResponse("cel1")


@csrf_exempt
def call_back(request):

    mpesa_body = request.body.decode('utf-8')
    print(mpesa_body)
    
    pass


@csrf_exempt
def validation(request):
    mpesa_body = request.body.decode('utf-8')
    print(mpesa_body)

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    
    mpesa_body = request.body.decode('utf-8')
    print(mpesa_body)
    mpesa_payment = json.loads(mpesa_body)






    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],

    )
    payment.save()



    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse(dict(context))
