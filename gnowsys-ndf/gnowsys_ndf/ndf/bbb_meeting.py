from urllib import urlopen
from urllib import urlencode
from hashlib import sha1
import xml.etree.ElementTree as ET
import random
# from gnowsys_ndf.ndf.models import *

SALT = "8cd8ef52e8e101574e400365b55e11a6"
BBB_API_URL = "http://test-install.blindsidenetworks.com/bigbluebutton/api/"

def parse(response):
    try:
        xml = ET.XML(response)
        code = xml.find('returncode').text
        if code == 'SUCCESS':
            return xml
        else:
            raise
    except:
        return None

def api_call(query,call):
	prepared = "%s%s%s" % (call,query,SALT)
	checksum = sha1(prepared).hexdigest()
	result = "%s&checksum=%s" % (query,checksum)
	return result

def is_running(self):
    call = 'isMeetingRunning'
    query = urlencode((
        ('meetingID', self.meeting_id),
    ))
    hashed = self.api_call(query, call)
    url = settings.BBB_API_URL + call + '?' + hashed
    result = parse(urlopen(url).read())
    if result:
        return result.find('running').text
    else:
        return 'error'

def bbb_start(name,meeting_id):
	call = 'create'
	voicebridge = 70000 + random.randint(0,9999)
	query = urlencode((
		('name', name),
		('meetingID', meeting_id),
		('attendeePW', "pass"),
		('moderatorPW', "pass"),
		('voiceBridge', voicebridge),
		('welcome',"Welcome!"),
	))
	hashed = api_call(query, call)
	url = BBB_API_URL + call + '?' + hashed
	result = parse(urlopen(url).read())
	if result:
		return result
	else:
		pass

def join_url(meeting_id, name, password):
    call = 'join'
    query = urlencode((
        ('fullName', name),
        ('meetingID', meeting_id),
        ('password', password),
    ))
    hashed = api_call(query, call)
    url = settings.BBB_API_URL + call + '?' + hashed
    return url

