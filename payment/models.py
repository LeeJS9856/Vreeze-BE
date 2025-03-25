from django.db import models

class Payment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    subscription = models.CharField(max_length=20) #구독권 종류
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.subscription}"
    