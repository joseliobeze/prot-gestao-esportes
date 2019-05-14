from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Index(request):
	template_name = 'system/index.html'
	return render(request, template_name)