from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from . forms import UserRegForm, UserLoginForm,UserUpdateForm,PasswordChangeForm
from . models import User
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def Registration(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data['Firstname']
            lastname = form.cleaned_data['Lastname']
            gender = form.cleaned_data['Gender']
            address = form.cleaned_data['Address']
            email = form.cleaned_data['Email']
            photo = form.cleaned_data['Photo']
            place = form.cleaned_data['Place']
            phone = form.cleaned_data['Phone']
            village = form.cleaned_data['Village']
            district = form.cleaned_data['District']
            password = form.cleaned_data['Password']
            confirmpassword = form.cleaned_data['Confirmpassword']
            

            ur = User.objects.filter(Email=email).exists()

            if ur:
                msg="User with same email is already exist!"
                args={'form':form,'error':msg}
                return render(request,'app/registerpage.html',args)

            elif password!=confirmpassword:
                msg="Enter correct password! passwword mismatch"
                args={'form':form,'error':msg}
                return render(request,'app/registerpage.html',args)

            else:
                res=User(Firstname=firstname,Lastname=lastname,Gender=gender,Address=address,Email=email,Photo=photo,Place=place,
                            Phone=phone,Village=village,District=district,Password=password,Confirmpassword=confirmpassword)
                res.save()
                # messages.success("registration successfull")
                return redirect('/')
    else:
        form=UserRegForm()
    return render(request,'app/registerpage.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            try:
                ur = User.objects.get(Email=email)

               
                if not ur:
                    msg="Incorrect Email or password!"
                    args={'form':form,'error':msg}
                    return render(request,'app/user_login.html',args)

                elif password!=ur.Password:
                    msg="Incorrect Email or Password"
                    args={'form':form,'error':msg}
                    return render(request,'app/user_login.html',args)

                else:
                    request.session['email'] = email
                    request.session['sid'] = ur.id
                    request.session['logged_in'] = True
                    return redirect('/user_home/%s' % ur.id)
            except:
                msg = "Incorrect Email or password!"
                args = {'form': form,'error': msg}
                return render(request, 'app/user_login.html',args)
    else:
        form=UserLoginForm()
    return render(request,'app/user_login.html',{'form':form})

def user_home(request,id):
    if request.session.has_key:
        email = request.session['email']
        uid = request.session['sid']
        user = User.objects.get(id=id)
        ur = User.objects.get(Email=email) 
        return render(request, 'app/user_home.html', {'ur':ur, 'user':user})

# Create your views here.
def view_user_profile(request, id):
    email = request.session['email']
    user = User.objects.get(id=id)
    form = UserUpdateForm(request.POST,instance=user )
    if form.is_valid():
        firstname = form.cleaned_data['Firstname']
        lastname = form.cleaned_data['Lastname']
        gender = form.cleaned_data['Gender']
        address = form.cleaned_data['Address']
        email = form.cleaned_data['Email']
        photo = form.cleaned_data['Photo']
        place = form.cleaned_data['Place']
        phone = form.cleaned_data['Phone']
        village = form.cleaned_data['Village']
        district = form.cleaned_data['District']
        res = User(id=id, Firstname=firstname, Lastname=lastname, Gender=gender, Address=address, Email=email, Photo=photo, Place=place, Phone=phone, Village=village, District=district)
        res.save()
        messages.success(request, "Upadated successfully")
        return redirect('/user_home/%s' %id)
    return render(request,'app/view_user_profile.html',{'form':form,'user':user})


def logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('/index')

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/index")

def change_password(request, id):
    uid = request.session['sid']
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            oldpassword = form.cleaned_data['OldPassword']
            newpassword = form.cleaned_data['NewPassword']
            confirmpassword = form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                msg = "Enter Correct Password"
                return render(request, 'app/change_password.html', {'form':form, 'error':msg, 'user':user})
            elif newpassword!=confirmpassword:
                msg = "Password Does Not Match"
                return render(request, 'app/change_password.html', {'form':form, 'error':msg, 'user':user})
            else:
                user.Password = newpassword
                user.Confirmpassword = confirmpassword
                user.save()
                msg = "Password Changed Successfully"
                return redirect('/user_home/%s' %id)
                return render(request, 'app/change_password.html', {'form':form, 'error':msg, 'user':user})
    else :
        form = PasswordChangeForm()
    return render(request, 'app/change_password.html', {'form':form, 'user':user})





        

    