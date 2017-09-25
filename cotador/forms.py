from django import forms
from .models import Quotation

class PostForm(forms.ModelForm):

    class Meta:
        model = Quotation
        fields = (
            'protocol',
            'client',
            'product',
            'uf',
            'city',
            'lvl_cob',
            'area',
            'sack_price',
            'prod_esp',
            'prod_seg',
            'total_is',
            'total_cost',
            'subv_fed',
            'subv_est',
            'final_cost',
            'created_date')
