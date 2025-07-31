from django.contrib import admin
from .models import chaiVariety,chaiCertificate,chaiReview,Store

# Register your models here.
class ChaiReviewInLine(admin.TabularInline):
    model=chaiReview
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added',)
    inlines=[ChaiReviewInLine]

class storeAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')


admin.site.register(chaiVariety,ChaiVarietyAdmin)
admin.site.register(Store,storeAdmin)
admin.site.register(chaiCertificate,ChaiCertificateAdmin)

