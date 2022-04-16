from itertools import chain

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from . import forms, models

# Create your views here.
"""
@login_required
def home(request):
    return render(request, 'cvblog/home.html')
"""


def accueil(request):
    cv = models.Cv.objects.filter(
        Q(usercv__is_superuser=True) & 
        Q(usercv__is_staff=True) ).order_by('-date_created')
    
    """
    lettre = models.Lettre.objects.filter(
        usercv=request.user)

    cv_and_lettre = sorted(
        chain(cv, lettre),
        key=lambda instance: instance.date_created,
        reverse=True
    )
    """

    #paginator = Paginator(cv_and_lettre, 6)
    paginator = Paginator(cv, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'cvblog/accueil.html', context=context)


def view_cv_admin(request, cv_id):
    cv = get_object_or_404(models.Cv, id=cv_id)
    return render(request, 'cvblog/view_cv_admin.html', {'cv': cv})


@login_required
def home(request):
    cv = models.Cv.objects.filter(
        Q(usercv=request.user))
    lettre = models.Lettre.objects.filter(
        usercv=request.user)

    cv_and_lettre = sorted(
        chain(cv, lettre),
        key=lambda instance: instance.date_created,
        reverse=True
    )
    paginator = Paginator(cv_and_lettre, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'cvblog/home.html', context=context)




@login_required
def cv_upload(request):
    form = forms.CvForm()
    if request.method == 'POST':
        form = forms.CvForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            # set the uploader to the user before saving the model
            cv.usercv = request.user
            # now we can save
            cv.save()
            return redirect('home')
    return render(request, 'cvblog/cv_upload.html', context={'form': form})

@login_required
def view_cv(request, cv_id):
    cv = get_object_or_404(models.Cv, id=cv_id)
    return render(request, 'cvblog/view_cv.html', {'cv': cv})

@login_required
def edit_cv(request, cv_id):
    cv = get_object_or_404(models.Cv, id=cv_id)
    edit_form = forms.CvForm(instance=cv)
    delete_form = forms.DeleteCvForm()
    if request.method == 'POST':
        if 'edit_cv' in request.POST:
            edit_form = forms.CvForm(request.POST, instance=cv)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_cv' in request.POST:
            delete_form = forms.DeleteCvForm(request.POST)
            if delete_form.is_valid():
                cv.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'cvblog/edit_cv.html', context=context)

@login_required
def lettre_upload(request):
    form = forms.LettreForm()
    if request.method == 'POST':
        form = forms.LettreForm(request.POST)
        if form.is_valid():
            print("yes")
            lettre = form.save(commit=False)
            # set the uploader to the user before saving the model
            lettre.usercv = request.user
            # now we can save
            lettre.save()
            return redirect('home')
        print("no")
    return render(request, 'cvblog/lettre_upload.html', context={'form': form})

@login_required
def view_lettre(request, lettre_id):
    lettre = get_object_or_404(models.Lettre, id=lettre_id)
    return render(request, 'cvblog/view_lettre.html', {'lettre': lettre})

@login_required
def edit_lettre(request, lettre_id):
    lettre = get_object_or_404(models.Lettre, id=lettre_id)
    edit_form = forms.LettreForm(instance=lettre)
    delete_form = forms.DeleteLettreForm()
    if request.method == 'POST':
        if 'edit_lettre' in request.POST:
            edit_form = forms.LettreForm(request.POST, instance=lettre)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_lettre' in request.POST:
            delete_form = forms.DeleteLettreForm(request.POST)
            if delete_form.is_valid():
                lettre.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'cvblog/edit_lettre.html', context=context)

@login_required
def cv_feed(request):
    cv = models.Cv.objects.filter(
        usercv=request.user).order_by('-date_created')
    paginator = Paginator(cv, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'cvblog/cv_feed.html', context=context)

@login_required
def lettre_feed(request):
    lettre = models.Lettre.objects.filter(
        usercv=request.user).order_by('-date_created')
    paginator = Paginator(lettre, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'cvblog/lettre_feed.html', context=context)


