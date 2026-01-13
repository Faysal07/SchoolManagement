from django.shortcuts import render

from django.views.generic import ListView

from schoolmember.models import SchoolMember

# Class Base View Here
class MemberListsView(ListView):
    template_name = "member.html"
    model = SchoolMember
    context_object_name = 'members'
    paginate_by = 3
    
    def get_queryset(self):
        # Get All Data in Query Set
        filterQuerySet = SchoolMember.objects.all()
        
        # Member Type Filter Option
        chooseMember = self.request.GET.get('type')
        
        if chooseMember:
            filterQuerySet = filterQuerySet.filter(member_type = chooseMember)
        
        return filterQuerySet


# Function Base views here.
# def memberLists(request):
#     # Start With all Notice
#     members = SchoolMember.objects.all()    
#     return render (request, 'member.html', {"members": members})
