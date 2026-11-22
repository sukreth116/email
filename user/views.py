from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime



# Create your views here.
def userhome(request):
    return render(request,'userhome.html')
def userregister(request):
    coun=country_tb.objects.all()
    ste=state_tb.objects.all()
    hby=hobbyname_tb.objects.all()
    return render(request,'userregister.html',{"country":coun,"state":ste,"hobby":hby})
def getstate(request):
    country=request.GET['country']
    ste=state_tb.objects.filter(countryid=country)
    return render(request,'getstate.html',{"state":ste})
def userRegisterAction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    country=request.POST['country']
    state=request.POST['state']
    dob=request.POST['dob']
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    user=user_register_tb(name=name,address=address,gender=gender,phone=phone,countryid_id=country,stateid_id=state,dob=dob,security_questions=securityquestion,answers=answer,username=username+"@mymail.com",password=password)
    user.save()
    check=request.POST.getlist('checkbox')
    for c in check:
        #hobbies=hobby_tb.objects.filter(id=c)
        hoby=hobby_tb(hobbyid_id=c,userid_id=user.id)
        hoby.save()            
    return redirect('userregister')
def new_message(request):
    return render(request,'newmessage.html')
def new_messageAction(request):
    senderid=request.session['id']
    receiver=request.POST['receiver']
    rec=user_register_tb.objects.get(username=receiver)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    user=message_tb(senderid_id=senderid,receiverid=rec,message=message,subject=subject,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,"Message send")
    return redirect('new_message')
def checkusername(request):
    username=request.GET['usernameid']
    user=user_register_tb.objects.filter(username=username)
    if len(user)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def checkreceiver(request):
    receiver=request.GET['receiverid']
    user=user_register_tb.objects.filter(username=receiver)
    if  len(user)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def sent_message(request):
    senderid=request.session['id']
    status=['deleted by receiver','pending']
    usermessage=message_tb.objects.filter(senderid=senderid,status__in=status)    
    return render(request,'sent_message.html',{"viewmessage":usermessage})
def deletemessage(request,id):
    delete=message_tb.objects.filter(id=id).delete()
    return redirect('sent_message')
def inbox(request):
    receiverid=request.session['id']
    status=['delete by sender','pending']#before applying filter
    agefactor=customer_agefactor_tb.objects.filter(userid=receiverid)
    for factor in agefactor:
        msg=message_tb.objects.filter(receiverid=receiverid,filter_status="pending",message__icontains=factor.factorid.age_factor).exclude(receiverid__in=blacklist_tb.objects.filter(userid=receiverid).values('contactid')).update(filter_status="filtered")
    hobbyfactor=customer_hobbyfactor_tb.objects.filter(userid=receiverid)
    for factor1 in hobbyfactor:
        msg1=message_tb.objects.filter(receiverid=receiverid,filter_status="pending",message__icontains=factor1.factorid.factor).exclude(receiverid__in=blacklist_tb.objects.filter(userid=receiverid).values('contactid')).update(filter_status="filtered")
    seasoncountryfactor=customer_seasoncountry_tb.objects.filter(userid=receiverid)
    for factor2 in seasoncountryfactor:
        msg2=message_tb.objects.filter(receiverid=receiverid,filter_status="pending",message__icontains=factor2.factorid.seasonfactor).exclude(receiverid__in=blacklist_tb.objects.filter(userid=receiverid).values('contactid')).update(filter_status="filtered")
    contact=contact_tb.objects.filter(userid=receiverid)
    for c in contact:
        msg3=message_tb.objects.filter(receiverid=receiverid,filter_status="pending",senderid=c.contactid).update(filter_status="filtered")
    inboxmessage=message_tb.objects.filter(receiverid=receiverid,status__in=status,filter_status='filtered').exclude(id__in=trash_tb.objects.filter(receiverid=receiverid).values('messageid_id'))
    #inboxmessage=message_tb.objects.filter(receiverid=receiverid,status__in=status).exclude(id__in=trash_tb.objects.filter(receiverid=receiverid).values('messageid'))
    return render(request,'inbox.html',{"viewmessage":inboxmessage})
