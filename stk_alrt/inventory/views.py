from django.shortcuts import render
from .utils.model import train_model
from datetime import datetime, timedelta
from django.http import HttpResponse
def forecast_view(request):
    try:
        sub_category = request.GET.get('product', 'Phones')
        model, df = train_model(sub_category)
        last_day = df['Days'].max()
        future_days = [int(last_day + i) for i in range(1, 31)]  # Convert to int
        predictions = model.predict([[day] for day in future_days])
        
        context = {
            'labels': [(df['Order Date'].min() + timedelta(days=int(day))).strftime("%Y-%m-%d") for day in future_days],  # Convert to int
            'data': [round(val) for val in predictions],
            'product': sub_category,
        }
        return render(request, 'inventory/dashboard.html', context)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)