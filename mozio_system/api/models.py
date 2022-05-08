from django.contrib.gis.db.models import PolygonField
from django.db.models import Model, CharField, EmailField, DecimalField, ForeignKey, DO_NOTHING
from mozio_system.settings import NAME_MAX_LEN, PHONE_MAX_LEN, LANGUAGES_LIST, CURRENCY_LIST, LANGUAGES_MAX_LEN, \
    CURRENCY_MAX_LEN, PRICE_DIGITS, PRICE_DECIMAL_DIGITS


class Provider(Model):
    name = CharField(max_length=NAME_MAX_LEN, verbose_name='Name')
    email = EmailField(verbose_name='Email')
    phone = CharField(max_length=PHONE_MAX_LEN)
    language = CharField(choices=LANGUAGES_LIST, max_length=LANGUAGES_MAX_LEN)
    currency = CharField(choices=CURRENCY_LIST, max_length=CURRENCY_MAX_LEN)


class ServiceArea(Model):
    name = CharField(max_length=NAME_MAX_LEN, verbose_name='Name')
    provider = ForeignKey('api.Provider', default=None, null=True, blank=True, on_delete=DO_NOTHING)
    price = DecimalField(max_digits=PRICE_DIGITS, decimal_places=PRICE_DECIMAL_DIGITS)
    polygon = PolygonField(verbose_name='polygon')
