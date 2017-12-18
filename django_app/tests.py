from django.test import TestCase

# Create your tests here.
#!/usr/bin/env python
# -*- conding:utf-8 -*-

import  datetime
from django.utils import  timezone

from .models import Question

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_futrue_quesiton(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futrue_quesiton = Question(pub_date=time)
        self.assertEqual(futrue_quesiton.was_published_recently(),False)

    def test_was_published_recently_with_old_quesiton(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(),False)\

    def test_was_published_recently_with_recent_quesiton(self):
        time = timezone.now() -  datetime.timedelta(hours=1)
        recent_quesiton = Question(pub_date=time)
        self.assertEqual(recent_quesiton.was_published_recently(),True)









