from django.shortcuts import render
from orders.models import Order

def home(request):
    return render(request, "index.html")

def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        plan = request.POST.get("plan", "")
        Order.objects.create(name=name, phone=phone, plan=plan)
        return render(request, "checkout.html", {"success": True})
    return render(request, "checkout.html")