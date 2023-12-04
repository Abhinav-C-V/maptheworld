from django.db import models

# Create your models here.
class Package(models.Model):
    package_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default= None, upload_to='images/')
    normal_price = models.IntegerField(null=True, blank=True)
    Inclusion = models.CharField(max_length=200, blank=True)
    Days = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.package_name
    
class PackageGallery(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_gallery/')
    def __str__(self):
        return f"Gallery Image for {self.package.package_name}"
    
class Banner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='package_gallery/banner')
    def __str__(self):
        return self.name