# -----------------------------------------------------#
# Imports
# -----------------------------------------------------#

import logging
from logging import Formatter, FileHandler
from flask import render_template, request
from flask import session, redirect
from app import app #, db
#from app.models import users, accounts, get_or_create
from app.oauth import authenfication
from app import fakeAgendaService

# -----------------------------------------------------#
# Global Variable
# -----------------------------------------------------#
oauth = None


# -----------------------------------------------------#
# Controllers.
# -----------------------------------------------------#


@app.route('/')
def home():
    if 'user_token' in session:
        return "connected to RDV"
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login', methods=['GET'])
def login():
    type = request.args.get('authtype')
    if type is None:
        type = 'facebook'
    global oauth
    oauth = authenfication(type).Get_OAuth()
    redirect_url = request.host_url + 'login/authorized?authtype=' + type
    return oauth.authorize(callback=redirect_url, _external=True)


@app.route('/login/authorized', methods=['GET'])
def authorized():
    global oauth
    resp = oauth.authorized_response()
    type = request.args['authtype']
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if type == 'google':
        session['user_token'] = (resp['access_token'], '')
        userinfo = oauth.get('userinfo', token=session['user_token']).data
        if userinfo != 'Not Found':
            #userSql = get_or_create(users, name=userinfo["family_name"],
                                    #email=userinfo["email"], surname=userinfo["given_name"])
            #get_or_create(accounts, type='google', oauth_token=resp['access_token'], user=userSql.id)
            return "connected with google"
    elif type == 'facebook':
        session['user_token'] = (resp['access_token'], '')
        userinfo = oauth.get('me?fields=email,first_name,last_name', token=session['user_token']).data
        if 'error' not in userinfo:
            #userSql = get_or_create(users, name=userinfo['last_name'],
                                    #email=userinfo['email'], surname=userinfo['first_name'])
            #get_or_create(accounts, type='facebook', oauth_token=resp['access_token'], user=userSql.id)
            return "connected with facebook"
    return "connection not handled"


@app.route('/logout')
def logout():
    session.clear()
    return redirect(request.host_url)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    base_path = app.config['basedir']
    '''
    error_log = os.path.join(base_path, 'error.log')
    file_handler = FileHandler(error_log)
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')
    '''


@app.route('/findDates', methods=['GET'])
def findDates():
    friendIds = request.args['ids'];
    dates = fakeAgendaService.getDates(friendIds);
    print(dates)
    return render_template('pages/placeholder.results.html', dates=dates)





