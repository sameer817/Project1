from django.contrib import admin
from testapp.models import ContactModel, GenerateTextmodel, EmailModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'comment')




class GenerateTextmodelAdmin(admin.ModelAdmin):
    list_display = ('id','Name', 'Text')


class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'From', 'To', 'Subject', 'Message')



admin.site.register(ContactModel, ContactAdmin)
admin.site.register(GenerateTextmodel, GenerateTextmodelAdmin)
admin.site.register(EmailModel, EmailModelAdmin)
