# -*- coding: UTF-8 -*-
import re, json, requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/homepage')
def homepage():
    return app.send_static_file('homepage.html')


@app.route('/add', methods=['POST'])
def add():
    url = request.form.get('url')
    if re.match(r'^http?:/{2}\w.+$', url):
        r = requests.get(url)
        slotList = re.findall(r'你的君主编号:(.*?)&nbsp;&nbsp;', r.text)
        if len(slotList) > 0:
            stayurl = {int(slotList[0]): url}
            with open('data.json') as f:
                data = json.load(f)
            data.update(stayurl)
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return app.send_static_file('success.html')
        return app.send_static_file('incorrect.html')
    else:
        return app.send_static_file('incorrect.html')


@app.route('/add_Multi')
def add_Multi():
    return app.send_static_file('add_Multi.html')


@app.route('/add_Multi_Post', methods=['POST'])
def add_Multi_Post():
    sucess = 0
    url = request.form.get('url')
    urls = url.splitlines()
    for values in urls:
        if re.match(r'^http?:/{2}\w.+$', values):
            r = requests.get(values)
            slotList = re.findall(r'你的君主编号:(.*?)&nbsp;&nbsp;', r.text)
            if len(slotList) > 0:
                stayurl = {int(slotList[0]): values}
                with open('data.json') as f:
                    data = json.load(f)
                data.update(stayurl)
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                sucess = sucess+1
    return '成功数量 '+str(sucess)


if __name__ == '__main__':
    app.run()
