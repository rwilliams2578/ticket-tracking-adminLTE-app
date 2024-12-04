from django.db import models

# Choices for the Priority field on the Ticket Model
PRIORITY_CHOICES = (
    (1, "Expedite"),
    (2, "High"),
    (3, "Medium"),
    (4, "Low"),
    (5, "None"),
)


class Project(models.Model):
    """Represents a single project"""

    name = models.CharField(max_length=200)
    members = models.ManyToManyField("auth.User")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """String conversion"""
        return self.name

    def open_tickets(self):
        """Get open tickets"""
        return self.tickets.filter(completed=False)

    def closed_tickets(self):
        """Get closed tickets"""
        return self.tickets.filter(completed=True)

    def expedite_priority_tickets(self):
        """Get tickets with expedite priority"""
        return self.tickets.filter(priority=1, completed=False)

    def high_priority_tickets(self):
        """Get tickets with high priority"""
        return self.tickets.filter(priority=2, completed=False)

    def medium_priority_tickets(self):
        """Get tickets with medium priority"""
        return self.tickets.filter(priority=3, completed=False)

    def low_priority_tickets(self):
        """Get tickets with low priority"""
        return self.tickets.filter(priority=4, completed=False)

    def no_priority_tickets(self):
        """Get tickets with no priority"""
        return self.tickets.filter(priority=5, completed=False)


class Ticket(models.Model):
    """Represents a ticket for a project"""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    assigned_to = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="tickets",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    completed_by = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """String conversion"""
        return f"{self.project} - {self.name}"
