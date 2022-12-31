#!/usr/bin/python3

import flask

app = flask.Flask(__name__)

@app.route('/')
def main():
    #basic functions of a server
    #are get user text data and
    #to get and send files
    return '''
           <a href="gt_url">get text from client</a><br>
           <a href="gf_url">get file from client</a><br>
           <a href="sf_url">send file to client</a>
           '''





@app.route('/gt_url')
def gt():
    #html for getting text from client
    return '''
           <form action="get_text_url" method="POST">
           <input name="textvar" type="text"/>
           </form>
           '''
@app.route('/get_text_url', methods=["POST"])
def get_text():
    #flask for getting text from client
    note = flask.request.form["textvar"]
    print(note)
    return flask.redirect(flask.url_for('main'))







@app.route('/gf_url')
def gf():
    #html for getting files from client
    return '''
           <form action="get_file_url"
            enctype="multipart/form-data"
            method="post">
               <input name="file" type="file"/>
               <button>send</button>
           </form>
            '''
@app.route('/get_file_url', methods=["POST"])
def get_file():
    #flask for getting files from client
    gfob = flask.request.files["file"]
    name = gfob.filename
    gfob.save('folder/' + name)
    return flask.redirect(flask.url_for('main'))







@app.route('/sf_url')
def sf():
    #url includes path to file
    return '''
           <a href="send_file_url/folder/test_file.txt">
           name</a>
           '''
@app.route('/send_file_url/folder/test_file.txt')
def send_file():
    return flask.send_file('folder/test_file.txt',
                           download_name='test_file.txt')



if __name__ == '__main__':

    app.run(host = '0.0.0.0',
            port = 5050,
            debug = True)


