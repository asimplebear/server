#!/usr/bin/python3

import flask
from utility import get_file_list

app = flask.Flask(__name__)

@app.route('/')
def main():
    filelist = get_file_list()
    return flask.render_template('index.html',
                                 filelist = filelist)


@app.route('/get_text_url', methods=["POST"])
def get_text():
    #flask for getting text from client
    note = flask.request.form["textvar"]
    print(note)
    return flask.redirect(flask.url_for('main'))


@app.route('/get_file_url', methods=["POST"])
def get_file():
    #flask for getting files from client
    gfob = flask.request.files["file"]
    name = gfob.filename
    gfob.save('assets/' + name)
    return flask.redirect(flask.url_for('main'))


@app.route('/send_file_url/assets/<cargo>')
def send_file(cargo):
    print(cargo)
    return flask.send_file('assets/'+cargo,
                            download_name=cargo)


if __name__ == '__main__':

    app.run(host = '0.0.0.0',
            port = 5050,
            debug = True)


