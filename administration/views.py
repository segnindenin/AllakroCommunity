from django.shortcuts import render, redirect
from exchange.models import Habitant, Recensement
from administration import models


def adminHome(request):
    return render(request, 'home.html')

def dynamism(request):
    page_request = request.GET.get('dynamism')
    recensement = models.Recensement.objects.filter(type_recensement=page_request)
    return render(request, 'dynamisme/dynamisme_liste.html', 
                  {'recensement':recensement,
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
    return render(request, 'projet/projet_form.html')

def projetUpdate(request, id):
    projet = models.Markaz.objects.get(id=id)
    if request.method == 'POST':
        projet.voir = request.POST.get('topic')
        projet.name = request.POST.get('name')
        projet.topic = request.POST.get('name')
        projet.description = request.POST.get('description')
        projet.save()
        return redirect('home')
    context = {'markaz': markaz}
    return render(request, 'base/room_form.html', context)

def markaz(request):
    page_request = request.GET.get('center')
    centers = Recensement.objects.filter(institut=page_request)
    return render(request, 'projet/center.html', {'centers':centers})

def markazForm(request):
    if request.method == 'POST':
        new_centre = models.Markaz.objects.create(
            institut=request.POST['institut'], 
            center_name=request.POST['center_name'], 
            place=request.POST['place'], 
            description=request.POST['description'], 
            )
    return render(request, 'projet/center_form.html')

def markazUpdate(request, id):
    markaz = models.Markaz.objects.get(id=id)
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        markaz.name = request.POST.get('name')
        markaz.topic = request.POST.get('name')
        markaz.description = request.POST.get('description')
        markaz.save()
        return redirect('home')
    context = {'markaz': markaz}
    return render(request, 'base/room_form.html', context)

def healthData(request):
    data = models.HealthData.objects.all()
    return render(request, 'sante/data_list.html', {'data':data})

def healthConsultation(request):
    if request.method == 'POST':
        fiche = models.HealthData.objects.create(
            patient_name=request.POST['patient_name'], 
            medecin=request.POST['medecin'], 
            constante=request.POST['constante'], 
            prescription=request.POST['prescription'], 
            diagnostique=request.POST['diagnostique'], 
            date=request.POST['date'], 
            )
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