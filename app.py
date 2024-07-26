from flask import Flask, render_template


app = Flask(__name__)

ATHLETES =[
    {
        'id': 1,
        'first_name': "Shantay",
        'last_name': "Augustine",
        'birthdate': '30/11/2006',
        'gender':'Female'
    },
    {
        'id': 2,
        'first_name': "Ethan",
        'last_name': "Sam",
        'birthdate': '11/01/2007',
        'gender': 'Male'
    },
    {
        'id': 3,
        'first_name': "Devonni",
        'last_name': "Ferguson",
        'birthdate': '17/10/2005',
        'gender': 'Male'
    },
    {
        'id': 4,
        'first_name': "Rhea",
        'last_name': "Flanders",
        'birthdate': '21/08/2004',
        'gender': 'Female'
    }    
]

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/athletes')
def athletes_page():
    return render_template('athletes.html', athletes=ATHLETES)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
  