from flask import Flask, request
import redis
 
#twilio_account_sid = 'ACXXXXX'
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)
 
@app.route('/sms', methods=['POST'])
def handle_sms():
    user = request.form['From']
    course = request.form['Body'].strip().upper()
 
    redis_client.sadd(course, user.encode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
