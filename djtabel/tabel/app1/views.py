from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from app1.forms import FormBuyer
from app1.models import LogisticInfo, TextFile
from django.db.models import *
from django.core.files import File as DjangoFile

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logforma(request):
    if request.method == 'POST':
        forma = FormBuyer(request.POST)
        if forma.is_valid():
            new_log_info = LogisticInfo(
                distance=request.POST['distance'],
                type_delivery=request.POST['type_delivery'],
                masa=request.POST['masa'],
                pib=request.POST['pib'],
                phone=request.POST['phone'],
                email=request.POST['email'],
            )
            new_log_info.save()
            return HttpResponseRedirect('menu_after_form/')
    else:
        forma = FormBuyer()
    return render(request, 'forma_buy.html', {'form': forma})

def create_check(request):
    last_id = LogisticInfo.objects.aggregate(Max('id')) #знаходимо останній ІД з бази даних
    cr_check = LogisticInfo.objects.get(id=last_id['id__max']).__dict__ #формуємо словник останнього запису

    text = f'******************************' \
           f'*Квитанція Вашого замовлення:*' \
           f'******************************' \
           f'\nЗамовник послуги - {cr_check["pib"]};' \
           f'\nНомер телефону - {cr_check["phone"]};' \
           f'\nЕлектронна пошта - {cr_check["email"]};' \
           f'\nВідстань доставки - {cr_check["distance"]} км;' \
           f'\nВартість доставки складе: {cr_check["distance"]*5+(cr_check["masa"]*20/100)} грн;'
    with open('app1/create_check/text.txt', 'w', encoding="utf-8") as f:
        print(text, file=f) #запис ф-строки text в текстовий файл
    file_obj = DjangoFile(open('app1/create_check/text.txt', mode='rb'), name='check.txt')#створення об'єкта текстового файлу
    TextFile.objects.create(file=file_obj, text_date=datetime.datetime.now())#запис в базу даних текстового файлу
    last_id_check = TextFile.objects.aggregate(Max('id')) #знаходження останнього запису в базі даних
    check_file = TextFile.objects.get(id=last_id_check['id__max']) #дістаємо останній запис з бази даних для передачі в render
    return render(request, 'menu_after_form.html', {'check_file': check_file})

