from django.contrib import admin
from .models import Stock, Currency, Account, AccountCurrency, AccountStock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")
    # Остальные настройки администратора для Stock...

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
    # Вы можете добавить дополнительные настройки для Currency, если это необходимо

@admin.register(AccountCurrency)
class AccountCurrencyAdmin(admin.ModelAdmin):
    pass
    # Дополнительные настройки для AccountCurrency, если это необходимо

@admin.register(AccountStock)
class AccountStockAdmin(admin.ModelAdmin):
    pass
    # Дополнительные настройки для AccountStock, если это необходимо

class AccountCurrencyInline(admin.TabularInline):
    model = AccountCurrency

class AccountStockInline(admin.TabularInline):
    model = AccountStock

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountCurrencyInline, AccountStockInline]
    # Дополнительные настройки для Account, если это необходимо
