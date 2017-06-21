#!/usr/bin/python2.6
# -*-coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def pdc(request):
    if request.method == "GET":
        r = self.request.GET.get('temperature')
    return render(request, 'cotador/pdc.html', {
        'temperature': r,
        })

def cpfcnpj_request(cpf_cnpj):
    if validate_cpf(cpf_cnpj):
        try:
            insured = Insured.objects.get(cpf_cnpj=cpf_cnpj)
            return insured.name
        except:
            return "now"
    else:
        return "Documento Inválido"
            

def quotation(request):
    pages = ["Cotação"]
    subpage = 1
    products = Product.objects.filter(active=1)
    if request.method == "POST":
        cpf_cnpj = request.POST['cpf_cnpj']
        insured = cpfcnpj_request(cpf_cnpj)
        insured_error = ""
        return render(request, 'cotador/multirrisco.html', {
            'pages': pages,
            'products': products,
            'cpf_cnpj': cpf_cnpj,
            'insured_name': insured
            })

    return render(request, 'cotador/multirrisco.html', {
        'pages': pages,
        'products': products
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

def get_insured_name(cpf_cnpj):
    key = 'e6cc0c8ac7fddca7d4a7bb45bcb2a813'
    url = "https://api.cpfcnpj.com.br/" + key + "/1/json/" + cpfNumber
    result = requests.get(url)
    cpfJson = result.json()
    return cpfJson
