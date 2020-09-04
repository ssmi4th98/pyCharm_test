from unittest import TestCase
import src.HelloWorld as first


class Test(TestCase):
    def test_hello(self):
        self.assertEqual(first.Hello.hello(self), 'Hello, World')


