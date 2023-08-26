from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, timedelta
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from administration.models import Projects
from . import forms

# Create your views here.


def home(request):
    return render(request, 'exchange/authentification/home.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-home') 
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'exchange/authentification/connection.html', context={'error_message': error_message})

def registerPage(request):
    choix_statut = models.Acteur.STATUT_CHOICES
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # HabitantID = request.POST.get('HabitantID')
        statut = request.POST.get('statut')
        if not username or not password: # or not HabitantID :
            messages.error(request, 'Veuillez remplir tous les champs.')
            # return render(request, 'exchange/authentification/inscription.html')
        elif models.Acteur.objects.filter(username=username).exists():
            messages.error(request, 'Cet utilisateur existe déjà.')
            # return render(request, 'registration/register.html')
        else:
            # try:
            # habitant = models.Habitant.objects.get(id=HabitantID) 
            user = get_user_model().objects.create_user(username=username, password=password, statut=statut)
            messages.success(request, 'Utilisateur enregistré avec succès.')
            # login(request, user)
            # return redirect('home')
            # except models.Habitant.DoesNotExist:
            #     messages.error(request, 'Habitant non trouvé.')
    return render(request, 'exchange/authentification/inscription.html', context={'choix_statut': choix_statut})

def recensementForm(request):
    page = request.GET.get('type_recensement')
    if request.method == 'POST':
        new_recensement = models.Recensement.objects.create(
            type_recensement=page, 
            statut_recensement='waiting',
            fullname=request.POST['fullname'],
            father_fullname=request.POST['father_fullname'], 
            mother_fullname=request.POST['mother_fullname'], 
            sexe=request.POST['sexe'], 
            work_name=request.POST['work_name'], 
            birth_date=request.POST['birth_date'], 
            event_date=request.POST['event_date'], 
            event_space=request.POST['event_space'], 
            personal_home=request.POST['personal_home'],)
        messages.success(request, "Le formulaire a été soumis avec succès.")
    return render(request, f'exchange/recensement/{page}.html')

def recensementWait(request):
    cencus_request = models.Recensement.objects.filter(statut_recensement='waiting')
    prestation_request = models.Service.objects.filter(statut_recensement='waiting')
    return render(request, 'exchange/communaute/community_detail.html',
            {
            'cencus_request':cencus_request, 
            'prestation_request':prestation_request,
            })

def recensementValidation(request, id):
    services = request.GET.get('services')
    if services:
        demande = models.Service.objects.get(id=id)
    else:
        demande = models.Recensement.objects.get(id=id)
    demande.statut_recensement = 'validated'
    demande.save()
    return redirect('recensement-validation')

def recensementDenied(request, id):
    services = request.GET.get('services')
    if services:
        demande = models.Service.objects.get(id=id)
    else:
        demande = models.Recensement.objects.get(id=id)
    demande.delete()
    return redirect('recensement-validation')

def notification(request):
    nbre_waiting = (models.Recensement.objects.filter(statut_recensement='waiting').count() 
                  + models.Service.objects.filter(statut_recensement='waiting').count())
    data = {'nbre_waiting': nbre_waiting}
    return JsonResponse(data)

def prestationForm(request):
    if request.method == 'POST':
        new_prestation = models.Service.objects.create(
            statut_recensement='waiting', 
            fullname=request.POST['fullname'], 
            services=request.POST['services'], 
            specificity=request.POST['specificity'], 
            contact=request.POST['contact'], 
            work_space=request.POST['work_space'], 
            payement_code=request.POST['payement_code'],
            photo=request.FILES.get('photo'),
            )
        messages.success(request, "Le formulaire a été soumis avec succès.")
    return render(request, 'exchange/emplois/postulate.html')

def prestationRom(request):
    #pour les 7jrs
    today = datetime.now().date()
    one_week_ago = today - timedelta(days=7)
    prestations = models.Service.objects.filter(pub_date__gte=one_week_ago)
    #pour les 7jrs
    prestations = models.Service.objects.filter(statut_recensement='validated') 
    return render(request, 'exchange/emplois/prestataire.html', context={'prestations': prestations})

def newsFile(request):
    #pour les 7jrs
    today = datetime.now().date()
    one_week_ago = today - timedelta(days=7)
    publications = models.Recensement.objects.filter(event_date__gte=one_week_ago)
    prestations = models.Service.objects.filter(pub_date__gte=one_week_ago)
    #pour les 7jrs
    publications = models.Recensement.objects.filter(statut_recensement='validated') 
    prestations = models.Service.objects.filter(statut_recensement='validated') 
    return render(request, 'exchange/communaute/actuality.html', 
                  context={
                    'publications': publications,
                    'prestations':prestations})

def healthRoom(request):
    pjts = models.Projet.objects.all()
    return render(request, 'exchange/sante/centre_sante.html', context={'pjts': pjts})


def projectsRoom(request):
    projets = Projects.objects.all()
    return render(request, 'exchange/projet/projet_list.html', context={'projets': projets})

def centerInterest(request):
    publications = models.Activity.objects.all()
    return render(request, 'exchange/center_interest.html', context={'publications': publications})

def Posts(request):
    page = 'page_post'
    form = forms.ActivityForm()
    if request.method == 'POST':
        form = forms.ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center-interest')
    return render(request, 'exchange/center_interest.html', context={'form': form, 'page':page})

def Community(request):
    page = 'liste'
    categorie_filter = request.GET.get('categorie')
    if categorie_filter:
        listeC = models.Communauty.objects.filter(categorie=categorie_filter)
    else:
        listeC = models.Communauty.objects.all()
    return render(request, 'exchange/pct_causes.html', context={'listeC': listeC, 'page':page})

def Health(request):
    return render(request, 'exchange/pct_causes.html')

def romHealth(request):
    page = 'Health'
    bulletins = models.CarnetSante.objects.all()
    return render(request, 'exchange/pct_causes.html', context={'page':page, 'bulletins':bulletins})

def consultationHealth(request):
    form = forms.CarnetSanteForm()
    if request.method == 'POST':
        form = forms.CarnetSanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rom-health')
    return render(request, 'exchange/list_health.html', context={'form':form})

def createCommunity(request):
    form = forms.CommunautyForm()
    if request.method == 'POST':
        form = forms.CommunautyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')
    return render(request, 'exchange/community.html', context={'form': form})        

def buisnessSpace(request):
    page = 'liste'
    categorie_filter = request.GET.get('categorie')
    if categorie_filter:
        listeCo = models.Communauty.objects.filter(categorie=categorie_filter)
        listeof = models.joboffer.objects.filter
    else:
        listeCo = models.Communauty.objects.all()
    return render(request, 'exchange/buisness_space.html', context={'listeCo': listeCo, 'listeof':listeof, 'page':page})

def jobOffer(request):
    form = forms.jobofferForm()
    if request.method == 'POST':
        form = forms.jobofferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job-offer')
    return render(request, 'exchange/buisness_space.html', context={'form': form})

def infoPage(request):
    projets = models.Projet.objects.all()
    centre_sanitaire = models.Projet.objects.all()
    return render(request, 'exchange/info-page.html', context={'projets': projets, 'centre_sanitaire': centre_sanitaire})

def createProjects(request):
    page = 'page_create_pjt'
    form = forms.ProjetForm()
    if request.method == 'POST':
        form = forms.ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'exchange/projects.html', context={'form': form, 'page':page})