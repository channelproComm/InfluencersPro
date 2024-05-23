from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import User


# Create your models here

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    package_choices = [
        ('silver', 'Silver'),
        ('platinum', 'Platinum'),
        ('gold', 'Gold'),
    ]
    package = models.CharField(max_length=10, choices=package_choices, default='platinum')

    def __str__(self):
        return f"{self.user.username}'s Package: {self.package}"
    

class Category(models.Model):
    category=models.CharField(max_length=100)
    price=models.FloatField(max_length=500000)
    user = models.ManyToManyField(User) 

    def calculate_final_price(self,user):
        user_profile = UserProfile.objects.get(user=user)
        package = user_profile.package.lower()
        price = self.price

        if package == 'platinum':
            price += price * 0.05
        elif package == 'silver':
            price += price * 0.20
        elif package == 'gold':
             price += price * 0.10 
        else:
            price += price * 0.05

        return price

    def __str__(self):
        return self.category
    

class Links(models.Model):
    logo=models.ImageField(upload_to='Links/images')
    media=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    industry=models.CharField(max_length=50)
    visting=models.CharField(max_length=50)
    audience=models.CharField(max_length=150)
    action=models.URLField(blank=True)
    cost=models.FloatField(max_length=1000000,null=True)
    category = models.ManyToManyField(Category)


    def calculate_final_price(self,user):
        user_profile = UserProfile.objects.get(user=user)
        package = user_profile.package.lower()
        cost = self.cost

        if package == 'platinum':
            cost += cost * 0.05
        elif package == 'silver':
            cost += cost * 0.20
        elif package == 'gold':
            cost += cost * 0.10 
        else:
            cost += cost * 0.05
        
        return cost
    def __str__(self):
        return self.media