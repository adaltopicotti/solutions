from django.shortcuts import render

# Create your views here.
def quotation(request):
    return render(request, 'cotador/cotador.html', {})
