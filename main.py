from flask import Flask, request, escape, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/<name>', methods=['POST', 'GET'])
def say_hello(name='World'):
  color = "%06x" % random.randint(0, 0xFFFFFF)
  style = "style=\"background-color:#" + str(color) + "\""
  html = "<h1 " + style + ">Hello " + name + "!!!</h1>"
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, use_reloader=True,
	  debug=True, threaded=True)
