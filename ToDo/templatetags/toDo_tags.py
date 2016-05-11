from django import template


register = template.Library()

@register.filter('fieldtype')
def fieldtype(field):
    return field.field.widget.__class__.__name__

@register.filter('optiontype')
def optiontype(field):
    res = []
    if field.field.widget.__class__.__name__=='Select':
	for i in field.field.choices:
	    res.append(i[1])
    return res
