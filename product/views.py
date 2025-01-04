from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.views.generic import UpdateView

from .models import Product, Client
from .forms import ProductForm


def home(request):
    return render(request, 'pages/home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In!')
            return redirect('home')
        else:
            messages.success(request, 'Please try again.....')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Success Logout!')
    return redirect('home')


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        client_name = request.POST.get('client_name')
        client_phone = request.POST.get('client_phone')

        if form.is_valid():
            # Check if Client exists
            client, created = Client.objects.get_or_create(
                name=client_name,
                phone=client_phone
            )

            product = form.save(commit=False)
            product.client = client
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'pages/product_form.html', {
        'form': form,
        'title': 'Create New Product',
    })


def product_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(serial_number__icontains=query) |
        Q(client__phone__icontains=query) |
        Q(client__name__icontains=query)  # Add this line to search by client's phone number
    ).select_related('client')  # Use select_related to optimize database queries

    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/product_table.html', {'page_obj': page_obj, 'query': ""})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            try:
                # Extract client information
                client_name = request.POST.get('client_name')
                client_phone = request.POST.get('client_phone')

                # Try to get an existing client with the same phone number
                client, created = Client.objects.get_or_create(
                    phone=client_phone,
                    defaults={'name': client_name}
                )

                if not created:
                    # If client already exists, update the name
                    client.name = client_name
                    client.save()

                # Save the product and associate with the client
                updated_product = form.save(commit=False)
                updated_product.client = client
                updated_product.save()

                messages.success(request, 'Product updated successfully.')
                return redirect(reverse('product_list'))
            except IntegrityError:
                messages.error(request, 'An error occurred. The phone number might be associated with another client.')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'title': 'Edit Product',
        'client_name': product.client.name if product.client else '',
        'client_phone': product.client.phone if product.client else '',
    }
    return render(request, 'pages/product_form.html', context)


# Delete View
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect(reverse('product_list'))
    return render(request, 'pages/product_confirm_delete.html', {'product': product})


def client_list(request):
    query = request.GET.get('q', '')
    clients = Client.objects.annotate(product_count=Count('products')).filter(
        Q(name__icontains=query) | Q(phone__icontains=query)
    ).order_by('name')

    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/client_table.html', {'page_obj': page_obj, 'query': ''})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    products = client.products.all()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/client_detail.html', {
        'client': client,
        'page_obj': page_obj,
        'title': f"Client Details: {client.name}"
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/product_detail.html', {'product': product})


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'pages/client_update.html'
    fields = ['name', 'phone']
    success_url = reverse_lazy('client_list')
