import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(donation_amount):
    stripe_price = stripe.Price.create(
        # по умолчанию выводит в копейках, это будет также и с долларами, поэтому *100
        currency="rub",
        unit_amount=donation_amount*100,
        # recurring={"interval": "month"},
        product_data={"name": "Donation"},
    )
    return stripe_price['id']
def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{
            "price": stripe_price_id,
            "quantity": 1}],
        mode="payment",
    )
    return stripe_session['url'], stripe_session['id']