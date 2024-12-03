from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label='Tên đăng nhập',  # Custom label
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username or Email'})
    )
    password = forms.CharField(
        label='Mật khẩu',  # Custom label
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    class Meta:
        model = User
        field = ['username','password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure form fields are styled and have placeholders
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Mật khẩu',  # Custom label
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )

    password2 = forms.CharField(
        label='Xác nhận mật khẩu',  # Custom label
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'profile_image', 'password1', 'password2']
        labels = {
            "username": "Họ và tên",
            "email": "email",
            "phone_number": "Số điện thoại",
            "address":"Địa chỉ",
            "profile_image":"Ảnh đại diện",
        }
        widgets = {
            'address': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    