def move_to_trash(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    check=request.POST.getlist('checkbox')
    for c in check:
        message=message_tb.objects.get(id=c)
        receiverid=request.session['id']
        user=trash_tb(time=time,date=date,messageid=message,receiverid_id=receiverid)
        user.save()
    return redirect('inbox')
def trash(request):
    receiver=request.session['id']
    viewtrash=trash_tb.objects.filter(receiverid=receiver)
    return render(request,'trash.html',{"view":viewtrash})
def delete_trash(request,id):
    trash=trash_tb.objects.filter(id=id)
    message=message_tb.objects.filter(id=trash[0].messageid_id)
    status=message[0].status
    if status=='pending':
        upd1=message_tb.objects.filter(id=trash[0].messageid_id).update(status="deleted by receiver")
        upd2=trash_tb.objects.filter(id=id).delete()
    return redirect('trash')
def forward(request,id):
    frwd=message_tb.objects.filter(id=id)
    return render(request,'forward.html',{"view":frwd})
def forwardAction(request):
    senderid=request.session['id']
    receiver=request.POST['receiver']
    receiverid=user_register_tb.objects.get(username=receiver)
    message=request.POST['message']
    subject=request.POST['subject']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    user=message_tb(senderid_id=senderid,receiverid=receiverid,message=message,subject=subject,date=date,time=time)
    user.save()
    return redirect('inbox')
def reply(request,id):
    rply=message_tb.objects.filter(id=id)
    return render(request,'reply.html',{"view":rply})
def replyAction(request):
    senderid=request.session['id']
    receiver=request.POST['receiver']
    receiverid=user_register_tb.objects.get(username=receiver)
    message=request.POST['message']
    subject=request.POST['subject']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    user=message_tb(senderid_id=senderid,receiverid=receiverid,message=message,subject=subject,date=date,time=time)
    user.save()
    return redirect('inbox')
def addcontact(request):
    return render(request,'addcontact.html')
def check_username_contact(request):
    contactid=request.GET['contact']
    username=user_register_tb.objects.filter(username=contactid)
    if  len(username)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({"valid":msg})
def addcontactAction(request):
    userid=request.session['id']
    contact=request.POST['contact']
    contactid=user_register_tb.objects.get(username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=contact_tb(userid_id=userid,contactid=contactid,name=name,remarks=remarks,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,"Contact saved")
    return redirect('addcontact')
def addblacklist(request):
    return render(request,'addblacklist.html')
def addblacklistAction(request):
    userid=request.session['id']
    contact=request.POST['contact']
    contactid=user_register_tb.objects.get(username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=blacklist_tb(userid_id=userid,contactid=contactid,name=name,remarks=remarks,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,"Contact added to blacklist")
    return redirect('addblacklist')
def viewcontacts(request):
    userid=request.session['id']
    contacts=contact_tb.objects.filter(userid=userid)
    return render(request,'viewcontacts.html',{"view":contacts})
def deletecontact(request,id):
    delete=contact_tb.objects.filter(id=id).delete()
    return redirect('viewcontacts')
def viewblacklist(request):
    userid=request.session['id']
    blacklist=blacklist_tb.objects.filter(userid=userid)
    return render(request,'viewblacklist.html',{"view":blacklist})
def deleteblacklist(request,id):
    delete=blacklist_tb.objects.filter(id=id).delete()
    return redirect('viewblacklist')
def move_to_blacklist(request,id):
    user=request.session['id']
    move=contact_tb.objects.filter(id=id)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    name=move[0].name
    remarks=move[0].remarks
    contactid=move[0].contactid
    user=blacklist_tb(name=name,remarks=remarks,contactid=contactid,userid_id=user,date=date,time=time)
    user.save()
    move.delete()    
    return redirect('viewcontacts')
def customer_hobbyfactor(request):
    userid=request.session['id']
    hobby=hobby_tb.objects.filter(userid=userid)
    return render(request,'customer_hobbyfactor.html',{"view":hobby})
def getfactor_customerhobby(request):
    hobby=request.GET['hobby']
    factor=hobbyfactor_tb.objects.filter(hobbyid=hobby)
    return render(request,'getfactor_customerhobby.html',{"view":factor})
def customer_hobbyfactorAction(request):
    userid=request.session['id']
    hobby=request.POST['hobby']
    hobbyfactor=request.POST['hobbyfactor']
    user=customer_hobbyfactor_tb(factorid_id=hobbyfactor,hobbyid_id=hobby,userid_id=userid)
    user.save()
    return redirect('customer_hobbyfactor')
def customer_agefactor(request):
    userid=request.session['id']
    user=user_register_tb.objects.filter(id=userid)
    birthdate=user[0].dob
    by=birthdate.split('-')
    ty=by[0]
    date=datetime.date.today()
    year=date.year
    age=year-int(ty)
    useragefactor=agefactor_tb.objects.filter(minimum_age__lte=age,maximum_age__gte=age)
    return render(request,'customer_agefactor.html',{"view":useragefactor})
def customer_agefactorAction(request):
    userid=request.session['id']
    factorid=request.POST['agefactor']
    user=customer_agefactor_tb(userid_id=userid,factorid_id=factorid)
    user.save()
    return redirect('customer_agefactor')
def customer_seasoncountryfactor(request):
    userid=request.session['id']
    user=user_register_tb.objects.filter(id=userid)
    countryid=user[0].countryid
    stateid=user[0].stateid
    date=datetime.date.today()
    month=date.month
    fltr=seasoncountry_tb.objects.filter(countryid=countryid,stateid=stateid,months=month)
    return render(request,'customer_seasoncountryfactor.html',{"view":fltr})
def customer_seasoncountryfactorAction(request):
    userid=request.session['id']
    seasonfactor=request.POST['seasonfactor']
    user=customer_seasoncountry_tb(userid_id=userid,factorid_id=seasonfactor)
    user.save()
    return redirect('customer_seasoncountryfactor')
def update_user_profile(request):
    sender=request.session['id']
    upd=user_register_tb.objects.filter(id=sender)
    country=country_tb.objects.all()
    hobby=hobbyname_tb.objects.all()
    userhobby=hobby_tb.objects.filter(userid=sender)
    return render(request,'update_user_profile.html',{"view":upd,"countries":country,"hobby":hobby,"userhobby":userhobby})
def update_user_profileAction(request):
    sender=request.session['id']
    upd=user_register_tb.objects.filter(id=sender)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    country=request.POST['country']
    state=request.POST['state']
    dob=request.POST['dob']
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    user=user_register_tb.objects.filter(id=sender).update(name=name,address=address,gender=gender,phone=phone,countryid_id=country,stateid_id=state,dob=dob,security_questions=securityquestion,answers=answer,username=username,password=password)
    firsthobby=hobby_tb.objects.filter(userid=sender).delete()
    check=request.POST.getlist('hobbies')
    print(check)
    for c in check:
        hobby=hobby_tb(hobbyid_id=c,userid_id=sender)
        hobby.save()
    return redirect('update_user_profile')
def view_spam_messages(request):
    receiverid=request.session['id']
    status=['deleted by sender','pending']
    mess=message_tb.objects.filter(receiverid=receiverid,status__in=status,filter_status__in=status)
    return render(request,'viewspammail.html',{"view":mess})
def delete_spam_messages(request,id):
    spam=message_tb.objects.filter(id=id)
    status=spam[0].status
    if status=="deleted by sender":
        delspam=message_tb.objects.filter(id=id).delete()
    else:
        updatespam=message_tb.objects.filter(id=id).update(status="deleted by reciever")
    return redirect('view_spam_messages')