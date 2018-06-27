from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.db.models import *
import os
import django
import json
import logging
import datetime
import traceback
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Quadeye_Nw.settings')
from locater.models import *

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','locater.settings')
# Create your views here.
                        # Logger #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Log_location=os.path.join(BASE_DIR,"logs")
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(Log_location)
hdlr.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

def index(request):
	try:
		dcs = dataCentre.objects.all()
		lks = link.objects.all()
		data_centre={}
		lk={}
		links={}
		status='True'
		for dc in dcs:
		    data_centre[dc.name]={}
		    data_centre[dc.name]['latitude']=dc.latitude
		    data_centre[dc.name]['longitude']=dc.longitude
		    data_centre[dc.name]['region']= dc.region
		return render(request, 'index.html',{'data_centre':data_centre,'status':status})
	except Exception as e:
		print str(e)
		logger.info("Error rendering index page "+str(e))	    



def marker(request):
	try:
		dcs = dataCentre.objects.all()
		lks = link.objects.all()
		data_centre={}
		links={}
		for dc in dcs:
		    data_centre[dc.name]={}
		    data_centre[dc.name]['latitude']=dc.latitude
		    data_centre[dc.name]['longitude']=dc.longitude
		    data_centre[dc.name]['region']= dc.region

		for lk in lks:
		    links[lk.linkname]={}
		    #links[lk.linkname]=lk.linkname
		    if(lk.dc_type is 'source'):
		        idc=dataCentre.objects.filter(name=lk.ass_dc)
		        links[lk.linkname]['src_latitude']=idc.latitude
		        links[lk.linkname]['src_longitude']=idc.longitude
		        ilk= link.objects.filter(linkname=lk.name,dc_type='dest')
		        ilk1 = ilk.ass_dc
		        dest_dc = dataCentre.objects.filter(name=ilk1)
		        dest_lat= dest_dc.latitude
		        dest_long= dest_dc.longitude
		        links[lk.linkname]['dest_latitude']=dest_lat
		        links[lk.linkname]['dest_longitude']=dest_long
		    else:
		        idc=dataCentre.objects.get(name=lk.ass_dc)
		        links[lk.linkname]['dest_latitude']=idc.latitude
		        links[lk.linkname]['dest_longitude']=idc.longitude
		        ilk= link.objects.get(linkname=lk.linkname,dc_type='source')
		        ilk1 = ilk.ass_dc
		        src_dc = dataCentre.objects.get(name=ilk1)
		        src_lat= src_dc.latitude
		        src_long= src_dc.longitude
		        links[lk.linkname]['src_latitude']=src_lat
		        links[lk.linkname]['src_longitude']=src_long
		return render(request, 'map.html',{'data_centre':data_centre,'links':links})
	except Exception as e:
		print str(e)
		logger.info("Error marking map "+str(e))	           	                

def add_centre(request):
	try:
		name=request.POST.get('name','')
		lng=request.POST.get('longitude','')
		lat=request.POST.get('latitude','')
		#reg=request[region]
		t=dataCentre(name=name,region='Null',longitude=lng,latitude=lat)
		t.save()
		#print "Here"
		return HttpResponse(json.dumps({'resp':'True'}))
	except Exception as e:
		logger.info("Error adding centre "+str(e))
		print str(e)
		return HttpResponse(json.dumps({'resp':'False'}))

def add_link(request):
	try:
		name=request.POST.get('name','')
		src_dc=str(request.POST.get('src',''))
		dest_dc=str(request.POST.get('dest',''))
		src=dataCentre.objects.get(name=src_dc)
		dst=dataCentre.objects.get(name=dest_dc)
		t=link(linkname=name,latency=0.0,ass_dc=src,dc_type='source')
		t.save()
		t=link(linkname=name,latency=0.0,ass_dc=dst,dc_type='dest')
		t.save()
		return HttpResponse(json.dumps({'resp':'True'}))
	except Exception as e:
		logger.info("Error adding Link "+str(e))
		print(e)
		return HttpResponse(json.dumps({'resp':'False'}))


