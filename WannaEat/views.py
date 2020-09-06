from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Receipt
from .forms import ReviewForm
from .serializers import ReceiptListSerializer


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


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.receipt_id = pk
            form.save()
            print("congratz for send msg")
        else:
            print("message wasn't sended")
        # full path to current page
        return redirect(Receipt.objects.get(id=pk).get_absolute_url())


class ReceiptListView(APIView):
    def get(self, request):
        receipt = Receipt.objects
        serializer = ReceiptListSerializer(receipt, many=True)
        return Response(serializer.data)
