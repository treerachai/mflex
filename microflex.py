# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, datetime,  time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib
from datetime import timedelta, date
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup
from zalgo_text import zalgo
from threading import Thread,Event
requests.packages.urllib3.disable_warnings()
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient
listApp = ["CHROMEOS"]
try:
	for app in listApp:
		try:
			try:
				with open("authToken.txt", "r") as token:
					authToken = token.read().replace("\n","")
					if not authToken:
						client = LINE()
						with open("authToken.txt","w") as token:
							token.write(client.authToken)
						continue
					client = LINE(authToken, speedThrift=False, appName="{}\t2.1.5\tHelloWorld\t11.2.5".format(app))
				break
			except Exception as error:
				print(error)
				if error == "REVOKE":
					exit()
				elif "auth" in error:
					continue
				else:
					exit()
		except Exception as error:
			print(error)
except Exception as error:
	print(error)
with open("authToken.txt", "w") as token:
    token.write(str(client.authToken))
clientMid = client.profile.mid
clientStart = time.time()
clientPoll = OEPoll(client)
settings = {
    "commentPost": "Autolike by DPK - Bot",
    "keyCommand": "",
    "setKey": False,
    "siderMessage": "   ngintip aja lo "
}
read = {
    "readMember": {},
    "readPoint": {}
}
cctv = {
	"cyduk":{},
	"point":{},
	"sidermem":{}
}
def siderMembers(to, mid):
	try:
		arrData = ""
		textx = "{}".format(str(len(mid)))
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@x\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention+settings["siderMessage"]
			if no < len(mid):
				no += 1
				textx += "%i. " % (num)
				num=(num+1)
			else:
				try:
					no = "{}".format(str(client.getGroup(to).name))
				except:
					no = "Succes"
	except Exception as error:
		client.sendMessage(to, "ERROR :\n" + str(error))
def NoteCreate(to,cmd,msg):
	h = []
	s = []
	if cmd == 'tagnote':
		sakui = client.getProfile()
		group = client.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
		data = nama
		k = len(data)//20
		for aa in range(k+1):
			nos = 0
			if aa == 0:dd = '╭─[ Mention Note ]';no=aa
			else:dd = '';no=aa*20
			msgas = dd
			for i in data[aa*20 : (aa+1)*20]:
				no+=1
				if no == len(data):msgas+='\n│{}. @  \n╰─[ Mention Note ]'.format(no)
				else:msgas+='\n│{}. @'.format(no)
			msgas = msgas
			for i in data[aa*20 : (aa+1)*20]:
				gg = []
				dd = ''
				for ss in msgas:
					if ss == '@':
						dd += str(ss)
						gg.append(dd.index('@'))
						dd = dd.replace('@',' ')
					else:
						dd += str(ss)
				s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
				nos +=1
			h = client.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
def restartBot():
	print ("BOT RESETTED")
	python = sys.executable
	os.execl(python, python, *sys.argv)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        client.sendMessage(to, "Error :\n" + str(error))
