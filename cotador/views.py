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


def calc(price, area):
     is_total = ((price * 24.33) *area)
     total_cost = is_total * 0.165
     subv_fed = total_cost * 0.45
     final_cost = total_cost - subv_fed
     return [total_cost, final_cost, subv_fed, is_total]
