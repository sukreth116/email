from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def siteadminhome(request):
    return render(request,'siteadminhome.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    siteadmin=siteadmin_tb.objects.filter(username=username,password=password)
    user=user_register_tb.objects.filter(username=username,password=password)
    if  siteadmin.count()>0:
        request.session['id']=siteadmin[0].id
        return render(request,'siteadminhome.html')
    elif    user.count()>0:
            request.session['id']=user[0].id
            return render(request,'userhome.html')
    else:
        return render(request,'login.html')
def addhobby(request):
    return render(request,'addhobby.html')
def addhobbyAction(request):
    hobbyname=request.POST['hobbyname']
    admin=hobbyname_tb(hobby=hobbyname)
    admin.save()
    return redirect('addhobby')
def hobbyfactor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,'hobbyfactor.html',{"hobby":hobby})
def hobbyfactorAction(request):
    hobbyname=request.POST['hobbyname']
    factor=request.POST['factor']
    user=hobbyfactor_tb(hobbyid_id=hobbyname,factor=factor)
    user.save()
    messages.add_message(request,messages.INFO,"A new factor for hobby is added")
    return redirect('hobbyfactor')
def addseason(request):
    return render(request,'addseason.html')
def addseasonAction(request):
    seasonname=request.POST['seasonname']
    admin=season_tb(season_name=seasonname)
    admin.save()
    messages.add_message(request,messages.INFO,"A new season is added")
    return redirect('addseason')
def seasonfactor(request):
    season=season_tb.objects.all()
    return render(request,'seasonfactor.html',{"season":season})
def seasonfactorAction(request):
    seasonid=request.POST['seasonid']
    seasonfactor=request.POST['seasonfactor']
    admin=seasonfactor_tb(seasonfactor=seasonfactor,seasonid_id=seasonid)
    admin.save()
    messages.add_message(request,messages.INFO,"A new factor for season is added")
    return redirect('seasonfactor')
def seasoncountry(request):
    seasons=season_tb.objects.all()
    #ste=state_tb.objects.all()
    countries=country_tb.objects.all()
    return render(request,'seasoncountry.html',{"season":seasons,"country":countries})
def getstate_season(request):
    country=request.GET['country']
    ste=state_tb.objects.filter(countryid=country)
    return render(request,'getstate_season.html',{"state":ste})
def getfactor_season(request):
    season=request.GET['season']
    sfact=seasonfactor_tb.objects.filter(seasonid=season)
    return render(request,'getfactor_season.html',{"sfact":sfact})
def seasoncountryAction(request):
    country=request.POST['country']
    state=request.POST['state']
    season=request.POST['season']
    seasonfactor=request.POST['seasonfactor']
    month=request.POST['month']
    admin=seasoncountry_tb(countryid_id=country,stateid_id=state,seasonid_id=season,season_factorid_id=seasonfactor,months=month)
    admin.save()
    messages.add_message(request,messages.INFO,"Country and Season added")
    return redirect('seasoncountry')
def agefactor(request):
    return render(request,'agefactor.html')
def agefactorAction(request):
    min_age=request.POST['min_age']
    max_age=request.POST['max_age']
    age_factor=request.POST['age_factor']
    admin=agefactor_tb(minimum_age=min_age,maximum_age=max_age,age_factor=age_factor)
    admin.save()
    messages.add_message(request,messages.INFO,"Age Factor Added")
    return redirect('agefactor')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotpasswordAction(request):
    username=request.POST['username']
    phone=request.POST['phone']
    user=user_register_tb.objects.filter(username=username,phone=phone)
    if  user.count()>0:
        request.session['id']=user[0].id
        return render(request,'check_sq.html',{"data":user})
    else:
        return redirect('login')
def check_sqAction(request):
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    user=user_register_tb.objects.filter(security_questions=securityquestion,answers=answer)
    if  user.count()>0:
        request.session['id']=user[0].id
        return render(request,'newpassword.html',{"data":user})
    else:
        return redirect('forgotpassword')
def newpasswordAction(request):
    userid=request.session['id']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if newpassword==confirmpassword:
        passwordupdate=user_register_tb.objects.filter(id=userid).update(password=newpassword)
        return render(request,'login.html')
    else:
        return render(request,'newpassword.html')
def logout(request):
    request.session.flush()
    return redirect('index')
def userlist(request):
    user=user_register_tb.objects.all()
    return render(request,'userlist.html',{'view':user})
def deleteuser(request,id):
    uid=user_register_tb.objects.filter(id=id).delete()
    return redirect('userlist')
