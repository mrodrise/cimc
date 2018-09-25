from server import app
from flask import render_template, request, flash, Flask, session, redirect, url_for
from forms import loginForm, yourHomeForm
from weather import actualWeather
from wtforms.validators import Required
from fireprobability import fireProbability

import mysql.connector
from flask import jsonify
from listvalues import yourhome_list, yourhome_list_order
from configbbdd import config
from userdata import userData
from maproute import mapRoute
from analysislanguage import analysisLanguage
from userfireload import userFireLoad
from fireload import fireLoad
from report import get_alluserdata, get_alluserfireload, get_housesecure
from home_risk import homeRisk


app.secret_key = 'development key'



@app.route('/testdb')
def testdb():

    connect = mysql.connector.connect(**config)
    cur = connect.cursor()
    cur.execute("SHOW DATABASES")

    for row in cur:
        print(row[0])

    connect.close()

    state = {"status": "Connection to Database OK"}
    return jsonify(state)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/index')
@app.route('/')
@app.route('/', methods=['POST'])
def index():
    form = loginForm()


    if request.method == 'POST':

        if form.validate() == False:
            flash('All fields are required.')
            return render_template('index.html', form=form)

        else:
            _username = form.email.data
            _password = form.password.data

            try:
                con = mysql.connector.connect(**config)
                cursor = con.cursor()

                if form.login.data:

                    cursor.callproc('sp_validateLogin', (_username,))

                    for result in cursor.stored_results():
                        data = result.fetchall()

                    if len(data) > 0:
                        if (str(data[0][2])==_password):
                            print("data y password son iguales")
                            session['email'] = _username
                            session['password'] = _password
                            return render_template('index.html', success=True, form=form, email=session['email'])
                        else:
                            flash('The password is incorrect.')
                            return render_template('index.html', form=form)
                    else:
                        flash('The user does not exist.')
                        return render_template('index.html', form=form)
                else:
                    cursor.callproc('sp_createUser', (_username, _password))

                    for result in cursor.stored_results():
                        data = result.fetchall()

                    if len(data[0][0]) is 0:
                        con.commit()
                        session['email'] = _username
                        session['password'] = _password
                        return render_template('index.html', success=True, form=form, email=session['email'])
                    else:
                        flash('El ususario ya existe.')
                        return render_template('index.html', form=form)

            except Exception as e:
                    flash('Ha habido un error.')
            finally:
                cursor.close()
                con.close()


    elif request.method == 'GET':
        if ('email' in session) and (session['email'] is not None):
            return render_template('index.html', success=True, form=form, email=session['email'])
        else:
            return render_template('index.html', form=form)

@app.route('/yourhome', methods=['GET', 'POST'])
def yourhome():
    form=yourHomeForm()

    if ('email' not in session) or (session['email'] is None):
        return redirect(url_for('index'))

    else:
        user_data = userData(session['email'])

        if request.method == 'POST':
            address = request.form.get('address')
            city = request.form.get('city')
            postal_code = request.form.get('postal_code')
            your_home_list_values = []
            your_home_list_values.append(request.form.get('house_orientation'))
            your_home_list_values.append(request.form.get('type_of_house'))
            your_home_list_values.append(request.form.get('topography'))
            your_home_list_values.append(request.form.get('drought'))
            your_home_list_values.append(request.form.get('access_way'))
            your_home_list_values.append(request.form.get('high_tension_towers'))
            your_home_list_values.append(request.form.get('next_the_house'))
            your_home_list_values.append(request.form.get('fence'))
            your_home_list_values.append(request.form.get('water'))
            your_home_list_values.append(request.form.get('outer_walls'))
            your_home_list_values.append(request.form.get('accumulation_of_leaves'))
            your_home_list_values.append(request.form.get('roof'))
            your_home_list_values.append(request.form.get('barbecue'))
            your_home_list_values.append(request.form.get('waterproof'))
            your_home_list_values.append(request.form.get('water_source'))
            print("yourhome - Imprimo la lista de valores antes de invocar a Watson para ver el riesgo")
            print(your_home_list_values)

#           La lavadora
#            list_values = []
#            n = 0
#            i = 0
#            for value in your_home_list_values:
#                if i > 3:
#                    list_values.append(yourhome_list[yourhome_list_order[n]][int(value)][1])
#                    n = n+1
#                i = i+1

#            print("yourhome - Imprimo la lista de valores antes de invocar a Watson para ver el riesgo")
#            print(list_values)
            risk = homeRisk(your_home_list_values)

            home_risk = risk.get_risk()
            print("yourhome - Imprimo el riesgo calculado")
            print(home_risk)

            if  (user_data.get_userdata() == None):
                print("No encuentra al usuario, por lo que inserta")
                user_data.insert_userdata(address, city, postal_code, your_home_list_values, home_risk)
                print("Se supone que ha insertado")
            else:
                print("Estoy updateando")
                user_data.update_userdata(address, city, postal_code, your_home_list_values, home_risk)
            return redirect(url_for('index'))

        elif request.method == 'GET':
            yourhome_list_values = user_data.get_userdata()
            if  yourhome_list_values == None:
                yourhome_list_values = ["","","","","","","","","","","","","","","","","","","",""]
                return render_template('yourhome.html', form=form, yourhome_list=yourhome_list,
                        yourhome_list_values=yourhome_list_values)
            else:
                print(yourhome_list_values)
                return render_template('yourhome.html', form=form, yourhome_list=yourhome_list,
                        yourhome_list_values=yourhome_list_values)


