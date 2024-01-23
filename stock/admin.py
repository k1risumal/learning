from django.contrib import admin
from .models import Stock, Currency

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")
    # Остальные настройки администратора для Stock...

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
    # Вы можете добавить дополнительные настройки для Currency, если это необходимо


