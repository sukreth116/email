"""spammail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from siteadmin import views as siteadminview
from user import views as userview
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',siteadminview.index,name="index"),
    path('siteadminhome/',siteadminview.siteadminhome,name="siteadminhome"),
    path('login/',siteadminview.login,name="login"),
    path('loginAction/',siteadminview.loginAction,name="loginAction"),
    path('userregister/',userview.userregister,name="userregister"),
    path('userhome/',userview.userhome,name="userhome"),
    path('getstate/',userview.getstate,name="getstate"),
    path('userRegisterAction/',userview.userRegisterAction,name="userRegisterAction"),
    path('addhobby/',siteadminview.addhobby,name="addhobby"),
    path('addhobbyAction/',siteadminview.addhobbyAction,name="addhobbyAction"),
    path('hobbyfactor/',siteadminview.hobbyfactor,name="hobbyfactor"),
    path('hobbyfactorAction/',siteadminview.hobbyfactorAction,name="hobbyfactorAction"),
    path('addseason/',siteadminview.addseason,name="addseason"),
    path('addseasonAction/',siteadminview.addseasonAction,name="addseasonAction"),
    path('seasonfactor/',siteadminview.seasonfactor,name="seasonfactor"),
    path('seasonfactorAction/',siteadminview.seasonfactorAction,name="seasonfactorAction"),
    path('seasoncountry/',siteadminview.seasoncountry,name="seasoncountry"),
    path('getstate_season/',siteadminview.getstate_season,name="getstate_season"),
    path('getfactor_season/',siteadminview.getfactor_season,name="getfactor_season"),
    path('seasoncountryAction/',siteadminview.seasoncountryAction,name="seasoncountryAction"),
    path('agefactor/',siteadminview.agefactor,name="agefactor"),
    path('agefactorAction/',siteadminview.agefactorAction,name="agefactorAction"),
    path('new_message/',userview.new_message,name="new_message"),
    path('new_messageAction/',userview.new_messageAction,name="new_messageAction"),
    path('checkusername/',userview.checkusername,name="checkusername"),
    path('checkreceiver/',userview.checkreceiver,name="checkreceiver"),
    path('sent_message/',userview.sent_message,name="sent_message"),
    path('deletemessage<int:id>/',userview.deletemessage,name="deletemessage"),
    path('inbox/',userview.inbox,name="inbox"),
    path('move_to_trash/',userview.move_to_trash,name="move_to_trash"),
    path('trash/',userview.trash,name="trash"),
    path('delete_trash<int:id>/',userview.delete_trash,name="delete_trash"),
    path('forward<int:id>/',userview.forward,name="forward"),
    path('forwardAction/',userview.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userview.reply,name="reply"),
    path('replyAction/',userview.replyAction,name="replyAction"),
    path('addcontact/',userview.addcontact,name="addcontact"),
    path('addcontactAction/',userview.addcontactAction,name="addcontactAction"),
    path('check_username_contact/',userview.check_username_contact,name="check_username_contact"),
    path('addblacklist/',userview.addblacklist,name="addblacklist"),
    path('addblacklistAction/',userview.addblacklistAction,name="addblacklistAction"),
    path('viewcontacts/',userview.viewcontacts,name="viewcontacts"),
    path('viewblacklist/',userview.viewblacklist,name="viewblacklist"),
    path('deletecontact<int:id>/',userview.deletecontact,name="deletecontact"),
    path('deleteblacklist<int:id>/',userview.deleteblacklist,name="deleteblacklist"),
    path('move_to_blacklist<int:id>/',userview.move_to_blacklist,name="move_to_blacklist"),
    path('customer_hobbyfactor/',userview.customer_hobbyfactor,name="customer_hobbyfactor"),
    path('getfactor_customerhobby/',userview.getfactor_customerhobby,name="getfactor_customerhobby"),
    path('customer_hobbyfactorAction/',userview.customer_hobbyfactorAction,name="customer_hobbyfactorAction"),
    path('customer_agefactor/',userview.customer_agefactor,name="customer_agefactor"),
    path('customer_agefactorAction/',userview.customer_agefactorAction,name="customer_agefactorAction"),
    path('customer_seasoncountryfactor/',userview.customer_seasoncountryfactor,name="customer_seasoncountryfactor"),
    path('customer_seasoncountryfactorAction/',userview.customer_seasoncountryfactorAction,name="customer_seasoncountryfactorAction"),
    path('update_user_profile/',userview.update_user_profile,name="update_user_profile"),
    path('update_user_profileAction/',userview.update_user_profileAction,name="update_user_profileAction"),
    path('forgotpassword/',siteadminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',siteadminview.forgotpasswordAction,name="forgotpasswordAction"),
    path('check_sqAction/',siteadminview.check_sqAction,name="check_sqAction"),
    path('newpasswordAction/',siteadminview.newpasswordAction,name="newpasswordAction"),
    path('view_spam_messages/',userview.view_spam_messages,name="view_spam_messages"),
    path('delete_spam_messages<int:id>/',userview.delete_spam_messages,name="delete_spam_messages"),
    path('logout/',siteadminview.logout,name="logout"),
    path('userlist/',siteadminview.userlist,name="userlist"),
    path('deleteuser<int:id>/',siteadminview.deleteuser,name="deleteuser"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)