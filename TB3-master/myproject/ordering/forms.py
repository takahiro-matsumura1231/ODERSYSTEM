from django import forms
from .models import Product

class MenuForm(forms.ModelForm):
    name = forms.CharField(
        required = True,
        label = "商品名",
        )
    price = forms.IntegerField(
        required = True,
        label = "価格")
    tax = forms.BooleanField(
        required = False,
        
        widget=forms.RadioSelect(
            choices=[
                (True, "8%"),
                (False, "10%")
                ]
            ),
        label = "税率"
    )
    category_id = forms.ChoiceField(
        choices = (
            (1, "食べ物"),
            (2, "飲み物"),
            (3, "お持ち帰り"),
        ),
        required=True,
        widget=forms.widgets.Select,
        label = "カテゴリ"
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'tax', 'category_id']