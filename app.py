from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            filename = stream.download()
            return redirect(url_for('sucess', name=filename))
        except:
            return render_template('index.html', message='Hubo un error al descargar el video.')
    else: 
        return render_template('index.html')


@app.route('/success/<name>')
def success(name):
    return render_template('sucess.html', video_url=name)


if __name__=='__main__':
    app.run(debug=True)


