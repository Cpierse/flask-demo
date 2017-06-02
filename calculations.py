import requests
import pandas as pd

from bokeh.embed import components
from bokeh.plotting import figure, show
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

from flask import render_template

#%% Constants:
api_key = '42pwVGC7x4TYPy1pCa4N'
columns = ['ticker','date','opening','high','low','closing','volume',
           'ex-dividend','split_ratio','adj_opening','adj_high',
           'adj_low','adj_closing','adj_volume']
colors = ['red','blue','green','blueviolet','gold','darkolivegreen',
          'darkseagreen','deeppink']

#%% User input - comment when using script:
#ticker = 'GOOG'
#params = ['opening','high','low','closing','adj_opening','adj_high',
#           'adj_low','adj_closing']
days = 31
#%% Generated from input:
# Acquire data:
def plot_data(ticker,params,show_plot=False):
    url = 'https://www.quandl.com/api/v3/datatables/' + \
        'WIKI/PRICES.json?ticker={0}&api_key={1}'.format(ticker,api_key)
    r = requests.get(url)
    
    data = pd.DataFrame(r.json()['datatable']['data'])
    if sum(data.shape)==0: 
        return None
    data.columns = columns
    data['date']=pd.to_datetime(data['date'])
    
    fig = figure(title=ticker + ' ticker data', x_axis_type='datetime')
    for idx,param in enumerate(params):
        fig.line(data['date'][-days:-1],data[param][-days:-1],color=colors[idx],legend=ticker+': '+param.replace('adj_','adjusted '), line_width=2)
    fig.xaxis.axis_label = 'Date'
    fig.yaxis.axis_label = 'Cost'
    if show_plot: show(fig)
    return fig

def make_bokeh_div(ticker,params):
    # Get the figure object:
    fig = plot_data(ticker,params)
    if fig ==None:
        return render_template('error.html')
    # Get the necessary resources:
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    # Get the script to create the figure and associated div:
    script, div = components(fig)
    # Create html:
    html = render_template(
        'embed.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        color='Blue',
        _from=0,
        to=10)
    return encode_utf8(html)
