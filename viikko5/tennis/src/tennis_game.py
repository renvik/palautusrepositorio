class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
# refactor1: point variable instead of 1 (magic number)
    def won_point(self, player_name):
        point = 1
        if player_name == "player1":
            self.m_score1 = self.m_score1 + point
            print("player1 got a point")
        else:
            self.m_score2 = self.m_score2 + point
            print("player2 got a point")
# refactor 2: split to different methods
    def get_score(self):
        score = ""
        temp_score = 0

        #which player wins a game (erä) -method
        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All" # both players have 0 points
            elif self.m_score1 == 1:
                score = "Fifteen-All" # both have 15 points, wan 1 ball each
            elif self.m_score1 == 2: # both have 30 points, wan 2 balls each
                score = "Thirty-All"
            else:
                score = "Deuce" # both have 40 points, wan **3** balls each
        # case deuce / advantage: in deuce player needs two points in a row after deuce
        # 
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
