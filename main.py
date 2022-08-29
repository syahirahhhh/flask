from flask import Flask, render_template
import logging

app = Flask(__name__)
logging.basicConfig(filename='records.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def home():
   app.logger.info('Info level log')
   app.logger.warning('Warning level log')
   return render_template('index.html')
   
if __name__ == '__main__':
   app.run()
