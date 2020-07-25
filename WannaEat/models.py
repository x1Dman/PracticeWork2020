from django.db import models


class Category(models.Model):
    """Category"""
    name = models.CharField("Category", max_length=50)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class User(models.Model):
    """User"""
    user_img = models.ImageField("Image", upload_to="users/")
    email = models.EmailField()
    nickname = models.CharField("Nickname", max_length=100, default="Unknown")
    friend_list = models.ForeignKey
    info = models.TextField("Information")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class FriendList(models.Model):
    # TODO fix the dublicate friends
    # main user
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_parent_friends")
    # list of users, that in friendship with parent
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "friend_list"
        verbose_name_plural = "friend_lists"


class Product(models.Model):
    name = models.CharField("Name", max_length=60)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="products/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductsList(models.Model):
    product = models.ManyToManyField(Product, related_name="list_product")
    product_count = models.IntegerField("Product_count")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Products list"
        verbose_name_plural = "Products lists"


class Receipt(models.Model):
    """Receipt"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="receipts/")
    video_ulr = models.SlugField(max_length=160, unique=True)
    cooking_steps = models.TextField("Cooking_steps")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    product_list = models.OneToOneField(
        ProductsList, related_name="Receipt_list", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Receipt"
        verbose_name_plural = "Receipts"


class ReceiptShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="receipt_shots/")
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shot"
        verbose_name_plural = "Shots"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Star"
        verbose_name_plural = "Stars"


class Rating(models.Model):
    ip = models.CharField("IP", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class ReceiptBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.TextField("Message")
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )
    receipt = models.ForeignKey(
        Receipt, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} - {self.receipt}"

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"