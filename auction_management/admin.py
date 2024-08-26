# auction_management/admin.py

from django.contrib import admin
from .models import Auction, Bid

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'start_time', 'end_time', 'start_price', 'highest_bid', 'winner')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'user', 'amount', 'bid_time')
