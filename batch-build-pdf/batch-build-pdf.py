import webbrowser

validserver = False
validfile = False

def chooseserver():
	global validserver, server, baseURL, servername
	server = raw_input ("Enter 1 for Textbook-Dev, 2 for Textbook-QA server, 'q' to quit: ")

	if server.lower() =='q':
		exit()
	elif server == '1':
		validserver = True
		print "Dev server chosen"
		baseURL = 'http://legacy-textbook-dev.cnx.org/content/'
		servername = 'Textbook-Dev'
	elif server == '2':
		validserver = True
		print "QA server chosen"
		baseURL = 'http://legacy-textbook-qa.cnx.org/content/'
		servername = 'Textbook-QA'
	else:
		print "try again, enter 1 or 2"

def choosefile():
	global inputfile
	inputfile = raw_input ("Enter the name of your text input file (default is './input.txt'): ")
	if inputfile == '':	inputfile = 'input.txt'

#call the functions above
while validserver == False:
	chooseserver()
choosefile()
while validfile == False:
	try:
		buildlist = open(inputfile)
		validfile = True
	except:
		print "Invalid file, try again"
		choosefile()

for each in buildlist:
	collID = each.strip()
	if collID.startswith('col') and len(collID) == 8 and collID[3:].isdigit():
		buildurl = baseURL + collID + "/latest/enqueue"
		print "* " + collID + " enqueued on " + servername
	elif collID[0:4].isdigit() and len(collID) == 5:
		buildurl = baseURL + "/col" + collID + "/latest/enqueue"
		print "* " + collID + " enqueued on " + servername
	else: 
		print "* Skipped collection " + collID + " due to incorrect formatting"
		continue
	webbrowser.open(buildurl, new=0, autoraise=False)