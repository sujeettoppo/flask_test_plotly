from flask import Flask, render_template
import plotly.graph_objs as go
import plotly
import json


app = Flask(__name__)

@app.route('/')
def index():
    # Create a simple Plotly graph
    # x = [1, 2, 3, 4, 5, 6, 7, 8]
    
    x = ['JAN 2022', 'FEB 2022', 'MAR 2022', 'APR 2022', 'MAY 2022', 'JUN 2022', 'JUL 2022', 'AUG 2022']
    
    y = [200, 160, 140, 110, 160, 122, 110, 115]
    
    data = [go.Bar(x=x, y=y)]
    
    layout = go.Layout(
        title='Sales by Month',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Sales(Dollars)')
    )
    
    fig = go.Figure(data=data, layout=layout)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', graphJSON=graphJSON)
    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    # print(graphJSON)
    # return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True, port = 5004)
