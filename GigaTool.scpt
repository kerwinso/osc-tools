#CNX Collection GIGATOOL: Choose from 8 servers and 8 different actions!
# v2.2 (5-11-16) -- fixed production URL

global collectionID, cidlength, validID, servername, serverURL, baseurl
set validID to false

# Choose server
on chooseserver()
	set serverlist to {"Textbook-dev", "QA", "Production", "staging1", "staging2", "staging3", "staging4", "staging5"}
	set server to {choose from list serverlist with title "CNX collection GigaTool 2.2" with prompt "Choose server:" OK button name {"OK"} cancel button name {"Cancel"} without multiple selections allowed}
	
	#cancel button doesn't work
	if server is false then
		error number -128
		super quit
	end if
	
	if item 1 of server is {"Textbook-dev"} then
		set servername to "Textbook-dev"
		set serverURL to "legacy-textbook-dev.cnx.org"
	else if item 1 of server is {"QA"} then
		set servername to "QA"
		set serverURL to "legacy-textbook-qa.cnx.org"
	else if item 1 of server is {"Production"} then
		set servername to "Production"
		set serverURL to "legacy.cnx.org"
	else if item 1 of server is {"staging1"} then
		set servername to "staging1"
		set serverURL to "legacy-staging1.cnx.org"
	else if item 1 of server is {"staging2"} then
		set servername to "staging2"
		set serverURL to "legacy-staging2.cnx.org"
	else if item 1 of server is {"staging3"} then
		set servername to "staging3"
		set serverURL to "legacy-staging3.cnx.org"
	else if item 1 of server is {"staging4"} then
		set servername to "staging4"
		set serverURL to "legacy-staging4.cnx.org"
	else if item 1 of server is {"staging5"} then
		set servername to "staging5"
		set serverURL to "legacy-staging5.cnx.org"
	end if
end chooseserver

# Enter collection ID
on enterCID()
	set userinput to display dialog "Enter collection ID or module ID:" default answer "Use col12345 or 12345 for collections; or m12345 for modules" with title "CNX collection GigaTool 2.0"
	set collectionID to text returned of userinput
	set cidlength to length of collectionID
	#error check
	if cidlength = 5 then
		set validID to true
		set baseurl to "http://" & serverURL & "/content/col" & collectionID & "/latest/"
	else if cidlength = 8 and collectionID starts with "col" then
		set validID to true
		set baseurl to "http://" & serverURL & "/content/" & collectionID & "/latest/"
	else if cidlength = 6 and collectionID starts with "m" then
		set validID to true
		set baseurl to "http://" & serverURL & "/content/" & collectionID & "/latest/"
	else
		set validID to false
	end if
end enterCID


# Action list!
on moduleaction()
	set moduledialog to display dialog "Module ID entered, choose your action:" buttons {"Cancel", "View latest", "View source in Chrome"}
	set modulebutton to button returned of moduledialog
	if modulebutton = "View latest" then
		open location baseurl
	else if modulebutton = "View source in Chrome" then
		tell application "Google Chrome"
			activate
			open location baseurl & "source"
		end tell
	end if
end moduleaction

on chooseaction()
	set actionlist to {"Enqueue PDF", "Download complete zip", "query_ptool", "View printinfo", "View latest content", "Download PDF", "View version history", "Update print parameters", "Open queue tool *(mgr permissions req'd)"}
	set action to {choose from list actionlist with title "CNX collection GigaTool 2.0" with prompt "Choose action for collection:"}
	
	if item 1 of action is {"Enqueue PDF"} then
		enqueue()
	else if item 1 of action is {"Download complete zip"} then
		downloadzip()
	else if item 1 of action is {"query_ptool"} then
		queryptool()
	else if item 1 of action is {"View printinfo"} then
		printinfo()
	else if item 1 of action is {"View latest content"} then
		viewlatest()
	else if item 1 of action is {"Download PDF"} then
		downloadpdf()
	else if item 1 of action is {"View version history"} then
		versionhistory()
	else if item 1 of action is {"Update print parameters"} then
		updateparameters()
	else if item 1 of action is {"Open queue tool *(mgr permissions req'd)"} then
		open location "http://" & serverURL & "/queue_tool/manage_overview"
	end if
end chooseaction

#Action list Functions!
# Enqueue PDF 
on enqueue()
	display dialog "This will enqueue collection " & collectionID & " on " & servername & " in your default browser." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "enqueue"
	#delay 4
	#open location baseurl & "query_ptool"
end enqueue

# Download zip 
on downloadzip()
	display dialog "This will download the complete zip for collection " & collectionID & " on " & servername & " in your default browser." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "complete"
end downloadzip

# query_ptool
on queryptool()
	#display dialog "This will load query_ptool for collection " & collectionID & " on " & servername & " in your default browser." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "query_ptool"
end queryptool

# printinfo
on printinfo()
	#display dialog "This will load query_ptool for collection " & collectionID & " on " & servername & " in your default browser." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "printinfo"
end printinfo

#view latest 
on viewlatest()
	#display dialog "This will view the latest content in the editor for collection " & collectionID & " on " & servername & " in your default browser." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl
end viewlatest

#insert download pdf function here
on downloadpdf()
	display dialog "This will download the PDF for collection " & collectionID & " on " & servername & " in your default browser. 
	NOTE: this may take a while depending on the collection." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "pdf"
end downloadpdf

#insert version history function
on versionhistory()
	open location baseurl & "content_info"
end versionhistory

#update parameters
on updateparameters()
	display dialog "This will take you to the print parameter update page for " & collectionID & " on " & servername & " in your default browser. 

NOTE: Another dialog will appear shortly reminding you to setState back to public." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "collection_parameters"
	delay 5
	activate
	display dialog "Don't forget to setState back to public! Click OK now to do this." buttons {"Cancel", "OK"} default button "OK"
	open location baseurl & "setState?value=public"
end updateparameters


# CALL ALL FUNCTIONS, with error-checking logic
chooseserver()
repeat until validID is true
	enterCID()
	if validID is false then
		display dialog "Collection ID formatted incorrectly, click OK to retry" buttons {"Cancel", "OK"} default button "OK"
	else if collectionID starts with "m" then
		moduleaction()
	else
		chooseaction()
	end if
end repeat
