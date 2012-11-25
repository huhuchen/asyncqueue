======================

asyncqueue: an asynchronous message queue

=====================

usage:

:: 

    import asyncqueue

    async = asyncqueue.Queue(["mail"], redis_host="localhost", redis_port=6379)

    @async.enqueue("mail")
    def send_mail():
        return {"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"}

    u = async.dequeue("mail")    
    ##u = {"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"} 
