from bingo.wsgi import db

class RuleT(db.Model):
    __tablename__ = 'rules'

    id = db.Column(db.Integer, db.Sequence('rules_id_seq'), primary_key=True)
    value = db.Column(db.Text)
    name = db.Column(db.String(30))
    active = db.Column(db.Boolean)

    def __init__(self, name, value, active=False):
        self.name = name
        self.value = value
        self.active = active

    def __repr__(self):
        return '<rule {0}>'.format(self.name)
