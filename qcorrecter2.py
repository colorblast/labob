def qcorrecter2(string):
    yandex0=False
    yandex1=False
    for x in range(len(string)):
        if string[x]=='"' and yandex0==False:
            string=string[:x]+"``"+string[x+1:]
            yandex0=True
    return(string)
