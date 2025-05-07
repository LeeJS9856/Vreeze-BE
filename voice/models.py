from django.db import models

class Record(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    uuid = models.CharField(max_length=8, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.uuid}"
    

class Avatar(models.Model) :
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    uuid = models.CharField(max_length=8, unique=True, editable=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.uuid}"

