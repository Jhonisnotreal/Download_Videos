from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
	yt = YouTube(request.form['url'])
	stream = yt.streams.get_highest_resolution()
	stream.download
	return render_template('index.html')

if __name__ == '__main__':
		app.run(debug=True)
