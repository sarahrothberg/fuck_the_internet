# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, session 
from flask import render_template
from twilio.util import TwilioCapability

import twilio.twiml
import os


import serial
import time

ser = serial.Serial('/dev/tty.usbmodem411', 9600)

textTime = "0"
lastTextTime = "0"

app = Flask(__name__)

smsReceived = None
count = 0
account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)


@app.route("/", methods=['GET', 'POST'])
def mainFunction():	
	return render_template('main.html')

def write_out():
	body = request.form['date_created'] # get SMS body
	for char in body:
		signals = alpha[char.lower()]
		for signal in signals:
			if signal == '1':
				on(0.2) # Send dot
			elif signal == '2':
				on(0.4) # Send dash
			time.sleep(.02)
	return '<Response></Response>'

@app.route("/ledOff", methods=['GET', 'POST'])
def test():
	ser.write("0")
	# smsReceived = True
	print "Low in LED OFF"
	return render_template('gif.html')

@app.route("/gifDisplay", methods=['GET', 'POST'])
def displayGif():
	return render_template('gif.html')


@app.route("/textRefresher", methods=['GET', 'POST'])
def textRefresher():
	message = client.messages.list(
		to = "+17472334999"
		)
	badwords = ['anal', 'analbleed', 'analcavity', 'analcrevass', 'analfuck', 'analingus', 'analintercourse', 'analinvade', 'analjuice', 'analleakage', 'anallovin', 'anallyretentivepubiclouse', 'analmunch', 'analorafice', 'analorgy', 'analpirate', 'analprobe', 'analrape', 'analretentivepubiclouse', 'analsex', 'analspew', 'analspray', 'analtail', 'analtroop', 'analungus', 'analviolate', 'analwart', 'analwhore', 'analzone', 'animalsex', 'anus', 'arse', 'arsebandit', 'arsefuck', 'arsephuck', 'arsephuk', 'arsepiece', 'arsestab', 'arsewipe', 'asphinct', 'ass', 'assbandit', 'assbeat', 'assbite', 'assbiteme', 'assblast', 'assboy', 'assbutt', 'assbyte', 'asscheek', 'asscheese', 'assclown', 'asscock', 'asscrack', 'asscream', 'assenlarge', 'assenmunch', 'assface', 'assfish', 'assfuck', 'assfuk', 'assfunk', 'assgoblin', 'assgrab', 'asshair', 'asshead', 'assho', 'asshoe', 'asshol', 'asshole', 'asshorisin', 'assinahole', 'assjuice', 'asskick', 'asskickboy', 'asskikr', 'asslessone', 'asslick', 'asslip', 'asslord', 'assman', 'assmast', 'assmeat', 'assmilk', 'assmine', 'assmite', 'assmoankey', 'assmong', 'assmonk', 'assmonkey', 'assmunch', 'assowipo', 'assowippo', 'assown', 'asspack', 'asspeddle', 'assphinct', 'assphuck', 'asspiece', 'asspirate', 'assplug', 'asspoop', 'assram', 'assrape', 'assrapingyak', 'assream', 'assrip', 'assrob', 'asstab', 'asstang', 'asstheif', 'asstink', 'asstomp', 'assuck', 'asswack', 'asswater', 'assweed', 'asswhipe', 'asswhole', 'asswhop', 'asswhore', 'asswipe', 'asswoop', 'assylip', 'assynip', 'assyniple', 'asszila', 'badass', 'bastard', 'basterd', 'bastid', 'biach', 'biatch', 'bicht', 'bigass', 'bigassball', 'bigasslip', 'bigbooty', 'bigbutthole', 'bigcock', 'bigdick', 'bigdik', 'bigfatass', 'bigfuk', 'biggay', 'biggaykill', 'biggayman', 'biggaypeck', 'biggusdikus', 'bigho', 'bighoe', 'bigjuicynut', 'biglesbian', 'bignigger', 'bignut', 'bignutsack', 'bigoldick', 'bigschlong', 'bigslut', 'bigtits', 'bigusdikkus', 'bigusdikus', 'bigwang', 'bigwood', 'biotch', 'bitch', 'bitchass', 'bitchfuck', 'bitchnig', 'bitchqueen', 'bitchslap', 'bitchwhore', 'bitemyass', 'bitemyprick', 'biyotch', 'blowjob', 'bltch', 'boner', 'bulshit', 'bumfuck', 'bumhole', 'bumholeengineer', 'cameljockey', 'castrate', 'charliesnif', 'cherrypop', 'chinesewhore', 'chingachgook', 'chink', 'chinkill', 'chinkslope', 'chinksrgay', 'chinkssuck', 'chokingthechicken', 'clit', 'clitlick', 'clitoral', 'clitorious', 'clitoris', 'cock', 'cockandball', 'cockbite', 'cockboy', 'cockface', 'cockhead', 'cocklick', 'cocknball', 'cocksmoke', 'cocksniff', 'cocksuck', 'cocktease', 'coksuck', 'condomeat', 'condomlick', 'condommunch', 'condomsniff', 'coochie', 'coonfuck', 'crackwhore', 'crazychink', 'crazyjap', 'creamycunt', 'creamyknick', 'creamypant', 'crotchsniff', 'crotchwatch', 'cuckmysock', 'cum', 'cumbubble', 'cumbucket', 'cumburp', 'cumgargle', 'cumguzzle', 'cumindabum', 'cumlick', 'cummbubble', 'cumofsomeguy', 'cumonme', 'cumonmytummy', 'cumonu', 'cumquat', 'cumsalot', 'cumshot', 'cumslut', 'cumstain', 'cumswallow', 'cunalingus', 'cungalingus', 'cunnilingus', 'cunningilus', 'cunny', 'cunt', 'cuntface', 'cunthead', 'cuntlick', 'cuntlip', 'cuntylip', 'dasskick', 'dicckweed', 'dicface', 'dichead', 'dick', 'dickbrain', 'dickforabrain', 'dickhead', 'dicklick', 'dickwad', 'dickweed', 'dicwad', 'dik', 'dildo', 'dlldo', 'doggystyle', 'douchebag', 'dumbass', 'fag', 'faggot', 'fannybatter', 'fannycream', 'fannyfart', 'fannyhair', 'fannyjuice', 'fatass', 'fcuk', 'fecalhead', 'fellatio', 'flameinghomo', 'fock', 'fothermuck', 'fucayou', 'fuccer', 'fuccwitme', 'fucd', 'fucface', 'fuchead', 'fuck', 'fuckboy', 'fuckcoons', 'fuckedsideway', 'fuckedup', 'fuckedupanddown', 'fuckedupndown', 'fuckface', 'fuckgm', 'fuckhead', 'fuckhole', 'fuckingyamom', 'fuckinstoned', 'fuckman', 'fuckme', 'fuckmehard', 'fuckmyass', 'fuckmonkey', 'fuckpirate', 'fucknut', 'fuckoff', 'fuckshit', 'fucku', 'fuckubitch', 'fuckup', 'fuckymamma', 'fuckyou', 'fuckyoucock', 'fuckyoucunt', 'fuckyougm', 'fuckyouii', 'fucoff', 'fucq', 'fucqdat', 'fucqu', 'fuct', 'fuctup', 'fucxyou', 'fucya', 'fucyou', 'fucyoubich', 'fudgehole', 'fudgepack', 'fudpuck', 'fugm', 'fugmpuke', 'fuhq', 'fuk', 'fukad', 'fukaduck', 'fukahire', 'fukallyou', 'fukayouho', 'fukc', 'fukchop', 'fukdabitch', 'fukdabtch', 'fukdischit', 'fukead', 'fukedatbirth', 'fukedup', 'fukedyomom', 'fukengruven', 'fukengruvin', 'fukface', 'fukfest', 'fukhole', 'fukinbad', 'fukingfisher', 'fukinggayman', 'fukinggook', 'fukingjap', 'fukingroovin', 'fukingulg', 'fukinlag', 'fukiniger', 'fukinpimp', 'fukinrapist', 'fukit', 'fukjap', 'fukhead', 'fukknut', 'fukkyou', 'fukme', 'fukmegood', 'fukmerun', 'fukmyass', 'fuknclown', 'fukndork', 'fukngruv', 'fukngrv', 'fuknklown', 'fuknmonke', 'fukntheif', 'fuknthief', 'fuknurmom', 'fuknut', 'fukoff', 'fukslut', 'fuksuckblow', 'fukter', 'fuku', 'fukuall', 'fukualso', 'fukuashole', 'fukubiatch', 'fukubizzach', 'fukubyatch', 'fukufuku', 'fukuinyour', 'fukumen', 'fukuo', 'fukuoka', 'fukup', 'fukuppl', 'fukusima', 'fukusuk', 'fukuup', 'fukuusuck', 'fukyah', 'fukyallmofo', 'fukyermom', 'fukyew', 'fukyoass', 'fukyou', 'fukyouanddie', 'fukyouus', 'fumonkey', 'funkynegro', 'fuq', 'fuqbich', 'fuqbiotch', 'fuqew', 'fuqfugu', 'fuqnut', 'fuqoff', 'fuqu', 'fuque', 'futhermucker', 'futtbuck', 'fuvkmehard', 'fuvku', 'fuxjoo', 'fuxkyou', 'fuxyou', 'fyuocuk', 'gangbang', 'gangrape', 'gayrape', 'gaywad', 'goatfuck', 'goddam', 'gook', 'hairyclamb', 'hitler', 'honkey', 'hoochiemom', 'hughboobs', 'hugherection', 'hughgass', 'hughgdlck', 'hughgkoch', 'hughgrect', 'hughgrekshon', 'hughgrekshyn', 'hughgshaft', 'hughjardon', 'hughjas', 'hughjassole', 'hughjaynus', 'hughjaz', 'hughjorgan', 'hughjorgen', 'iloveboobs', 'japhate', 'japkill', 'japkillerusa', 'jerkoff', 'jewbag', 'jewboy', 'jewboynigger', 'jewishnazi', 'jewishwhore', 'jiz', 'killaniga', 'kunt', 'lickalotpuss', 'lickatit', 'lickball', 'lickemball', 'lickitgood', 'lickithard', 'lickityoufuc', 'lickmebalz', 'lickmecock', 'lickmyanus', 'lickmyass', 'lickmyball', 'lickmycock', 'lickmycrack', 'lickmycrotch', 'lickmynad', 'lickmynut', 'lickmyownpee', 'lickmysack', 'lickmywetbox', 'likmekok', 'likmiclit', 'likmybut', 'masturbate', 'moelester', 'motherfuck', 'mutherfock', 'mycock', 'mydick', 'nazijewraper', 'naziskinhead', 'niga', 'nigahbytch', 'nigaretto', 'nigatrash', 'nigazbiotch', 'nigbeater', 'nigerbeater', 'nigerman', 'nigga', 'niggaboo', 'niggafag', 'niggah', 'nigge', 'nigghaz', 'niggher', 'niggkilla', 'niggor', 'niggr', 'niggrian', 'nigguh', 'niggurs', 'niggy', 'nigiro', 'niglet', 'nigletbard', 'nigletmaster', 'nigofger', 'nigore', 'nigrkill', 'nigromance', 'nigz', 'nipalicious', 'nipplelicker', 'penis', 'pinktaco', 'pootang', 'prick', 'punkass', 'pussie', 'pussy', 'pussyhole', 'pussylick', 'pussylip', 'pussypound', 'pyropussy', 'queer', 'raghead', 'rape', 'rapeme', 'rectalprobe', 'rectum', 'schit', 'schithead', 'schitngrin', 'schitzngrin', 'scrotum', 'semen', 'shiet', 'shit', 'shite', 'shiteat', 'shithead', 'shitman', 'shitstab', 'sitonmyface', 'slut', 'slutass', 'slutznwhore', 'snatch', 'sperm', 'spermburp', 'spermpants', 'spick', 'spooge', 'spoogebob', 'suckme', 'suckmydick', 'sucmybawl', 'supabiatch', 'tit', 'twat', 'vageyenuh', 'vagina', 'vaginal', 'vaginallip', 'vaginuh', 'vagiskin', 'wellhung', 'whore'];
	text = message[0].body
	textwords = text.lower().split()
	for word in badwords:
		if word in textwords:
			post = "UH OH! SOMEONE SAID @#!$"
			break
		else:
			post = message[0].body
	return post

