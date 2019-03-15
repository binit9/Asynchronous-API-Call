from flask import Flask, jsonify, request
import wcpt_tag_extraction as tag_extraction
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://localhost//',
app.config['CELERY_RESULT_BACKEND']='amqp://localhost//'

celery = make_celery(app)

@celery.task(name='mytasks.tag_extraction_celery')
def tag_extraction_celery(req_json):
    print("Inside celery")
    return tag_extraction.extract_tag(req_json)

@app.route("/receipt", methods = ['POST'])
def tag_extraction_service():
    req_json = request.get_json()
    task = tag_extraction_celery.delay(req_json)
    id = task.id
    tr_id = req_json['transaction_id']
    tr_path = ''.join(['/home/ubuntu/policy/AI-Policy/tasks/',tr_id,'.txt'])
    f = open(tr_path,'w')
    f.write(id)
    f.close()
    return jsonify({"message": "Your task is running. To check status use transaction id.", "transaction_id": tr_id})

@app.route("/status", methods = ['POST'])
def status_result():
    status_json = request.get_json()
    transaction_id = status_json['transaction_id']
    tr_path = ''.join(['/home/ubuntu/policy/AI-Policy/tasks/',transaction_id,'.txt'])
    print("Searching for status...")
    f = open(tr_path,'r')
    id = f.read()
    result = celery.AsyncResult(id)
    return jsonify({"task_status": result.state, "result": result.get(),"transaction_id":transaction_id})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)



