from django.contrib import admin
from .models import Newspaper,Video,Audio,Image

@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
	list_display = ["title"]
	list_display_links = []
	list_editable = []
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Newspaper


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ["title"]
	list_display_links = []
	list_editable = []
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Video	


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
	list_display = ["title"]
	list_display_links = []
	list_editable = []
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Audio


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ["title"]
	list_display_links = []
	list_editable = []
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Image

