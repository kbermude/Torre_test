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