@login_required
def contact(request):
    contacts = models.Contact.objects.filter(
        Q(usercv=request.user) & Q(deactive=True)).order_by('-date_created')
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            # set the uploader to the user before saving the model
            contact.usercv = request.user
            contact.nomuser = request.user.username
            # now we can save
            contact.save()
            form = forms.ContactForm()
    
    paginator = Paginator(contacts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'contacts':contacts,
        'form': form,
    }

    return render(request, 'cvblog/contact.html', context)


@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(models.Contact, id=contact_id)
    contact_edit = models.Contact(
        nomuser = contact.nomuser,
        message = contact.message,
        usercv = contact.usercv,
        deactive = False,
        date_created = contact.date_created
         )
    edit_form = forms.ContactForm(instance=contact)
    delete_form = forms.DeleteContactForm()
    if request.method == 'POST':
        if 'edit_contact' in request.POST:
            edit_form = forms.ContactForm(request.POST, instance=contact)
            if edit_form.is_valid():
                contact_edit.save()
                edit_form.save()
                return redirect('contact')
        if 'delete_contact' in request.POST:
            delete_form = forms.DeleteContactForm(request.POST)
            if delete_form.is_valid():
                contact.deactive = False
                contact.save()
                #contact.delete()
                return redirect('contact')
    
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'cvblog/edit_lettre.html', context=context)




@login_required
def some_view_cv(request, cv_id):
    cv = get_object_or_404(models.Cv, id=cv_id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 825, "Nom : {}".format(cv.usercv.last_name))
    p.drawString(100, 800, "Prénom : {}".format(cv.usercv.first_name))
    p.drawString(100, 750, "Email : {}".format(cv.usercv.email))
    p.drawString(100, 700, "Date de Naissance : {}".format(cv.usercv.date_birth))
    p.drawString(100, 650, "Lieu de Naissance: {}".format(cv.usercv.place_birth))
    p.drawString(100, 600, "Sexe : {}".format(cv.sexe))
    p.drawString(100, 550, "Situation Matrimoniale : {}".format(cv.matrimoniale))
    p.drawString(100, 500, "Enfant: {}".format(cv.enfant))
    p.drawString(100, 450, "Telephone : {}".format(cv.telephone))
    p.drawString(100, 400, "Formation : {}".format(cv.formation))
    p.drawString(100, 350, "Competence : {}".format(cv.competence))
    p.drawString(100, 300, "Expérience Académique: {}".format(cv.experience_A))
    p.drawString(100, 250, "Expérience Proffesionnelle : {}".format(cv.experience_P))
    p.drawString(100, 200, "Langue : {}".format(cv.langue))
    p.drawString(100, 150, "Certifications : {}".format(cv.certifications))
    p.drawString(100, 100, "Reference : {}".format(cv.reference))
    p.drawString(100, 50, "Description : {}".format(cv.description))


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="{}.pdf".format(cv.nomcv))

@login_required
def some_view_lettre(request, lettre_id):
    lettre = get_object_or_404(models.Lettre, id=lettre_id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(400, 825, "{}, le {}".format(lettre.ville, lettre.date))
    p.drawString(10, 825, "Nom : {}".format(lettre.usercv.last_name))
    p.drawString(10, 800, "Prénom : {}".format(lettre.usercv.first_name))
    p.drawString(10, 775, "Email : {}".format(lettre.usercv.email))
    p.drawString(10, 750, "Profession : {}".format(lettre.profession))
    p.drawString(300, 650, "A Mr/Mme {}".format(lettre.destinateur))
    p.drawString(100, 600, "Objet : {}".format(lettre.objet))
    p.drawString(10, 550, "{}".format(lettre.lettre))
    p.drawString(10, 300, "Pièce jointe {}".format(lettre.jointe))



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="{}.pdf".format("lettre_motivation"))


