from rest_framework import generics
from rest_framework.permissions import AllowAny

from dogs.serializers.donation import DonationSerializer
from dogs.services import create_stripe_price, create_stripe_session


class DonationCreateView(generics.CreateAPIView):
    serializer_class = DonationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        donation = serializer.save()
        stripe_price_id = create_stripe_price(donation.donation_amount)
        donation.payment_link, donation.payment_id  = create_stripe_session(stripe_price_id)
        donation.save()
