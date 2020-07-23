from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from django_countries.fields import CountryField

import random
import string


# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sport wear'),
#     ('OW', 'Outwear')
# )

def randomslug():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


CATEGORY_CHOICES = (

    ('Laptops', 'Laptops'),
    ('Smartphones', 'Smartphones'),
    ('Tablets', 'Tablets'),
    ('Headphones', 'Headphones'),
    ('Camera', 'Camera'),
    ('Accesories', 'Accesories'),
    ('Tv', 'Tv'),
)

LABEL_CHOICES = (
    ('new', 'new'),
    ('best rated', 'best rated'),
    ('best seller', 'best seller')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


# class EcommerceUser(AbstractUser):
# is_retailer = models.BooleanField(default=False)

# created = models.DateTimeField(auto_now_add=True)
# modified = models.DateTimeField(auto_now=True)


class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logged_in_user')
    session_key = models.CharField(max_length=32)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    is_retailer = models.BooleanField(default=False)
    company_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(choices=LABEL_CHOICES, max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ManyToManyField('Category', related_name='items')
    label = models.ManyToManyField('Label', related_name='items')
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media_root')
    created_on = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def no_of_ratings(self):
        ratings = Rating.objects.filter(item=self)
        return len(ratings)

    def avg_rating(self):
        sum_of_ratings = 0
        ratings = Rating.objects.filter(item=self)
        for rating in ratings:
            sum_of_ratings += rating.rate
        if len(ratings) > 0:
            return sum_of_ratings / len(ratings)
        else:
            return 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='review')
    # name = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # validators=[MinValueValidator(1), MaxValueValidator(5)]
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    subject = models.CharField(max_length=50, blank=True)
    review = models.TextField()
    # ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def review_posted_when(self):
        now = timezone.now()
        duration = now - self.created_on
        seconds = duration.total_seconds()
        mins = int((seconds % 3600) // 60)
        hors = int(seconds // 3600)

        if hors > 24:
            return f"{duration.days} days ago"
        elif hors < 24:
            if seconds > 60:
                if hors > 0:
                    return f"{hors} hrs {mins} mins ago"
                else:
                    return f"{mins} mins ago"
            elif seconds < 60:
                return "just now"

    def __str__(self):
        return 'Comment on  {} by {}'.format(self.subject, self.user)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^(?:254|\+254|0)?(7(?:[129][0-9])|(?:0[0-9]))[0-9]{6})$',
                                 message="phone number must be entered in the format:'+2547*******'")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"
