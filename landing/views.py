from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article,Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Appointment,Cart
import requests
from django.views.decorators.clickjacking import xframe_options_exempt
import uuid



# def cart_list(request):
#     cart = [
#         {"name": "Item A", "price": 19.99, "quantity": 2, "image": {"url": "/static/item-a.jpg"}},
#         {"name": "Item B", "price": 9.99, "quantity": 1, "image": {"url": "/static/item-b.jpg"}},
#     ]

#     for item in cart:
#         item['total_price'] = item['price'] * item['quantity']

#     total = sum(item['total_price'] for item in cart)

#     return render(request, 'cart.html', {'cart': cart, 'total': total})

 # Create your views here.


def home(request):
    blogg=Article.objects.all()
    return render(request,"index.html",{"blogg":blogg})

def blog(request):
    blogg=Article.objects.all()
    return render(request,"section/blog.html",{"blogg":blogg})

def return_policy(request):
    return render(request,"section/footer/return.html")

def terms_condition(request):
    return render(request,"section/footer/terms.html")

def privacy_policy(request):
    return render(request,"section/footer/privacy.html")



# Blog and Article
def blog_detail(request, pk):
    blog = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})


def unique_id(request):
    cart_id = request.COOKIES.get('cart_id')

    if not cart_id: 
        cart_id = str(uuid.uuid4())

    return cart_id

# a8de4232-fc52-41e3-a526-a489cb2aba73
# Product
def product_list(request, category):
    cart_id = unique_id(request)
    # print(cart_id)
    products = Product.objects.filter(category=category)
    cart_count = sum(item.quantity for item in Cart.objects.filter(user_idd=cart_id))

    response = render(request, 'product/product.html', {'products': products,'cart_count':cart_count})
    if 'cart_id' not in request.COOKIES:
        response.set_cookie("cart_id",cart_id,max_age = 31536000)
    return response

@xframe_options_exempt
def cart_list(request):
    cart_id = unique_id(request)
    cart = Cart.objects.filter(user_idd = cart_id)
    total = sum([ Cart.price*Cart.quantity for Cart in Cart.objects.filter(user_idd = cart_id)])
    return render(request,"product/cart.html",{'cart':cart,'total':total})

def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    cart_id = unique_id(request)

    if list(Cart.objects.filter(name = product,user_idd = cart_id)) == []:

        Cart.objects.create(
            name = product,
            price = product.price,
            image = product.image,
            quantity = 1,
            user_idd = cart_id
        )
    else:
        cart = Cart.objects.get(name = product)
        cart.quantity +=1
        cart.save()
        print(cart.quantity)

    

    return redirect(request.META.get('HTTP_REFERER', '/'))

def remove_item(request,item_id):
    cart_item = Cart.objects.get(id = item_id)
    cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def book_appointment(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        time = request.POST['time']
        place = request.POST['place']
        gender = request.POST['gender']
        service = request.POST['service']

        appointment = Appointment.objects.create(
            name=name,
            phone=phone,
            dob=dob,
            time=time,
            place=place,
            gender=gender,
            service=service
        )

        return render(request,"payment/success.html",{"message":"Appointment Book Successfully"})
        
   
    return render(request, 'index.html')


def payment_success(request):
    print("sucess")
    # payment_order_id = request.GET.get('order_id')
    # payment_reference_id = request.GET.get('reference_id')
    # payment_signature = request.GET.get('signature')

    # # Prepare data to verify signature and payment status with Cashfree
    # verification_data = {
    #     "order_id": payment_order_id,
    #     "reference_id": payment_reference_id,
    #     "payment_signature": payment_signature,
    # }

    # # Verify payment using Cashfree's API (Verify Payment)
    # response = requests.post("https://sandbox.cashfree.com/pg/orders/verify", json=verification_data, headers=headers)
    # data = response.json()
    # print("Cashfree Response:", data)

    # if data.get('status') == 'OK' and data.get('payment_status') == 'SUCCESS':
    #     # Update database for successful payment
    #     appointment = Appointment.objects.get(id=payment_order_id)
    #     appointment.payment_status = 'Paid'
    #     appointment.save()

    #     return render(request, 'payment/success.html', {"message": "Payment Successful!"})
    # else:
    #     return render(request, 'payment/failure.html', {"message": "Payment Failed. Please try again."})


def payment_failure(request):
    # Handle failure (Log details or display a failure message)
    return render(request, 'payment/failure.html', {"message": "Payment Failed. Please try again."})
