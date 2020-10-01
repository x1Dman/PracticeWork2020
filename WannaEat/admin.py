from django.contrib import admin
from .models import Receipt, Rating, RatingStar, User, FriendList, Product, ProductsList, \
    Category, ReceiptBoard, ReceiptShots


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Receipt)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(User)
admin.site.register(FriendList)
admin.site.register(Product)
admin.site.register(ProductsList)
admin.site.register(ReceiptShots)
admin.site.register(ReceiptBoard)

