import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Item, Order
from django.http import JsonResponse



stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_order(request, order_pk):
    """
        Создает новую сессию оплаты Stripe для заказа с указанным primary key.
        Параметры:
            - request: HttpRequest объект
            - order_pk: int, primary key заказа

        Возвращает JsonResponse объект со значением session_id созданной сессии оплаты Stripe.
        """
    order = get_object_or_404(Order, pk=order_pk)

    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': order.currency,
                'unit_amount': round(item.total() * 100),
                'product_data': {
                    'name': item.name,
                },
            },
            'quantity': 1,
        })

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        metadata={
            "product_id": int(order.id),
        },
        mode='payment',
        success_url=request.build_absolute_uri('/') + 'success/',
        cancel_url=request.build_absolute_uri('/') + 'cancel/',
    )
    return JsonResponse({'session_id': checkout_session.id})


def buy(request, item_pk):
    """
        Создает новый объект платежа Stripe (PaymentIntent) для товара с указанным primary key.
        Параметры:
            - request: HttpRequest объект
            - item_pk: int, primary key товара

        Возвращает JsonResponse объект со значением payment_intent созданного объекта платежа Stripe.
        """
    item = get_object_or_404(Item, pk=item_pk)
    total_amount = int(item.total() * 100)

    currency = item.currency
    if currency == 'USD':
        stripe.api_key = settings.STRIPE_SECRET_KEY
    elif currency == 'EUR':
        stripe.api_key = settings.STRIPE_SECRET_KEY

    payment_intent = stripe.PaymentIntent.create(
        amount=total_amount,
        currency=currency,
        payment_method_types=['card'],
        description=item.name,
        metadata={
            "item_id": item.id,
        }
    )
    return JsonResponse({'payment_intent': payment_intent})


def checkout(request):
    """
        Отображает страницу оформления заказа, на которой пользователь может выбрать товары для покупки.
        Параметры:
            - request: HttpRequest объект

        Возвращает HttpResponse объект со страницей оформления заказа.
        """
    items = Item.objects.all()
    return render(request, 'checkout.html', {'items': items})


def success(request):
    """
        Отображает страницу успешной оплаты.
        Параметры:
            - request: HttpRequest объект

        Возвращает HttpResponse объект со страницей успешной оплаты.
        """
    return render(request, 'success.html')


def cancel(request):
    """
        Отображает страницу отмены оплаты.
        Параметры:
            - request: HttpRequest объект

        Возвращает HttpResponse объект со страницей отмены оплаты.
        """
    return render(request, 'cancel.html')


def item(request, item_pk):
    """
        Отображает страницу товара с указанным primary key.
        Параметры:
            - request: HttpRequest объект
            - item_pk: int, primary key товара

        Возвращает HttpResponse объект со страницей товара.
        """
    item = get_object_or_404(Item, pk=item_pk)
    return render(
        request, 'item.html', {
            'item': item, "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY})


def create_order(request):
    """
       Создает новый заказ на основе выбранных товаров и сохраняет его в базу данных.
       Параметры:
           - request: HttpRequest объект

       Возвращает JsonResponse объект со значением order_id созданного заказа.
       """
    selected_item_ids = (request.POST['selectedItems']).split(',')
    try:
        if (request.POST['selectedItems']):
            items = Item.objects.filter(pk__in=selected_item_ids)
            currencies = set(item.currency for item in items)
            if len(currencies) > 1:
                return JsonResponse(
                    {'error_message': 'Выбранные продукты используют разные валюты'}, status=422)

            total_price = sum(item.price for item in items)
            discounted_price = sum(item.discounted_price() for item in items)

            order = Order(
                total_price=total_price,
                discounted_price=discounted_price)
            order.save()
            order.items.set(items)

            return JsonResponse({'order_id': order.pk})
        else:
            return JsonResponse(
                {'error_message': "Выберите продукты для создания заказа"}, status=422)
    except ValueError as e:
        return JsonResponse({'error_message': e}, status=500)


def get_order(request, order_pk):
    """
        Отображает страницу заказа с указанным primary key.
        Параметры:
            - request: HttpRequest объект
            - order_pk: int, primary key заказа

        Возвращает HttpResponse объект со страницей заказа.
        """
    order = get_object_or_404(Order, pk=order_pk)
    total_price = 0
    for item in order.items.all():
        total_price += item.total()
    context = {
        'items': order.items.all(),
        'amount': int(order.total_price / 100),
        'total': total_price,
        'order': order,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'order.html', context)
