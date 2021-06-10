from django.db import models

OPPORTUNITY_LIST = (('Internships', 'Internships'),('Employee', 'Employee'),('Freelancer', 'Freelancer'))

class Opportunity(models.Model):
    title       = models.CharField(max_length=120)
    code        = models.CharField(max_length=120)
    opportunity = models.CharField(max_length=120, default='Employee', choices=OPPORTUNITY_LIST)
    company     = models.ForeignKey('Company', on_delete=models.CASCADE)
    remote      = models.BooleanField(default=True)
    location    = models.CharField(max_length=120, null=True, blank=True)
    salary      = models.CharField(max_length=120, null=True, blank=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

class Job:
    def __init__(self, title, code, opportunity, companies, remote, locations, salary):
        self.title      = title
        self.code       = code
        self.opportunity= opportunity
        self.companies  = companies
        self.remote     = remote
        self.locations  = locations
        self.salary     = salary

class Salary:
    def __init__(self, code=None, currency=None, min_amount=None, max_amount=None, periodicity=None, visible=None):
        self.code       = code
        self.currency   = currency
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.periodicity= periodicity
        self.visible    = visible

class Company(models.Model):
    name    = models.CharField(max_length=120)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

