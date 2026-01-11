from django.db import models

# School Member Model Here
class SchoolMember(models.Model):
    MEMBER_TYPE = (
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )
    
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE)
    memberName = models.CharField(max_length=200)
    memberDesignation = models.CharField(max_length=200)
    memberDepartment = models.CharField(max_length=200)
    memberEmail = models.EmailField(unique=True)
    memberPhone = models.CharField(max_length=11)
    memberImage = models.ImageField(upload_to="schoolmember/images/", blank=True, null=True)
    memberApprove = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.memberName