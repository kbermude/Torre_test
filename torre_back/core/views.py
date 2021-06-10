from django.shortcuts import render

from .models import Opportunity, Job, Salary, Company

def opportunity(request):    
	return render(request,'opportunity.html')