from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from email.policy import default
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from .models import *
from django.db.models import Q
import datetime
from django.utils import timezone
import pytz 
from django.core.files.storage import FileSystemStorage



def index(request):
    return render(request, 'index.html')
def com_home(request):
    return render(request, 'com_home.html')
def admin_home(request):
    return render(request, 'admin/admin_home.html')
def farmer_home(request):
    return render(request, 'farmer/farmer_home.html')
def user_home(request):
    return render(request, 'user/user_home.html')
def inv_home(request):
    return render(request, 'investor/inv_home.html')


def farmer_reg(request):
    msg=""
    if request.POST:
        name=request.POST["a1"]
        phone=request.POST["a2"]
        loca=request.POST["a3"]
        address=request.POST["a4"]
        email=request.POST["a5"]
        passs=request.POST["a6"]
        cpass=request.POST["a7"]
        
        if cpass==passs:
            if(Logintable.objects.filter(l_email=email).exists()):
                msg="email already exist"
            else:
                
                obj=Farmertable.objects.create(f_name=name,f_phone=phone,f_email=email,f_pass=passs,f_loca=loca,f_address=address,f1="pending")
                obj.save()
                obj1=Logintable.objects.create(l_email=email,l_pass=passs,l_type="farmer",l_status="pending")
                obj1.save()
                # msg="Welcome"
                
                return HttpResponseRedirect("/login")
        else:
            msg="password mismatch"
            # print(msg)
            
            return render(request,"farmer_reg.html",{"msg":msg})

    return render(request, 'farmer_reg.html')

def user_reg(request):
    msg=""
    if request.POST:
        name=request.POST["a1"]
        phone=request.POST["a2"]
        loca=request.POST["a3"]
        address=request.POST["a4"]
        email=request.POST["a5"]
        passs=request.POST["a6"]
        cpass=request.POST["a7"]
        
        if cpass==passs:
            if(Logintable.objects.filter(l_email=email).exists()):
                msg="email already exist"
            else:
                
                obj=Usertable.objects.create(u_name=name,u_phone=phone,u_email=email,u_pass=passs,u_loca=loca,u_address=address,u1="pending")
                obj.save()
                obj1=Logintable.objects.create(l_email=email,l_pass=passs,l_type="user",l_status="pending")
                obj1.save()
                # msg="Welcome"
                
                return HttpResponseRedirect("/login")
        else:
            msg="password mismatch"
            # print(msg)
            
            return render(request,"farmer_reg.html",{"msg":msg})

    return render(request, 'farmer_reg.html')


def inv_reg(request):
    msg=""
    if request.POST:
        name=request.POST["a1"]
        phone=request.POST["a2"]
        loca=request.POST["a3"]
        address=request.POST["a4"]
        email=request.POST["a5"]
        passs=request.POST["a6"]
        cpass=request.POST["a7"]
        
        if cpass==passs:
            if(Logintable.objects.filter(l_email=email).exists()):
                msg="email already exist"
            else:
                
                obj=Investortable.objects.create(inv_name=name,inv_phone=phone,inv_email=email,inv_pass=passs,inv_loca=loca,inv_address=address,inv1="pending")
                obj.save()
                obj1=Logintable.objects.create(l_email=email,l_pass=passs,l_type="investor",l_status="pending")
                obj1.save()
                # msg="Welcome"
                
                return HttpResponseRedirect("/login")
        else:
            msg="password mismatch"
            # print(msg)
            
            return render(request,"inv_reg.html",{"msg":msg})

    return render(request, 'inv_reg.html')



def login(request):
  
    msg=""
    # msgg=request.GET.get('msg')
    # print(msgg)
    if request.POST: 
        msg=""
        log_user=request.POST["log1"]
        log_pass=request.POST["log2"]
        request.session["unme"]=log_user
        obj=Logintable.objects.filter(Q(l_email=log_user)&Q(l_pass=log_pass))
        if obj:
            if (obj[0].l_type=="farmer"):
                if (obj[0].l_status=="approved"):
                
                    obj1=Farmertable.objects.filter(f_email=log_user)
                    request.session["fid"]=obj1[0].fid
                    return HttpResponseRedirect("/farmer_home")
                else:
                    msg="please wait..."
