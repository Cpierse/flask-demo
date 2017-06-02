from flask import Flask, render_template, request, redirect

# Imports from my code:
from calculations import  make_bokeh_div

#%% Definitions:


#%% The flask app:
app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',  methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Identify the parameters:
        ticker = request.form['ticker']
        params = dict(request.form)
        params = [x for x in params.keys() if x != 'ticker']
        if len(params)>0 and len(ticker)>0:
            print(ticker)
            print(params)
            return make_bokeh_div(ticker,params)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=33507)
