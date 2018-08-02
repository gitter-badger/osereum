#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import osereum.views, osereum.apilist

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', osereum.views.landing),
    url(r'^login', osereum.views.login),
    url(r'^logout', osereum.views.logout),
    url(r'^transactions', osereum.views.ws),


    #REST API
    url(r'^api/v1/checkwallet/', osereum.views.checkwallet),
    url(r'^api/v1/sendosereum', osereum.views.sendosereum),
    url(r'^api/v1/createnewwallet/', osereum.views.createnewwallet),
    url(r'^api/v1/alltransactions/', osereum.apilist.alltransactions),
    url(r'^api/v1/gettransaction/(?P<tid>\w+)/$', osereum.apilist.gettransaction,  name='gettransaction'),
    url(r'^api/v1/getwalletfrompkey/(?P<pkey>\w+)/$', osereum.apilist.getwalletfrompkey, name='getwalletfrompkey'),
    url(r'^api/v1/getpublickeyfromprikey/(?P<private_key>\w+)/$', osereum.apilist.getpublickeyfromprikey, name='getpublickeyfromprikey'),
    url(r'^api/v1/getbalancefromwallet/(?P<wallet>\w+)/$', osereum.apilist.getbalancefromwallet, name='getbalancefromwallet'),
    url(r'^api/v1/getwalletdetails/(?P<wallet>\w+)/$', osereum.apilist.getwalletdetails, name='getwalletdetails'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
