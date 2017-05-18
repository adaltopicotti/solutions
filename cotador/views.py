from django.shortcuts import render

# Create your views here.
def quotation(request):
     if request.method == "POST":
          price = request.POST['price']
          area = request.POST['area']
          result = calc(float(price), float(area))
          return render(request, 'cotador/cotador.html', {'total_cost': repr(result[0]),
                                                         'final_cost': repr(result[1]),
                                                         'subv_fed': repr(result[2]),
                                                         'is_total': repr(result[3])})
     return render(request, 'cotador/cotador.html', {})


def calc(price, area):
     is_total = round(((price * 24.33) *area),2)
     total_cost = round(is_total * 0.165,2)
     subv_fed = round(total_cost * 0.45,2)
     final_cost = round(total_cost - subv_fed,2)
     return [total_cost, final_cost, subv_fed, is_total]