# -------------------------------------------------------------------------
            elif (obj[0].l_type=="user"):
                if (obj[0].l_status=="approved"):
                
                    obj1=Usertable.objects.filter(u_email=log_user)
                    request.session["uid"]=obj1[0].uid
                    return HttpResponseRedirect("/user_home")
                else:
                    msg="please wait..."
# -------------------------------------------------------------------------
            elif (obj[0].l_type=="investor"):
                if (obj[0].l_status=="approved"):
                
                    obj1=Investortable.objects.filter(inv_email=log_user)
                    request.session["invid"]=obj1[0].invid
                    return HttpResponseRedirect("/inv_home")
                else:
                    msg="please wait..."
# -----------------------------------------------------------------------------
            # if (obj[0].l_type=="media"):
            #     if (obj[0].l_status=="approved"):
                
            #         obj1=Mediatable.objects.filter(n_email=log_user)
            #         request.session["mid"]=obj1[0].nid
            #         return HttpResponseRedirect("/media_home")
            
            elif (obj[0].l_type=="admin"):
                obj1=Logintable.objects.filter(l_email=log_user)
                request.session["aid"]=obj1[0].lid
                return HttpResponseRedirect("/admin_home")
            
            
        else:
            msg="invalid username and password"
            print("msg "+msg)
            # return HttpResponseRedirect("/login")
    return render(request,'login.html',{"msg":msg})


def admin_view_far(request):
    abc=Farmertable.objects.filter(f1="pending")
    if request.POST:
        a1=request.POST['a1']
        a2=request.POST['a2']
        a2=int(a2)
        print("========",a2)
        if a2==1:
            up1=Farmertable.objects.filter(fid=a1).update(f1="approved")
            lup=Farmertable.objects.filter(fid=a1)
            loup=lup[0].f_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="approved")
            
        elif a2==2:
            up1=Farmertable.objects.filter(fid=a1).update(f1="rejected")
            lup=Farmertable.objects.filter(fid=a1)
            loup=lup[0].f_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="rejected")
        
    return render(request,'admin/admin_view_far.html',{"abc":abc})

def admin_view_user(request):
    abc=Usertable.objects.filter(u1="pending")
    if request.POST:
        a1=request.POST['a1']
        a2=request.POST['a2']
        a2=int(a2)
        print("========",a2)
        if a2==1:
            up1=Usertable.objects.filter(uid=a1).update(u1="approved")
            lup=Usertable.objects.filter(uid=a1)
            loup=lup[0].u_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="approved")
            
        elif a2==2:
            up1=Usertable.objects.filter(uid=a1).update(u1="rejected")
            lup=Usertable.objects.filter(uid=a1)
            loup=lup[0].u_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="rejected")
        
    return render(request,'admin/admin_view_user.html',{"abc":abc})

def admin_view_inv(request):
    abc=Investortable.objects.filter(inv1="pending")
    if request.POST:
        a1=request.POST['a1']
        a2=request.POST['a2']
        a2=int(a2)
        print("========",a2)
        if a2==1:
            up1=Investortable.objects.filter(invid=a1).update(inv1="approved")
            lup=Investortable.objects.filter(invid=a1)
            loup=lup[0].inv_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="approved")
            
        elif a2==2:
            up1=Investortable.objects.filter(invid=a1).update(inv1="rejected")
            lup=Investortable.objects.filter(invid=a1)
            loup=lup[0].inv_email
            up2=Logintable.objects.filter(l_email=loup).update(l_status="rejected")
        
    return render(request,'admin/admin_view_inv.html',{"abc":abc})


