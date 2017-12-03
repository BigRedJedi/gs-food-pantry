from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# Add per page 245
from .tasks import order_created

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from shop.models import Product

'''
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
'''

class Error:
    def __init__(self, name, qt):
        self.product_name = name
        self.quantity = qt


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            errors = []
            for item in cart:
                print("Entered here")
                OrderItem.objects.create(order=order, product=item['product'],
                                         # price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
                updated_stock = Product.objects.all().filter(name=item['product'])[0].stock - item['quantity']
                print("Updated Stock is:",updated_stock)
                if (int(updated_stock) < 0):
                    errors.append(Error(item['product'], Product.objects.all().filter(name=item['product'])[0].stock))
                else:
                    Product.objects.all().filter(name=item['product']).update(stock=updated_stock)
            cart.clear()

            if len(errors) > 0:
                print("Number of errors:",len(errors))
                return render(request,
                              'orders/order/create.html',
                              {'order': order,'errors':errors})


            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})

'''
@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\
        "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')])
    return response

'''