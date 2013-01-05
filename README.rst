======================

asyncqueue: an asynchronous message queue

=====================

usage:

:: 

    from asyncqueue import Queue

    ex1:
    greet_queue = Queue("great", redis_host="localhost", redis_port=6379)

    def greet_friends(friend_name):
        greetings = "come on! %s" % friend_name
        return {"greetings": greetings}

    friend_name = "Tom"
    greet_queue.enqueue(greet_friends, friend_name)
    print greet_queue.worker()

    out:{'greetings': 'come on! Tom'} 


    ex2:
    notice_queue = Queue("notice")

    class Notice(object):
    
        def __init__(self):
            pass
    
        def remind_user(self, username):
            return {"username": username}

    notice = Notice()
    notice_queue.enqueue(notice.remind_user, "huhuchen")

    print notice_queue.worker()
    out:{'username': 'huhuchen'}


    ex3:
    mail_queue = Queue("mail")

    @mail_queue()
    def send_mail(subject, content, sender, destination):
        mail = {"subject": subject, "content": content, "sender": sender, "destination": destination}
        return mail
        
    send_mail.delay("welcome you!", "nice to meet you", "huhuchen@github", "god@heaven")
    print mail_queue.worker()
    out:{'content': 'nice to meet you', 'destination': 'god@heaven', 'sender': 'huhuchen@github', 'subject': 'welcome you!'}
