import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get_score(self):
        return self.get_secure_cookie("score")

    def set_answer(self, is_left):
        self.set_secure_cookie("right_answer", 'left' if is_left else 'right')

    def get_answer(self):
        return self.get_secure_cookie("right_answer")

    def increment_score(self):
        score = self.get_score()
        if score is None:
            score = 0
        self.set_secure_cookie("score", str(int(score) + 1))

    def set_score_to_zero(self):
        self.set_secure_cookie("score", '0')

    def save_result(self):
        self.set_secure_cookie("result", self.get_score())
        self.set_score_to_zero()

    def get_result(self):
        return self.get_secure_cookie("result")


class MainHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.set_answer(True)
        self.render("index.html", question="How much money did Brad Pitt invest in \"LifePath Active 2020 Fund\"?",
                    answer1='More than $5M', answer2='Less than $5M',
                    image='/static/img/brad_pitt.jpg')

    def post(self):
        answer = self.get_argument('answer')
        if self.get_answer().decode('ascii') == answer:
            self.increment_score()
            self.write('correct')
        else:
            self.save_result()
            self.write('wrong')


class LeaderBoardHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        with open('data/users.txt', 'r') as f:
            lines = f.readlines()
        scores = [(line.rsplit(maxsplit=1)[0], int(line.rsplit(maxsplit=1)[1])) for line in lines]
        if len(scores) == 1:
            top = [(scores[0][0], scores[0][1]), ('Unknown', 0), ('Unknown', 0)]
        elif len(scores) == 2:
            top = sorted(scores, key=lambda x: x[1], reverse=True)[:2]
            top.append(('Unknown', 0))
        else:
            top = sorted(scores, key=lambda x: x[1], reverse=True)[:3]
        self.render("leaderboard.html", top1=top[0][0], score1=top[0][1],
                                        top2=top[1][0], score2=top[1][1],
                                        top3=top[2][0], score3=top[2][1])

    def post(self):
        action = self.get_argument('action')


class AuthHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render("auth.html", score=int(self.get_result()))

    def post(self):
        username = self.get_argument('username')
        score = int(self.get_argument('score').replace('You\'ve got ', '').replace(' points!', ''))
        with open('data/users.txt', 'a') as f:
            f.write('{} {}\n'.format(username, score))
            print(username, score)
        self.set_current_user(username)
        self.redirect(self.get_argument("next", u"/"))

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", user)
        else:
            self.clear_cookie("user")
