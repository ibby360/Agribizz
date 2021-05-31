from django.shortcuts import get_object_or_404, render, get_list_or_404, resolve_url

from shop.models import Category, Product
from cart.forms import CartAddProdcutForm

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category= get_object_or_404(Category, slug=category_slug)
        products= products.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'shop/product_list.html', context)

def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProdcutForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product_details.html', context)

def checkout(request):
    return render(request, 'shop/checkout.html',{})