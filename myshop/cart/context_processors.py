from .cart import Cart

def cart(request):
    cart = Cart(request)
    cart_items = list(cart)  # Convert the cart items to a list
    print(cart_items)  # Print the items in the cart
    cart_length = len(cart)
    return {'cart': Cart(request)}
