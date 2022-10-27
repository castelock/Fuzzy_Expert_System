class Experiment:
        def __init__(self, id, precision, f1_score,recall):
            self.id = id
            self.precision = precision
            self.f1_score = f1_score
            self.recall = recall

        def __repr__(self):
            return repr((self.id, self.precision, self.f1_score, self.recall))    