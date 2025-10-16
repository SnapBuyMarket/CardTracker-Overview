import os
from flask import Flask, jsonify, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))
TPL_DIR = os.path.join(ROOT, 'web', 'templates')
STATIC_DIR = os.path.join(ROOT, 'web', 'static')

app = Flask(__name__, template_folder=TPL_DIR, static_folder=STATIC_DIR)

@app.get('/health')
def health():
    return jsonify(ok=True, app='CardTracker-Overview')

@app.get('/dash')
def dash():
    rows = [
        {'player':'Kobe Bryant','set':'Topps Chrome','year':1996,'number':'138','sport':'Basketball','market_value':120.0,'roi_pct':55},
        {'player':'Michael Jordan','set':'Fleer','year':1987,'number':'59','sport':'Basketball','market_value':95.0,'roi_pct':48},
        {'player':'Shohei Ohtani','set':'Topps Chrome','year':2018,'number':'HMT1','sport':'Baseball','market_value':80.0,'roi_pct':42},
    ]
    tpl = os.path.join(TPL_DIR, 'collx_ultimate.html')
    if os.path.exists(tpl):
        return render_template('collx_ultimate.html', rows=rows)
    return '<h1>CardTracker — Overview</h1><p>Demo running.</p>'

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.getenv("PORT","5099")))
