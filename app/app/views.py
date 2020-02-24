from django.shortcuts import render


def homepage(request):
    template = 'home-electronics-store.html'
    context = {}
    return render(request, template, context)

def address(request):
    template = 'account-address.html'
    context = {}
    return render(request, template, context)

def orders(request):
    template = 'account-orders.html'
    context = {}
    return render(request, template, context)

def recovery(request):
    template = 'account-password-recovery.html'
    context = {}
    return render(request, template, context)

def payment(request):
    template = 'account-payment.html'
    context = {}
    return render(request, template, context)

def profile(request):
    template = 'account-profile.html'
    context = {}
    return render(request, template, context)

def singin(request):
    template = 'account-signin.html'
    context = {}
    return render(request, template, context)

def ticket(request):
    template = 'account-single-ticket.html'
    context = {}
    return render(request, template, context)

def tickets(request):
    template = 'account-tickets.html'
    context = {}
    return render(request, template, context)

def wishlist(request):
    template = 'account-wishlist.html'
    context = {}
    return render(request, template, context)

def complete(request):
    template = 'checkout-complete.html'
    context = {}
    return render(request, template, context)

def details(request):
    template = 'checkout-details.html'
    context = {}
    return render(request, template, context)

def payments(request):
    template = 'checkout-payment.html'
    context = {}
    return render(request, template, context)

def review(request):
    template = 'checkout-review.html'
    context = {}
    return render(request, template, context)

def shipping(request):
    template = 'checkout-shipping.html'
    context = {}
    return render(request, template, context)

def contacts(request):
    template = 'contacts.html'
    context = {}
    return render(request, template, context)

def add(request):
    template = 'dashboard-add-new-product.html'
    context = {}
    return render(request, template, context)

def sales(request):
    template = 'dashboard-sales.html'
    context = {}
    return render(request, template, context)

def otracking(request):
    template = 'order-tracking.html'
    context = {}
    return render(request, template, context)

def scart(request):
    template = 'shop-cart.html'
    context = {}
    return render(request, template, context)

def categories(request):
    template = 'shop-categories.html'
    context = {}
    return render(request, template, context)

def grid(request):
    template = 'shop-grid-ft.html'
    context = {}
    return render(request, template, context)