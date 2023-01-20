from django.urls import path
from . import views
app_name = 'board'
urlpatterns = [
    path('', views.index, name='board_index'),
    path('<int:product_id>/product/', views.board_product, name='board_product'),
    path('product/create/', views.index, name='board_product_create'),
    path('product/delete/<int:product_id>', views.board_product_delete, name='board_product_delete'),
    path('product/modify/<int:product_id>', views.board_product_modify, name='board_product_modify'),
    path('product/create/<int:product_id>/comment/', views.board_comment_create, name='board_comment_create'),
    path('product/delete/<int:product_id>/<int:comment_id>/comment/', views.board_comment_delete, name='board_comment_delete'),

]
