from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.models import Client, Bank, Bill

# Create your views here.
def get_all_bank(request):
    all_bank = []
    banks = Bank.objects.all()
    for bank in banks:
        # print(bank.name)
        all_bank.append(bank.name)
    return JsonResponse({
        "status": 200,
        "data": all_bank})

def get_client_info(request):

    return JsonResponse({
        "status": 200,
        "data": {
            "name": "小黄",
            "money": 100000
        }
    })

def get_all_billings(request):
    all_bill = []
    bills = Bill.objects.all()
    for bill in bills:
        all_bill.append({
            "bank": bill.bank.name,
            "name": bill.client.name,
            "count": bill.money,
            "status": bill.status,
            "start_time": bill.start_date,
            "expiration": bill.expiration,
            "ensure_time": bill.ensure_time,
            "billing_number": bill.client_certificate
        })
    return JsonResponse(
        {
            "status": 200,
            "data": all_bill
        }
    )

def client_certificate(request):
    return {
            "status":200,
            "data":true
            }