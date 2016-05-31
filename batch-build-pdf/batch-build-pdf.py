# add docstring
"""
Build book PDFs in batch.

https://github.com/kerwinso/osc-tools
"""

# use cURL : http://pycurl.io/
# or requests : http://docs.python-requests.org/en/master/
# instead of a full browser
# import webbrowser
import requests
# check if a file exists before trying to read it
import os.path

# move the variables to the global namespace automatically
# and use standard naming conventions
server = ''
base_url = ''
server_name = ''
# use return values instead of variables
# validserver = False
# validfile = False


# def chooseserver():
def choose_server():
    """Select textbook server."""  # add the function docstring
    # global validserver, server, baseURL, servername
    global server, base_url, server_name
    # use spaces instead of tabs for indentation - allows flexibility for users
    # aim for a max code width of 80 characters
    server = raw_input("Enter 1 for Textbook-Dev, 2 for Textbook-QA " +
                       "server, 'q' to quit: ")
    if server.lower() == 'q':
        exit()
    # merge '' and '1' because the actions are the same
    # elif server == '':
    elif server == '' or server == '1':
        # use return value instead
        # validserver = True
        print('Dev server chosen')
        base_url = 'http://legacy-textbook-dev.cnx.org/content/'
        server_name = 'Textbook-Dev'
        return True
    # merged above
    # elif server == '1':
    #     validserver = True
    #     print "Dev server chosen"
    #     baseURL = 'http://legacy-textbook-dev.cnx.org/content/'
    #     servername = 'Textbook-Dev'
    elif server == '2':
        # validserver = True
        # use return value instead
        print('QA server chosen')
        base_url = 'http://legacy-textbook-qa.cnx.org/content/'
        server_name = 'Textbook-QA'
        return True
    else:
        print('try again, enter 1 or 2')


def choose_file():
    """Select the batch input file."""  # add the function docstring
    # global inputfile
    # aim for a max code width of 80 characters
    file_name = raw_input("Enter the name of your text input file " +
                          "(default is './input.txt'): ")
    # keep a line to a single command unless using the uniary operator:
    # in general, casting in Python is bad i.e. "bool(_____)" but it makes the
    # line a bit clearer
    return file_name if bool(file_name) else 'input.txt'
    # if inputfile == '':   inputfile = 'input.txt'


# call the functions above
while not choose_server():
    pass
input_file = choose_file()
while not os.path.isfile(input_file):
    print('Invalid file, try again')
    input_file = choose_file()

# use 'with' to open and close a file cleanly
# use Python naming conventions
with open(input_file, 'r') as batch:
    for collection in batch:
        collection_id = collection.strip()
        if collection_id.startswith('col') and len(collection_id) == 8 and \
                collection_id[3:].isdigit():
            build_url = '%s%s/latest/enqueue' % (base_url, collection_id)
            print('* %s enqueued on %s' % (collection_id, server_name))
            print(requests.get(build_url))
        elif collection_id[0:4].isdigit() and len(collection_id) == 5:
            build_url = '%s/col%s/latest/enqueue' % (base_url, collection_id)
            print('* %s enqueued on %s' % (collection_id, server_name))
            print(requests.get(build_url))
        else:
            print('* Skipped collection %s due to incorrect formatting' %
                  collection_id)
# for each in buildlist:
#     collID = each.strip()
#     if collID.startswith('col') and len(collID) == 8 and collID[3:].isdigit()
# :
#         buildurl = baseURL + collID + "/latest/enqueue"
#         print "* " + collID + " enqueued on " + servername
#     elif collID[0:4].isdigit() and len(collID) == 5:
#         buildurl = baseURL + "/col" + collID + "/latest/enqueue"
#         print "* " + collID + " enqueued on " + servername
#     else:
#         print "* Skipped collection " + collID + " due to incorrect formattin
# g"
#         continue
#     webbrowser.open(buildurl, new=0, autoraise=False)
