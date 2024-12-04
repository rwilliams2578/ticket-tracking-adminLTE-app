from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Project, Ticket


class ProjectListView(ListView):
    """Show list of projects"""

    model = Project
    template_name = "project_list.html"


class ProjectDetailView(DetailView):
    """Show open tickets for project"""

    model = Project
    template_name = "project_detail.html"


class ProjectDetailClosedView(DetailView):
    """Show closed tickets for project"""

    model = Project
    template_name = "project_detail_closed.html"


class ProjectCreateView(CreateView):
    """Create a new project"""

    model = Project
    template_name = "project_create.html"
    fields = [
        "name",
        "members",
    ]

    def get_success_url(self):
        """Return the location to redirect to on success"""
        messages.success(self.request, "Project Created Successfully")
        return reverse("project_list")


class ProjectEditView(UpdateView):
    """Create a new project"""

    model = Project
    template_name = "project_update.html"
    fields = [
        "name",
        "members",
    ]

    def get_success_url(self):
        """Return the location to redirect to on success"""
        messages.success(self.request, "Project Updated Successfully")
        return reverse("project_list")


class TicketCreateView(CreateView):
    """Create a new Ticket"""

    model = Ticket
    template_name = "ticket_create.html"
    fields = [
        "name",
        "description",
        "priority",
        "assigned_to",
        "completed_by",
        "completed",
    ]

    def get(self, request, project_pk, *args, **kwargs):
        """Handle GET Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def post(self, request, project_pk, *args, **kwargs):
        """Handle POST Request"""
        self.project_pk = project_pk
        return super().post(request, project_pk, *args, **kwargs)

    def get_context_data(self):
        """Add variables to the template context"""
        context = super().get_context_data()
        context["project"] = Project.objects.get(pk=self.project_pk)
        return context

    def form_valid(self, form):
        """Code to run when form is valid"""
        form.instance.project = Project.objects.get(pk=self.project_pk)
        return super().form_valid(form)

    def get_success_url(self):
        """Return the location to redirect to on success"""
        messages.success(self.request, "Ticket Created Successfully")
        return reverse("project_detail", kwargs={"pk": self.project_pk})


class TicketEditView(UpdateView):
    """Update a new Ticket"""

    model = Ticket
    template_name = "ticket_update.html"
    fields = [
        "name",
        "description",
        "priority",
        "assigned_to",
        "completed_by",
        "completed",
    ]

    def get(self, request, project_pk, *args, **kwargs):
        """Handle GET Request"""
        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)

    def post(self, request, project_pk, *args, **kwargs):
        """Handle POST Request"""
        self.project_pk = project_pk
        return super().post(request, project_pk, *args, **kwargs)

    def get_context_data(self):
        """Add variables to the template context"""
        context = super().get_context_data()
        context["project"] = Project.objects.get(pk=self.project_pk)
        return context

    def get_success_url(self):
        """Return the location to redirect to on success"""
        messages.success(self.request, "Ticket Updated Successfully")
        return reverse("project_detail", kwargs={"pk": self.project_pk})
