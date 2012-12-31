======================

asyncqueue: an asynchronous message queue

=====================

usage:

:: 

    import asyncqueue

    async = asyncqueue.queue(["mail"], redis_host="localhost", redis_port=6379)

    @async("mail")
    def send_mail():
        return {"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"}

    send_mail.delay()

    u = async.worker("mail")
    print u ##{"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"} 
