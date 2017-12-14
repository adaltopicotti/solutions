#!/usr/bin/python2.6
# -*-coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import *
import json, requests
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
# Create your views here.

def weather(request):
    weather = get_wheater('-23,4252777777777','-51,93861111111111')
    icon = manage_icon(int(weather['rain']))
    today = date.today()
    return render(request, 'pdc/weather.html', {'weather': weather, 'icon': icon, 'today': today})

def get_wheater(lat,lon):
    key = 'fab2e031061742d03b32b8ee6da17203'
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&APPID=" + key
    result = requests.get(url)
    weather = result.json()
    temp = round(weather['main']['temp'] - 273.15,2)
    rain = 0
    clouds = weather['clouds']['all']
    humidity = weather['main']['humidity']
    wind = round(weather['wind']['speed'] * 3.599997)
    result = {
        "temp":temp,
        "rain":rain,
        "humidity":humidity,
        "clouds":clouds,
        "wind":wind}
    return result


def manage_icon(rain):
    if rain == 0:
        icon = '1'
    elif (rain <= 15) and (rain > 0):
        icon = '2'
    elif (rain <= 45) and (rain > 0):
        icon = '4'
    else:
        icon = '1'
    return icon

def pdc(request):
    weather = get_wheater('-23,4252777777777','-51,93861111111111')
    icon = manage_icon(int(weather['rain']))
    today = date.today()
    return render(request, 'pdc/pdc.html', {
        'icon': icon,
        'today': today,
        'weather': weather
        })


def pdc_add(request):
    if request.method == "GET":
        form = PostWeather(request.GET)
        if form.is_valid():
            post = form.save(commit=False)
            post.temperature = request.GET['T']
            post.rain = request.GET['R']
            post.humidity = request.GET['H']
            post.wind = request.GET['W']
            post.date = timezone.now()
            post.save()
    return "Concluido"

#pdc/add?T=24.0&H=69.9&P=930.91&I=26.83&Hi=36&Ti=28"
def add(request):
    today = date.today()
    if request.method == "GET":
        form = PostWeather(request.GET)
        if form.is_valid():
            post = form.save(commit=False)

            post.temperature = request.GET['T']
            post.rain = request.GET['R']
            post.humidity = request.GET['H']
            post.wind = request.GET['W']
            post.date = timezone.now()
            post.save()
        return render(request, 'pdc/pdc.html', {
            'temp': temperature,
            'rain': rain,
            'humidity': humidity,
            'wind': wind,
            'weather': weather,
            'today': today,
            })



def add_2(request):
    today = date.today()
    if request.method == "GET":
        temperature = request.GET['T']
        rain = request.GET['R']
        humidity = request.GET['H']
        wind = request.GET['W']
        icon = manage_icon(int(rain))
        weather = {
           'temp' : temperature,
           'humidity' : humidity,
           'rain' : rain,
           'wind': wind
        }
        form = PostWeather(request.GET)
        form.date = timezone.now()
        form.save()
        return render(request, 'pdc/pdc.html', {
            'icon': icon,
            'temp': temperature,
            'rain': rain,
            'humidity': humidity,
            'wind': wind,
            'weather': weather,
            'today': today,
            })

def cpfcnpj_request(cpf_cnpj):
    if validate_cpf(cpf_cnpj):
        try:
            pre_register = PreRegister.objects.get(cpf_cnpj=cpf_cnpj)
            return pre_register.name
        except:
            #cpf_info = get_cpf_name(cpf_cnpj) only for localhost
            return "Aqui vai um nome"
    else:
        return "Documento Inválido"


def quotation_new(request):
    form = PostForm()
    return render(request, 'cotador/quotation_edit.html', {'form': form})

