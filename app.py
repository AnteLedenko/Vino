from flask import Flask , render_template , request, redirect, url_for , jsonify, session

from models import WineList

from data import europe_datastore, african_datastore, asian_datastore, n_american_datastore, s_american_datastore, australia_datastore

app = Flask(__name__)
app.secret_key = 'whatcoulditbe'

my_wish_list = {}
continent_datastores = {
    'europe': europe_datastore,
    'africa': african_datastore,
    'asia': asian_datastore,
    'n_america': n_american_datastore,
    's_america': s_american_datastore,
    'australia': australia_datastore
}

@app.route('/')
def home():
    return render_template('index.html',)

@app.route('/europe')
def europe():
    return render_template('europe.html',euwinelist = europe_datastore, wishlist = my_wish_list)

@app.route('/asia')
def asia():
    return render_template('asia.html', aswinelist = asian_datastore, wishlist = my_wish_list)

@app.route('/africa')
def africa():
    return render_template('africa.html', afwinelist = african_datastore, wishlist = my_wish_list)

@app.route('/n_america')
def n_america():
    return render_template('n_america.html', nawinelist = n_american_datastore, wishlist = my_wish_list)

@app.route('/s_america')
def s_america():
    return render_template('s_america.html', sawinelist = s_american_datastore, wishlist = my_wish_list)

@app.route('/australia')
def australia():
    return render_template('australia.html', auwinelist = australia_datastore, wishlist = my_wish_list)

# the fetch request is posted to this route
@app.route('/add_to_wishlist/<id>', methods=['POST'])
def add_to_wishlist(id):
    wine = None
    # looping through continent datastores to find the wine by id
    for datastore in continent_datastores.values():
        if id in datastore:
            wine = datastore[id]
            break
    # if wine not already in the wishlist it adds it
    if wine and id not in my_wish_list:
        my_wish_list[id] = wine
    # uses jsonify to send back a structured json response
    return jsonify({
        'success': True,
        'wishlist_count': len(my_wish_list)
    })

@app.route('/delete_my_wish_list/<id>', methods = ['POST'])
def delete_my_wish_list(id):
    my_wish_list.pop(id)
    return redirect(url_for('profile'))
    # this route removes item from wishlsit and redirects back to profile html updated

@app.route('/login/', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        #receives username and pw from form in login page 
        username = request.form['username']
        password = request.form['password']
        
        #if provided logs you in 
        if username and password:
            session['logged_in'] = True
            session['username'] = username #username stored here
            return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))
    #this route removes log in and redirects to home page 

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('profile.html',username = username, wishlist = my_wish_list)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
