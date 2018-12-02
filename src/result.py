class Result:

    def __init__(self, query_id, doc_number, rank, score):
        self.query_id = query_id
        self.iteration = "Q0"
        self.doc_number = doc_number
        self.rank = rank
        self.score = score
        self.system = "42-Crew"
