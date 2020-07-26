from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Receipt


class ReceiptView(ListView):
    # model = Receipt
    # queryset = Receipt.objects.all()
    # template_name = "receipts/receipts_list.html"
    def get(self, request):
        receipts = Receipt.objects.all()
        return render(request, "receipts/receipts_list.html", {"receipts": receipts})


class ReceiptDetailView(DetailView):
    # model = Receipt
    # slug_field = "video_ulr"
    def get(self, request, slug):
        receipt = Receipt.objects.get(video_ulr=slug)
        return render(request, "receipts/receipt_detail.html", {"receipt": receipt})

