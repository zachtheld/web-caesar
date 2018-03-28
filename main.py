from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <lable>
                Rotate by: 
                <input type="text" name="rot" value="0"/>
            </lable> 
            <textarea type="text" name="text" value='[0]'>{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
'''

@app.route("/", methods=['POST'])
def encrypt():
    message = request.form["text"]
    rotation = request.form["rot"]
    encrypt_message = rotate_string(message,int(rotation))
    return form.format(encrypt_message)

@app.route("/")
def index():
    return form.format("")


app.run()
