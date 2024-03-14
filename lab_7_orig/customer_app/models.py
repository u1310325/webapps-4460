from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/',null=True)
    notes = models.TextField(null=True)
    linkedin = models.URLField(null=True)
    OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3')]
    choices = models.CharField(max_length=100,choices=OPTION_CHOICES,null=True)
    def __str__(self):
        return self.name
    


    
class Order(models.Model):

    customer = models.ForeignKey(to = Customer,on_delete = models.CASCADE)
    order_total = models.DecimalField(max_digits=7,decimal_places=2)
    notes = models.CharField(max_length=100,default='')

    status_choices = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed')
    )

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='pending'
    )


class Contact(models.Model):
    customer=models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    phone=models.CharField(max_length=17)
    email=models.EmailField()


