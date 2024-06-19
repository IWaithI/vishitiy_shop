from cart.cart import Cart

def cart(request):
    #  Контекстный процессор для добавления объекта корзины в контекст шаблона.
    return {'cart': Cart(request)}