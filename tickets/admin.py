from adminlte2_pdq.admin_menu import AdminMenu
from django.contrib import admin
from .models import Project, Ticket

# Register Ticket models and change ALTE icons
admin.site.register(Project)
AdminMenu.set_model_icon("Project", "fa fa-archive")

admin.site.register(Ticket)
AdminMenu.set_model_icon("Tickets", "fa fa-ticket")

AdminMenu.set_app_icon("Tickets", "fa fa-certificate")

# Set icons for built in user Auth
AdminMenu.set_model_icon("Group", "fa fa-users")
AdminMenu.set_model_icon("User", "fa fa-user")
AdminMenu.set_app_icon("Authentication and Authorization", "fa fa-user-o")
