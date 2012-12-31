#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for asyncqueue"""

from tests import AsyncqueueTestCase
from asyncqueue import queue

mail_queue = queue("mail")
greet_queue = queue("greet")

@greet_queue()
def greet_friends(friend_name):
    greetings = "come on! %s" % friend_name
    return {"greetings": greetings}

@mail_queue()
def send_mail(subject, content, sender, destination):
    mail = {"subject": subject, "content": content, "sender": sender, "destination": destination}
    return mail

def handler():
    friend_name = "Tom"
    greet_friends.delay(friend_name)

    send_mail.delay("welcome you!", "nice to meet you", "huhuchen@github", "god@heaven")

    print mail_queue.worker()
    print greet_queue.worker()

class QueueTestCase(AsyncqueueTestCase):

    def test_handler(self):
        handler()


