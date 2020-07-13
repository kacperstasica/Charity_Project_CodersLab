from django.db import models
from django.db.models import Sum

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


class Institution(models.Model):
    FUNDACJA = 'FND'
    ORGANIZACJA_POZARZADOWA = 'NGO'
    ZBIORKA_LOKALNA = 'LOC'
    INSTITUTION_TYPE_CHOICES = [
        (FUNDACJA, 'Fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'Organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'Zbiórka lokalna'),
    ]
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(
        max_length=3,
        choices=INSTITUTION_TYPE_CHOICES,
        default=FUNDACJA,
    )
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name} ({self.type})'

    @property
    def category_ids(self):
        return ','.join([str(x.id) for x in self.category.all()])


    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=58)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_quantity(cls):
        quantity = cls.objects.all().aggregate(Sum('quantity')).get('quantity__sum')
        if quantity is None:
            return '0'
        return quantity
