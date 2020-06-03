from locust import User, task, between, HttpUser
import random

products = [
        '0PUK6V6EV0',
        '1YMWWN1N4O',
        '2ZYFJ3GM2N',
        '66VCHSJNUP',
        '6E92ZMYYFZ',
        '9SIQT8TOJO',
        'L9ECAV7KIM',
        'LS4PSXUNUM',
        'OLJCESPC7Z']
data = [{
        'email': 'someone@example.com',
        'street_address': '1600 Amphitheatre Parkway',
        'zip_code': '94043',
        'city': 'Mountain View',
        'state': 'CA',
        'country': 'United States',
        'credit_card_number': '4432-8015-6152-0454',
        'credit_card_expiration_month': '1',
        'credit_card_expiration_year': '2039',
        'credit_card_cvv': '672',
            },
            {
       'email': 'test@test.com',
        'street_address': '1096 Urban St',
        'zip_code': '16485',
        'city': 'Clemont',
        'state': 'Auvergne',
        'country': 'Mexico',
        'credit_card_number': '4432-8015-6152-0454',
        'credit_card_expiration_month': '8',
        'credit_card_expiration_year': '2024',
        'credit_card_cvv': '181',
            },
            {
        'email': 'canada@canda.ca',
        'street_address': '1096 Main St',
        'zip_code': '16485',
        'city': 'Toronto',
        'state': 'Ontario',
        'country': 'Canada',
        'credit_card_number': '4432-8015-6152-0454',
        'credit_card_expiration_month': '8',
        'credit_card_expiration_year': '2024',
        'credit_card_cvv': '181',
            }]

class MyUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(10)
    def index(self):
        self.client.get("/")

    @task(1)
    def setCurrency(self):
        currencies = ['EUR', 'USD', 'JPY', 'CAD']
        self.client.post("/setCurrency",
                {'currency_code': random.choice(currencies)})
    
    @task(2)
    def browseProduct(self):
        self.client.get("/product/" + random.choice(products))

    @task(3)
    def addToCart(self):
        product = random.choice(products)
        self.client.get("/product/" + product)
        self.client.post("/cart", { 'product_id': product, 'quantity': random.choice([1,2,3,4,5,10]) })

    @task(4)
    def viewCart(self):
        self.client.get("/cart")

    @task(5)
    def checkout(self):
        #self.addToCart(self)
        product = random.choice(products)
        self.client.get("/product/" + product)
        self.client.post("/cart", {
            'product_id': product,
            'quantity': random.choice([1,2,3,4,5,10])
            })

        self.client.post("/cart/checkout", random.choice(data) )
