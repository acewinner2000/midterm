from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="test")  
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class sp_Services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="test")  
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class data(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)




class price(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="test") 
    fee=models.FloatField(default=15.5)
    data=models.ManyToManyField(data)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
