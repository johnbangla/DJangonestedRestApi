from django.db import models

# Create your models here.
# title images( url thumbnailUrl) price categoryId userId location (latitude longitude)
#    image = models.ImageField(blank=True,null=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    categoryId = models.IntegerField(default=1)
    userId = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# class Myimage(models.Model):
#     album = models.ForeignKey(
#         Album, related_name='iimages', on_delete=models.CASCADE)
#     url = models.CharField(max_length=300)
#     thumbnailUrl = models.CharField(max_length=300)

#     def __str__(self):
#         return self.url
    
class IImage(models.Model):
    album = models.ForeignKey(
        Album, related_name='iimages', on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    thumbnailUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.url


class Location(models.Model):
    album = models.ForeignKey(
        Album, related_name='locations', on_delete=models.CASCADE)
    latitude = models.IntegerField(default=1)
    longitude = models.IntegerField(default=2)


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
