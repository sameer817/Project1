from django.shortcuts import render
from testapp.forms import ContactForm, EmailForm, SignUpForm, GenerateTextmodelForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.models import GenerateTextmodel




def homeview(request):
    return render(request, 'testapp/home.html')


@login_required
def projectsview(request):
    return render(request, 'testapp/projects.html')


@login_required(login_url='/accounts/login/')
def aboutview(request):
    return render(request, 'testapp/aboutme.html')


@login_required
def contactview(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print('details saved successfully')
            return render(request, 'testapp/thanks.html')

    return render(request, 'testapp/contact.html', {'form':form})


@login_required
def EmailFormview(request):
    # post = get_object_or_404(post, id=id, status= 'published')
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['From']
            subject = form.cleaned_data['Subject']
            message = form.cleaned_data['Message']
            recipients = form.cleaned_data['To']
            receiver = [recipients,]

            send_mail(subject, message, sender, receiver, fail_silently = False)
            sent = True
        return render(request, 'testapp/thanks.html')


    return render(request, 'testapp/email.html', {'form' : form})


def SignUpFormview(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()

        # user = form.save()
        # user.set_password(user.password)
        # user.save()
        return HttpResponseRedirect('/accounts/login/')


    return render(request, 'testapp/signup.html', {'form' : form})

from django.urls import reverse
@login_required
def GenerateTextmodelview(request):
    form = GenerateTextmodelForm()
    # import pdb;
    # pdb.set_trace()
    if request.method == 'POST':
        form = GenerateTextmodelForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print("Text data saved")
            return HttpResponseRedirect('/Text_Generator_view/')
    return render(request, 'testapp/text.html', {'form' : form})

def generate_Text_data_view(request):
    text_data = GenerateTextmodel.objects.all()
    return render(request, 'testapp/textview.html', {'text_data' : text_data})
