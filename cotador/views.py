from django.shortcuts import render, get_object_or_404, redirect
from .models import City
# Create your views here.
def quotation(request):
    cities = City.objects.all()
    if request.method == "POST":
        price = request.POST['price']
        area = request.POST['area']
        city = request.POST['city']
        result = calc(float(price), float(area))
        city_sel = City.objects.get(id=city)
        return render(request, 'cotador/cotador.html', {'cities': cities,
                                                    'total_cost': repr(result[0]),
                                                    'final_cost': repr(result[1]),
                                                    'subv_fed': repr(result[2]),
                                                    'is_total': repr(result[3]),
                                                    'city': city_sel})


    return render(request, 'cotador/cotador.html', {'cities': cities})


def calc(price, area):
    is_total = round(((price * 24.33) *area),2)
    total_cost = round(is_total * 0.165,2)
    subv_fed = round(total_cost * 0.45,2)
    final_cost = round(total_cost - subv_fed,2)
    return [total_cost, final_cost, subv_fed, is_total]

"""
class CityChainedSelectWidget(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(u' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = u''
        customer_reference = u''
        if option_value:
            customer_id = City.objects.get(id=option_value).customer.id
            customer_reference = u' class={0}'.format(customer_id)
        return format_html(u'<option value="{0}"{1}{2}>{3}</option>',
                           option_value,
                           selected_html,
                           customer_reference,
                           force_text(option_label))
class DepartmentForm(PersonForm):
    country = forms.ModelChoiceField(
        label=u'País',
        queryset=Country.objects.all(),
    )
    class Meta:
        model = Department
        fields = (
            'name',
            'city',
        )
        widgets = {
            'city': CityChainedSelectWidget(),
        }"""
