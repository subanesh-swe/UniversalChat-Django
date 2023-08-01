from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from . import forms

def userLogout(request):
    logout(request)
    return redirect('home')

def userLogin(request):
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            #print("username", username,"password", password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'result': True, 'redirect': '/messenger', 'alert': 'Login successful'})
            else:
                return JsonResponse({'result': False, 'redirect': '/users/login', 'alert': 'Invalid username or password'})
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]
            return JsonResponse({'result': False, 'redirect': '/users/login', 'alert': errors})
    else:
        form = forms.loginForm( request.POST)
    return render(request, 'users/login.html', {'form': form})

# method 1 (more optimized) :

def userSignup(request):
    if request.method == 'POST':
        #print("request.body:",request.body)
        #print("request.POST:",request.POST)
        form = forms.signupForm( request.POST )
        if form.is_valid():
            form.save()
            #print("form",form)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return JsonResponse({'result':True, 'redirect': '/users/login', 'alert': "Account created successfully"})
            #messages.success(request, f'Account created for {username}!')
            #return redirect('/messenger')
        else:
            #print("form.errors:",form.errors)
            #return JsonResponse({'result':False, 'alert': form.errors})
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]
            print("form.errors:",form.errors)
            return JsonResponse({'result':False, 'redirect': '/users/signup', 'alert': errors})
    else:
        form = forms.signupForm(request.POST)
    return render(request, 'users/signup.html', {'form': form})


# headers shouls be changed

#function formSubmitHandler(event, formId) {
#    event.preventDefault();
#    const formData = new FormData(document.getElementById(formId));
#    //console.log(JSON.stringify(Object.fromEntries(formData.entries())));
#    const data = Object.fromEntries(formData.entries());
#    console.log("posting data = " + JSON.stringify(data));
#    //fetch('/messenger/rooms', {
#    fetch(window.location.pathname, {
#        method: 'POST',
#        headers: {
#            'Content-Type': 'application/json',
#            'X-CSRFToken': csrfToken,
#        },
#        body: JSON.stringify(data)
#    })
#        .then(response => response.json())
#        .then(data => {
#            console.log("response data = " + JSON.stringify(data));
#            if (data.result === true) {
#                //alert(`Result : true -> ${JSON.stringify(data)}`);
#                window.location.href = data.redirect;
#            } else {
#                alert(data.alert);
#            }
#        })
#        .catch(error => {
#            alert("Something went wrong, Try again after sometime!!!");
#            console.error(error);
#        });
#}


##method 2 (own auth) (form handler is same as method 1):

#from django.shortcuts import render, redirect
#from django.contrib import messages
#from django.contrib.auth import authenticate, login
#from django.http import JsonResponse
#from django.contrib.auth.models import User
#import json

#def signup(request):
#    if request.method == 'POST':
#        received_json_data = json.loads(request.body)
#        username = received_json_data.get('username')
#        email = received_json_data.get('email')
#        password1 = received_json_data.get('password1')
#        password2 = received_json_data.get('password2')

#        returnData = {'result': True, 'redirect': '/messenger', 'alert': 'User created successfully!!!'}

#        if password1 != password2:
#            returnData.update({'result': False, 'redirect': '/users/signup', 'alert': 'Passwords do not match!!!'})

#        if User.objects.filter(username=username).exists():
#            returnData.update({'result': False, 'redirect': '/users/signup', 'alert': 'Username already taken!!!'})

#        if User.objects.filter(email=email).exists():
#            returnData.update({'result': False, 'redirect': '/users/signup', 'alert': 'Email already taken!!!'})
            
#        if returnData['result'] :
#            user = User.objects.create_user(username=username, email=email, password=password1)
#            user.save()
#            user = authenticate(request, username=username, password=password1)
#            login(request, user)

#        return JsonResponse(returnData)

#    else:
#        return render(request, 'users/signup.html')

## method 3 (default method) :

#def signup(request):
#    if request.method == 'POST':
#        print("request.POST:",request.POST)
#        form = forms.signupForm(request.POST)
#        if form.is_valid():
#            form.save()
#            #print("form",form)
#            #user = authenticate(request, username=username, password=password)
#            #login(request, user)
#            username = form.cleaned_data.get('username')
#            return JsonResponse({'result':True, 'alert': "Account created successfully"})
#            #messages.success(request, f'Account created for {username}!')
#            #return redirect('/messenger')
#        else:
#            print("form.errors:",form.errors)
#            #return JsonResponse({'result':False, 'alert': form.errors})
#            errors = {}
#            for field, error_list in form.errors.items():
#                errors[field] = error_list[0]
#            return JsonResponse({'result':False, 'alert': errors})
#    else:
#        form = forms.signupForm(request.POST)
#    return render(request, 'users/signup.html', {'form': form})


#function formSubmitHandler(event, formId) {
#    event.preventDefault();
#    const formData = new FormData(document.getElementById(formId));
#    console.log("posting data = " + JSON.stringify(formData));
#    fetch(window.location.pathname, {
#        method: 'POST',
#        headers: {
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'X-CSRFToken': csrfToken,
#        },
#        body: new URLSearchParams(formData).toString()
#    })
#        .then(response => response.json())
#        .then(data => {
#            console.log("response data = " + JSON.stringify(data));
#            if (data.result === true) {
#                //alert(`Result : true -> ${JSON.stringify(data)}`);
#                window.location.href = data.redirect;
#            } else {
#                alert(data.alert);
#            }
#        })
#        .catch(error => {
#            alert("Something went wrong, Try again after sometime!!!");
#            console.error(error);
#        });
#}