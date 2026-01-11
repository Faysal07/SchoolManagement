from django.shortcuts import render

from schoolmember.models import SchoolMember

# Create your views here.
def memberLists(request):
    # Start With all Notice
    members = SchoolMember.objects.all()    
    return render (request, 'member.html', {"members": members})
