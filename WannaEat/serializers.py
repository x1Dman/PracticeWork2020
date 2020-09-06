from rest_framework import serializers
from .models import Receipt


class ReceiptListSerializer(serializers.ModelSerializer):
    """All receipts"""

    class Meta:
        model = Receipt
        fields = ("title", "description", "image", "cooking_steps")
