from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ["title"]
	list_display_links = []
	list_editable = []
	list_filter = []
	search_fields = []
	
	class Meta:
		model = Testimonial