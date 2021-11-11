from myapp import db


class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(30), unique=True, nullable=False)
	city_rank = db.Column(db.Integer, unique=True, nullable=False)
	is_visited = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, city_name,city_rank):
		self.city_name = city_name
		self.city_rank = city_rank

	def __repr__(self):
		return f"{self.city_name}"
