from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    userBalance  = models.DecimalField(max_digits=15,decimal_places=2, default=0.00)


    def __str__(self):
        return f"UserProfile-{self.user.username}-{self.user.id}"

    
    class Meta:
        verbose_name = "User Profile"         
        verbose_name_plural = "User Profiles"  
    