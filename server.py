#!/usr/bin/python3

import flask
import helpers
bomb = helpers.bomb

app = flask.Flask(__name__)

@app.route('/', defaults = {"_route": "index.html"})
@app.route('/noscript', defaults = {"_route": "noscript.html"})
def main(_route):

    bomb.files, bomb.notes = helpers.list_assets()
    return flask.render_template(_route, bomb = bomb)


@app.route('/add-note', methods=["POST"])
def addnote():

    note = flask.request.form["note"]
    helpers.add_note(note)

    helpers.update_tree()

    return flask.redirect(flask.url_for('main'))


@app.route('/remove-note/<hsh>')
def removenote(hsh):

    helpers.remove_note(hsh)

    helpers.update_tree()

    return flask.redirect(flask.url_for('main'))


@app.route('/add-file', methods = ["POST"])
def addfile():

    rfob = flask.request.files["file"]
    name = rfob.filename

    helpers.add_file(rfob, name)

    helpers.update_tree()

    return flask.redirect(flask.url_for('main'))


@app.route('/remove-file/<hsh>/<name>')
def removefile(hsh, name):

    helpers.remove_file(hsh, name)

    helpers.update_tree()

    return flask.redirect(flask.url_for('main'))


@app.route('/deliver-file/<hsh>/<name>')
def deliverfile(hsh, name):

    path = helpers.deliver_path(hsh, name)

    #newer python version changed ::
    #return flask.send_file(path, attachment_filename="a")
    #return flask.send_file(path, download_name="a")
    return flask.send_file(path, download_name=name)


@app.route('/add-desc/<hsh>/<name>', methods=['POST'])
def adddesc(hsh, name):

    desc = flask.request.form['desc']
    helpers.add_desc(hsh, name, desc)

    return flask.redirect(flask.url_for('main'))


if not helpers.pa:
    app.run(host = '0.0.0.0', port = 5000, debug = True)
