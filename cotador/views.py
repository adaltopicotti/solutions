from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Prod_Esp, Culture, Product, Safra, Tax, Lvl_Cob
# Create your views here.
def quotation(request):
    page = 0
    pages = ["Cotação"]
    cities = City.objects.all()
    products = Product.objects.filter(active=1)
    ncs = Lvl_Cob.objects.all()
    page = 1
    if request.method == "POST":
            product = request.POST['product']
            price = request.POST['price']
            area = request.POST['area']
            if page == 1:
                pages = ["Cotação",Product.objects.get(id=product)]
                cultures = Culture.objects.filter(product_id=product)
                page = 2
            return render(request, 'cotador/cotador.html', {
                'products': products,
                'cultures': cultures,
                'cities': cities,
                'product_sel': int(product),
                'pages': pages,
                'product': product
            })
            if page == 2:
                #safra_sel = Safra.objects.get(culture_id=culture, active=1)
                nc_sel = request.POST['niv_cob']
                city_sel_name = City.objects.get(id=city)
                city = request.POST['city']
                result = calc(float(price), float(area), city, product, nc_sel)
                #product_sel = Product.objects.get(id=product)
                return render(request, 'cotador/cotador.html', {
                    'products': products,
                    'cultures': cultures,
                    'cities': cities,
                    'total_cost': repr(result[0]),
                    'final_cost': repr(result[1]),
                    'subv_fed': repr(result[2]),
                    'is_total': repr(result[3]),
                    'prod_esp': result[4],
                    'prod_seg': result[5],
                    'city': city_sel_name,
                    'ncs': ncs,
                    'price': price,
                    'area': area,
                    'product_sel': int(product),
                    'city_sel':int(city),
                    'nc_sel': int(nc_sel)})


    return render(request, 'cotador/cotador.html', {
        'pages': pages,
        'products': products,
        'cities': cities})
        #'ncs': ncs})


def calc(price, area, city, product, nc):
    prod_esp = Prod_Esp.objects.get(city_id=city, product_id=product)
    tax = case_nc(nc, city, product)
    prod_seg = round((prod_esp.value) * 0.6,2)
    sc = prod_seg/60
    is_total = round(((price * sc) *area),2)
    total_cost = round((is_total * tax),2)#round(is_total * 0.165,2)
    subv_fed = round(total_cost * 0.45,2)
    final_cost = round(total_cost - subv_fed,2)
    return [total_cost, final_cost, subv_fed, is_total, prod_esp.value, prod_seg, tax]



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
