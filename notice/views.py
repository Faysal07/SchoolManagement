from django.shortcuts import render
from .models import Notice

# Q Import Here
from django.db.models import Q

# Create your views here.
def noticeLists(request):
    
    # Start With all Notice
    notices = Notice.objects.all()
    
    # Search Functionality
    search_quary = request.GET.get('search', '')
    if search_quary:
        notices = notices.filter(
            Q(noticeTitle__icontains=search_quary) |
            Q(noticeCatagory__catagoryName__icontains=search_quary)
        )
    
    # #Filter by Title
    # title_filter = request.GET.get('title', '')
    # if title_filter:
    #     notices = notices.filter(noticeTitle = title_filter)
    
    
    # return render (request, 'notice.html', {"notices": notices})

    return render(request, 'notice.html', {
        "notices": notices,
        "search_quary": search_quary
    })
    