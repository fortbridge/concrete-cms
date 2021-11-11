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

    for i in range(500000):
        engine.queue(target.req) # my upload
        
def handleResponse(req, interesting):
    if req.status!=404: 
         table.add(req)

