from django.contrib import admin
from django.contrib.auth.models import User
from .models import Receipt, Rating, RatingStar, FriendList, Product, ProductsList, \
    Category, ReceiptBoard, ReceiptShots


class CategoryAdmin(admin.ModelAdmin):
    pass

class ReceiptAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "image", "video_ulr", "creator", "category", "product_list", "cooking_steps")
	actions = None
	
	def save_model(self, request, obj, form, change):
		if not obj.creator_id:
			obj.creator = request.user
		print("HELLO")
		obj.save()

admin.site.register(Category)
admin.site.register(Receipt)
admin.site.register(Rating)
admin.site.register(RatingStar)
#admin.site.register(User)
admin.site.register(FriendList)
admin.site.register(Product)
admin.site.register(ProductsList)
admin.site.register(ReceiptShots)
admin.site.register(ReceiptBoard)

