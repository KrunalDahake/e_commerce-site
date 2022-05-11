from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced, UserForm

# Register your models here.
@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','pincode','state']
    
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','type','product_image']

@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
    

@admin.register(OrderPlaced)
class OrderplacedAdminModel(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','status']
    
@admin.register(UserForm)

class FormModelAdmin(admin.ModelAdmin):
    list_display=['id','username','password','password2']
