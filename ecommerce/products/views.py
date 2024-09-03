from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Cart, Product

def home(request):
    return render(request,'home.html')

class CategoryView(View):
    def get(self,request,val):
        product =Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,'category.html',locals())
    
def account(request):
    return render(request,'account.html')

# def add_to_cart(request):
#     product_id=request.GET.get('prod_id')
#     product=Product.objects.get(id=product_id)
#     Cart(Product=product).save()
#     return redirect('/cart')
    

# def show_cart(request):
#     return render(request,'addtocart.html',locals())

def add_to_cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        product = Product.objects.get(id=prod_id)
        cart_item, created = Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')
    return render(request, 'home.html')    

def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'addtocart.html', {'cart_items': cart_items})

