from django.db import models

# All User Create models here.

# Catagory Models Here
class Catagory(models.Model):
    catagoryName = models.CharField(max_length=100)
    
    # Notice database a Data Show er Code
    def __str__(self):
        return self.catagoryName

class Notice(models.Model):
    noticeID = models.IntegerField(max_length=1000)
    noticeTitle = models.CharField(max_length=256)
    noticeDescription = models.TextField()
    noticeCatagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    noticeCreate = models.DateTimeField(auto_now_add=True)
    noticeImage = models.ImageField(upload_to="notice/images/", blank=True, null=True)
    
