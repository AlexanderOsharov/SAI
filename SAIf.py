from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)


@app.route('/get_answer', methods=['POST'])
def get_answer():
    content = request.json
    input_str = content['input_str']
    model_ = content.get('model_', 'gpt-3.5-turbo')

    response = g4f.ChatCompletion.create(
        model=model_,
        messages=[{"role": "user", "content": input_str}],
        stream=False,
    )

    result = "".join([message['content'] for message in response])

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
