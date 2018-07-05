from .cart import Cart
from .models import Delivery, Order, OrderItem
import stripe
from django.conf import settings

def get_user_delivery_addresses(user):
    """
    """
    return Delivery.objects.filter(user=user)
    
def get_full_delivery_object(pk):
    """
    """
    return Delivery.objects.get(pk=pk)
    
def process_stripe_payment(request):
    """
    from stipe documentation
    https://stripe.com/docs/charges
    """
    stripe.api_key = settings.STRIPE_SECRET
    # changed from value in docs: token = request.form['stripeToken'] 
    # fixed bug: 'WSGIRequest' object has no attribute 'form'
    token = request.POST['stripeToken'] 
    
    charge = stripe.Charge.create(
        amount=999,
        currency='usd',
        description='Example charge',
        source=token,
    )
    
    
def process_order(request, user):
    """
    """
    delivery_pk = request.POST.get("deliverySelection")
    delivery_object = get_full_delivery_object(delivery_pk)
    order = Order(user=user, delivery_address=delivery_object)
    order.save()
    
    cart = Cart(request)
    for item in cart:
        order_item = OrderItem(order=order, item=item["item"], quantity=item["quantity"])
        order_item.save()
        
    cart.clear()