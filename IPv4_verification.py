a="17.316.254.1" 
b="2.254.255.0"
c='1m15.26.3.222'

def isIPv4Address(inputString):
    s=inputString.split('.')
    if len(s)!=4:
        return False
    for elem in s:
        if len(elem)==0:
            return False
        if not elem.isdigit():
            return False
        if not 0<=int(elem)<=255:
            return False
    return True
    
#print(isIPv4Address(a)) --> True
#print(isIPv4Address(b)) --> True
#print(isIPv4Address(c)) --> False