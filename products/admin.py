from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea


admin.site.register(Sizes)
admin.site.register(Materials)
admin.site.register(MotivationDiscount)

# class CommentsInline(admin.TabularInline):
#     model = Comments
#     extra = 1
#     # readonly_fields = ['ticket', 'user', 'text', 'attachment']
#     # readonly_fields = ('user', 'product', 'title', 'detail', 'rate', 'film', 'image1', 'image2', 'image3', 'image4','active')
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'30'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':60})},
#     }
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store', 'cover_image_admin', 'cover_image_back_admin', 'wholesale')
    # inlines = [CommentsInline,]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    # list_display = ('product', 'image_admin', 'color_admin')
    def color_name(self, obj):
        return obj.color.name
    color_name.short_description = 'رنگ'

@admin.register(FirstSubCategory)
class FirstSubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SecondSubCategory)
class SecondSubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'mother')

@admin.register(ThirdSubCategory)
class ThirdSubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'mother')

@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    exclude=("url ",)
    readonly_fields=('url', )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'user', 'rate')




