import yagmail

def ymail():
    #the Gmail user is the parameter
    yag = yagmail.SMTP('oscontentqa')
    vari = "some string here"
    contents = [

    'This is the body, and here is just text. Next, here is a variable: ' + vari +'. \n This should be on a new line.'
    ]
    yag.send('brw5@rice.edu', 'Yagmail test', contents)

ymail()