from django.db import models

# Create your models here.
gender=(
    ('male','Male'),
    ('female','Female'),
    ('transgender','Transgender')
)

district=(
    ('kasaragod','Kasaragod'),
    ('kannur', 'Kannur'),
    ('kozhikode', 'Kozhikode'),
    ('wayanad', 'Wayanad'),
    ('malappuram', 'Malappuram'),
    ('palakkad', 'Palakkad'),
    ('thrissur', 'Thrissur'),
    ('kottayam', 'Kottayam'),
    ('idukki','Idukki'),
    ('alappuzha','Alappuzha'),
    ('kollam','Kollam'),
    ('ernakulam', 'Ernakulam'),
    ('pathanamthitta','Pathanamthitta'),
    ('thiruvananthapuram','Thiruvananthapuram')
)

class User(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100,choices=gender)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Photo = models.ImageField(upload_to = "media/", default=0)
    Place = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Village = models.CharField(max_length=100)
    District = models.CharField(max_length=100,choices=district)
    Password = models.CharField(max_length=8)
    Confirmpassword = models.CharField(max_length=8)

    def __str___(self):
        return self.Firstname