@app.route('/homerecommendations')
def homerecommendations():
    if ('email' not in session) or (session['email'] is None):
        return redirect(url_for('index'))
    else:
        user_data = userData(session['email'])
        stored_values = user_data.get_userdata()
        risk = stored_values[19]
#        list_values = []
#        n = 0
#        i = 0
#        for value in stored_values:
#            if i > 3:
#                print(i)
#                print(yourhome_list[yourhome_list_order[n]][int(value)][1])
#                list_values.append(yourhome_list[yourhome_list_order[n]][int(value)][1])
#                n = n+1
#            i = i+1
#
#        print(list_values)
#
#        home_risk = homeRisk(list_values)
#        risk = home_risk.get_risk()
        return render_template('homerecommendations.html', risk=risk)

@app.route('/riskasessment', methods=['GET', 'POST'])
def riskasessment():

    if ('email' not in session) or (session['email'] is None):
        return redirect(url_for('index'))

    else:
        user_fireload = userFireLoad(session['email'])

        if request.method == 'POST':
            user_fireload_values = []
            user_fireload_values.append(request.form.get('activity'))
            user_fireload_values.append(request.form.get('area'))
            user_fireload_values.append(request.form.get('wood'))
            user_fireload_values.append(request.form.get('paperboard'))
            user_fireload_values.append(request.form.get('cereals'))
            user_fireload_values.append(request.form.get('alcohol'))
            user_fireload_values.append(request.form.get('olive'))
            user_fireload_values.append(request.form.get('propane'))

            fire_load = fireLoad(user_fireload_values)
            user_fireload_values.append(fire_load.get_fire_load())

            print("riskasessment - Contenido de user_fireload_values")
            print (user_fireload_values)

            if  (user_fireload.get_userfireload() == None):
                print("riskasessment - No encuentra al usuario, por lo que inserta")
                user_fireload.insert_userfireload(user_fireload_values)
                print("riskasessment - Se supone que ha insertado")
            else:
                print("riskasessment - Estoy updateando")
                user_fireload.update_userfireload(user_fireload_values)
            return render_template('riskasessment.html', user_fireload_values=user_fireload_values)

        elif request.method == 'GET':
            user_fireload_values = user_fireload.get_userfireload()
            if  user_fireload == None:
                user_fireload_values = ["","","","","","","","",""]
            print(user_fireload_values)
            return render_template('riskasessment.html', user_fireload_values=user_fireload_values)

@app.route('/evacuationrecommendation')
def evacuationrecommendation():
    # Trip duration from the escape point to the meeting point
    origin = "Carrer Margarit, 3, Sant Cugat del Valles, Barcelona"
    destination = "Via Augusta, 251, Barcelona"
    scapemap = mapRoute(origin=origin, destination=destination)
    duration = scapemap.get_duration()

    # Analysys language, takes different text to know if the sentiment is negative or positive
    # in order to use the road or not
    text_people_road = [
        'The escape is occupied, it takes a lot of time to reach the principal road',
        'I can see the fire from the escape road, I think it was not a good idea',
        'It is arriving smoke to the cars, the escape road is a trap',
        'I am in a traffic jam in the escape road, it is getting worse'
    ]

    positive = 0
    negative = 0
    neutral = 0
    text_people_road_sentiment = []
    for i in text_people_road:
        print("sacando el analisis con el target")
        alanguage = analysisLanguage(i, 'escape')
        print("ahora voy a preguntar por el sentimiento")
        sentiment = alanguage.get_sentiment()
        if sentiment == 'positive':
            positive = positive + 1
        elif sentiment == 'negative':
            negative = negative +1
        else:
            neutral = neutral + 1
        print("ahora anexo el sentimiento a la lista")
        text_people_road_sentiment.append(sentiment)

    print (text_people_road_sentiment)

    house_secure = get_housesecure()

    return render_template('evacuationrecommendation.html', duration=duration/60,
                    text_people_road=text_people_road, text_people_road_sentiment=text_people_road_sentiment,
                    positive=positive, negative=negative, neutral=neutral, house_secure=house_secure)

@app.route('/firedetection')
def firedetection():
    if ('email' not in session) or (session['email'] is None):
        return redirect(url_for('index'))
    else:
        user_data = userData(session['email'])
        postal_code = user_data.get_userdata()[3]
        print("Codigo postal " + postal_code)
        weather = actualWeather('ES', postal_code)
        fireprobability = fireProbability(weather)
        value_fireprobability = fireprobability.get_fire_probability()
        print (value_fireprobability)

    return render_template('firedetection.html', weather=weather, fireprobability=fireprobability.get_fire_probability())


@app.route('/cimc')
def cimc():
    return render_template('cimc.html')

@app.route('/cimc_houses')
def cimc_houses():
    all_houses = get_alluserdata()
    return render_template('cimc_houses.html', all_houses=all_houses)

@app.route('/cimc_fireload')
def cimc_fireload():
    all_fireload = get_alluserfireload()
    return render_template('cimc_fireload.html', all_fireload=all_fireload)


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
