======================

asyncqueue: an asynchronous message queue

=====================

usage:

:: 

    import asyncqueue

    mail_queue = asyncqueue.queue("mail", redis_host="localhost", redis_port=6379)

    @mail_queue()
    def send_mail():
        return {"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"}

    send_mail.delay()

    u = mail_queue.worker()
    print u ##{"sender": huhuchen@gmail.com, "to": "god@heaven", "content": "hello god"} 
