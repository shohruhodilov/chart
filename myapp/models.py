from django.db import models


class Club(models.Model):

    name = models.CharField(max_length=100)
    money = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.money}"

class MilliyHisob(models.Model):
    name = models.CharField(max_length=150)
    year_2010 = models.CharField(max_length=15)
    year_2011 = models.CharField(max_length=15)
    year_2012 = models.CharField(max_length=15)
    year_2013 = models.CharField(max_length=15)
    year_2014 = models.CharField(max_length=15)
    year_2015 = models.CharField(max_length=15)
    year_2016 = models.CharField(max_length=15)
    year_2017 = models.CharField(max_length=15)
    year_2018 = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.name}|{self.year_2010}|{self.year_2011}|{self.year_2012}|{self.year_2013}|{self.year_2014}|" \
            f"{self.year_2015}|{self.year_2016}|{self.year_2017}|{self.year_2018}"