import requests
import os

your_token = os.environ['TODOIST_KEY']
tasks = 'https://beta.todoist.com/API/v8/tasks'
project = input('Project: ')

m5 = requests.get(
    tasks,
    params={
        "filter": 'today & @m5 & ##%s' % project
    }, 
    headers={"Authorization": "Bearer %s" % your_token
    }).json()

m15 = requests.get(
    tasks,
    params={
        "filter": 'today & @m15 & ##%s' % project
    }, 
    headers={"Authorization": "Bearer %s" % your_token
    }).json()

m30 = requests.get(
    tasks,
    params={
        "filter": 'today & @m30 & ##%s' % project
    }, 
    headers={"Authorization": "Bearer %s" % your_token
    }).json()

m45 = requests.get(
    tasks,
    params={
        "filter": 'today & @m45 & ##%s' % project
    }, 
    headers={"Authorization": "Bearer %s" % your_token
    }).json()


def sum(i5, i15, i30, i45):
    s5 = len(m5) * 5
    s15 = len(m15) * 15
    s30 = len(i30) * 30
    s45 = len(i45) * 45
    total_seconds = (s5 + s15 + s30 + s45)*60

    hours = total_seconds // 3600
    minutes = total_seconds // 60 - hours * 60

    my_len = "%d:%02d" % (hours, minutes)
    return my_len


print(sum(m5,m15,m30,m45))