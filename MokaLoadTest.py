#coding=utf-8

import grequests,gevent,random,time

def getBooks(host,port,booknum,reqnum,prefix):
    '''协程函数'''
    #uid = random.randint(1,100000)
    #try:
    #    res = requests.get("http://{0}:{1}/guess/books/{2}/{3}".format(host, port, uid, booknum))
    #except requests.exceptions.Timeout:
    #    return -1
    #else:
    #    return res.status_code,res.elapsed.total_seconds()
    len_reqnum = len(reqnum)
    #请求生成器用prefix跟zfill填充的i组成uid
    reqite = (grequests.get("http://{0}:{1}/guess/books/{2}/{3}".format(host, port, prefix+str(i).zfill(len_reqnum+1), booknum),timeout=3) for i in xrange(reqnum))
    #统计map的执行时间
    s_time = time.time()
    ress = grequests.map(reqite)
    e_time = time.time()-s_time    #map执行时间
    failnum = 0    #请求失败次数
    restime = 0    #最大响应时间
    thresholds = iter([int(0.5*reqnum), int(0.9*reqnum), int(0.99*reqnum)])    #阈值生成器
    threshold = thresholds.next()    #当前阈值
    restimelist = []    #阈值最大响应时间列表
    i = 1    #阈值计数器
    for res in ress:
        if res:
            if res.status_code == 200:
                #替换最大响应时间
                if res.elapsed.total_seconds()>restime:
                    restime=res.elapsed.total_seconds()
            else:
                failnum+=1
        else:
            failnum+=1
        if i==threshold:    #记录当前阈值的最大响应时间并更新阈值
            restimelist.append(restime)
            threshold = thresholds.next()
        i+=1
    #restimelist倒数第二个元素为failnum，最后为e_time
    restimelist.append(failnum)
    restimelist.append(e_time)
    return restimelist