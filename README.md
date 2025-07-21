## This is a test package app in django
Mô phỏng lại chức năng của Signal trong Django, cụ thể là:

Trong signals.py:
```
from django.dispatch import Signal
payment_completed = Signal()
```
Trong services.py:
```
from .signals import payment_completed

def complete_payment(order_id, amount):
    print(f"App TEST_PACKAGE đã bắn đi tín hiệu Signal: Payment completed for order {order_id} with amount {amount}")

    # Send the signal after completing the payment
    payment_completed.send(sender=None, order_id=order_id, amount=amount)
```

Trong app ssr_views_tutorial hoặc bất kỳ app nào khác cùng hệ thống, có thể nhận Signal trên từ test_package_app. Bằng cách:

```
from test_package_app.signals import payment_completed
@receiver(payment_completed)
def payment_completed_handler(sender, **kwargs):
    order_id = kwargs.get('order_id')
    amount = kwargs.get('amount')
    print_log(f"App SSR_VIEWS đã nhận được Signal từ app TEST_PACKAGE: Payment completed signal received for order {order_id} with amount {amount}")
    # Additional logic can be added here if needed
    # For example, updating order status, sending notifications, etc.
    # This is just a placeholder for demonstration purposes.
    # You can also access the sender if needed: sender
    print(f"Sender: {sender}")
```
