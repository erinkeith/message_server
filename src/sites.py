class Sites(object):
    def __init__(self):
        self.list = {}

    def add_site(self, site_id):
        if site_id not in self.list:
            self.list[site_id] = Site()

    def get_site(self, site_id):
        try:
            return self.list[site_id]
        except KeyError as _:
            return None

    def list_sorted_site_ids(self):
        return sorted(self.list)


class Site(object):
    def __init__(self):
        self.online = False
        self.messages = 0
        self.emails = 0
        self.operators = {}
        self.visitors = []

    def add_operator(self, operator_id):
        self.operators[operator_id] = True

    def remove_operator(self, operator_id):
        self.operators[operator_id] = False

    def add_visitor(self, visitor_id):
        if not visitor_id in self.visitors:
            self.visitors.append(visitor_id)

    def num_online_operators(self):
        online_operators = 0
        for operator in self.operators:
            if self.operators[operator]:
                online_operators += 1
        return online_operators

    def num_operators(self):
        return len(self.operators)

    def num_visitors(self):
        return len(self.visitors)