from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club, MilliyHisob

class ClubChartView(TemplateView):
    template_name = 'myapp/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        context['mil'] = MilliyHisob.objects.all()
        print(context['mil'])
        print(context)
        return context

def hisobla(request):
    with open('D:\django\chart\data\gdp2.csv', encoding='latin1') as f:
        # contents = f.readline()
        # milliy_hisoblar = MilliyHisob.objects.all()
        # print(milliy_hisoblar)
        for i in f:
            fields = i.split(';')
            a = MilliyHisob(name=fields[0], year_2010=fields[1], year_2011=fields[2], year_2012=fields[3], year_2013=fields[4], year_2014=fields[5], year_2015=fields[6], year_2016=fields[7], year_2017=fields[8], year_2018=fields[9])
            a.save()
            print(a)
            print(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6])
        return render(request, 'myapp/chart2.html')
