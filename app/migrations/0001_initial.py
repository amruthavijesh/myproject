# Generated by Django 3.1.5 on 2021-02-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(upload_to='')),
                ('Place', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Village', models.CharField(max_length=100)),
                ('District', models.CharField(choices=[('kasaragod', 'Kasaragod'), ('kannur', 'Kannur'), ('kozhikode', 'Kozhikode'), ('wayanad', 'Wayanad'), ('malappuram', 'Malappuram'), ('palakkad', 'Palakkad'), ('thrissur', 'Thrissur'), ('kottayam', 'Kottayam'), ('idukki', 'Idukki'), ('alappuzha', 'Alappuzha'), ('kollam', 'Kollam'), ('ernakulam', 'Ernakulam'), ('pathanamthitta', 'Pathanamthitta'), ('thiruvananthapuram', 'Thiruvananthapuram')], max_length=100)),
                ('Password', models.CharField(max_length=8)),
                ('Confirmpassword', models.CharField(max_length=8)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
