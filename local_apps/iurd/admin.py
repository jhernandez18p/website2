from django.contrib import admin

from .models import (Church, Event, Feed, Project, Schedule, Reunion, Subscriber, Category)
# Register your models here.

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["mail", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Church


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["mail", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Event


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["url_feed", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Feed


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["category", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Project


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["description", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Schedule


@admin.register(Reunion)
class ReunionAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["description", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Reunion


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["description", "name"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Subscriber


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ["name", "updated",]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["description", "name"]
	search_fields = ["name", "description"]
	
	class Meta: 
		model = Category