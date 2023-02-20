from django.urls import path
from . import api_view
from . import views

urlpatterns = [
    path('create/', api_view.ProductCreate.as_view(), name='products'),
    # path('list/category/', api_view.ProductCategoryCreate.as_view(), name='products_category'),
    path('create/images/', api_view.ProductImagesCreate.as_view(), name='products_images'),
    path('list/', api_view.ProductsList.as_view(), name='products_list'),
    path('colors/', api_view.ColorsList.as_view(), name='products_colors'),
    path('list/details/<int:id>', api_view.ProductDetails.as_view(), name='products_images'),
    path('list/images/<int:id>', api_view.ProductImagesList.as_view(), name='products_images'),
    path('searchbox/', views.SearchboxView, name='searchbox'),
    path('comments/list/', api_view.CommentsList.as_view(), name='comments'),
    path('comments/create/', api_view.CommentsCreate.as_view(), name='comments'),
    path('FirstSubCategoryList/list/', api_view.FirstSubCategoryList.as_view(), name='firstSubcategorylist'),
    path('SecondSubCategoryList/list/', api_view.SecondSubCategoryList.as_view(), name='secondsubsategoryList'),
    path('ThirdSubCategoryList/list/', api_view.ThirdSubCategoryList.as_view(), name='thirdsubcategoryList'),
    #motivation discount
    path('motivation/', api_view.MotivationDiscountList.as_view(), name='motivation'),
    path('motivation/edit/<int:id>', api_view.MotivationDiscountUpdate.as_view(), name='MotivationDiscountUpdate'),
    #active or deactive motivation discount
    path('motivation/activate/<int:id>', api_view.ChangeActiveDiscount.as_view(), name='ChangeActiveDiscount'),
]