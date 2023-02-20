from django.db import models
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# ---------- Main Category of products -------------
class FirstSubCategory(models.Model):
    

    name = models.CharField(max_length=999, verbose_name='name')
    slug = models.CharField(max_length=999, verbose_name='slug')
    image = models.ImageField(upload_to='product/category/')
    def __str__(self):
        return f"{self.name}"

class SecondSubCategory(models.Model):
    

    name = models.CharField(max_length=999, verbose_name='name')
    slug = models.CharField(max_length=999, verbose_name='slug')
    mother = models.ForeignKey("FirstSubCategory", related_name="secondmother", on_delete=models.CASCADE, verbose_name="mother")
    image = models.ImageField(upload_to='product/category/', blank=True, null=True)
    def __str__(self):
        return f"{self.name} / {self.mother}"

class ThirdSubCategory(models.Model):
    

    name = models.CharField(max_length=999, verbose_name='name')
    slug = models.CharField(max_length=999, verbose_name='slug')
    mother = models.ForeignKey("SecondSubCategory", related_name="thirdmother", on_delete=models.CASCADE, verbose_name="mother")
    image = models.ImageField(upload_to='product/category/', blank=True, null=True)
    def __str__(self):
        return f"{self.name} / {self.mother}"

# class Category(models.Model):
#     class Meta:
#         verbose_name="دسته‌بندی"
#         verbose_name_plural="دسته‌بندی‌ها"

#     child1 = models.ForeignKey("FirstSubCategory", on_delete=models.CASCADE, verbose_name="زیرشاخه اول")
#     child2 = models.ForeignKey("SecondSubCategory", on_delete=models.CASCADE, blank=True, null=True, verbose_name="زیرشاخه دوم")
#     child3 = models.ForeignKey("ThirdSubCategory", on_delete=models.CASCADE, blank=True, null=True, verbose_name="زیرشاخه سوم")
#     def __str__(self):
#         return f"{self.child1.name} / {self.child2.name} / {self.child3}"

# --------------- Products Information ------------------
class Colors(models.Model):
    

    name = models.CharField(max_length=999, verbose_name='name')
    url = models.TextField(verbose_name="url", default=
    '''برای انتخاب رنگ، وارد لینک زیر شده و اسم رنگ دلخواه را در فیلد وارد کنید 
    
    https://htmlcolorcodes.com/color-names/''')

    def __str__(self):
        return self.name

class Sizes(models.Model):

    name = models.CharField(max_length=999, verbose_name='name')
    def __str__(self):
        return self.name

class Materials(models.Model):

    name = models.CharField(max_length=999, verbose_name='name')
    def __str__(self):
        return self.name




class Products(models.Model):
 

    name = models.CharField(max_length=999, verbose_name='name')
    description = models.TextField(max_length=999, verbose_name='description')
    price = models.IntegerField(verbose_name='price')
    discount_price = models.IntegerField(default=0, null=True, blank=True)
    store = models.IntegerField(verbose_name='store')
    child1 = models.ForeignKey("FirstSubCategory", verbose_name=("child1"), on_delete=models.CASCADE)
    child2 = models.ForeignKey("SecondSubCategory", verbose_name=("child2"), on_delete=models.CASCADE, blank=True, null=True)
    child3 = models.ForeignKey("ThirdSubCategory", verbose_name=("child3"), on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField("Colors", blank=True, verbose_name="color")
    size = models.ManyToManyField("Sizes", blank=True, verbose_name="size")
    material = models.ManyToManyField("Materials", blank=True, verbose_name="material")
    cover_image = models.ImageField(upload_to='product/cover/', verbose_name='cover_image')
    cover_image_back = models.ImageField(upload_to='product/cover/', verbose_name='cover_image_back')
    wholesale = models.BooleanField(verbose_name="wholesale")

    def cover_image_admin (self):
        return format_html("<img height='100px' src='/media/{}'>".format(self.cover_image))
    cover_image_admin.allow_tags = True
    cover_image_admin.short_description = "تصویر"
    
    def cover_image_back_admin (self):
        return format_html("<img height='100px' src='/media/{}'>".format(self.cover_image_back))
    cover_image_back_admin.allow_tags = True
    cover_image_back_admin.short_description = " تصویر پشت"

    def __str__(self):
        return f"{self.name}"




    # def color_admin (self):
    #     return format_html("<div style='background-color:{}; width:20px; height:20px; border-radius:15px'></div>".format(self.color))
    # color_admin.allow_tags = True
    # color_admin.short_description = "رنگ"
    #
    # def __str__(self):
    #     return self.product.name


class ProductImages(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='product')
    image = models.ImageField(upload_to='product/image', verbose_name='image')
    color = models.ForeignKey("Colors", on_delete=models.CASCADE, null=True, blank=True, verbose_name="color")

    def image_admin(self):
        return format_html("<img height='100px' src='/media/{}'>".format(self.image))

    image_admin.allow_tags = True
    image_admin.short_description = "تصویر"

class MotivationDiscount (models.Model):

    name = models.CharField(max_length=999, verbose_name='name')
    detail = models.TextField(blank=True, null=True, verbose_name='detail')
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    percentage = models.PositiveIntegerField(verbose_name='percentage')
    products = models.ManyToManyField(Products, verbose_name="products")
    active = models.BooleanField(verbose_name='active')

    def __str__(self):
        return self.name


class Comments (models.Model):

    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name="product", on_delete=models.CASCADE)
    title = models.CharField(max_length=999)
    detail = models.TextField(verbose_name='detail')
    rate = models.PositiveIntegerField(verbose_name='rate')
    film = models.FileField(upload_to="comments/film", blank=True, null=True)
    image1 = models.ImageField(upload_to="comments/image", blank=True, null=True)
    image2 = models.ImageField(upload_to="comments/image", blank=True, null=True)
    image3 = models.ImageField(upload_to="comments/image", blank=True, null=True)
    image4 = models.ImageField(upload_to="comments/image", blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