def farmer_add_pro(request):
    fid=request.session.get('fid')
    print(fid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("Product Name")
        category = request.POST.get("Category")
        stock = request.POST.get("Stock")
        price = request.POST.get("Price")
        fid=request.session["fid"]
        print(fid)
        ab = Product_table.objects.create(
                p_name=productname, p_img=myfile, p_stock=stock, p_rate=price, p_cat=category,p_date ="date",fid_id=fid)
        ab.save()    
        msg = "Added sucessfully"
    # return render(request, 'Admin/admin_add_product.html',{"msg": msg})
    return render(request,'farmer/farmer_add_pro.html',{"msg": msg})

# =======================view product= ===============================

def farmer_view_product(request):
    msg = request.GET.get("msg")
    fid=request.session.get('fid')
    
    abc=Product_table.objects.filter(fid_id=fid)
    return render(request, 'farmer/farmer_view_pro.html',{"abc":abc,"msg":msg})


# ===============================admin delete product===========================


def delete_product(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Product_table.objects.filter(pid=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/farmer_view_product?msg="+msg)


def update_product(request):
    id=request.GET["id"]
    
    abc=Product_table.objects.filter(pid=id)    
    if request.POST:
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        a3=request.POST["a3"]
        qun = abc[0].p_stock
        # qty = request.POST["a4"]
        # print(qty)
            # Total = int(rate)*int(qty)
        upqun = int(qun)+int(a2)
        upqun = str(upqun)
        abc=Product_table.objects.filter(pid=id).update(p_name=a1,p_stock=upqun,p_rate=a3)
        msg="updated"
        
        print(id)
        print("-----------------------------------------")
        return HttpResponseRedirect("/farmer_view_product?msg="+msg)
    return render(request,"farmer/farmer_update_pro.html",{"abc":abc})



# ===============================user veiw product=========================================

def user_view_product(request):
    msg = request.GET.get("msg")
    uid=request.session['uid']
    
    
    abc=Product_table.objects.all()
    current_date = datetime.date.today()
    current_time = timezone.now()
    current_time = timezone.now() 
    timezone_India = pytz.timezone('Asia/Kolkata') 
    India_time = current_time.astimezone(timezone_India) 

    # id=request.GET["id"]
    if request.POST:
        # addadd=Usertable.objects.filter(userid=uid)
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        # a3=request.POST["a3"]
        obc=Product_table.objects.filter(pid=a1)  
        qun = obc[0].p_stock
        rate=obc[0].p_rate
        
      
        upqun = int(qun)-int(a2)
        total=int(rate)*int(a2)
        # ad=addadd[0].user_address
        # print(ad)
        # b="add details"
        # if ad==b:
        #     msg=""
        #     return HttpResponseRedirect("/update_profile?msg="+msg)
            
        
        if upqun>0:
            upqun = str(upqun)
            total=str(total)
            abcd=Product_table.objects.filter(pid=a1).update(p_stock=upqun)
            obj=Cart_table.objects.create(pid_id=a1, cart_stock=a2,cart_date=India_time,cart_rate=total,uid_id=uid,cart_name="user",cart_cat="booked")
            obj.save
            print("============================",upqun)
            print(total)
            print(India_time)
            print(uid)
            msg="added to user cart"
            
        else:
            msg="item out of stock"
    # return HttpResponseRedirect("/admin_view_user?msg="+msg)
    return render(request, 'user/user_view_product.html',{"abc":abc,"msg":msg})


def user_booked_product(request):
    msg=""
    btn=""
    uid=request.session['uid']

    abc=Cart_table.objects.filter(uid_id=uid,cart_cat="booked")
    return render(request, 'user/view_booked_product.html',{"abc":abc,"msg":msg})

def payment(request):
    uid=request.session.get('uid')
    
    
    total = 0
    abc = Cart_table.objects.filter(cart_cat="booked",uid_id=uid)
    for i in abc:
        total += int(i.cart_rate)
    print(total)
    if request.POST:
        obj=Cart_table.objects.filter(uid_id=uid).update(cart_cat="paid")
    return render(request,"user/payment.html",{"total":total})
def history(request):
    uid=request.session.get('uid')
    abc = Cart_table.objects.filter(cart_cat="paid",uid_id=uid)
    return render(request,"user/history.html",{"abc":abc})
    

def farmer_view_booked_product(request):
    msg=""
    btn=""
    total=0
    fid=request.session['fid']
   
    abc = Cart_table.objects.filter(cart_cat="paid")
    if abc:
        id=Cart_table.objects.filter(cart_cat="paid")
        id=id[0].uid_id
        abcd = Usertable.objects.filter(uid=id)
    for i in abc:
        total += int(i.cart_rate)
    print("============",total)
    if request.POST:
        abc = Cart_table.objects.filter(uid_id=id).update(cart_cat="deliverd")



    abc=Cart_table.objects.filter(pid_id__fid=fid,cart_cat="paid")
    return render(request, 'farmer/farmer_view_booked_product.html',{"abc":abc,"msg":msg,"total":total})

def farmer_view_inv(request):
    abc=Investortable.objects.filter(inv1="approved")
    return render(request, 'farmer/farmer_view_inv.html',{"abc":abc})

def add_scheme(request):
    msg=""
    if request.POST:
        loan_name=request.POST["a1"]
        type_loan=request.POST["a2"]
        repayment=request.POST["a3"]
        docu=request.POST["a4"]
        amount=request.POST["a5"]
        interest=request.POST["a6"]
        invid=request.session.get('invid')
        if(Schemetable.objects.filter(loan_name=loan_name).exists()):
            msg="Plan already exist"
        else:
            obj=Schemetable.objects.create(loan_name=loan_name,
                                            type_loan=type_loan,
                                            repayment=repayment,
                                            docu=docu,
                                            amount=amount,
                                            interest=interest,
                                            invid_id=invid)
            obj.save()
    return render(request, 'investor/inv_add_scheme.html')

def farmer_view_plan(request):
    id=request.GET.get('id')
    abc=Schemetable.objects.filter(invid_id=id)
    return render(request, 'farmer/farmer_view_plan.html',{"abc":abc})
def farmer_apply_plan(request):
    id=request.GET.get('id')
    print(id)
    if request.POST:
        app_amount=request.POST["a2"]
        doc1=request.POST.get("a3")
        myfile1 = request.FILES["a3"]
        doc2=request.POST.get("a4")
        myfile2 = request.FILES["a4"]
        
        doc3=request.POST.get("a5")
        myfile3 = request.FILES["a5"]
        
        # amount=request.POST["a5"]
        fid=request.session.get('fid')
        if(Loantable.objects.filter(fid_id=fid,loanid_id=id).exists()):
            msg=" already Applied"
        else:
            obj=Loantable.objects.create(app_amount=app_amount,
                                            docmnt1=myfile1,
                                            docmnt2=myfile2,
                                            docmnt3=myfile3,
                                            loanid_id=id,
                                            fid_id=fid)
            obj.save()
    return render(request, 'farmer/farmer_apply_loan.html')

def calc(request):
    return render(request,'farmer/calc.html')

def inv_view_loan_req(request):
    invid=request.session.get('invid')
    abc=Loantable.objects.filter(loanid_id__invid=invid,app1="")
    return render(request,'investor/inv_view_loan_req.html',{"abc":abc})

def doc(request):
    id=request.GET.get('id')
    abc=Loantable.objects.filter(appid=id)
    if request.POST:
        a1=request.POST['a1']
        a2=request.POST['a2']
        a1=int(a1)
        if a1==1:
            print("===================================",a2)
            app=Loantable.objects.filter(appid=a2).update(app1="approved")
        elif a1==2:
            app1=Loantable.objects.filter(appid=a2).update(app1="Rejected")
    return render(request, 'investor/doc.html',{"abc":abc})

def farmer_view_loan_status(request):
    fid=request.session.get('fid')
    abc=Loantable.objects.filter(fid_id=fid)
    return render(request, 'farmer/farmer_view_loan_status.html',{"abc":abc})
    
    
def add_equipment(request):
    return render(request, 'admin/add_equipment.html')
def farmer_view_supply(request):
    return render(request, 'farmer/farmer_view_supply.html')

def admin_add_seed(request):
    # fid=request.session.get('fid')
    # print(fid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("a1")
        category = request.POST.get("a4")
        stock = request.POST.get("a2")
        price = request.POST.get("a3")
        # fid=request.session["fid"]
        # print(fid)
        ab = Supply_table.objects.create(
                s_name=productname, s_img=myfile, s_stock=stock, s_rate=price, s_cat=category)
        ab.save()    
        msg = "Added sucessfully"
    return render(request, 'admin/admin_add_seed.html',{"msg":msg})
def admin_add_fert(request):
    # fid=request.session.get('fid')
    # print(fid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("a1")
        category = request.POST.get("a4")
        stock = request.POST.get("a2")
        price = request.POST.get("a3")
        # fid=request.session["fid"]
        # print(fid)
        ab = Supply_table.objects.create(
                s_name=productname, s_img=myfile, s_stock=stock, s_rate=price, s_cat=category)
        ab.save()    
        msg = "Added sucessfully"
    return render(request, 'admin/admin_add_fert.html',{"msg":msg})
def admin_add_tools(request):
    # fid=request.session.get('fid')
    # print(fid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("a1")
        category = request.POST.get("a4")
        stock = request.POST.get("a2")
        price = request.POST.get("a3")
        # fid=request.session["fid"]
        # print(fid)
        ab = Supply_table.objects.create(
                s_name=productname, s_img=myfile, s_stock=stock, s_rate=price, s_cat=category)
        ab.save()    
        msg = "Added sucessfully"
    return render(request, 'admin/admin_add_tools.html',{"msg":msg})

def admin_view_pro(request):
    msg = request.GET.get("msg")
    # fid=request.session.get('fid')
    
    abc=Supply_table.objects.all()
    return render(request, 'admin/admin_view_pro.html',{"abc":abc,"msg":msg})

def admin_delete_product(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Supply_table.objects.filter(sid=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_pro?msg="+msg)


def admin_update_product(request):
    id=request.GET["id"]
    
    abc=Supply_table.objects.filter(sid=id)    
    if request.POST:
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        a3=request.POST["a3"]
        qun = abc[0].s_stock
        # qty = request.POST["a4"]
        # print(qty)
            # Total = int(rate)*int(qty)
        upqun = int(qun)+int(a2)
        upqun = str(upqun)
        abc=Supply_table.objects.filter(sid=id).update(s_name=a1,s_stock=upqun,s_rate=a3)
        msg="updated"
        
        print(id)
        print("-----------------------------------------")
        return HttpResponseRedirect("/admin_view_pro?msg="+msg)
    return render(request,"admin/admin_update_pro.html",{"abc":abc})

def farmer_view_seed(request):
    msg = request.GET.get("msg")
    fid=request.session['fid']
    
    
    abc=Supply_table.objects.filter(s_cat="seed")
    current_date = datetime.date.today()
    current_time = timezone.now()
    current_time = timezone.now() 
    timezone_India = pytz.timezone('Asia/Kolkata') 
    India_time = current_time.astimezone(timezone_India) 

    # id=request.GET["id"]
    if request.POST:
        # addadd=Usertable.objects.filter(userid=uid)
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        # a3=request.POST["a3"]
        obc=Supply_table.objects.filter(sid=a1)  
        qun = obc[0].s_stock
        rate=obc[0].s_rate
        
      
        upqun = int(qun)-int(a2)
        total=int(rate)*int(a2)
        # ad=addadd[0].user_address
        # print(ad)
        # b="add details"
        # if ad==b:
        #     msg=""
        #     return HttpResponseRedirect("/update_profile?msg="+msg)
            
        
        if upqun>0:
            upqun = str(upqun)
            total=str(total)
            abcd=Supply_table.objects.filter(sid=a1).update(s_stock=upqun)
            obj=Supply_cart_table.objects.create(sid_id=a1, s_cart_stock=a2,s_cart_date=India_time,s_cart_rate=total,fid_id=fid,s_cart_name="user",s_cart_cat="booked")
            obj.save
            print("============================",upqun)
            print(total)
            print(India_time)
            print(fid)
            msg="added to user cart"
            
        else:
            msg="item out of stock"
    # return HttpResponseRedirect("/admin_view_user?msg="+msg)
    return render(request, 'farmer/farmer_view_seed.html',{"abc":abc,"msg":msg})

def farmer_view_fert(request):
    msg = request.GET.get("msg")
    fid=request.session['fid']
    
    
    abc=Supply_table.objects.filter(s_cat="fert")
    current_date = datetime.date.today()
    current_time = timezone.now()
    current_time = timezone.now() 
    timezone_India = pytz.timezone('Asia/Kolkata') 
    India_time = current_time.astimezone(timezone_India) 

    # id=request.GET["id"]
    if request.POST:
        # addadd=Usertable.objects.filter(userid=uid)
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        # a3=request.POST["a3"]
        obc=Supply_table.objects.filter(sid=a1)  
        qun = obc[0].s_stock
        rate=obc[0].s_rate
        
      
        upqun = int(qun)-int(a2)
        total=int(rate)*int(a2)
        # ad=addadd[0].user_address
        # print(ad)
        # b="add details"
        # if ad==b:
        #     msg=""
        #     return HttpResponseRedirect("/update_profile?msg="+msg)
            
        
        if upqun>0:
            upqun = str(upqun)
            total=str(total)
            abcd=Supply_table.objects.filter(sid=a1).update(s_stock=upqun)
            obj=Supply_cart_table.objects.create(sid_id=a1, s_cart_stock=a2,s_cart_date=India_time,s_cart_rate=total,fid_id=fid,s_cart_name="user",s_cart_cat="booked")
            obj.save
            print("============================",upqun)
            print(total)
            print(India_time)
            print(fid)
            msg="added to user cart"
            
        else:
            msg="item out of stock"
    # return HttpResponseRedirect("/admin_view_user?msg="+msg)
    return render(request, 'farmer/farmer_view_fert.html',{"abc":abc,"msg":msg})
def farmer_view_tools(request):
    msg = request.GET.get("msg")
    fid=request.session['fid']
    
    
    abc=Supply_table.objects.filter(s_cat="tool")
    current_date = datetime.date.today()
    current_time = timezone.now()
    current_time = timezone.now() 
    timezone_India = pytz.timezone('Asia/Kolkata') 
    India_time = current_time.astimezone(timezone_India) 

    # id=request.GET["id"]
    if request.POST:
        # addadd=Usertable.objects.filter(userid=uid)
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        # a3=request.POST["a3"]
        obc=Supply_table.objects.filter(sid=a1)  
        qun = obc[0].s_stock
        rate=obc[0].s_rate
        
      
        upqun = int(qun)-int(a2)
        total=int(rate)*int(a2)
        # ad=addadd[0].user_address
        # print(ad)
        # b="add details"
        # if ad==b:
        #     msg=""
        #     return HttpResponseRedirect("/update_profile?msg="+msg)
            
        
        if upqun>0:
            upqun = str(upqun)
            total=str(total)
            abcd=Supply_table.objects.filter(sid=a1).update(s_stock=upqun)
            obj=Supply_cart_table.objects.create(sid_id=a1, s_cart_stock=a2,s_cart_date=India_time,s_cart_rate=total,fid_id=fid,s_cart_name="user",s_cart_cat="booked")
            obj.save
            print("============================",upqun)
            print(total)
            print(India_time)
            print(fid)
            msg="added to user cart"
            
        else:
            msg="item out of stock"
    # return HttpResponseRedirect("/admin_view_user?msg="+msg)
    return render(request, 'farmer/farmer_view_tools.html',{"abc":abc,"msg":msg})


def farmer_view_cart(request):
    msg=""
    btn=""
    fid=request.session['fid']

    abc=Supply_cart_table.objects.filter(fid_id=fid,s_cart_cat="booked")
    return render(request, 'farmer/farmer_view_cart.html',{"abc":abc,"msg":msg})

def farmer_payment(request):
    fid=request.session.get('fid')
    
    
    total = 0
    abc = Supply_cart_table.objects.filter(s_cart_cat="booked",fid_id=fid)
    for i in abc:
        total += int(i.s_cart_rate)
    print(total)
    if request.POST:
        obj=Supply_cart_table.objects.filter(fid_id=fid).update(s_cart_cat="paid")
    return render(request,"farmer/payment.html",{"total":total})

def admin_view_booked_sup(request):
    msg=""
    btn=""
    total=0
    # fid=request.session['fid']
   
    abc = Supply_cart_table.objects.filter(s_cart_cat="paid")
    if abc:
        id=Supply_cart_table.objects.filter(s_cart_cat="paid")
        id=id[0].fid_id
        abcd = Farmertable.objects.filter(fid=id)
    for i in abc:
        total += int(i.s_cart_rate)
    print("============",total)
    if request.POST:
        abc = Supply_cart_table.objects.filter(fid_id=id).update(s_cart_cat="deliverd")



    abc=Supply_cart_table.objects.filter(s_cart_cat="paid")
    return render(request, 'admin/admin_view_booked_sup.html',{"abc":abc,"msg":msg,"total":total})
