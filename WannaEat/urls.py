from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReceiptView.as_view()),
    path("receipt/", views.ReceiptListView.as_view()),
    path("<slug:slug>/", views.ReceiptDetailView.as_view(), name='receipt_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
