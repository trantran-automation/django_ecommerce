from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'stock','image'] 
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }
        labels = {
            "name": "Tên mặt hàng",
            "description": "Miêu tả",
            "price": "Giá",
            "stock":"Số lượng",
            "image":"Ảnh mặt hàng",
        }