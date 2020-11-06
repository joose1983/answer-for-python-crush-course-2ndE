from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
submission_links, comments, labels = [], [], []

for submission_id in submission_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    if not response_dict.__contains__('descendants'):
        continue
    
    comment = response_dict['descendants']
    comments.append(comment)

    title = response_dict['title']
    submission_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    submission_link = f"<a href='{submission_url}'>{title}</a>"
    submission_links.append(submission_link)
    label = f"{title}<br />{submission_link}"
    labels.append(label)


# Make visualization.
data = [{
    'type':'bar',
    'x': submission_links,
    'y': comments,
    'hovertext':labels,
    'marker': {
        'color':'rgb(60, 100, 150)',
        'line': {'width':1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]
my_layout = {
    'title':'Top stories on Hacker-news',
    'titlefont': {'size':28},
    'xaxis': {'title': 'Titles',
              'titlefont':{'size':24},
              'tickfont':{'size':14},
    },
    'yaxis': {'title': 'Submission comments',
              'titlefont': {'size':24},
              'tickfont': {'size':14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_hacker_news.html')
                          

