from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from . import forms

# Create your views here.


def home(request):
    return render(request, 'exchange/authentification/home.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après la connexion
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'exchange/authentification/connection.html', context={'error_message': error_message})

def registerPage(request):
    choix_statut = models.Acteur.STATUT_CHOICES
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        HabitantID = request.POST.get('HabitantID')
        statut = request.POST.get('statut')
        if not username or not HabitantID or not password:
            messages.error(request, 'Veuillez remplir tous les champs.')
            # return render(request, 'exchange/authentification/inscription.html')
        if models.Acteur.objects.filter(username=username).exists():
            messages.error(request, 'Cet utilisateur existe déjà.')
            # return render(request, 'registration/register.html')
        else:
            try:
                habitant = models.Habitant.objects.get(id=HabitantID) 
                user = models.Acteur.objects.create(username=username, HabitantID=habitant, password=password, statut=statut)
                messages.success(request, 'Utilisateur enregistré avec succès.')
                login(request, user)
                return redirect('home')
            except models.Habitant.DoesNotExist:
                messages.error(request, 'Habitant non trouvé.')
    return render(request, 'exchange/authentification/inscription.html', context={'choix_statut': choix_statut})

def census(request):
    context = {
    'choix_census' : models.recensement,
    'choix_nationality' : models.Pays,
    'choix_piece' : models.Pieces,
    'choix_marital' : models.Matrimonal,
    'choix_studies' : models.Diplome,
    'work_space' : models.lieux,
    'works' : models.ReferentielMetier.objects.all()
    }
    if request.method == 'POST':
        work_name_ids=request.POST.getlist('work_name')
        habitant = models.Habitant.objects.create(
            type_recensement=request.POST['type_recensement'], 
            firstname=request.POST['firstname'], 
            lastname=request.POST['lastname'], 
            nationality=request.POST['nationality'], 
            type_piece=request.POST['type_piece'], 
            piece_number=request.POST['piece_number'], 
            marital_status=request.POST['marital_status'], 
            contact=request.POST['contact'], 
            level_studies=request.POST['level_studies'], 
            read_ability=request.POST['read_ability'], 
            installation_date=request.POST['installation_date'], 
            neighborhoodmove=request.POST['neighborhoodmove'], 
            birthdate=request.POST['birthdate'], 
            deathdate=request.POST['deathdate'],  
            work_space=request.POST['work_space'],)
        habitant.work_name.set(work_name_ids)
        return redirect('home')
    return render(request, 'exchange/recensement/inscription.html', context)

def Projects(request):
    pjts = models.Projet.objects.all()
    return render(request, 'exchange/projet/projet_list.html', context={'pjts': pjts})

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

def newsFile(request):
    publications = models.Activity.objects.all()
    return render(request, 'exchange/news_file.html', context={'publications': publications})

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