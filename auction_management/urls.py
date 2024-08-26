from django.urls import path
from .views import AuctionListCreateView, AuctionDetailView, BidView

urlpatterns = [
    path('auctions/', AuctionListCreateView.as_view(), name='auction-list'),
    path('auctions/<int:pk>/', AuctionDetailView.as_view(), name='auction-detail'),
    path('auctions/<int:auction_id>/bid/', BidView.as_view(), name='bid'),
]
