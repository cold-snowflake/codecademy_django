from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from routes.models import Line, Station, Stop
from routes.forms import LineForm, StationForm, StopForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'routes/home.html'


class LinesView(ListView):
    model = Line
    template_name = 'routes/lines.html'


class CreateLineView(CreateView):
    model = Line
    form_class = LineForm
    template_name = 'routes/add_line.html'
    success_url = reverse_lazy("routes:lines")


class UpdateLineView(UpdateView):
    model = Line
    form_class = LineForm
    template_name = 'routes/update_line.html'
    success_url = reverse_lazy("routes:lines")


class DeleteLineView(DeleteView):
    model = Line
    template_name ='routes/delete_line.html'
    success_url = reverse_lazy("routes:lines")


class StationsView(ListView):
    model = Station
    template_name = 'routes/stations.html'


class CreateStationView(CreateView):
    model = Station
    form_class = StationForm
    template_name = 'routes/add_station.html'
    success_url = reverse_lazy('routes:stations')


class UpdateStationView(UpdateView):
    model = Station
    form_class = StationForm
    template_name = 'routes/update_stations.html'
    success_url = reverse_lazy('routes:stations')


class DeleteStationView(DeleteView):
    model = Station
    template_name = 'routes/delete_station.html'
    success_url = reverse_lazy('routes:stations')


class StopsView(ListView):
    model = Stop
    template_name = 'routes/stops.html'


class CreateStopView(CreateView):
    model = Stop
    form_class = StopForm
    template_name = 'routes/add_stop.html'
    success_url = reverse_lazy('routes:stops')


class UpdateStopView(UpdateView):
    model = Stop
    form_class = StopForm
    template_name = 'routes/update_stop.html'
    success_url = reverse_lazy('routes:stops')


class DeleteStopView(DeleteView):
    model = Stop
    template_name = 'routes/delete_stop.html'
    success_url = reverse_lazy('routes:stops')
