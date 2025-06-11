from django.core.mail import send_mail
from inventory.models import Product
from .model import train_model

def check_and_alert():
    alerts = []
    for product in Product.objects.all():
        model, df = train_model(product.sub_category)
        future_day = df['Days'].max() + 1
        forecasted_qty = model.predict([[future_day]])[0]
        if forecasted_qty < product.restock_threshold:
            alerts.append((product.name, forecasted_qty))
            send_mail(
                subject=f'Restock Alert for {product.name}',
                message=f'Forecasted quantity for tomorrow is {forecasted_qty:.2f}. Please restock!',
                from_email='nischalchy15@gmail.com',
                recipient_list=['nischalchy19@gmail.com']
            )
    return alerts
