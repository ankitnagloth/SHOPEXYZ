from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm



from .models import(
    Customer,
    Product,
    Cart,
    OrederPlaced
)

class ProductView(View):
    def get(self, request):
        camera = Product.objects.filter(category='C')
        men = Product.objects.filter(category='M')
        women = Product.objects.filter(category='W')
        sunglasses = Product.objects.filter(category='S')
        shoes = Product.objects.filter(category='SH')
        context = {
            'camera': camera,
            'shoes': shoes,
            'sunglasses': sunglasses,
            'men': men,
            'women': women,
        }


        return render(request ,'index.html',context)

class ProductDetails(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render (request,'ProductDetails.html', {'product':product})

def shoes(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='SH')

    elif data == 'Campus':
         products = Product.objects.filter(category='SH').filter(brand = 'Campus')

    elif data == 'Nike':
         products = Product.objects.filter(category='SH').filter(brand = 'Nike') 

    elif data == 'below':
         products = Product.objects.filter(category='SH').filter(discounted_price__lt = 300)

    elif data == 'above':
         products = Product.objects.filter(category='SH').filter(discounted_price__gt = 300)              
        
    return render(request, 'shoes.html', {'products' : products}) 

def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains= q)
    return render(request, 'search.html',{'data':data,'q':q})
   
   

def carts (request):
    return render (request,'carts.html')  


class RegistrationView(View):
    def get(self, request):
     form = RegistrationForm()
     return render(request, 'registration.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'registration.html', {'form':form})
    

 