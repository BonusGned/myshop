from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe


def order_detail(obj):
    return mark_safe(
        f'<a href="{reverse_lazy("orders:admin_order_detail", args=[obj.id])}">Просмотр</a>'
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_pdf(obj):
    return mark_safe(
        f'<a href="{reverse_lazy("orders:admin_order_pdf", args=[obj.id])}">PDF</a>'
    )

# def order_pdf(obj):
#     return mark_safe('<a href="{}">PDF</a>'.format(
#         reverse_lazy('orders:admin_order_pdf', args=[obj.id])))

order_pdf.short_description = 'Invoice'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated', ]
    inlines = [OrderItemInline]
