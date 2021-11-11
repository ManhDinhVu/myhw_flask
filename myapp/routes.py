from myapp import myapp_obj
from flask import flash,render_template, redirect
from myapp import db
from myapp.models import City
from myapp.forms import TopCities

@myapp_obj.route("/home", methods=['GET', 'POST'])
def home():
	title='Top Cities'
	myname = 'Dinh'
	model = City.query.all()
	form = TopCities()

	if form.validate_on_submit():
		flash(f'Form Submitted for {form.city_name.data}!')
		name = form.city_name.data
		rank = form.city_rank.data
		city = City(name,rank)
		db.session.add(city)
		db.session.commit()
		return redirect('/home')

	return render_template("home.html",title=title,XX = myname,top_city=form,name_city=model)
