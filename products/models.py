from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True 

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    product_quantity = models.CharField(max_length=100, null=True, blank=True)
    product_measuring = models.CharField(max_length=100, null=True, blank=True, choices=(("KG", "KG"),("ML", "ML"),("L", "L")))
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} Meta Information"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_image = models.ImageField(upload_to="products")

    def __str__(self):
        return f"{self.product.product_name} Image"
