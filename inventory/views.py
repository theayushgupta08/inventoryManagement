from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Supplier, SaleOrder, StockMovement
from .forms import ProductForm, SupplierForm, SaleOrderForm, StockMovementForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'inventory/list_products.html', {'products': products})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_suppliers')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/list_suppliers.html', {'suppliers': suppliers})

def add_stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_stock_movements')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/add_stock_movement.html', {'form': form})

def list_stock_movements(request):
    stock_movements = StockMovement.objects.all()
    return render(request, 'inventory/list_stock_movements.html', {'stock_movements': stock_movements})

def create_sale_order(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sale_orders')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/create_sale_order.html', {'form': form})

def list_sale_orders(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, 'inventory/list_sale_orders.html', {'sale_orders': sale_orders})

def cancel_sale_order(request, order_id):
    sale_order = get_object_or_404(SaleOrder, id=order_id)
    if sale_order.status != 'Cancelled':
        sale_order.status = 'Cancelled'
        sale_order.product.stock_quantity += sale_order.quantity
        sale_order.product.save()
        sale_order.save()
    return redirect('list_sale_orders')
    

def complete_sale_order(request, order_id):
    sale_order = get_object_or_404(SaleOrder, id=order_id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Completed'
        sale_order.save()
    return redirect('list_sale_orders')

def stock_level_check(request):
    products = Product.objects.all()
    stock_levels = {product.name: product.stock_quantity for product in products}
    return render(request, 'inventory/stock_level_check.html', {'stock_levels': stock_levels})

def dashboard(request):
    return render(request, 'inventory/dashboard.html')