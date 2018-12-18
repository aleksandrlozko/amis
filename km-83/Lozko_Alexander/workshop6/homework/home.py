import re
import plotly
import plotly.graph_objs as go
from plotly import tools
def getName(app):
    result = re.split(r'"\w+', app, maxsplit=1)
list_of_category = []
list_of_app = []
list_of_count = []
list_of_rating = []
list_of_size = []
with open('data/googleplaydata.csv', encoding = 'utf-8') as f:
    header = f.readline()
    dataset = dict()
    for line in f:
        columns = line.strip().replace('"','').split(",")
        app = columns[0]
        category = columns[1]
        rating = columns[2]
        size = columns[4]
        list_of_category.append(category)
        list_of_count.append(list_of_category.count(category))
        list_of_rating.append(rating)
        list_of_app.append(app)
        list_of_size.append(size)
        if category not in dataset:
            dataset[category] = dict()
        if app not in dataset[category]:
            dataset[category][app] = dict()
        if size not in dataset[category][app]:
            dataset[category][app]['size'] = size
        if rating not in dataset[category][app]:
            dataset[category][app]['rating'] = rating

    bar_of_count = go.Bar(
        x = list_of_category,
        y = list_of_count,
        name = 'Category and their count'
    )
    bar_of_rating = go.Bar(
        x = list_of_category,
        y = list_of_rating,
        name = 'Category and their rating'
    )
    '''pie = go.Pie(
       labels = list_of_app,
        values = list_of_size,
        name = 'App and their size '
    )'''


    fig = tools.make_subplots(rows=3, cols=3)

    fig.append_trace(bar_of_count,1,1)
    fig.append_trace(bar_of_rating,1,2)
    '''fig.append_trace(pie,1,3)'''

    plotly.offline.plot(fig, filename='plotly.html')