#coding=utf-8

import grequests,gevent,random,time

def getBooks(host,port,booknum,reqnum):
    #uid = random.randint(1,100000)
    #try:
    #    res = requests.get("http://{0}:{1}/guess/books/{2}/{3}".format(host, port, uid, booknum))
    #except requests.exceptions.Timeout:
    #    return -1
    #else:
    #    return res.status_code,res.elapsed.total_seconds()
    reqite = (grequests.get("http://{0}:{1}/guess/books/{2}/{3}".format(host, port, uid, booknum),timeout=3) for i in xrange(reqn
um))
    s_time = time.time()
    ress = grequests.map(rs)
    e_time = time.time()-s_time
    failnum = 0 
    restime = 0 
    thresholds = itre([int(0.5*reqnum), int(0.9*reqnum), int(0.99*reqnum)]) 
    restimelist = []
    i = 1 
    for res in ress:
        if res:
            if res.status_code == 200:
                if res.elapsed.total_seconds()>restime:
                    restime=res.elapsed.total_seconds()
            else:
                failnum+=1
        else:
            failnum+=1
