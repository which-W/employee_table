from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms
from app01.uels.pwd_md5 import md5_pwd
from app01.uels.font_virity import check_code
from io import BytesIO


class Account_login(forms.Form):
    username = forms.CharField(label="用户名",
                               max_length=32,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label="密码",
                               max_length=64,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    code = forms.CharField(label="验证码",
                           max_length=10,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入验证码'}))

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5_pwd(pwd)


# 登录
def account_login(request):
    # Check if the request method is GET
    if request.method == "GET":
        # Create a form object
        form = Account_login()
        # Render the account_login.html page with the form object
        return render(request, "account_login.html", {"form": form})
    # Create a form object with the POST data
    form = Account_login(data=request.POST)
    # Check if the form is valid
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('img_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'account_login.html', {'form': form})
        # Get the user object from the database
        user = models.Admin.objects.filter(**form.cleaned_data).first()
        # Check if the user object is valid
        if not user:
            # Add an error to the form
            form.add_error('password', '用户名或密码错误！')
            # Render the account_login.html page with the form object
            return render(request, "account_login.html", {"form": form})
        # Set the session info
        request.session['info'] = {'id': user.id, 'username': user.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        # Redirect to the list page
        return redirect("/admin/list")
    return render(request, 'account_login.html', {'form': form})


def account_font(request):
    # Generate a random code
    img, code_string = check_code()
    # Store the code in the session
    request.session['img_code'] = code_string
    # Set the session to expire after 60 seconds
    request.session.set_expiry(60)
    # Create a BytesIO object
    stream = BytesIO()
    # Save the image to the BytesIO object
    img.save(stream, format='png')
    # Return the image in the response
    return HttpResponse(stream.getvalue())


def account_logout(request):
    request.session.clear()
    return redirect("/admin/login")



