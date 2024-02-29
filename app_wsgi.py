from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Default.aspx')

@app.route('/About')
def about():
    return render_template('AboutUs.aspx')

@app.route('/Contact')
def contact():
    return render_template('Contact.aspx')

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
