import webbrowser

validserver = False

def chooseserver():
	global server
	server = raw_input ("Enter 1 for Textbook-Dev, 2 for Textbook-QA server, 'q' to quit: ")

# WORKS, but need to set the actual servers
def servercheck():
	global validserver, server, baseURL
	if server.lower() =='q':
		exit()
	elif server == '1':
		validserver = True
		print "Dev server chosen"
		baseURL = 'http://legacy-textbook-dev.cnx.org/content/'
	elif server == '2':
		validserver = True
		print "QA server chosen"
		baseURL = 'http://legacy-textbook-qa.cnx.org/content/'
	else:
		validserver = False
		print "try again, enter 1 or 2"

#call the functions above
while validserver == False:
	chooseserver()
	servercheck()

inputfile = raw_input ("Enter the name of your text input file (default is './input.txt'): ")

#Hit Enter without typing anything to assume input file named 'input.txt'
if inputfile == '':
	inputfile = 'input.txt'
elif inputfile.lower() =='q':
	exit()
else:
	inputfile = inputfile

buildlist = open(inputfile)

for each in buildlist:
	collID = each.strip()
	if collID.startswith('col') and len(collID) == 8 and collID[3:].isdigit():
		buildurl = baseURL + collID + "/latest/enqueue"
		print "* " + collID + " enqueued"
	elif collID[0:4].isdigit() and len(collID) == 5:
		buildurl = baseURL + "/col" + collID + "/latest/enqueue"
		print "* " + collID + " enqueued"
	else: 
		print "* Skipped collection " + collID + " due to incorrect formatting"
		continue
	webbrowser.open(buildurl, new=0, autoraise=False)