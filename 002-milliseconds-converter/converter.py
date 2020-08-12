  
from flask import Flask, request, render_template

app = Flask(__name__)

def convert(millis):
     seconds=(millis/1000)%60
     minutes=(millis/(1000*60))%60
     hours=(millis/(1000*60*60))%24
     return seconds, minutes, hours



@app.route('/', methods = ['GET'])

def main_get():
    return render_template('index.html', developer_name = 'Tulay', not_valid = False)


    
@app.route('/', methods = ['POST'])
def main_post():
    alpha = request.form ["number"]
    if not alpha.isdecimal():
        return render_template('index.html', developer_name = 'Tulay', not_valid = True)
    
    number = int(alpha)
    if (0 > number):
        return render_template('index.html', developer_name = 'Tulay', not_valid=True)
    return render_template ('result.html', milliseconds=number, result=convert(number), developer_name = 'Tulay')



if __name__ == '__main__':
     #app.run(host = '127.0.0.1', port=80, debug = True)

     app.run(host = '0.0.0.0', port=80, debug = True)