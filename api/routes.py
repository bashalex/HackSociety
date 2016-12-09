from api.handlers import *

routes = [
    (r"/", MainHandler),
    (r"/leaderboard", LeaderBoardHandler),
    (r"/auth", AuthHandler)
]
