from django.shortcuts import render
import requests
import json


CLIENT_ID = "78y1ltc2d1locm"
CLIENT_SECRET_KEY = "0GiCMyLae8UaZLlb"

def profile(request) :
	#print request
	authorization_code = request.GET.get("code","")
	if(authorization_code != "") : 
		url = "https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code"+"&code="+authorization_code+"&redirect_uri=http://192.168.0.102:8080/profile/&client_id="+CLIENT_ID+"&client_secret="+CLIENT_SECRET_KEY
		#print url
		resp = requests.get(url)
		resp = resp.json()
		accessToken = resp["access_token"]
		profile_info_url = "https://api.linkedin.com/v1/people/~:(first-name,last-name,headline,picture-urls::(original),courses,positions,recommendations-received,skills)?oauth2_access_token=" + accessToken
		#profile_info_url = "https://api.linkedin.com/v1/people/~?oauth2_access_token=" + accessToken
		resp = requests.request('GET',profile_info_url,headers={'x-li-format':'json'})
		profile_data_dict = resp.json()
		print profile_data_dict
		profile_data = {'profile_data':profile_data_dict}
	return render(request,'profile/profile.html',profile_data)
		
def home(request) :
	return render(request,'index.html')
