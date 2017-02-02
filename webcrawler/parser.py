import requests
from bs4 import BeautifulSoup


class Parser(object):
    def __init__(self, helper, encoding, base_url=None):
        """
        Crawls content from base_url using specific values from the helper.
        """
        super(Parser, self).__init__()
        self.helper = helper
        self.encoding = encoding
        self.base_url = helper.BASE_URL() if base_url is None else base_url

    def get_document(self, url, payload):
        """
        Load content from url and return a query enabled document. A dictionary
        of get parameters can be set in payload.
        """
        request = requests.get(url, params=payload)
        return BeautifulSoup(request.text, 'lxml')

    def landline_price(self, country_code):
        """
        Returns the landline price for a given country code.
        """
        document = self.get_document(self.base_url, { 'countryId': country_code })
        selection = document.select(self.helper.LANDLINE_PRICE_SELECTOR())
        element = selection[0]

        return element.string.encode(self.encoding).strip()

    def mobile_price(self, country_code):
        """
        Returns the mobile price for a given country code.
        """
        document = self.get_document(self.base_url, { 'countryId': country_code })
        selection = document.select(self.helper.MOBILE_PRICE_SELECTOR())
        element = selection[0]

        return element.string.encode(self.encoding).strip()

    def text_message_price(self, country_code):
        """
        Returns the text message price for a given country code.
        """
        document = self.get_document(self.base_url, { 'countryId': country_code })
        selection = document.select(self.helper.TEXT_MESSAGE_SELECTOR())
        element = selection[0]

        return element.string.encode(self.encoding).strip()
