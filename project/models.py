from django.db import models

class Project(models.Model):
    menage = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class AccountingItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.FloatField()
    def __str__(self):
        return self.name

class ItemInProject(models.Model):
    project = models.ForeignKey(Project)
    item = models.ForeignKey(AccountingItem)
    amount = models.IntegerField()
    date_debit = models.DateField()
    def __str__(self):
        return self.item.name + " in " + self.project.name

