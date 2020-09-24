from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Receipt
from django.contrib.auth.models import User

'''
class Receipt(models.Model):
    """Receipt"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="receipts/")
    video_ulr = models.SlugField(max_length=160, unique=True)
    cooking_steps = models.TextField("Cooking_steps")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    product_list = models.OneToOneField(
        ProductsList, related_name="Receipt_list", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    def get_review(self):
        return self.receiptboard_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse("receipt_detail", kwargs={"slug": self.video_ulr})

    class Meta:
        verbose_name = "Receipt"
        verbose_name_plural = "Receipts"
'''
class ReceiptListSerializer(serializers.ModelSerializer):
    """All receipts"""

    class Meta:
        model = Receipt
        fields = ("title", "description", "image", "video_ulr", "creator", "category", "product_list", "cooking_steps")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