def quotation(request):
    pages = ["Cotação"]
    insured = ""
    cities = ""
    subpage = 1
    indicator = 1
    products = Product.objects.filter(active=1)
    ufs = Uf.objects.all()
    lvl_cobs = Lvl_Cob.objects.all()
    if request.method == "POST":
        validator = request.POST['ind']
        uf_sel = request.POST['uf']
        cities = City.objects.filter(uf=uf_sel)
        city_sel = request.POST['city']
        cpf_cnpj = request.POST['cpf_cnpj']
        insured = city_sel
        #insured = cpfcnpj_request(cpf_cnpj)
        insured_error = ""
        if (request.POST['area'] != '') and (request.POST['sack_price'] != ''):
            area = request.POST['area']
            sack_price = request.POST['sack_price']
            nc_sel = request.POST['lvl_cob']
            quotation_res = calc(float(sack_price), float(area), city_sel, 1, nc_sel)
            total_cost = quotation_res[0]
            final_cost = quotation_res[1]
            subv_fed = quotation_res[2]
            subv_est = quotation_res[3]
            is_total = quotation_res[4]
            prod_esp = quotation_res[5]
            prod_seg = quotation_res[6]
            tax = quotation_res[7]
            quotation_number = '00123'
            return render(request, 'cotador/multirrisco.html', {
                'pages': pages,
                'products': products,
                'cpf_cnpj': cpf_cnpj,
                'insured_name': quotation_res[1],
                'ufs': ufs,
                'validator': indicator,
                'cities': cities,
                'uf_sel': int(uf_sel),
                'city_sel': int(city_sel),
                'lvl_cobs': lvl_cobs,
                'area': area,
                'sack_price': sack_price,
                'total_cost': total_cost,
                'final_cost': final_cost,
                'subv_fed': subv_fed,
                'subv_est': subv_est,
                'is_total': is_total,
                'prod_esp': prod_esp,
                'prod_seg': prod_seg,
                'tax': tax,
                'quotation_number': quotation_number
                })
        else:
            return render(request, 'cotador/multirrisco.html', {
                'pages': pages,
                'products': products,
                'cpf_cnpj': cpf_cnpj,
                'insured_name': insured,
                'ufs': ufs,
                'validator': indicator,
                'cities': cities,
                'uf_sel': int(uf_sel),
                'city_sel': int(city_sel),
                'lvl_cobs': lvl_cobs
                })
    else:
            cities = City.objects.filter(uf=16)

    return render(request, 'cotador/multirrisco.html', {
        'pages': pages,
        'products': products,
        'ufs': ufs,
        'uf_sel': 16,
        'validator': indicator,
        'cities': cities,
        'lvl_cobs': lvl_cobs
        })



def calc(price, area, city, product, nc):
    prod_esp = Prod_Esp.objects.get(city_id=city, product_id=product)
    tax = case_nc(nc, city, product)
    prod_seg = round((prod_esp.value) * 0.6,2)
    sc = prod_seg/60
    is_total = round(((price * sc) *area),2)
    total_cost = round((is_total * tax),2)#round(is_total * 0.165,2)
    subv_fed = round(total_cost * 0.45,2)
    subv_est = round((total_cost - subv_fed)/2,2)
    final_cost = round(total_cost - subv_fed,2)
    return [total_cost, final_cost, subv_fed, subv_est, is_total, prod_esp.value, prod_seg, tax]



def case_nc(x, city, product):
    tax_sel = Tax.objects.get(city_id=city, product_id=product)
    if x == '1':
        return tax_sel.nc_60
        # Do the thing
    elif x == '2':
        return tax_sel.nc_65
    # Do the other thing
    elif x == '3':
        return tax_sel.nc_70
    else:
        return 0

def validate_cpf(cpfNumber):
        cpfNumber_invalidos = [11*str(i) for i in range(10)]
        if cpfNumber in cpfNumber_invalidos:
            return False

        if not cpfNumber.isdigit():
            """ Verifica se o cpfNumber contem pontos e hifens """
            cpfNumber = cpfNumber.replace( ".", "" )
            cpfNumber = cpfNumber.replace( "-", "" )

        if len( cpfNumber ) < 11:
            """ Verifica se o cpfNumber tem 11 digitos """
            return False
        if len( cpfNumber ) > 11:
            """ cpfNumber tem que ter 11 digitos """
            return False
        selfcpfNumber = [int( x ) for x in cpfNumber]
        cpfNumber = selfcpfNumber[:9]
        while len( cpfNumber ) < 11:
            r =  sum( [( len( cpfNumber )+1-i )*v for i, v in [( x, cpfNumber[x] ) for x in range( len( cpfNumber ) )]] ) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpfNumber.append( f )
        return bool( cpfNumber == selfcpfNumber )

def get_cpf_name(cpf_cnpj):
    key = '3956b0407de435019a01b0521402bd4c'
    url = "https://api.cpfcnpj.com.br/" + key + "/1/json/" + cpf_cnpj
    result = requests.get(url)
    cpfJson = result.json()
    return cpfJson
