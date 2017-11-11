from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name,
                                                                                               order.id)
    mail_sent = send_mail(subject, message, 'admin@food-pantry.com', [order.email])
    return mail_sent


# May want to add this to the settings.py file if we don't add email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Unable to start the celery worker, see page 245, code to be executed in the command shell
# celery -A myshop worker -l info
# celery -A myshop flower