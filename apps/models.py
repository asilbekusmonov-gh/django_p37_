from django.db.models import Model, ForeignKey, CASCADE, ImageField, DecimalField, \
    PositiveIntegerField, CheckConstraint, Q, F
from django.db.models.fields import CharField


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return f' {self.name}'


class Product(Model):
    name = CharField(null=False, max_length=100, blank=False)
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
    image = ImageField(upload_to='products/%Y/%m/%d')
    price = DecimalField(max_digits=10, decimal_places=2)
    discount_price = DecimalField(max_digits=10, decimal_places=2, default=0,
                                  help_text='Discount should be less than price')
    shipping_cost = PositiveIntegerField(default=0)

    quantity = PositiveIntegerField(default=1)

    @property
    def is_in_stock(self):
        return self.quantity > 0

    class Meta:
        constraints = [
            CheckConstraint(condition=Q(discount_price__lte=F('price')), name='check product price',
                            violation_error_message='discount price should be less than price'),
        ]
