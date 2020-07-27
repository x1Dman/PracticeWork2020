from django import template
from WannaEat.models import Category, Receipt

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('receipts/tags/last_recipes.html')
def get_last_movie():
    receipts = Receipt.objects.order_by("id")[:5]
    return {"last_receipts": receipts}
