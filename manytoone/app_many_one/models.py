from django.db import models

class BiriyaniCatModel(models.Model):
    bc_id=models.AutoField(primary_key=True)
    b_cat=models.CharField(max_length=50)

    def __str__(self):
        return self.b_cat
class BiriyaniModel(models.Model):
    b_id=models.AutoField(primary_key=True)
    b_name=models.CharField(max_length=50)
    b_price=models.FloatField()
    b_type=models.ForeignKey(BiriyaniCatModel,on_delete=models.CASCADE)


