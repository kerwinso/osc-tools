# Purpose of this program: enqueue PDF, check latest version in legacy editor, or look up query_ptool for a given colid in Textbook-Dev only
# Version 2.0
# INITIALIZE VARIABLES
global collectionID, cidlength, validID, statusbutton, statusID
set validID to false
set serverID to 1

# FUNCTIONS
# User input
on inputCID()
	set userinput to display dialog "Textbook-Dev MegaTool (there will be no confirmations!): 
	
	Enter collection ID and choose action below:" default answer "either col12345 or 12345; or m12345 (view only)" buttons {"Enqueue PDF", "query_ptool", "View latest version in editor"}
	
	set collectionID to text returned of userinput
	set statusbutton to button returned of userinput
	if statusbutton = "Enqueue PDF" then
		set statusID to 1
	else if statusbutton = "query_ptool" then
		set statusID to 2
	else if statusbutton = "View latest version in editor" then
		set statusID to 3
	end if
	set cidlength to length of collectionID
end inputCID

# Error check of user input
on lengthcheck()
	if cidlength = 5 or cidlength = 8 then
		set validID to true
	else if cidlength = 6 and collectionID starts with "m" then
		set validID to true
	else
		set validID to false
	end if
end lengthcheck

# Main function, runs if CID is the correct length
on statusaction()
	#enqueue
	if statusID is 1 then
		if collectionID starts with "col" or collectionID starts with "m" then
			open location "http://legacy-textbook-dev.cnx.org/content/" & collectionID & "/latest/enqueue"
		else
			open location "http://legacy-textbook-dev.cnx.org/content/col" & collectionID & "/latest/enqueue"
		end if
		
		# query_ptool
	else if statusID is 2 then
		if collectionID starts with "col" or collectionID starts with "m" then
			open location "http://legacy-textbook-dev.cnx.org/content/" & collectionID & "/latest/query_ptool"
		else
			open location "http://legacy-textbook-dev.cnx.org/content/col" & collectionID & "/latest/query_ptool"
		end if
		
		# view latest
	else if statusID is 3 then
		if collectionID starts with "col" or collectionID starts with "m" then
			open location "http://legacy-textbook-dev.cnx.org/content/" & collectionID & "/latest"
		else
			open location "http://legacy-textbook-dev.cnx.org/content/col" & collectionID & "/latest"
		end if
	end if
	
end statusaction


# CALL FUNCTIONS, with error-checking logic
repeat until validID is true
	inputCID()
	lengthcheck()
	if validID is false then
		display dialog "Collection ID formatted incorrectly, click OK to retry" buttons {"Cancel", "OK"} default button "OK"
	else
		statusaction()
	end if
end repeat
