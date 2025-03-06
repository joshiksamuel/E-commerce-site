from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from esite.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        address=request.POST['address']
        message=request.POST['message']
        obj=Contact()
        obj.name = name
        obj.phoneno = phoneno
        obj.email = email
        obj.address = address
        obj.message = message
        obj.save()
        messages.success(request,"Register successfully")
    return render(request,'contact.html')
def account(request):
    return render(request,'account.html')
def signup(request):
    if request.method =='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Password=request.POST['Password']
        obj=Register()
        obj.Username=Username
        obj.Email=Email
        obj.Password=Password
        obj.save()
        messages.success(request,"Register successfully")
        return render(request,'signup.html') 
    return render(request,'signup.html')  
def login(request):
    if request.method =='POST':        
        try:
            register=Register.objects.get(Email=request.POST['Email'],Password=request.POST['Password'])
            am=register.Email
            return render(request,'index.html',{'iam':am})
        except:
            messages.warning(request,"username|password invalid")
    
    return render(request,'login.html')
def logoutpage(request):
    logout(request)
    return redirect('login')
def changepassword(request):
    if request.method=='POST':
        rem=request.POST['Email']
        rep=request.POST['NPASSWORD']
        r=Register.objects.get(Email=rem)
        r.Password=rep
        r.save()
        messages.success(request,'Password is changed successfully')
        return render(request,'changepassword.html')
    return render(request, 'changepassword.html')


@login_required
def add_to_cart(request, product_id):
    cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
       
    else:
        CartItem.objects.create(user=request.user, product_id=product_id)
        
    return redirect('cart')
    

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.user == request.user:
        cart_item.delete()
       
    return redirect('cart')

 
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.quantity * item.product.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)
    

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

@login_required
def productdetails(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product details.html', context)

def increase_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.quantity += 1
    product.save()
    return JsonResponse({'quantity': product.quantity})

def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.quantity > 0:
        product.quantity -= 1
        product.save()
    return JsonResponse({'quantity': product.quantity})

def order_item(request,product_id):
    cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
       
    else:
        CartItem.objects.create(user=request.user, product_id=product_id)
        
    return redirect('buynow')

def buynow(request):
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.quantity * item.product.price for item in cart_items)
        context = {
                'cart_items': cart_items,
                'total_price': total_price,
                    }
        return render(request,'buynow.html',context)
    
def checkout(request):    
        if request.method ==  'POST':
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            zipcode=request.POST['zipcode']
            namecard=request.POST['namecard']
            creditno=request.POST['creditno']
            expmonth=request.POST['expmonth']
            cvv=request.POST['cvv']
            obj=shipping()
            obj.name = name
            obj.email = email
            obj.address = address
            obj.city= city
            obj.state= state
            obj.zipcode= zipcode
            obj.namecard= namecard
            obj.creditno=creditno
            obj.expmonth=expmonth
            obj.cvv=cvv
            obj.save()
            messages.success(request,"Register successfully")
        return redirect('buynow')


