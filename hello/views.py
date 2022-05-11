from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm,LoginForm,CustomerProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Customer, Product,Cart, UserForm,OrderPlaced
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, 'hello/home.html')


def contact(request):
    return render(request, 'hello/contact.html')


def about(request):
    return render(request, 'hello/about.html')

# for signup form


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            # nm = fm.cleaned_data['username']
            # fn = fm.cleaned_data['first_name']
            # ln = fm.cleaned_data['last_name']
            # em = fm.cleaned_data['email']
            # pm = fm.cleaned_data['password']
            # reg = User(username=nm, first_name=fn, last_name=ln, email=em,password=pm)
            # reg.save()
            fm.save()
            messages.success(request, 'Account created successfully')
    else:
        fm = SignUpForm()
    return render(request, 'hello/signup.html', {'form': fm})


def user_login(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']

            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = LoginForm()
    return render(request, 'hello/login.html', {"form": fm})
 else:
     return HttpResponseRedirect('/profile/')
 
 
def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/')
 
@login_required
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=CustomerProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                us=request.user
                nm=fm.cleaned_data['name']
                lc=fm.cleaned_data['locality']
                ct=fm.cleaned_data['city']
                st=fm.cleaned_data['state']
                pn=fm.cleaned_data['pincode']
                reg=Customer(user=us,name=nm,locality=lc,city=ct,state=st,pincode=pn)
                reg.save()
                messages.success(request,'Profile Updated!!!!')
        else:
            fm=CustomerProfileForm(instance=request.user)
        return render(request,'hello/profile.html',{'name':request.user,'form':fm,'active':'btn-primary'})
    else:
        return HttpResponseRedirect('/login/')
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'hello/address.html',{'add':add,'active':'btn-primary'})    

def product(request):
    veg=Product.objects.filter(category='VG')
    return render(request,'hello/product.html',{'veg':veg})

def product2(request):
    fruits=Product.objects.filter(category='FS')
    return render(request,'hello/product2.html',{'fruits':fruits})

def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    item_already_in_cart=False
    item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request,'hello/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/showcart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        # print(cart)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount+shipping_amount
            return render(request,'hello/add_to_cart.html',{'cart':cart,'totalamount':totalamount,'amount':amount})
        return render(request,'hello/emptycart.html')
        
    

def buy_now(request):
    return render(request,'hello/buynow.html')

@login_required
def check_out(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount += tempamount
            totalamount = amount+shipping_amount
    return render(request,'hello/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})

@login_required
def payment_done(request):
    user=request.user
    custid=request.GET.get("custid")
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')

@login_required
def orders(request):
    op=OrderPlaced.objects.filter(user=request.user)
    return render(request,'hello/order.html',{'order_placed':op})

def user_form(request):
    if request.method=='POST':
        usnm=request.POST.GET('name')
        pass1=request.POST.GET('password')
        pass2=request.POST.GET('re-type')
        reg=UserForm(username=usnm,password=pass1,password2=pass2)
        reg.save()
        
        
        