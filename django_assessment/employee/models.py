from django.db import models

# Model for Employee


class Employee(models.Model):
    full_name = models.CharField(
        max_length=200, blank=False, null=True)
    address = models.CharField(max_length=120, null=True, blank=False)
    email = models.EmailField(max_length=120, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    image = models.ImageField(upload_to='employee-image', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_name)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = "Employees"
