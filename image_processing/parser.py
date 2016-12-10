import re


f = open('data.txt', 'r')
txts = f.read().split('______________')
output = open('result.txt', 'w')
for idx, txt in enumerate(txts):
    amount_pattern = re.compile(r'[€$][\di‘,. ]+')
    client_pattern = re.compile(r'[Cc]lient [A-Z][a-z\-A-Z]+[\w\- .]*\n')
    ticker_pattern = re.compile(r'\b[A-Z\d]{5}\b')  # works good
    authorizer_pattern = re.compile(r'[Aa]uthorizer [A-Z][a-z\-\'A-Z]+[\w\-\' .]*\n')
    direction = -1
    if txt.find('SUB') >= 0 or txt.find('S U B') >= 0:
        direction = 'SUB'
    if txt.find('RED') >= 0 or txt.find('R E D') >= 0:
        direction = 'RED'

    client = client_pattern.findall(txt)
    ticker = ticker_pattern.findall(txt)
    i = 0
    while i < len(ticker):
        if ticker[i].lower() in {'black', 'krock', 'gamma'}:
            del ticker[i]
        else:
            i += 1
    if len(ticker) == 1:
        ticker = ticker[0]
    elif len(ticker) > 1:
        print('ticker error!: ', ticker)
        ticker = ticker[0]
    else:
        ticker = re.findall(r'\b[A-Z\d]{4}\b', txt)
        i = 0
        print(ticker)
        while i < len(ticker):
            if ticker[i] == 'MSCI' or ticker[i] == 'BLAC' or ticker[i] == 'EAFE' or \
                            ticker[i] == 'ACWI' or\
                    ticker[i].isdigit():
                del ticker[i]
            else:
                i += 1
        if len(ticker) == 1:
            ticker = ticker[0]
        else:
            ticker = re.findall(r'\b[A-Z\d]{3}\b', txt)
            i = 0
            while i < len(ticker):
                if ticker[i] == 'ETF' or ticker[i].isdigit():
                    del ticker[i]
                else:
                    i += 1
            if len(ticker) == 1:
                ticker = ticker[0]
            elif len(ticker) > 1:
                ticker = ticker[0]
                print('ticker:', ticker)
            else:
                print(idx, 'skipped')
                continue
    amount = amount_pattern.findall(txt)
    if len(amount) > 0:
        amount = amount[0].replace('i', ',').replace('‘', ',').replace(' ', '')
    else:
        amount = -1
    second = 'unknown'
    if len(client) == 1 and 'sign' not in client[0].lower() and 'client' not in client[0].lower():  # first type of image
        client = client[0].replace('Client', '').strip()
        second = authorizer_pattern.findall(txt)
        if len(second) > 0:
            second = second[0].replace('Authorizer', '').strip()
    else:
        txt = txt.replace('Financial Advisor Name', '').replace('Financial Adviser Name', '')
        txt = txt.replace('Financial Advisor Sign off', '').replace('Financial Adviser Sign off', '')
        name_pattern = re.compile(r'[A-Z][a-z\-A-Z]+\b [A-Z]+[\w.]*\b')
        names = name_pattern.findall(txt)
        print(names)
        i = 0
        while i < len(names):
            if 'investment' in names[i].lower() or\
                            'fund' in names[i].lower() or\
                            'credit' in names[i].lower() or\
                            'client' in names[i].lower() or\
                            'ticker' in names[i].lower() or \
                            'blac' in names[i].lower() or \
                            'krock' in names[i].lower() or \
                            'duration' in names[i].lower() or \
                            'index' in names[i].lower() or \
                            'total' in names[i].lower() or \
                            'income' in names[i].lower() or \
                            'term' in names[i].lower() or \
                            'trust' in names[i].lower() or \
                            'product' in names[i].lower() or \
                            'opportunities' in names[i].lower() or \
                            'secondary' in names[i].lower() or \
                            'sign' in names[i].lower() or \
                            'basic' in names[i].lower() or \
                            'name' in names[i].lower() or \
                            'advisor' in names[i].lower() or \
                            'please' in names[i].lower() or \
                            'complete' in names[i].lower() or \
                            'currency' in names[i].lower() or \
                            'msci' in names[i].lower() or \
                            'eafe' in names[i].lower() or \
                            'account' in names[i].lower() or \
                            'details' in names[i].lower() or \
                            'corporate' in names[i].lower() or \
                    'direction' in names[i].lower() or \
                    'value' in names[i].lower() or \
                    'active' in names[i].lower() or \
                    'new' in names[i].lower() or \
                    'international' in names[i].lower() or\
                    'authorizer' in names[i].lower():
                del names[i]
            else:
                i += 1
        if len(names) == 2:
            client = names[0]
            second = names[1]
        elif len(names) == 1:
            client = names[0]
        elif len(names) > 2:
            client = names[0]
            second = names[-2]
            print(names)
        else:
            print(names)
    output.write("ticker: '{}', amount: '{}', client: '{}', second: '{}', direction: '{}'\n".format(
          ticker, amount, client, second, direction))
    print(idx)
f.close()
output.close()
