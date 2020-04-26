import re #importing regex

def email():
    txt = open("EmailValidator.txt", "r")
    x = re.findall('\n([\w%\-+.!]{1,64}|^\"[\s\w\.]{1,62}\")(@{1}[\w\-]{1,})([^@])([\w.+-@\%]{1,})',txt.read())
    print(x)
    return;

def websites():
    txt = open("websites.txt", "r")
    x = re.findall('\n(http://|https://)?([/.])?(www.)?([\w\d/?%#+&=-]{1,})([/.]{1}([a-zA-Z]){2,3})([\w\d/#=+&%?-]{0,})',txt.read())
    print(x)
    return;
email()
websites()

