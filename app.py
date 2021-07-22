from flask import Flask, request, jsonify, render_template
from model import predict

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def test():

    image_file_names = []

    images = request.files.to_dict() #convert multidict to dict
    for image in images:     #image will be the key 
        file_name = images[image].filename
        image_file_names.append(file_name)
        images[image].save('components/recieved_images/'+file_name)
    response = {'result':'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)