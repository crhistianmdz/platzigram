#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.options import BaseModelAdmin

#models
from django.contrib.auth.models import User
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone','website','picture')
    search_fields=('user__email','user__name','user__first_name','user__last_name','phone')
    list_filter=('user__is_active','user__is_staff','created','modified')
    fieldsets=(#esta variable recibe una tupla como primer parametro
        ('Profile',{#como segundo parametro una diccionario
            'fields':(#el valor asignado al diccionario es una tupla
                ('user','picture'),#se puede asignar tuplas anidadas para que se visualisen en la misma linea
            ),
        }),
        ('Extra info',{
            'fields':(
                ('website','phone'),
                ('biography'),
            ),
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),
            ),
        }),
    )
    readonly_fields=('created','modified','user')

#proceso para crear el profile desde la creacion del user en el admin de django
class ProfileInline(admin.StackedInline):#declara el modelo que sera asignado al modelo de user de django
    model = Profile
    can_delete=False
    verbose_name_plural='Profiles'


class UserAdmin(BaseUserAdmin):#esta clase hereda de modelo de UserAdmin de django y se le asigna el modelo que se usara en el mismo template
    inlines=(ProfileInline,)
    list_display=('username','email','first_name','last_name','is_active','is_staff')

admin.site.unregister(User)#sacamos del registro de la app el modelo estandar
admin.site.register(User,UserAdmin)#registramos el modelo con la herencia del profile 