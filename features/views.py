from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.mail import EmailMessage

import re

from features.models import ContactUs


class FeaturesContactView(View):
    def post(self, request):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # Revenir plus tard sur la fonctionnalité envoie d'email
        send_mail = EmailMessage("Contact site admin", "Vôtre demande de contact a bien été envoyé", to=[email])
        
        if (
            name
            and not name.isspace()
            and subject
            and not subject.isspace()
            and message
            and not message.isspace()
            and re.fullmatch(regex, email)
        ):
            ContactUs.objects.create(name=name, subject=subject, email=email, message=message)
            return HttpResponse("", status=201)
        return HttpResponse(
            "Imposible de donner suite a vôtre requête, veuiller vérifier les données saisi", 
            status=405
        )
