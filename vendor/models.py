from django.db import models
from django.utils.text import slugify
from userauths.models import User

class Vendor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.FileField(upload_to="vendor", blank=True, null=True, default='vendor.jpg')
  name = models.CharField(max_length=100, help_text="Shop Name", null=True, blank=True)
  email = models.CharField(max_length=100, help_text="Shop Email", null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  mobile =  models.CharField(max_length=100, help_text="Shop Name", null=True, blank=True)
  active = models.BooleanField(default=True)
  date = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(unique=True, max_length=500)

  class Meta:
    verbose_name_plural = 'Vendors'
    ordering = ['-date']

  def __str__(self):
    return str(self.name)
  
  def save(self, *args, **kwargs):
    if self.slug == "" or self.slug == None:
      self.slug = slugify(self.name)
    super(Vendor, self).save(*args, **kwargs)
  


