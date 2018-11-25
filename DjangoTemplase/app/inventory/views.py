from django.shortcuts import render

# Create your views here.
def main_point(request):

    return render(request, "inventory/inventory.html")
