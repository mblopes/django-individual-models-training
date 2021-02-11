from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Category {self.category_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_description = models.TextField(max_length=255, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=False, blank=False)
    product_category = models.ManyToManyField(Category)

    def __str__(self):
        return f"Product {self.product_name, self.product_description, self.product_price, self.product_category}"


class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_doc_number = models.CharField(max_length=14, null=False,
                                           blank=False)
    customer_phone = models.CharField(max_length=20, null=False, blank=False)
    customer_email = models.EmailField(max_length=50, null=False, blank=False)
    customer_gender = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Customer {self.customer_name, self.customer_doc_number, self.customer_phone, self.customer_email, self.customer_gender}"


class Sport(models.Model):
    sport_name = models.CharField(max_length=100, null=False, blank=False)
    sport_modality = models.CharField(max_length=100, null=False, blank=False)
    bet_value = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                    blank=False)

    def __str__(self):
        return f"Sports {self.sport_name, self.sport_modality, self.bet_value}"


class Team(models.Model):
    team_name = models.CharField(max_length=100, null=False, blank=False)
    team_sport = models.ManyToManyField(Sport)

    def __str__(self):
        return f"Teams {self.team_name, self.team_sport}"
