#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for asyncqueue"""

from tests import AsyncqueueTestCase
from asyncqueue import Queue

mail_queue = Queue("mail")
greet_queue = Queue("greet")
notice_queue = Queue("notice")

@greet_queue()
def greet_friends(friend_name):
    greetings = "come on! %s" % friend_name
    return {"greetings": greetings}

@mail_queue()
def send_mail(subject, content, sender, destination):
    mail = {"subject": subject, "content": content, "sender": sender, "destination": destination}
    return mail

class Notice(object):

    def __init__(self):
        pass

    @notice_queue()
    def remind_user(self, username):
        return {"username": username}

class QueueTestCase(AsyncqueueTestCase):

    def test_function_job(self):
        friend_name = "Tom"
        greet_friends.delay(friend_name)

        send_mail.delay("welcome you!", "nice to meet you", "huhuchen@github", "god@heaven")

        print mail_queue.worker()
        print greet_queue.worker()

    def test_method_job(self):
        notice = Notice()
        notice.remind_user.delay("huhuchen")

        print notice_queue.worker()

