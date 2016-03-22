import webbrowser

inputfile = raw_input ("Enter the name of your text input file: ")

#Hit Enter without typing anything to assume an input file named 'input.txt' on your desktop
if inputfile == '':
	inputfile = 'input.txt'
else:
	inputfile = inputfile

buildlist = open(inputfile)

for each in buildlist:
	collID = each.strip()
	if collID.startswith('col') and len(collID) == 8 and collID[3:].isdigit():
		buildurl = "http://legacy-textbook-dev.cnx.org/content/" + collID + "/latest/enqueue"
		print "* " + collID + " enqueued on textbook-dev (starts with col)"
	elif collID[0:4].isdigit() and len(collID) == 5:
		buildurl = "http://legacy-textbook-dev.cnx.org/content/col" + collID + "/latest/enqueue"
		print "* " + collID + " enqueued on textbook-dev (does not start with col)"
	else: 
		print "* Skipped collection " + collID + " due to incorrect formatting"
		continue
	webbrowser.open(buildurl, new=0, autoraise=False)