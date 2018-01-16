# Version 4.0 for Alan

# initialize variables
global username, sudopassword, collectionID, cidlength, validID, user, gitpath
set validID to false

#Functions

on set_user()
	display dialog "GitLogin 4.0: Which server do you want to log in to?" buttons {"Cancel", "textbook-dev", "devb"} default button "devb"
	if result = {button returned:"textbook-dev"} then
		set user to "alan@legacy-textbook-dev.cnx.org"
		set gitpath to "cd /opt/cnx-buildout/src/Products.RhaptosPrint/Products/RhaptosPrint/epub"
	else if result = {button returned:"devb"} then
		set user to "alan@devb.cnx.org"
		set gitpath to "cd /var/lib/cnx/cnx-buildout/epub"
	end if
end

# enter sudo password after ssh
on sudopwd()
	set sudopassword to the text returned of (display dialog "Alan, what is your sudo password?" default answer "" with hidden answer)
end sudopwd

#execute login process
on executelogin()
	tell application "Terminal"
		
		do script "ssh -t " & user & " exec sudo -H -u www-data -s /bin/bash" in window 1
		activate
		delay 3
		do script sudopassword in window 1
		delay 3
		do script gitpath in window 1
		delay 3
		do script "git branch -a" in window 1
		
	end tell
end executelogin

# get collection ID to check transforms
on entercolID()
	set collectionID to the text returned of (display dialog "Enter 5-digit ID of the collection to monitor:" default answer "you can use either col12345 or 12345" buttons {"Cancel", "Continue"} default button "Continue")
	set cidlength to length of collectionID
	
	# standardize collection ID formatting
	if collectionID starts with "col" then
		set collectionID to collectionID
	else
		set collectionID to "col" & collectionID
	end if
	
	# for error checking
	if cidlength = 5 or cidlength = 8 then
		set validID to true
	else
		set validID to false
	end if
	
end entercolID

# check on transforms in real-time
on monitortransform()
	tell application "Terminal"
		do script "cd /tmp" in window 1
		delay 1
		do script "ls -ltr" in window 1
		delay 4
		do script "tail colprint_" & collectionID & ".stderr -f" in window 1
		
	end tell
end monitortransform

# Run the thing! determine which flow to do
set_user()
display dialog "What do you want to do?" buttons {"Cancel", "Git login only", "Git login with transform monitoring"} default button "Git login only"
if result = {button returned:"Git login only"} then
	sudopwd()
	executelogin()
else if result = {button returned:"Git login with transform monitoring"} then
	repeat until validID is true
		entercolID()
		if validID is false then
			display dialog "Collection ID formatted incorrectly, click OK to retry" buttons {"Cancel", "OK"} default button "OK"
		else
			sudopwd()
			executelogin()
			monitortransform()
		end if
	end repeat
end if
