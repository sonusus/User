from django.db import models
class Logintable(models.Model):
    lid=models.AutoField(primary_key=True)
    l_email=models.CharField(max_length=150)
    l_pass=models.CharField(max_length=50)
    l_type=models.CharField(max_length=50)
    l_status=models.CharField(max_length=50)
    

class Farmertable(models.Model):
    fid = models.AutoField(primary_key=True)
    f_name=models.CharField(max_length=100)
    f_phone=models.CharField(max_length=100)
    f_address=models.CharField(max_length=100)
    f_email=models.CharField(max_length=100)
    f_pass=models.CharField(max_length=100)
    f_loca=models.CharField(max_length=100)
    f1=models.CharField(max_length=100,default="" )
    f2=models.CharField(max_length=100,default="" )  
    f3=models.CharField(max_length=100,default="" )  
    f4=models.CharField(max_length=100,default="" )  
    f5=models.CharField(max_length=100,default="" )  
    
class Usertable(models.Model):
    uid = models.AutoField(primary_key=True)
    u_name=models.CharField(max_length=100)
    u_phone=models.CharField(max_length=100)
    u_address=models.CharField(max_length=100)
    u_email=models.CharField(max_length=100)
    u_pass=models.CharField(max_length=100)
    u_loca=models.CharField(max_length=100)
    u1=models.CharField(max_length=100,default="" )
    u2=models.CharField(max_length=100,default="" )  
    u3=models.CharField(max_length=100,default="" )  
    u4=models.CharField(max_length=100,default="" )  
    u5=models.CharField(max_length=100,default="" )  
    
class Investortable(models.Model):
    invid = models.AutoField(primary_key=True)
    inv_name=models.CharField(max_length=100)
    inv_phone=models.CharField(max_length=100)
    inv_address=models.CharField(max_length=100)
    inv_email=models.CharField(max_length=100)
    inv_pass=models.CharField(max_length=100)
    inv_loca=models.CharField(max_length=100)
    inv1=models.CharField(max_length=100,default="" )
    inv2=models.CharField(max_length=100,default="" )  
    inv3=models.CharField(max_length=100,default="" )  
    inv4=models.CharField(max_length=100,default="" )  
    inv5=models.CharField(max_length=100,default="" ) 
    
    
class Product_table(models.Model):
    pid = models.AutoField(primary_key=True)
    p_date=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_img=models.ImageField(max_length=100)
    p_cat=models.CharField(max_length=100)
    p_stock=models.CharField(max_length=100)
    p_rate=models.CharField(max_length=100)
    fid=models.ForeignKey(Farmertable,on_delete=models.CASCADE,blank=True,null=True)
    pro1=models.CharField(max_length=100,default="" )
    pro2=models.CharField(max_length=100,default="" )
    
    
class Cart_table(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_date=models.CharField(max_length=100)
    cart_name=models.CharField(max_length=100)
    cart_cat=models.CharField(max_length=100)
    cart_stock=models.CharField(max_length=100)
    cart_rate=models.CharField(max_length=100)
    uid=models.ForeignKey(Usertable,on_delete=models.CASCADE,blank=True,null=True)
    pid=models.ForeignKey(Product_table,on_delete=models.CASCADE,blank=True,null=True)
    cart1=models.CharField(max_length=100,default="" )
    cart2=models.CharField(max_length=100,default="" )
    cart3=models.CharField(max_length=100,default="" )
    
    
class Schemetable(models.Model):
    loanid = models.AutoField(primary_key=True)
    loan_name=models.CharField(max_length=100)
    type_loan=models.CharField(max_length=100)
    repayment=models.ImageField(max_length=100)
    docu=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    interest=models.CharField(max_length=100)
    invid=models.ForeignKey(Investortable,on_delete=models.CASCADE,blank=True,null=True)
    loan1=models.CharField(max_length=100,default="" )
    loan2=models.CharField(max_length=100,default="" )
    
class Loantable(models.Model):
    appid = models.AutoField(primary_key=True)
    app_amount=models.CharField(max_length=100)
    docmnt1=models.ImageField(max_length=100)
    docmnt2=models.ImageField(max_length=100)
    docmnt3=models.ImageField(max_length=100)
    fid=models.ForeignKey(Farmertable,on_delete=models.CASCADE,blank=True,null=True)
    loanid=models.ForeignKey(Schemetable,on_delete=models.CASCADE,blank=True,null=True)
    app1=models.CharField(max_length=100,default="" )
    app2=models.CharField(max_length=100,default="" )
    
class Supply_table(models.Model):
    sid = models.AutoField(primary_key=True)
    # s_date=models.CharField(max_length=100)
    s_name=models.CharField(max_length=100)
    s_img=models.ImageField(max_length=100)
    s_cat=models.CharField(max_length=100)
    s_stock=models.CharField(max_length=100)
    s_rate=models.CharField(max_length=100)
    fid=models.ForeignKey(Farmertable,on_delete=models.CASCADE,blank=True,null=True)
    sup1=models.CharField(max_length=100,default="" )
    sup2=models.CharField(max_length=100,default="" )
    
class Supply_cart_table(models.Model):
    s_cart_id = models.AutoField(primary_key=True)
    s_cart_date=models.CharField(max_length=100)
    s_cart_name=models.CharField(max_length=100)
    s_cart_cat=models.CharField(max_length=100)
    s_cart_stock=models.CharField(max_length=100)
    s_cart_rate=models.CharField(max_length=100)
    fid=models.ForeignKey(Farmertable,on_delete=models.CASCADE,blank=True,null=True)
    sid=models.ForeignKey(Supply_table,on_delete=models.CASCADE,blank=True,null=True)
    s_cart1=models.CharField(max_length=100,default="" )
    s_cart2=models.CharField(max_length=100,default="" )
    s_cart3=models.CharField(max_length=100,default="" )