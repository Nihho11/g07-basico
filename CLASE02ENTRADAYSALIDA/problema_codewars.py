def ips_between(start,end):
    bro=1
    a=0
    c=4
    for i in range(len(start.split("."))):
        if start.split(".")[i]<end.split(".")[i]:
            a=end.split(".")[i]-start.split(".")[i]
            

    return start

ips_between("10.0.0.0",2)