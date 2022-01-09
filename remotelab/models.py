from django.db import models

# Create your models here.

class RemoteLab(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)  #user tablosuna atıf,işaret // on delete ile ilgili authorun tüm girdileri silinir
    title = models.CharField(max_length=50) #title max is 50
    content = models.TextField() #içerik alanı
    created_date = models.DateField(auto_now_add=True)
    acInput1 = models.FloatField("acInput1", default=0,blank=True)
    dcInput1 = models.IntegerField("dcInput1", default=0,blank=True)
    dcInput2 = models.IntegerField("dcInput2", default=0,blank=True)
    Channel2 = models.CharField("Channel2",max_length=1, default="",blank=True)
    Channel1 = models.CharField("Channel1",max_length=2, default="",blank=True)
    PotValue = models.IntegerField("PotValue", default=0,blank=True)
    image = models.FileField(null=True, blank=True,verbose_name = "Add Image to Experiment")

    def __str__(self):
        return self.title



