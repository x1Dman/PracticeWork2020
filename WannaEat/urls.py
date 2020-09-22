from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("", views.ReceiptView.as_view()),
    path("users/", views.UserCreate.as_view(), name="user_create"),
    path("receipt/", views.ReceiptListView.as_view(), name="receipt"),
    path("<slug:slug>/", views.ReceiptDetailView.as_view(), name='receipt_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
