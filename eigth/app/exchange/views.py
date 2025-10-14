from django.shortcuts import render
import requests


# Create your views here.

def exchange(request):
    responce = requests.get(url='https://www.cbr-xml-daily.ru/latest.js').json()
    currencies = responce.get('rates')
    date_curr = responce.get('date')

    if request.method == "GET":

        context = {'currencies': currencies}
        return render(request, 'exchange/index.html', context)
    else:
        from_amount = request.POST.get("from-amount")
        from_curr = request.POST.get("from-curr")
        to_curr = request.POST.get("to-curr")

        convert_ammount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)
        context = {'currencies': currencies,
                   'from_curr': from_curr,
                   'to_curr': to_curr,
                   'from_amount': from_amount,
                   'convert_ammount': convert_ammount,
                   'date_curr': date_curr,
                   }
        return render(request, 'exchange/index.html', context)