@app.route("/response", methods=['GET', 'POST'])
def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""		
	badwords = ['anal', 'analbleed', 'analcavity', 'analcrevass', 'analfuck', 'analingus', 'analintercourse', 'analinvade', 'analjuice', 'analleakage', 'anallovin', 'anallyretentivepubiclouse', 'analmunch', 'analorafice', 'analorgy', 'analpirate', 'analprobe', 'analrape', 'analretentivepubiclouse', 'analsex', 'analspew', 'analspray', 'analtail', 'analtroop', 'analungus', 'analviolate', 'analwart', 'analwhore', 'analzone', 'animalsex', 'anus', 'arse', 'arsebandit', 'arsefuck', 'arsephuck', 'arsephuk', 'arsepiece', 'arsestab', 'arsewipe', 'asphinct', 'ass', 'assbandit', 'assbeat', 'assbite', 'assbiteme', 'assblast', 'assboy', 'assbutt', 'assbyte', 'asscheek', 'asscheese', 'assclown', 'asscock', 'asscrack', 'asscream', 'assenlarge', 'assenmunch', 'assface', 'assfish', 'assfuck', 'assfuk', 'assfunk', 'assgoblin', 'assgrab', 'asshair', 'asshead', 'assho', 'asshoe', 'asshol', 'asshole', 'asshorisin', 'assinahole', 'assjuice', 'asskick', 'asskickboy', 'asskikr', 'asslessone', 'asslick', 'asslip', 'asslord', 'assman', 'assmast', 'assmeat', 'assmilk', 'assmine', 'assmite', 'assmoankey', 'assmong', 'assmonk', 'assmonkey', 'assmunch', 'assowipo', 'assowippo', 'assown', 'asspack', 'asspeddle', 'assphinct', 'assphuck', 'asspiece', 'asspirate', 'assplug', 'asspoop', 'assram', 'assrape', 'assrapingyak', 'assream', 'assrip', 'assrob', 'asstab', 'asstang', 'asstheif', 'asstink', 'asstomp', 'assuck', 'asswack', 'asswater', 'assweed', 'asswhipe', 'asswhole', 'asswhop', 'asswhore', 'asswipe', 'asswoop', 'assylip', 'assynip', 'assyniple', 'asszila', 'badass', 'bastard', 'basterd', 'bastid', 'biach', 'biatch', 'bicht', 'bigass', 'bigassball', 'bigasslip', 'bigbooty', 'bigbutthole', 'bigcock', 'bigdick', 'bigdik', 'bigfatass', 'bigfuk', 'biggay', 'biggaykill', 'biggayman', 'biggaypeck', 'biggusdikus', 'bigho', 'bighoe', 'bigjuicynut', 'biglesbian', 'bignigger', 'bignut', 'bignutsack', 'bigoldick', 'bigschlong', 'bigslut', 'bigtits', 'bigusdikkus', 'bigusdikus', 'bigwang', 'bigwood', 'biotch', 'bitch', 'bitchass', 'bitchfuck', 'bitchnig', 'bitchqueen', 'bitchslap', 'bitchwhore', 'bitemyass', 'bitemyprick', 'biyotch', 'blowjob', 'bltch', 'boner', 'bulshit', 'bumfuck', 'bumhole', 'bumholeengineer', 'cameljockey', 'castrate', 'charliesnif', 'cherrypop', 'chinesewhore', 'chingachgook', 'chink', 'chinkill', 'chinkslope', 'chinksrgay', 'chinkssuck', 'chokingthechicken', 'clit', 'clitlick', 'clitoral', 'clitorious', 'clitoris', 'cock', 'cockandball', 'cockbite', 'cockboy', 'cockface', 'cockhead', 'cocklick', 'cocknball', 'cocksmoke', 'cocksniff', 'cocksuck', 'cocktease', 'coksuck', 'condomeat', 'condomlick', 'condommunch', 'condomsniff', 'coochie', 'coonfuck', 'crackwhore', 'crazychink', 'crazyjap', 'creamycunt', 'creamyknick', 'creamypant', 'crotchsniff', 'crotchwatch', 'cuckmysock', 'cum', 'cumbubble', 'cumbucket', 'cumburp', 'cumgargle', 'cumguzzle', 'cumindabum', 'cumlick', 'cummbubble', 'cumofsomeguy', 'cumonme', 'cumonmytummy', 'cumonu', 'cumquat', 'cumsalot', 'cumshot', 'cumslut', 'cumstain', 'cumswallow', 'cunalingus', 'cungalingus', 'cunnilingus', 'cunningilus', 'cunny', 'cunt', 'cuntface', 'cunthead', 'cuntlick', 'cuntlip', 'cuntylip', 'dasskick', 'dicckweed', 'dicface', 'dichead', 'dick', 'dickbrain', 'dickforabrain', 'dickhead', 'dicklick', 'dickwad', 'dickweed', 'dicwad', 'dik', 'dildo', 'dlldo', 'doggystyle', 'douchebag', 'dumbass', 'fag', 'faggot', 'fannybatter', 'fannycream', 'fannyfart', 'fannyhair', 'fannyjuice', 'fatass', 'fcuk', 'fecalhead', 'fellatio', 'flameinghomo', 'fock', 'fothermuck', 'fucayou', 'fuccer', 'fuccwitme', 'fucd', 'fucface', 'fuchead', 'fuck', 'fuckboy', 'fuckcoons', 'fuckedsideway', 'fuckedup', 'fuckedupanddown', 'fuckedupndown', 'fuckface', 'fuckgm', 'fuckhead', 'fuckhole', 'fuckingyamom', 'fuckinstoned', 'fuckman', 'fuckme', 'fuckmehard', 'fuckmyass', 'fuckmonkey', 'fuckpirate', 'fucknut', 'fuckoff', 'fuckshit', 'fucku', 'fuckubitch', 'fuckup', 'fuckymamma', 'fuckyou', 'fuckyoucock', 'fuckyoucunt', 'fuckyougm', 'fuckyouii', 'fucoff', 'fucq', 'fucqdat', 'fucqu', 'fuct', 'fuctup', 'fucxyou', 'fucya', 'fucyou', 'fucyoubich', 'fudgehole', 'fudgepack', 'fudpuck', 'fugm', 'fugmpuke', 'fuhq', 'fuk', 'fukad', 'fukaduck', 'fukahire', 'fukallyou', 'fukayouho', 'fukc', 'fukchop', 'fukdabitch', 'fukdabtch', 'fukdischit', 'fukead', 'fukedatbirth', 'fukedup', 'fukedyomom', 'fukengruven', 'fukengruvin', 'fukface', 'fukfest', 'fukhole', 'fukinbad', 'fukingfisher', 'fukinggayman', 'fukinggook', 'fukingjap', 'fukingroovin', 'fukingulg', 'fukinlag', 'fukiniger', 'fukinpimp', 'fukinrapist', 'fukit', 'fukjap', 'fukhead', 'fukknut', 'fukkyou', 'fukme', 'fukmegood', 'fukmerun', 'fukmyass', 'fuknclown', 'fukndork', 'fukngruv', 'fukngrv', 'fuknklown', 'fuknmonke', 'fukntheif', 'fuknthief', 'fuknurmom', 'fuknut', 'fukoff', 'fukslut', 'fuksuckblow', 'fukter', 'fuku', 'fukuall', 'fukualso', 'fukuashole', 'fukubiatch', 'fukubizzach', 'fukubyatch', 'fukufuku', 'fukuinyour', 'fukumen', 'fukuo', 'fukuoka', 'fukup', 'fukuppl', 'fukusima', 'fukusuk', 'fukuup', 'fukuusuck', 'fukyah', 'fukyallmofo', 'fukyermom', 'fukyew', 'fukyoass', 'fukyou', 'fukyouanddie', 'fukyouus', 'fumonkey', 'funkynegro', 'fuq', 'fuqbich', 'fuqbiotch', 'fuqew', 'fuqfugu', 'fuqnut', 'fuqoff', 'fuqu', 'fuque', 'futhermucker', 'futtbuck', 'fuvkmehard', 'fuvku', 'fuxjoo', 'fuxkyou', 'fuxyou', 'fyuocuk', 'gangbang', 'gangrape', 'gayrape', 'gaywad', 'goatfuck', 'goddam', 'gook', 'hairyclamb', 'hitler', 'honkey', 'hoochiemom', 'hughboobs', 'hugherection', 'hughgass', 'hughgdlck', 'hughgkoch', 'hughgrect', 'hughgrekshon', 'hughgrekshyn', 'hughgshaft', 'hughjardon', 'hughjas', 'hughjassole', 'hughjaynus', 'hughjaz', 'hughjorgan', 'hughjorgen', 'iloveboobs', 'japhate', 'japkill', 'japkillerusa', 'jerkoff', 'jewbag', 'jewboy', 'jewboynigger', 'jewishnazi', 'jewishwhore', 'jiz', 'killaniga', 'kunt', 'lickalotpuss', 'lickatit', 'lickball', 'lickemball', 'lickitgood', 'lickithard', 'lickityoufuc', 'lickmebalz', 'lickmecock', 'lickmyanus', 'lickmyass', 'lickmyball', 'lickmycock', 'lickmycrack', 'lickmycrotch', 'lickmynad', 'lickmynut', 'lickmyownpee', 'lickmysack', 'lickmywetbox', 'likmekok', 'likmiclit', 'likmybut', 'masturbate', 'moelester', 'motherfuck', 'mutherfock', 'mycock', 'mydick', 'nazijewraper', 'naziskinhead', 'niga', 'nigahbytch', 'nigaretto', 'nigatrash', 'nigazbiotch', 'nigbeater', 'nigerbeater', 'nigerman', 'nigga', 'niggaboo', 'niggafag', 'niggah', 'nigge', 'nigghaz', 'niggher', 'niggkilla', 'niggor', 'niggr', 'niggrian', 'nigguh', 'niggurs', 'niggy', 'nigiro', 'niglet', 'nigletbard', 'nigletmaster', 'nigofger', 'nigore', 'nigrkill', 'nigromance', 'nigz', 'nipalicious', 'nipplelicker', 'penis', 'pinktaco', 'pootang', 'prick', 'punkass', 'pussie', 'pussy', 'pussyhole', 'pussylick', 'pussylip', 'pussypound', 'pyropussy', 'queer', 'raghead', 'rape', 'rapeme', 'rectalprobe', 'rectum', 'schit', 'schithead', 'schitngrin', 'schitzngrin', 'scrotum', 'semen', 'shiet', 'shit', 'shite', 'shiteat', 'shithead', 'shitman', 'shitstab', 'sitonmyface', 'slut', 'slutass', 'slutznwhore', 'snatch', 'sperm', 'spermburp', 'spermpants', 'spick', 'spooge', 'spoogebob', 'suckme', 'suckmydick', 'sucmybawl', 'supabiatch', 'tit', 'twat', 'vageyenuh', 'vagina', 'vaginal', 'vaginallip', 'vaginuh', 'vagiskin', 'wellhung', 'whore'];
	text = request.values.get('Body')
	textwords = text.lower().split()
	for word in badwords:
		if word in textwords:			
			msg = " UH OH, A$$FACE SAFESEARCH IS ON!"
			break
		else:	 
			msg = " THANKS FOR UR QUESTION. <3, THE INTERNET"
	resp = twilio.twiml.Response()			
	resp.message(msg)
	return str(resp)
	
if __name__ == "__main__":

	while True:
		message = client.messages.list(
			to = "+17472334999"
			)

		textTime = message[0].date_created

		print "last text time= " + lastTextTime
		print "current text time= " + textTime
		
		if textTime != lastTextTime:
			ser.write('1')
			lastTextTime = textTime
		else: 
			ser.write('0')
			

	port = int(os.environ.get('PORT', 8090))
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)


	

