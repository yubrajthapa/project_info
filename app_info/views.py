from django.shortcuts import render

# Create your views here.
def user_dashboard(request):
    return render(request, "users/dashboard.html")