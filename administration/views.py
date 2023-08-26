from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from exchange.models import Habitant, Recensement, Service
from django.contrib import messages
from administration import models
from datetime import datetime


@login_required(login_url='login')
def adminHome(request):
    nbre_projet = (models.Projects.objects.all().count()) 
    nbre_prestataire = (Service.objects.all().count())
    nbre_news = (Recensement.objects.all().count())
    nbre_recensement = (Recensement.objects.all().count())
    return render(request, 'home.html', 
                {   
                'nbre_projet':nbre_projet,
                'nbre_news':nbre_news,
                'nbre_recensement':nbre_recensement,
                'nbre_prestataire':nbre_prestataire
                })

def dynamism(request):
    page_request = request.GET.get('dynamism')
    recensements = Recensement.objects.filter(type_recensement=page_request)
    return render(request, 'dynamisme/dynamisme_liste.html', 
                  {'recensements':recensements,
                   'page_request':page_request})

def demography(request):
    habitants=Habitant.objects.all()
    return render(request, 'demographie/demographie_liste.html', {'habitants':habitants})

def demographyUpdate(request):
    habitants=Habitant.objects.all()
    return render(request, 'demographie/demographie_update.html', {'habitants':habitants})

def project(request):
    projets = models.Projects.objects.all()
    return render(request, 'projet/projet_liste.html', {'projets':projets})

def projectDetail(request, id):
    projets = models.Projects.objects.get(id=id)
    return render(request, 'projet/projet_detail.html', {'projets':projets})

def projectForm(request):
    if request.method == 'POST':
        new_project = models.Projects.objects.create(
            project_name=request.POST['project_name'], 
            budget=request.POST['budget'], 
            state=request.POST['state'], 
            owner=request.POST['owner'], 
            description=request.POST['description'],
            )
        messages.success(request, "Le formulaire a été soumis avec succès.")
    return render(request, 'projet/projet_form.html')

def projetUpdate(request, id):
    projet = models.Projects.objects.get(id=id)
    if request.method == 'POST':
        projet.project_name = request.POST.get('project_name')
        projet.budget = request.POST.get('budget')
        projet.state = request.POST.get('state')
        projet.owner = request.POST.get('owner')
        projet.description = request.POST.get('description')
        projet.save()
        return redirect('project-list')
    context = {'projet': projet}
    return render(request, 'projet/projet_update.html', context)

def markaz(request):
    institut = request.GET.get('center')
    centers = models.Markaz.objects.filter(institut=institut)
    return render(request, 'center/center.html', {'centers':centers, 'institut':institut})

def markazForm(request):
    if request.method == 'POST':
        new_centre = models.Markaz.objects.create(
            institut=request.POST['institut'], 
            center_name=request.POST['center_name'], 
            place=request.POST['place'], 
            description=request.POST['description'], 
            )
        messages.success(request, "Le formulaire a été soumis avec succès.")
        
    return render(request, 'center/center_form.html')

def markazUpdate(request, id):
    markaz = models.Markaz.objects.get(id=id)
    if request.method == 'POST':
        # topic_name = request.POST.get('topic')
        markaz.name = request.POST.get('name')
        markaz.topic = request.POST.get('name')
        markaz.description = request.POST.get('description')
        markaz.save()
        return redirect('home')
    context = {'markaz': markaz}
    return render(request, 'base/room_form.html', context)

def healthData(request):
    datas = models.HealthData.objects.all()
    return render(request, 'sante/data_list.html', {'datas':datas})

def healthConsultation(request):
    if request.method == 'POST':
        fiche = models.HealthData.objects.create(
            patient_name=request.POST['patient_name'], 
            medecin=request.POST['medecin'], 
            constante=request.POST['constante'], 
            prescription=request.POST['prescription'], 
            diagnostique=request.POST['diagnostique'], 
            date=datetime.now(), 
            )
        messages.success(request, "Le formulaire a été soumis avec succès.")
    return render(request, 'sante/consultation_form.html')

def healthDataUpdate(request):
    data = models.HealthData.objects.all()
    if request.method == 'POST':
        data.patient = request.POST.get('topic')
        data.name = request.POST.get('name')
        data.topic = request.POST.get('name')
        data.description = request.POST.get('description')
        data.save()
        return redirect('home')
    return render(request, 'sante/data_list.html', {'data':data})

def prestationList(request):
    prestations = Service.objects.filter(statut_recensement='validated') 
    return render(request, 'service/prestataire.html', context={'prestations': prestations})