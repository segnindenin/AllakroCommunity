from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

lieux = [
    ('Entre_Village', 'Entre du Village'),
    ('Sortie_Village', 'Sortie du Village'),
    ('Arbe_Palabre', 'Arbe Palabre'),
    ('Centre_Village', 'Centre du Village'),
    ]
recensement = [
    ('inscription', 'inscription'),
    ('amenagement', 'amenagement'),
    ('demenagement', 'demenagement'),
    ('naissance', 'naissance'),
    ('deces', 'deces'),
    ]
metier = [
    ('Mecanicien', 'Mecanicien'),
    ('maçon', 'maçon'),
    ('menusier', 'menusier'),
    ('plombier', 'plombier'),
    ('etudiant', 'etudiant'),
    ('Autre', 'Autre'),
    ]
Pieces = [
    ('Cart_National_Identity', 'CNI'),
    ('Extrait_Naissance', 'EN'),
    ('Attestation_Identity', 'AI'),
    ('Carte_Etudiant', 'CE'),
    ('Autre', 'Autre'),
    ]
Pays = [
    ('Ivorycoast', 'ivoirien'),
    ('Mali', 'malien'),
    ('BurkinaFaso', 'burkinabè'),
    ('Ghana', 'ghanaeen'),
    ('Benin', 'beninois'),
    ('Autre', 'autre'),
    ]
Diplome= [
    ('M3eme', 'M3eme'),
    ('BEPC', 'BEPC'),
    ('BAC', 'BAC'),
    ('LICENCE', 'LICENCE'),
    ('MASTER', 'MASTER'),
    ('DOCTORAT', 'DOCTORAT'),
    ('Autre', 'Autre'),
    ]
Matrimonal= [
    ('Marié', 'Marié'),
    ('Celibataire', 'Celibataire'),
    ('Divorcé', 'Divorcé'),
    ]
categories = [
    ('HealthCenter', 'Health Center'),
    ('CommercialCenter', 'Commercial Center'),
    ('AutoriteVillage', 'Autorite Village'),
    ('WorkCommunity', 'Work Community'),
    ]
type_maladie = [
    ('Paludisme', 'Paludisme'),
    ('FièvreTyphoide', 'Fièvre Typhoide'),
    ('COVID19', 'COVID19'),
    ('Autre', 'Autre'),
    ]

class ReferentielMetier(models.Model):
    work_name = models.CharField(max_length=20, choices=metier)
    def __str__(self):
        return f'{self.work_name}'


class Habitant(models.Model):
    type_recensement = models.CharField(choices=recensement, max_length=20)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    nationality = models.CharField(choices=Pays, max_length=20)
    type_piece = models.fields.CharField(choices=Pieces, max_length=25)
    piece_number = models.CharField(max_length=20, null=True)
    marital_status = models.fields.CharField(choices=Matrimonal, max_length=20)
    contact = models.CharField(max_length=50, null=True)
    level_studies = models.fields.CharField(choices=Diplome, max_length=20)
    read_ability = models.BooleanField()
    installation_date = models.DateField()
    neighborhoodmove = models.DateField(null=True, blank=True)
    birthdate = models.DateField()
    deathdate = models.DateField(null=True, blank=True)
    work_name = models.ManyToManyField(ReferentielMetier, related_name='travailleur', blank=True)
    work_space = models.CharField(max_length=20, choices=lieux, blank=True)
    def __str__(self):
        return f'{self.id} {self.firstname} {self.lastname}'
 
 
class Acteur(AbstractUser):
    ADMIN = 'ADMINISTRATEUR'
    CREATOR = 'RESPONSABLE'
    MEMBER = 'MEMBER'
    STATUT_CHOICES = (
        (ADMIN, 'Administrateurs'),
        (CREATOR, 'Responsables'),
        (MEMBER, 'Membres'),
    )
    statut = models.CharField(max_length=30, choices=STATUT_CHOICES, verbose_name='statut')
    HabitantID = models.OneToOneField(Habitant, null=True, on_delete=models.SET_NULL, related_name='utilisateur')
    def __str__(self):
        return f'{self.username}'


class Recensement(models.Model):
    type_recensement = models.CharField(choices=recensement, max_length=20)
    fullname = models.CharField(max_length=50, null=True)
    father_fullname = models.CharField(max_length=50, null=True)
    mother_fullname = models.CharField(max_length=50, null=True)
    sexe = models.CharField(max_length=20)
    work_name = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_space = models.CharField(max_length=50, blank=True)
    personal_home = models.CharField(max_length=50, blank=True)
    statut_recensement = models.CharField(max_length=20, 
    choices=[
        ('validated', 'validated'),
        ('refused', 'refused'),
        ('waiting', 'waiting'),
        ], 
        blank=True)
    def __str__(self):
        return f'{self.id} {self.type_recensement} {self.fullname}'


class Service(models.Model):
    fullname = models.CharField(max_length=50, null=True)
    services = models.CharField(max_length=50, null=True)
    specificity = models.TextField(max_length=500, null=True)
    contact = models.CharField(max_length=50, null=True)
    photo = models.ImageField(null=True, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    work_space = models.CharField(max_length=20, blank=True)
    payement_code = models.CharField(max_length=20, blank=True)
    statut_recensement = models.CharField(max_length=20, 
    choices=[
        ('validated', 'validated'),
        ('refused', 'refused'),
        ('waiting', 'waiting'),
        ],
        blank=True)
    def __str__(self):
        return f'{self.id} {self.fullname} {self.services}'

class Communauty(models.Model):
    name = models.CharField(max_length=20)
    categorie = models.CharField(max_length=20, choices=categories)
    localisation = models.CharField(max_length=20, choices=lieux, null=True, blank=True)
    service = models.TextField(max_length=2000, null=True, blank=True)
    membreID = models.ManyToManyField(Acteur, related_name='membre', blank=True)
    def __str__(self):
        return f'{self.name}'
    

class Activity(models.Model):
    objet = models.CharField(max_length=20)
    publication = models.TextField(max_length=2000, null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    acteurID = models.ForeignKey(Acteur, null=True, on_delete=models.SET_NULL, related_name='publieur')
    communityID = models.ForeignKey(Communauty, null=True, on_delete=models.SET_NULL, related_name='name_communauty')
    def __str__(self):
        return f'{self.acteurID}: {self.publication}'


class CarnetSante(models.Model):
    acteurID = models.ForeignKey(Habitant, on_delete=models.SET_NULL, related_name='patient', null=True)
    disease_name = models.CharField(max_length=20, choices=type_maladie)
    temperature = models.IntegerField(null=True, blank=True)
    date_recorder = models.DateField()
    def __str__(self):
        return f'{self.acteurID} {self.disease_name} {self.date_recorder}'


class joboffer(models.Model):
    publieursID = models.ForeignKey(Acteur, null=True, on_delete=models.SET_NULL, related_name='publieurs')
    titre = models.CharField(max_length=20)
    description = models.TextField(max_length=2000, null=True, blank=True)
    nbre_person = models.IntegerField()
    Diplome_Requirement = models.CharField(max_length=20, choices=Diplome)
    date_Appel_Offre = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.titre}'


class Postulation(models.Model):
    postulerID = models.ForeignKey(Acteur, null=True, on_delete=models.SET_NULL, related_name='postuleur')
    offreID = models.ForeignKey(joboffer, null=True, on_delete=models.CASCADE)


class Projet(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    description = models.TextField(max_length=2000, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    communityID = models.ForeignKey(Communauty, null=True, on_delete=models.SET_NULL, related_name='chef_projet')
    def __str__(self):
        return f'{self.name} {Communauty.name}'
