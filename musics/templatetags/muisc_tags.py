from django import template 
import math
register = template.Library()
@register.filter
def time_formatter(time):
	time = int(time)
	min = math_floor((time%3600)/60)
	sec = math.floor(time&60)
	if sec<10:
		pass
