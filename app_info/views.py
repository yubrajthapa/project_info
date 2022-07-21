from django.shortcuts import render, redirect

# importing forms classes
from . forms import StudentDetailForm, StudentLoginForm
# importing models
from . models import StudentDetail

# Create your views here.
def user_dashboard(request):
    studentdetail = StudentDetailForm
    context={
        'welcm_msg': "Welcome to Information Tracker",
    }
    return render(request, "users/dashboard.html", context)

def user_profile(request,id):
    data = StudentDetail.objects.get(id=id)
    context = {
        'db_data':data
    }
    return render(request, 'users/profile.html',context)

def user_edit(request,id):
    data = StudentDetail.objects.get(id=id)
    context = {
        'db_data' : data
    }
    if request.method == "POST":
        data.first_name = request.POST.get('first_name')
        data.middle_name = request.POST.get('middle_name')
        data.last_name = request.POST.get('last_name')
        data.email = request.POST.get('email')
        data.contact = request.POST.get('contact')
        data.save()
        context.setdefault('msg_success', "Updated Successfully")
        return render(request, 'users/profile.html',context)
    return render(request, "users/edit.html", context)

def user_login(request):
    login_form = StudentLoginForm()
    context = {
        'form' : login_form
    }
    if request.method == "POST":
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        try:
            std_data = StudentDetail.objects.get(email = req_email )
            if std_data.password == req_password:
                return render(request,"users/dashboard.html")
            else:
                context.setdefault("msg_error", "Invalid email or password!!")
                return render("users/login.html", context)

        except:
            context.setdefault("msg_error", "Invalid email or password!!")
            return render(request, "users/login.html", context)

    else:
        return render(request, "users/login.html", context)

def user_register(request):
    reg_form = StudentDetailForm()
    context = {
        'form' : reg_form
    }
    if request.method == "POST":
        #saving data using models
        std_detail = StudentDetail()
        std_detail.first_name = request.POST.get("first_name")
        std_detail.middle_name = request.POST.get("middle_name")
        std_detail.last_name = request.POST.get("last_name")
        std_detail.contact = request.POST.get("contact")
        std_detail.email = request.POST.get("email")
        std_detail.password = request.POST.get("password")
        std_detail.save()

    return render(request, "users/register.html", context)