def Dragon_Play_Killer(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "DPK BOT",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" 
    },
    "footer": {
      "backgroundColor": "#ff0000" 
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "DPK BOT", 
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
           "color": "#33ffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~arifistifik",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/ARIF_MH",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def command(text):
	pesan = text.lower()
	if settings["setKey"] == True:
		if pesan.startswith(settings["keyCommand"]):
			cmd = pesan.replace(settings["keyCommand"],"")
		else:
			cmd = "Undefined command"
	else:
		cmd = text.lower()
	return cmd

def menuHelp():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	menuHelp =	"───────────────────────" + "\n" + \
				"❄ Me" + "\n" + \
				"❄ Clear" + "\n" + \
				"❄ Logout" + "\n" + \
				"❄ Restart" + "\n" + \
				"❄ Speed" + "\n" + \
				"❄ Onread" + "\n" + \
				"❄ Offread" + "\n" + \
				"❄ Autolike" + "\n" + \
				"❄ Respond" + "\n" + \
				"❄ Tagall" + "\n" + \
				"❄ Tagnote"
	return menuHelp

def clientBot(op):
	try:
		if op.type == 0:
			return
		if op.type == 25:
			try:
				print("ARIFISTIFIK SEND MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				cmd = command(text)
				setKey = settings["keyCommand"].title()
				if settings["setKey"] == False:
					setKey = ''
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if msg.contentType == 0:
						if cmd == "help":
							helpMessage = menuHelp()
							Dragon_Play_Killer(msg.to, str(helpMessage))
						elif cmd == "restart":
							Dragon_Play_Killer(to, "Berhasil mereset bot")
							restartBot()
						elif cmd == "me":
							contact = client.getProfile()
							mids = [contact.mid]
							status = client.getContact(sender)
							data = {
  "contents": [
    {
     "type": "bubble",
     "size": "micro",
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "4:4",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "size": "micro",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "type": "button",
            "flex": 1,
            "style": "primary",
            "height": "sm",
            "action": {
                "type": "uri",
                "label": "{}".format(status.displayName),
                "uri": "http://line.me/ti/p/~arif.mh"
              },
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
							client.postFlex(to, data)
						elif cmd == "speed":
							start = time.time()
							client.sendMessage(to, "Menghitung kecepatan...")
							elapsed_time = time.time() - start
							client.sendMessage(to, "Kecepatan mengirim pesan {} detik".format(str(elapsed_time)))
						elif cmd == "clear":
							client.removeAllMessages(op.param2)
							Dragon_Play_Killer(to, "Cleaning all chat")
						elif cmd == "tagnote":
							NoteCreate(to,cmd,msg)
						elif cmd == "self":
							contact = client.getContact(sender)
							client.sendMention(to, "My name : @! \nMy Mid : {}".format(contact.mid), [sender])
							client.sendContact(to, sender)
							client.sendMessageMusic(to, sender)
						elif cmd == 'tagall':
							group = client.getGroup(to)
							midMembers = [contact.mid for contact in group.members]
							midSelect = len(midMembers)//20
							for mentionMembers in range(midSelect+1):
								no = 0
								ret_ = "╭──[ Mention Members ]"
								dataMid = []
								for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
									dataMid.append(dataMention.mid)
									no += 1
									ret_ += "\n├ {}. @!".format(str(no))
								ret_ += "\n╰──[ Total {} Members]".format(str(len(dataMid)))
								client.sendMention(to, ret_, dataMid)
						elif cmd == "onread":
							try:
								del cctv['point'][to]
								del cctv['sidermem'][to]
								del cctv['cyduk'][to]
							except:
								pass
							cctv['point'][to] = msg.id
							cctv['sidermem'][to] = ""
							cctv['cyduk'][to]=True
							Dragon_Play_Killer(to, "CCTV MEMBERS MODE ON")
						elif cmd == "offread":
							if to in cctv['point']:
								cctv['sidermem'][to] = []
								cctv['cyduk'][to]=False
								Dragon_Play_Killer(to, "CCTV MEMBERS MODE OFF")
							else:
								Dragon_Play_Killer(to, "CCTV MEMBERSMODE OFF")
			except Exception as error:
				pass
		if op.type == 26 or op.type == 25:
			msg = op.message
			text = msg.text
			msg_id = msg.id
			receiver = msg.to
			sender = msg._from
			if msg.text != None:
				if msg.toType == 2:
					dpk = client.getProfile().mid
					if dpk in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
						pilih = ['yang tag sy semoga dicium genderuwo','ngapain tag tag woe, kangen?','ada apa ini? ko di tag?','duhh kena tag, dianya kesepian kali yah','gk usah tag, gift tikel aja']
						rslt = random.choice(pilih)
						Dragon_Play_Killer(msg.to, str(rslt))
					else:
						pass
				else:
					pass
			else:
				pass
			if msg.toType == 0:
				if sender != client.profile.mid:
					to = sender
				else:
					to = receiver
			else:
				to = receiver
				if msg.contentType == 16:
					if msg.toType in (2,1,0):
						purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
						adw = client.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
						adws = client.createComment(purl[0], purl[1], settings["commentPost"])
						Dragon_Play_Killer(to, "AUTO LIKE SUCCES")
		if op.type == 55:
			if cctv['cyduk'][op.param1]==True:
				Name = client.getContact(op.param2).displayName
				if Name in cctv['sidermem'][op.param1]:
					pass
				else:
					cctv['sidermem'][op.param1] += "\n~ " + Name
					siderMembers(op.param1, [op.param2])
					contact = client.getContact(op.param2)
					cover = client.getProfileCoverURL(op.param2)
					tz = pytz.timezone("Asia/Jakarta")
					timeNow = datetime.now(tz=tz)
					data = {
                                       "type": "flex",
                                       "altText": "DPK_BOT",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://gifimage.net/wp-content/uploads/2018/06/ukuran-gif-dp-bbm-5.gif", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",  #"https://em.wattpad.com/4c7e5d80bb78b4c9abde154708b4efdb4e71c0c6/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6b63787836516f3833615a7a43413d3d2d3639323032383336312e313538306535356565336436353532663138343830393632343530302e676966?s=fit&w=720&h=720", #https://thumbs.gfycat.com/WickedMeekGazelle-size_restricted.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "21px",
"offsetStart": "21px",
"height": "157px",
"width": "117px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, 
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover,
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ud296655acef67cbd5e8208e63629f78b",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ 
{
"type": "text",
"text": "ᴄᴄᴛᴠ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "29px",
"backgroundColor": "#ffd700",
"offsetStart": "30px",
"height": "13px",
"width": "34px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ 
{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~arifistifik",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/ARIF_MH",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},
"flex": 0
},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
"size": "xl",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~arifistifik",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "42px",
"offsetStart": "24px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "  "+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "120px",
"backgroundColor": "#4b4b4b",
"offsetStart": "70px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": settings["siderMessage"],
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "138px",
"backgroundColor": "#4b4b4b",
"offsetStart": "47px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "    🐯 {} ".format(client.getContact(op.param2).displayName),
"weight": "bold",
"color": "#81FF00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "155px",
"offsetStart": "29px",
"height": "16px",
"width": "105px"
}
],
"paddingAll": "0px"
}
},
]
}
}
					client.postTemplate(op.param1, data),
	except Exception as error:
		pass
def run():
	while True:
		ops = clientPoll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				try:
					clientBot(op)
				except Exception as error:
					pass
				clientPoll.setRevision(op.revision)
if __name__ == "__main__":
	run()