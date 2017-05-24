from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Prod_Esp, Culture, Product, Safra, Tax, Lvl_Cob
# Create your views here.
def quotation(request):
    cities = City.objects.all()
    products = Product.objects.all()
    nc = Lvl_Cob.objects.all()
    if request.method == "POST":
        price = request.POST['price']
        area = request.POST['area']
        #culture = request.POST['culture']
        product = request.POST['product']
        city = request.POST['city']
        nc_sel = request.POST['nc']
        result = calc(float(price), float(area), city, product, nc_sel)
        #safra_sel = Safra.objects.get(culture_id=culture, active=1)
        #product_sel = Product.objects.get(culture_id=culture)
        city_sel = City.objects.get(id=city)
        return render(request, 'cotador/cotador.html', {
            'products': products,
            'cities': cities,
            'total_cost': repr(result[0]),
            'final_cost': repr(result[1]),
            'subv_fed': repr(result[2]),
            'is_total': repr(result[3]),
            'prod_esp': result[4],
            'prod_seg': result[5],
            'city': city_sel,
            'nc': nc,
            'price': price,
            'area': area,
            're_select':city_sel,
            'tax': result[6]})


    return render(request, 'cotador/cotador.html', {
        'products': products,
        'cities': cities,
        'nc': nc})


def calc(price, area, city, product, nc):
    prod_esp = Prod_Esp.objects.get(city_id=city, product_id=product)

    prod_seg = round((prod_esp.value) * 0.6,2)
    sc = prod_seg/60
    is_total = round(((price * sc) *area),2)
    total_cost = round((is_total * nc_f(nc, city, product)),2)#round(is_total * 0.165,2)
    subv_fed = round(total_cost * 0.45,2)
    final_cost = round(total_cost - subv_fed,2)
    return [total_cost, final_cost, subv_fed, is_total, prod_esp.value, prod_seg, nc_f(nc, city, product)]

def nc_f(x, city, product):
    tax = Tax.objects.get(city_id=city, product_id=product)
    if x == 1:
        return tax.nc_60
        # Do the thing
    elif x == 2:
        return tax.nc_65
    # Do the other thing
    else:
        return tax.nc_70
