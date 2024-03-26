from django.shortcuts import render,redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = {
        "invoice_total": Order.objects.all().order_by("-created_at").first().total_price,
        "all_orders_items_total": Order.objects.aggregate(Sum("quantity_ordered"))['quantity_ordered__sum'],
        "total_spend": Order.objects.aggregate(Sum("total_price"))['total_price__sum']
    }
    return render(request, "store/checkout.html", context)
    

def process_order(request):
    if request.method == 'POST':
        product_price = Product.objects.filter(id = request.POST['product_id']).first().price
        if product_price:
            quantity_from_form = int(request.POST["quantity"])
            price_from_form = float(product_price)
            total_charge = quantity_from_form * price_from_form
            print("Charging credit card...")
            Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
            return redirect('/checkout')
        return redirect('/')