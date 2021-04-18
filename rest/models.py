from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=64,null=False)

    def __str__(self):
        return f"school name={self.name}"



class Students(models.Model):
    name = models.CharField(max_length=64,null=False)
    age = models.IntegerField(null=False)
    standard = models.IntegerField(null=False)
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f"name={self.name} age={self.age} standard={self.standard} school={self.school}"