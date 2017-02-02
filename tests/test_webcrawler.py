# coding=utf-8

import unittest

from webcrawler.parser import Parser
from webcrawler.parserhelper import ParserHelper


class WebcrawlerTest(unittest.TestCase):
    def test_canada(self):
        helper = ParserHelper()
        parser = Parser(helper, 'utf-8')
        country = helper.CANADA()

        self.assertEquals(parser.landline_price(country), '£1.50')
        self.assertEquals(parser.mobile_price(country), '£1.50')
        self.assertEquals(parser.text_message_price(country), '35p')

    def test_germany(self):
        helper = ParserHelper()
        parser = Parser(helper, 'utf-8')
        country = helper.GERMANY()

        self.assertEquals(parser.landline_price(country), '£1.50')
        self.assertEquals(parser.mobile_price(country), '£1.50')
        self.assertEquals(parser.text_message_price(country), '35p')

    def test_iceland(self):
        helper = ParserHelper()
        country = helper.ICELAND()
        parser = Parser(helper, 'utf-8')

        self.assertEquals(parser.landline_price(country), '£1.50')
        self.assertEquals(parser.mobile_price(country), '£1.50')
        self.assertEquals(parser.text_message_price(country), '35p')

    def test_pakistan(self):
        helper = ParserHelper()
        country = helper.PAKISTAN()
        parser = Parser(helper, 'utf-8')

        self.assertEquals(parser.landline_price(country), '£2.00')
        self.assertEquals(parser.mobile_price(country), '£2.00')
        self.assertEquals(parser.text_message_price(country), '35p')

    def test_singapore(self):
        helper = ParserHelper()
        country = helper.SINGAPORE()
        parser = Parser(helper, 'utf-8')

        self.assertEquals(parser.landline_price(country), '£1.50')
        self.assertEquals(parser.mobile_price(country), '£1.50')
        self.assertEquals(parser.text_message_price(country), '35p')

    def test_south_africa(self):
        helper = ParserHelper()
        country = helper.SOUTH_AFRICA()
        parser = Parser(helper, 'utf-8')

        self.assertEquals(parser.landline_price(country), '£1.50')
        self.assertEquals(parser.mobile_price(country), '£1.50')
        self.assertEquals(parser.text_message_price(country), '35p')
