from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def beranda():
    return render_template('index.html')


@app.route('/fitur')
def fitur():
    return render_template('fitur.html')


@app.route('/hubungi-kami')
def hubungi():
    return render_template('hubungi_kami.html')


@app.route('/dagingSapi/sopSapi')
def sopSapi():
    return render_template('dagingSapi/sopSapi.html')


@app.route('/dagingSapi/semurSapi')
def semurSapi():
    return render_template('dagingSapi/semurSapi.html')


@app.route('/dagingSapi/rendangSapi')
def rendangSapi():
    return render_template('dagingSapi/rendangSapi.html')


@app.route('/dagingAyam/sopAyam')
def sopAyam():
    return render_template('dagingAyam/sopAyam.html')


@app.route('/dagingAyam/oporAyam')
def oporAyam():
    return render_template('dagingAyam/oporAyam.html')


@app.route('/dagingAyam/ayamBBQ')
def ayamBBQ():
    return render_template('dagingAyam/ayamBBQ.html')


@app.route('/dagingKambing/tongsengKambing')
def tongsengKambing():
    return render_template('dagingKambing/tongsengKambing.html')


@app.route('/dagingKambing/kambingKecap')
def kambingKecap():
    return render_template('dagingKambing/kambingKecap.html')


@app.route('/dagingKambing/osengKambing')
def osengKambing():
    return render_template('dagingKambing/osengKambing.html')
