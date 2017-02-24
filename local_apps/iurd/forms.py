from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import (Church, Event, Feed, Project, Schedule, Reunion)


class ChurchForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Church
        fields = [
            "name",
            "mail",
            "description",
            "image",
            "telephone_number",
        ]


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    start = forms.DateField(widget=forms.SelectDateWidget)
    end = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Event
        fields = [
            "name",
            "title",
            "description",
            "image",
            "start",
            "end",
            "mail",
            "start",
            "church",
            "location",
        ]


class FeedForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    url_feed = forms.URLField()
    class Meta:
        model = Feed
        fields = [
            "name",
            "title",
            "description",
            "image",
            "url_feed",
        ]


class ProjectForm(forms.ModelForm):
    GROUP = 'Groups'
    PROJECT = 'Projecs'

    CATEGORIES = (
        (GROUP,'Grupos'),
        (PROJECT,'Proyectos'),
    )

    description = forms.CharField(widget=CKEditorWidget())
    category = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CATEGORIES,
    )
    class Meta:
        model = Project
        fields = [
            "name",
            "title",
            "description",
            "image",
            "background_image",
            "category",
            "parentId",
        ]


class ScheduleForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    start = forms.DateField(widget=forms.SelectDateWidget)
    ends = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Schedule
        fields = [
            "name",
            "description",
            "start",
            "ends",
        ]


class ReunionForm(forms.ModelForm):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

    WEEKDAYS = (
        (SUNDAY,'Domingo'),
        (MONDAY,'Lunes'),
        (TUESDAY,'Martes'),
        (WEDNESDAY,'Miércoles'),
        (THURSDAY,'Jueves'),
        (FRIDAY,'Vierne'),
        (SATURDAY,'Sabado'),
    )

    description = forms.CharField(widget=CKEditorWidget())
    category = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=WEEKDAYS,
    )
    class Meta:
        model = Reunion
        fields = [
            "name",
            "title",
            "description",
            "image",
            "background_image",
            "category",
            "schedule",
        ]