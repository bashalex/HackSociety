import re
import random


class Transaction:
    def __init__(self, tx):
        ticker, amount, client, second, direction = tx
        self.ticker = ticker
        self.amount = amount
        self.client = client
        self.second = second
        self.direction = direction


class Data:
    path = 'result.txt'
    transactions = []
    actors = {'Brad Pitt': "https://media1.popsugar-assets.com/files/thumbor/9xeS3fpQc1QdvdtpD5I4grLYMI4/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2012/09/36/2/192/1922398/2540217bec064a5c_71841717_10/i/Brad-Pitt-got-handsy-2006-press-conference-Babel.jpg",
              'George C. Scott': "http://movieactors.com/photos-stars/george-c-scott-changeling-808.jpg",
              'Jude Law': "http://www.kino-teatr.ru/news/3452/44235.jpg",
              'Mel Gibson': "http://img.cinemablend.com/cb/e/5/1/b/7/5/e51b75eea3d12e2e7558f24d1ba71bce26aabaac524dd9caa4ba17eb7bb64ca7.jpg",
              'Tom Hanks': 'https://pmcvariety.files.wordpress.com/2016/09/tom-hanks.jpg?w=670&h=377&crop=1',
              'Will Smith': 'https://static.independent.co.uk/s3fs-public/styles/story_medium/public/thumbnails/image/2015/10/02/12/Will-Smith-Fresh-Prince.jpg',
              'Robbin Williams': 'http://static.parade.com/wp-content/uploads/2013/09/robin-williams-cover-ftr.jpg',
              'George Clooney': 'http://vignette2.wikia.nocookie.net/muppet/images/c/c8/George_Clooney.jpg/revision/latest?cb=20151209144015',
              'Matt Damon': 'http://cp91279.biography.com/1000509261001/1000509261001_2036180457001_BIO-Biography-Matt-Damon-LF.jpg',
              'Nicolas Cage': 'https://discdoesretro.files.wordpress.com/2013/07/tumblr_mftalf5cpv1qa934fo1_1280.png',
              'Woody Allen': 'http://www.woodyallenpages.com/wp-content/uploads/2015/08/woodyportrait-xlarge.jpg',
              'Anthony Hopkins': 'http://img.cinemablend.com/cb/e/5/e/d/1/9/e5ed19acebd1505b5e5f94a4145ab27913521cfa4c3f4b18f72fefd8dc8cdb9f.jpg',
              'Gary Oldman': 'https://saymber.files.wordpress.com/2015/10/bram-stoker-s-dracula-bram-stokers-dracula-gary-oldman.jpg?w=1024',
              'Samuel L Jackson': 'http://cdn1-www.craveonline.com/assets/uploads/2015/06/Samuel-L-Jackson-Pulp-Fiction.jpg',
              'Antonio Banderas': 'http://www.hotflick.net/flicks/1995_Desperado/big/fhd995PDO_Antonio_Banderas_013.jpg',
              'John Wayne': 'http://cdn.images.express.co.uk/img/dynamic/79/590x/11f38wayne1-469761.jpg',
              'Joseph Fiennes ': 'http://www.christianitytoday.com/images/67668.jpg?w=640',
              'Ben Kingsley': 'http://resizing.flixster.com/vKmH_1OS3Mm3RBPnToapsISpHuI=/700x380/dkpu1ddg7pbsk.cloudfront.net/site/10/27/28/10272876_ori.jpg',
              'Robert Redford': 'http://cp91279.biography.com/Robert-Redford_Early-Life_HD_768x432-16x9.jpg',
              'Sylvester Stallone': 'http://images.indianexpress.com/2016/01/sylvester-stallone-759.jpg',
              'Paul Newman': 'http://www.bestmoviesbyfarr.com.s3.amazonaws.com/articles/5ppqsS/images/2-1jjgrhu.jpg',
              'Roger Moore': 'http://www.007.com/wp-content/uploads/2014/01/Roger-Moore-james-bond-BW.jpg',
              'John Goodman': 'http://i.onionstatic.com/avclub/5568/96/16x9/960.jpg',
              'Gene Hackman': 'http://www.bestmoviesbyfarr.com/static-assets/images/articles/background/2016/01/gene-hackman-big.jpeg',
              'Mickey Rourke': 'http://www.hobbyconsolas.com/sites/hobbyconsolas.com/public/media/image/2015/02/448068-cine-superheroes-critica-iron-man-2.png',
              'Sean Connery': 'https://s-media-cache-ak0.pinimg.com/originals/d8/a3/c0/d8a3c0ee40b509ee3f4b2c6f844ea08a.jpg'}

    with open('questions.txt', 'r') as f:
        custom_questions = [line.split(';') for line in f.readlines()]

    custom_questions1 = [('What do you think Sean Connery spent €12,122,387.00 on?',
                          'https://s-media-cache-ak0.pinimg.com/originals/d8/a3/c0/d8a3c0ee40b509ee3f4b2c6f844ea08a.jpg',
                          'Ferrari 340/375 MM Berlinetta',
                          'Aston Martin DB4 GT')]

    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    tickers, amounts, clients, seconds, directions = [], [], [], [], []

    line_num = 0
    for i, line in enumerate(lines):
        tickers_pat = re.compile("ticker: '(.*)', amount")
        tickers.append(tickers_pat.findall(line)[0])
        amounts_pat = re.compile("amount: '(.*)', client")
        amounts.append(amounts_pat.findall(line)[0])
        clients_pat = re.compile("client: '(.*)', second")
        clients.append(clients_pat.findall(line)[0])
        seconds_pat = re.compile("second: '(.*)', direction")
        seconds.append(seconds_pat.findall(line)[0])
        directions_pat = re.compile("direction: '(.*)'")
        directions.append(directions_pat.findall(line)[0])
        line_num += 1

    for tx in zip(tickers, amounts, clients, seconds, directions):
        transactions.append(Transaction(tx))

    def random_actor(self):
        actor_id = random.randrange(len(self.actors))
        actor_name = None
        for _id, actor in enumerate(self.actors.keys()):
            if _id == actor_id:
                actor_name = actor
                break
        return actor_name

    def random_custom_question(self):
        return self.custom_questions[random.randrange(len(self.custom_questions))]

    def random_custom1_question(self):
        return self.custom_questions1[random.randrange(len(self.custom_questions1))]

    @staticmethod
    def amount_to_int(amount):
        return int(amount[1:-3].replace(',', '').replace('.', ''))

    @staticmethod
    def int_to_amount(amount):
        result = '00.'
        for i, symbol in enumerate(reversed(str(amount))):
            result += symbol
            if i % 3 == 2 and i != len(str(amount)) - 1:
                result += ','
        result += '€'
        return result[::-1]

    def richest_investor(self):
        maximum, top_investor = 0, None
        for transaction in self.transactions:
            current_amount = self.amount_to_int(transaction.amount)
            if maximum < current_amount:
                maximum = current_amount
                top_investor = transaction.client
        return top_investor

    def random_tx(self):
        return self.transactions[random.randrange(0, len(self.transactions))]

    def most_active_advisor(self):
        num_of_deals, advisor_name = 0, None
        for tx in self.transactions:
            _num_of_deals = self.num_of_entries_advisor(tx.second)
            if _num_of_deals > num_of_deals:
                num_of_deals = _num_of_deals
                advisor_name = tx.second
        return advisor_name

    def invested_money(self, name):
        return sum(self.amount_to_int(tx.amount) for tx in self.transactions if tx.client == name and tx.direction == 'RED')

    def withdrawn_money(self, name):
        return sum(self.amount_to_int(tx.amount) for tx in self.transactions if tx.client == name and tx.direction == 'SUB')

    def num_of_entries_advisor(self, name):
        return sum(1 for tx in self.transactions if tx.second == name)

    def number_of_entries_client(self, name):
        return sum(1 for tx in self.transactions if tx.client == name)

    @staticmethod
    def shuffle_answers(good_answer, bad_answer):
        ans = [good_answer, bad_answer]
        r = random.randrange(0, 2) == 0
        correct = 0 if r else 1
        return [ans[0] if r else ans[1], ans[1] if r else ans[0], correct]

    def next_question(self):
        question_type = random.randrange(0, 100)
        ans = None, None
        if question_type == 0:  # who is the guy who invested more money than others until now? 1%
            while ans[0] == ans[1]:
                ans = self.shuffle_answers(self.richest_investor(), self.random_tx().client)
            link = "http://pngimg.com/upload/money_PNG3545.png"
            question_text = "Who is the guy who invested more money than others until now?"
        elif question_type == 1:  # which advisor managed more deals than others? 1%
            while ans[0] == ans[1]:
                ans = self.shuffle_answers(self.most_active_advisor(), self.random_tx().second)
            link = "http://inspiregroup.ro/wp-content/uploads/2015/08/success-1.jpg"
            question_text = "Which advisor managed more deals than others?"
        elif question_type < 30:  # who is the financial advisor of <actor>? 28%
            tx = self.random_tx()
            while ans[0] == ans[1]:
                ans = self.shuffle_answers(tx.second, self.random_tx().client)
            link = self.actors.get(tx.client, "http://assets.howtobecome.com/assets/images/2014/03/Financial-Advisor.jpg")
            question_text = "Who is the financial advisor of {}?".format(tx.client)
        elif question_type < 50:  # how much money did <actor> withdraw? 20%
            tx = self.random_tx()
            while ans[0] == ans[1]:
                real_amount = self.int_to_amount(self.withdrawn_money(tx.client))
                ans = self.shuffle_answers(real_amount, self.random_tx().amount)
            link = self.actors.get(tx.client, "http://assets.howtobecome.com/assets/images/2014/03/Financial-Advisor.jpg")
            question_text = "How much money did {} withdraw?".format(tx.client)
        elif question_type < 60:  # custom question with two custom answers 10%
            question = self.random_custom1_question()
            question_text = question[0]
            link = question[1]
            ans = self.shuffle_answers(question[2], question[3])
        elif question_type < 75:  # how much money did <actor> invest? 15%
            tx = self.random_tx()
            while ans[0] == ans[1]:
                real_amount = self.int_to_amount(self.invested_money(tx.client))
                ans = self.shuffle_answers(real_amount, self.random_tx().amount)
            link = self.actors.get(tx.client, "http://assets.howtobecome.com/assets/images/2014/03/Financial-Advisor.jpg")
            question_text = "How much money did {} invest?".format(tx.client)
        elif question_type < 90:  # custom questions where the answer is a name 15%
            question_text, correct_ans, link = self.random_custom_question()
            while ans[0] == ans[1]:
                ans = self.shuffle_answers(correct_ans, self.random_actor())
        else:  # how many times does <actor> appear in out transactions data? 10%
            actor_name = self.random_actor()
            while ans[0] == ans[1]:
                print('actor: {}, times: {}'.format(actor_name, self.number_of_entries_client(actor_name)))
                ans = self.shuffle_answers(self.number_of_entries_client(actor_name), random.randrange(0, 10))
            print(ans)
            ans = '{} times'.format(ans[0]), '{} times'.format(ans[1]), ans[2]
            link = self.actors[actor_name]
            question_text = "How many times does {} appear in our transactions data as investor?".format(actor_name)
        return link, question_text, ans[0], ans[1], ans[2]
