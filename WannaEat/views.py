from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Receipt
from .forms import ReviewForm, UploadFileForm
from .serializers import ReceiptListSerializer, UserSerializer


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


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class ReceiptListView(APIView):
    def get(self, request):
        receipt = Receipt.objects
        serializer = ReceiptListSerializer(receipt, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['creator'] = request.user.id
        serializer = ReceiptListSerializer(data=request.data)
        if serializer.is_valid():
#            serializer.creator_id = User.objects.get(pk=request.user.id)
#            print(serializer.creator.id)
            #serializer.title = "NET"
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
