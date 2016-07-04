from django.shortcuts import render_to_response, redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from django_base.sensitive import CONTACT_FORM_TARGET
from django_base.sensitive import LINKEDIN_URL
from django_base.sensitive import TWITTER_URL
from django_base.sensitive import GITHUB_URL

from django_base.sensitive import BLOGGER_URL
from django_base.sensitive import BLOGGER_ATOM_URL


# Create your views here.


def send_contact_mail(name, message, email):
    """Sends an e-mail submitted through the contact form."""
    send_mail("Website Contact Form Submission",
              "From: " + name + "\n" + message, email, [CONTACT_FORM_TARGET])


def index(request):
    """Home page"""
    return render_to_response('frontend/index.html', locals())


def blog(request):
    """Blog page

    I couldn't be bothered with all the write-your-own-blog-engine stuff this
    time around because I'm not that good with Python. Instead there's a little
    CoffeeScript thingy that hooks into Google Blogger and just mirrors that
    stuff here.
    """
    return render(request, 'frontend/blog.html',
                  {'blogger_url': BLOGGER_URL, 'blogger_atom_url': BLOGGER_ATOM_URL})


def contact(request):
    """Contact page

    The only real python code block on this entire website.
    """

    errors = []
    if request.POST:
        try:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            if len(name) < 2:
                errors.append('The name you provide needs to 2 or more characters in length.')
            if len(message) < 30:
                errors.append('The message you submit needs to be 30 or more characters in length.')
            validate_email(email)
            if len(errors) == 0:
                send_contact_mail(name, message, email)
        except ValidationError:
            errors.append('The email address you provided is invalid.')
    return render(request, 'frontend/contact.html',
                  {'success': len(errors) == 0, 'errors': errors, 'post': request.POST})


# Social

def linkedin(request):
    """Redirects to configured LinkedIn URL."""
    return redirect(LINKEDIN_URL)


def twitter(request):
    """Redirects to configured Twitter URL."""
    return redirect(TWITTER_URL)


def github(request):
    """Redirects to configured GitHub URL."""
    return redirect(GITHUB_URL)


# Projects

def project_1(request):
    """First project page"""
    return render_to_response('frontend/project-1.html', locals())


def project_2(request):
    """Second project page"""
    return render_to_response('frontend/project-2.html', locals())


def project_3(request):
    """Third project page"""
    return render_to_response('frontend/project-3.html', locals())
