
# product/views_html.py


from django.shortcuts import render


def home(request):
    return render(request, 'product/home.html')

def search_product(request):
    return render(request, "product/search_product.html")





