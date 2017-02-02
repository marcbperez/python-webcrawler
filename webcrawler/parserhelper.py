class ParserHelper(object):
    def __init__(self):
        """
        Contains the default base url, query selectors, country codes and other
        necessary information. This file should be self explanatory.
        """
        super(ParserHelper, self).__init__()

    def BASE_URL(self):
        return \
        'http://international.o2.co.uk/internationaltariffs/getintlcallcosts'

    def LANDLINE_PRICE_SELECTOR(self):
        return '#paymonthlyTariffPlan #standardRatesTable tr:nth-of-type(1) \
            td:nth-of-type(2)'

    def MOBILE_PRICE_SELECTOR(self):
        return '#paymonthlyTariffPlan #standardRatesTable tr:nth-of-type(2) \
            td:nth-of-type(2)'

    def TEXT_MESSAGE_SELECTOR(self):
        return '#paymonthlyTariffPlan #standardRatesTable tr:nth-of-type(3) \
            td:nth-of-type(2)'

    def CANADA(self):
        return 'CAN'

    def GERMANY(self):
        return 'DEU'

    def ICELAND(self):
        return 'ISL'

    def PAKISTAN(self):
        return 'PAK'

    def SINGAPORE(self):
        return 'SGP'

    def SOUTH_AFRICA(self):
        return 'ZAF'
