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


class Ticket(models.Model):
    """Represents a ticket for a project"""

    Project = models.ForeignKey(
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
