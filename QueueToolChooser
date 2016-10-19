set serverURL to "none"
set serverlist to {"Textbook-dev", "QA", "staging1", "staging2", "staging3", "staging4", "staging5"}
set server to {choose from list serverlist with title "Queue Tool Chooser" with prompt "Choose server to load queue tool:" OK button name {"OK"} cancel button name {"Cancel"} without multiple selections allowed}

# cancel don't work =(
if server is false then
	super quit
end if

if item 1 of server is {"Textbook-dev"} then
	set serverURL to "legacy-textbook-dev.cnx.org"
else if item 1 of server is {"QA"} then
	set serverURL to "legacy-textbook-qa.cnx.org"
	# else if item 1 of server is {"Production"} then
	#	set serverURL to "cnx.org"
else if item 1 of server is {"staging1"} then
	set serverURL to "legacy-staging1.cnx.org"
else if item 1 of server is {"staging2"} then
	set serverURL to "legacy-staging2.cnx.org"
else if item 1 of server is {"staging3"} then
	set serverURL to "legacy-staging3.cnx.org"
else if item 1 of server is {"staging4"} then
	set serverURL to "legacy-staging4.cnx.org"
else if item 1 of server is {"staging5"} then
	set serverURL to "legacy-staging5.cnx.org"
end if


open location "http://" & serverURL & "/queue_tool/manage_overview"
