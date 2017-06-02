#!/usr/bin/python2.6
# -*-coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Prod_Esp, Culture, Product, Safra, Tax, Lvl_Cob
# Create your views here.

def getCPF(request):
    client_cpf = request.POST['cpf']
    if validateCPF(client_cpf):
            client_name = "CPF Válido"
            client_name = "Inválido"
    return client_name

def quotation(request):
    index = 0
    pages = ["Cotação"]
    products = Product.objects.filter(active=1)
    cities = City.objects.all()
    ncs = Lvl_Cob.objects.all()
    if request.method == "POST":
        index = index + 1
        product_sel = request.POST['product']
        cultures = Culture.objects.filter(product_id=product_sel)
        pages += [Product.objects.get(id=product_sel)]
        client_cpf = request.POST['cpf']
        if validateCPF(client_cpf):
            client_name = "CPF Válido"
            cpf_error = ""
        else:
            client_name = ""
            cpf_error = True
            index = index -1

        try:
            culture_sel = request.POST['culture']
            pages += [Culture.objects.get(id=culture_sel)]
            index = index + 1
        except:
            culture_sel = 0
        try:
            city_sel = request.POST['city']
            nc_sel = request.POST['niv_cob']
            pages += [City.objects.get(id=city_sel), Lvl_Cob.objects.get(id=nc_sel)]
            index = index + 1
        except:
            city_sel = 0
            nc_sel = 0
        try:
            price = request.POST['price']
            area = request.POST['area']
            index = index + 1
        except:
            price = 0
            area = 0
        if index == 4:
            result_calc = calc(float(price), float(area), city_sel, product_sel, nc_sel)
            return render(request, 'cotador/cotador.html', {
                'products': products,
                'cultures': cultures,
                'cities': cities,
                'ncs': ncs,
                'cpf': client_cpf,
                'client_name': client_name,
                'product_sel': int(product_sel),
                'culture_sel': int(culture_sel),
                'city_sel': int(city_sel),
                'nc_sel': int(nc_sel),
                'pages': pages,
                'index': index,
                'total_cost': (result_calc[0]),
                'final_cost': repr(result_calc[1]),
                'subv_fed': repr(result_calc[2]),
                'subv_est': repr(result_calc[3]),
                'is_total': repr(result_calc[4]),
                'prod_esp': result_calc[5],
                'prod_seg': result_calc[6]
                })
        else:
            return render(request, 'cotador/cotador.html', {
                'products': products,
                'cultures': cultures,
                'cities': cities,
                'ncs': ncs,
                'cpf': client_cpf,
                'client_name': client_name,
                'cpf_error': cpf_error,
                'product_sel': int(product_sel),
                'culture_sel': int(culture_sel),
                'city_sel': int(city_sel),
                'nc_sel': int(nc_sel),
                'pages': pages,
                'index': index
                })




    return render(request, 'cotador/cotador.html', {
        'pages': pages,
        'products': products,
        'cities': cities,
        'index': index
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

def validateCPF(cpfNumber):
        """
        Method to validate a brazilian cpfNumber number
        Based on Pedro Werneck source avaiable at
        www.PythonBrasil.com.br

        Tests:
        >>> print cpfNumber().validate('91289037736')
        True
        >>> print cpfNumber().validate('91289037731')
        False
        """
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

def get_Client_Name(request):

    key = 'e6cc0c8ac7fddca7d4a7bb45bcb2a813'
    if request.method == "POST":
        cpfNumber = request.POST['cpfNumber']
        if validateCPF(cpfNumber) == True:
            url = "https://api.cpfcnpj.com.br/" + key + "/1/json/" + cpfNumber
            result = requests.get(url)
            cpfJson = result.json()
            return render(request, 'application/cpf.html', {
                'r': cpfJson,
                'cpfInfo': cpfInfo,
                'page_title': 'CPF'})
        else:
            return render(request, 'application/cpf.html', {
                'r': '*Insira um CPF válido!',
                'cpfInfo': cpfInfo,
                'page_title': 'CPF'})
    else:
        return render(request, 'application/cpf.html', {'cpfInfo': cpfInfo, 'page_title': 'CPF'})
