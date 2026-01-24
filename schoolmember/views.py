from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from schoolmember.models import SchoolMember

# Class Base View Here

# Member View class Here
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
    
# Member Details View Here
class MemberDetailView(DetailView):
    template_name = "memberdetails.html"
    model = SchoolMember
    context_object_name = 'member'
    
# Member Add View Here
class MemberCreateView(CreateView):
    template_name = "memberinput.html"
    model = SchoolMember
    fields = ["member_type", "memberName", "memberDesignation", "memberDepartment", "memberEmail", "memberPhone", "memberImage"]
    success_url = reverse_lazy("members")
    
# Member Edit/ Update View Here
class MemberUpdateView(UpdateView):
    template_name = "memberinput.html"
    model = SchoolMember
    fields = ["member_type", "memberName", "memberDesignation", "memberDepartment", "memberEmail", "memberPhone", "memberImage"]
    success_url = reverse_lazy("members")
    
# Member Delete View Here
class MemberDeleteView(DeleteView):
    template_name = "memberdelete.html"
    model = SchoolMember
    context_object_name = 'member'
    success_url = reverse_lazy("members")


# Function Base views here.
# def memberLists(request):
#     # Start With all Notice
#     members = SchoolMember.objects.all()    
#     return render (request, 'member.html', {"members": members})
