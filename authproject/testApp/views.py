from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect
from testApp.models import quiz
def home_page_view(request):
    return render(request,'testApp/home.html')
@login_required
def java_page_view(request):
    equiz=quiz.objects.all()
    return render(request,'testApp/javaexams.html',{'quiz':equiz})
@login_required
def python_page_view(request):
    return render(request,'testApp/pythonexams.html')
@login_required
def Aptitude_page_view(request):
    return render(request,'testApp/aptitudeexams.html')
def logout_view(request):
    return render(request,'testApp/logout.html')
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')




    return render(request,'testApp/signup.html',{'form':form})

@login_required
def result(request):
    score = 0
    ques = quiz.objects.all()
    for i in ques:
        userans = request.POST.get(i.question)
        if userans == i.answer:
            score += 1
            print('score',score)
    return render(request,'testApp/result.html',{'score':score})
