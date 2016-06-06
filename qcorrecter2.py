def qcorrecter2(string):
    yandex0=False
    yandex1=False
    for x in range(len(string)):
        if string[x]=='"' and yandex0==False:
            string=string[:x]+"``"+string[x+1:]
            yandex0=True
        if string[x]=='"' and yandex0==True:
            string=string[:x]+"''"+string[x+1:]
            yandex0=False
        if string[x]=="'" and yandex1==False:
            string=string[:x]+"`"+string[x+1:]
            yandex1==True
        if string[x]=="'" and yandex1==True:
            yandex1==False
    for x in string:
        if x == '“':
            string.replace(x,"``")
        if x == '”':
            string.replace(x,"''")
        if x == "‘":
            string.replace(x,"`")
        if x == "’":
            string.replace(x,"'")
    return(string)
