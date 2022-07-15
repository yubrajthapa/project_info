from django.shortcuts import render

# Create your views here.
def user_dashboard(request):
    context={
        'welcom_msg': "Welcome to Information Tracker"
    }
    return render(request, "users/dashboard.html", context)