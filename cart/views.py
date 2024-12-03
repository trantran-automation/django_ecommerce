from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from cart.models import Cart,CartItem
from orders.models import Order
from django.contrib import messages

# Create your views here.
@login_required
def view_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
        else:
            cart_items = []
    else:
        cart_items = []  # For anonymous users, cart logic can be different
    
    # Calculate total (optional)
    cart_total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def update_cart(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        quantity = request.POST.get("quantity")

        if not item_id or not quantity:
            messages.error(request, "Invalid input. Please try again.")
            return redirect("cart")  # Replace 'cart' with your cart page name

        try:
            quantity = int(quantity)
            if quantity < 1:
                messages.error(request, "Quantity must be at least 1.")
                return redirect("cart")

            # Update cart item
            cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart updated successfully.")
        except CartItem.DoesNotExist:
            messages.error(request, "Cart item not found.")
        except ValueError:
            messages.error(request, "Invalid quantity.")
        
    return redirect("cart")  

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    order = Order.objects.create(user=request.user, cart=cart, total_price=total_price, status='pending')
    # Clear cart after checkout
    cart.items.all().delete()
    return render(request, 'order_confirmation.html', {'order': order})
