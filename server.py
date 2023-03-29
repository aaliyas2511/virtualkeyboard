#Import necessary libraries
from flask import Flask, render_template
#Initialize the Flask app
app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template('PBL_review3.html')
    return render_template('style.css')

    
@app.route('/my-link/')
def my_link():
    import virtual_keyboard.py
    virtual_keyboard.py()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
