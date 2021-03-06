from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

from pytz import timezone
from useraccounts.models import Customer
from useraccounts.models import Merchandiser
from django.contrib.auth import get_user_model
from product_seasons.models import Season
from product_groups.models import ProductGroup


# Create your models here.
User = get_user_model()


class Style(models.Model):
    style_no = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    style_description = models.TextField(
        _("Style description"), max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    delivery_date = models.DateField(
        _("Delivery date"), default=datetime.date.today)
    merchandiser = models.ForeignKey(Merchandiser, verbose_name=_(
        "Merchandiser name"), related_name="merchandiser", on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, verbose_name=_("Customer name"), related_name="customer", on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(
        auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    details_received_date = models.DateField()

    def __str__(self):
        return f'{self.style_no} | Delivery date: {self.delivery_date}'

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Style"
        verbose_name_plural = "Styles"
