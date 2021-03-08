import json
from django import template
from bib.models import ZotItem
register = template.Library()


@register.inclusion_tag('bib/tags/zotitem.html')
def bib_quote(item):
    values = {}
    values['quote'] = f"{item.zot_bibtex}"
    values['object'] = item
    return values
