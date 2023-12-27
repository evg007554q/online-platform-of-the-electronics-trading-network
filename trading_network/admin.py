from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from trading_network.models import Network, Product

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contractor_url', 'rank', 'date_of_creation', 'debt_to_supplier'
                    , 'country', 'city', 'email')

    list_filter = ('city',)
    actions = ['clear_debt']

    def contractor_url(self, obj):
        """ ссылка на поствшика  """
        if obj.contractor:
            url = reverse('admin:trading_network_network_change', args=[obj.contractor.id])
            return format_html('<a href=%s>%s</a>' % (url, obj.contractor.name))
        return None

    contractor_url.short_description = 'Поставщик'

    def clear_debt(self, queryset):
        """ Очистка задолженности перед поставщиком """
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price',)



#
#
# # @admin.action(description='Очистить задолженность перед поставщиком')
# # def