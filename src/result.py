class Result:

    system = "42-Crew"

    def __init__(self, query_id, iteration, doc_number, rank, score):
        self.query_id = query_id
        self.iteration = iteration
        self.doc_number = doc_number
        self.rank = rank
        self.score = score

