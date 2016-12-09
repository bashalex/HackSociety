import re
import random


class Transaction:
    def __init__(self, ticker, amount, client, second, direction):
        self.ticker = ticker
        self.amount = amount
        self.client = client
        self.second = second
        self.direction = direction


class Data:
    path = 'result.txt'
    lineNum = 0
    file = open(path, 'r')
    lines = file.readlines()
    tickers, amounts, clients, seconds, directions = [], [], [], [], []

    for line in lines:
        tickersPat = re.compile("ticker: '(.*)', amount")
        tickers.append(tickersPat.findall(line)[0])
        amountsPat = re.compile("amount: '(.*)', client")
        amounts.append(amountsPat.findall(line)[0])
        clientsPat = re.compile("client: '(.*)', second")
        clients.append(clientsPat.findall(line)[0])
        secondsPat = re.compile("second: '(.*)', direction")
        seconds.append(secondsPat.findall(line)[0])
        directionsPat = re.compile("direction: '(.*)'")
        directions.append(directionsPat.findall(line)[0])
        lineNum += 1

    transactions = []
    for i in range(0, lineNum):
        transactions.append(Transaction(tickers[i], amounts[i], clients[i], seconds[i], directions[i]))

    def findTopInvestor(self):
        maximum = 0
        for transaction in self.transactions:
            current_amount = transaction.amount[1:-3]
            current_amount = current_amount.replace(",", "")
            current_amount = int(current_amount.replace(".", ""))
            if maximum < current_amount:
                maximum = current_amount
                top_investor = transaction.client
        return top_investor

    def returnRand(self):
        rand = random.randrange(0,len(self.transactions))
        return rand

    def returnMostSuAdvisor(self):
        maxAppearances = 0
        for transaction1 in self.transactions:
            appearances = 0
            for transaction2 in self.transactions:
                if transaction1.second == transaction2.second:
                    appearances += 1
            if appearances > maxAppearances:
                maxAppearances = appearances
                toReturn = transaction1.second
        return toReturn

    def next_question(self):
        q = []

        link0 = "http://pngimg.com/upload/money_PNG3545.png"
        q.append((link0, "Who is the guy who invested the most up until now ?", self.findTopInvestor(), self.transactions[self.returnRand()].client, 0))

        link1 = "http://assets.howtobecome.com/assets/images/2014/03/Financial-Advisor.jpg"
        transaction1 = self.transactions[self.returnRand()]
        q.append((link1, "Who is the financial advisor of " + transaction1.client + " ?", transaction1.second, self.transactions[self.returnRand()].client, 0))

        link2 = "http://inspiregroup.ro/wp-content/uploads/2015/08/success-1.jpg"
        q.append((link2, "Who is the most succesfull advisor ?", self.returnMostSuAdvisor(), self.transactions[self.returnRand()].second, 0))

        # link3 = "https://media1.popsugar-assets.com/files/thumbor/9xeS3fpQc1QdvdtpD5I4grLYMI4/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2012/09/36/2/192/1922398/2540217bec064a5c_71841717_10/i/Brad-Pitt-got-handsy-2006-press-conference-Babel.jpg"
        # q.append((link3, "How many times does Brad Pitt appears in our transaction data?"))
        return q[random.randrange(0, len(q))]

a = Data()
print(a.next_question())
