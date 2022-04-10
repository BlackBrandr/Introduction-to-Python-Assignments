class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getsymbol(self):
        return self.__symbol

    def getname(self):
        return self.__name

    def getpreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getcurrentPrice(self):
        return self.__currentPrice

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) / (self.__previousClosingPrice * 100)


def main():

    stock = Stock("INTC", "IntelCorporation" , 20.5 , 20.35)

    print("The price change of", stock.getname(),"(", stock.getsymbol(), ")", "is", stock.getChangePercent())

main()