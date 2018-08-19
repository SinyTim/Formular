from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail

from .models import Post
from .models import Client
from .forms import EmailForm


def home(request):
    return render(request, 'mainApp/home.html')


def posts_list(request, page_num=1):
    list = Post.objects.order_by('-date')
    paginator = Paginator(list, 3)
    posts = paginator.get_page(page_num)
    return render(request, 'mainApp/posts_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'mainApp/post_detail.html', {'post': post})


def clients(request):
    clients = Client.objects.all()
    return render(request, 'mainApp/clients.html', {'clients': clients})


def contacts(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']
            send_email(sender, subject, message, cc_myself)
            return redirect('mainApp:contacts')
    else:
        form = EmailForm()
    return render(request, 'mainApp/contacts.html', {'form': form})


def send_email(sender, subject, message, cc_myself):
    recipients = ['sintim@mail.ru']
    if cc_myself:
        recipients.append(sender)
    message += '\n\n-----\n\n'
    message += 'From: ' + sender + '\n'
    message += 'To: ' + recipients[0]
    send_mail(subject, message, sender, recipients)
