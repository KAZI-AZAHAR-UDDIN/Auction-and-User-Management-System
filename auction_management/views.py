from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Auction, Bid
from .serializers import AuctionSerializer, BidSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

# Auction Views
class AuctionListCreateView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter to return only ongoing auctions
        return self.queryset.filter(end_time__gt=timezone.now())

class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

# Bid View
class BidView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, auction_id):
        auction = Auction.objects.get(id=auction_id)
        if auction.end_time <= timezone.now():
            return Response({'error': 'Auction has ended'}, status=status.HTTP_400_BAD_REQUEST)

        bid = Bid.objects.create(
            user=request.user,
            auction=auction,
            amount=request.data['amount']
        )

        if not auction.highest_bid or bid.amount > auction.highest_bid:
            auction.highest_bid = bid.amount
            auction.winner = request.user
            auction.save()

        return Response({'success': 'Bid placed successfully'}, status=status.HTTP_201_CREATED)

