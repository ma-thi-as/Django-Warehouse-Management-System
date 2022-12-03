from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UsuarioManager(BaseUserManager):
    def _create_user(self,nombre,apellido,rut,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            nombre = nombre,
            apellido = apellido, 
            rut = rut ,
            is_staff=True, 
            is_superuser= True,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,nombre,apellido,rut,password = None,**extra_fields):
        return self._create_user(nombre,apellido,rut,password,True,False,**extra_fields)

    def create_superuser(self,nombre,apellido,rut,password = None,**extra_fields):
        return self._create_user(nombre,apellido,rut,password,True,True,**extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField('Rut', max_length=9, unique= True, primary_key=True)
    class Cargo(models.TextChoices):
        ADMIN = 'ADMIN','Admin'
        OPERADOR = 'OPERADOR', 'Operador'
    cargo = models.CharField(_("Cargo"), max_length=30, choices=Cargo.choices, default=Cargo.ADMIN)
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField('Es miembro del staff',default= False)
    objects = UsuarioManager()
    history = HistoricalRecords()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    def save(self,*args, **kwargs):
        """
        Redifinición del metodo save
        """
        if not self.cargo:
            self.is_staff = False
        self.is_staff = True
        return super().save(*args,**kwargs)

    def __repr__ (self):
        return self.rut
        
    def __str__(self):
        return f'{self.nombre} {self.apellido}'



#Clases para la asignacion de cargo tanto superusers como usuarios staff.
class AdminManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        """Se realiza una consulta en base al padre usuario donde se le consulta cargo correspondiente"""
        return super().get_queryset(*args,**kwargs).filter(cargo = Usuario.Cargo.ADMIN)

class Admin(Usuario):
    objects = AdminManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        """Defincion metodo save de la clase Admin de tipo proxy(extendiente de Usuario).
    Si no tiene pk le decimos que self.cargo del modelo usuario , reciba el cargo correspondiente"""
        if not self.pk:
            self.cargo = Usuario.Cargo.ADMIN
        return super().save(*args,**kwargs)


class OperadorManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(cargo = Usuario.Cargo.OPERADOR)

class Operador(Usuario):
    objects = OperadorManager()
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.cargo = Usuario.Cargo.OPERADOR
        return super().save(*args,**kwargs)

