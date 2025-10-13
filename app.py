from flask import Flask, request, render_template, redirect, url_for
import helpers, os

app = Flask(__name__)

@app.route('/')
def index():
    campaigns = helpers.read_json('campaigns.json')
    return render_template('report.html', campaigns=campaigns)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        campaigns = helpers.read_json('campaigns.json')
        cid = str(len(campaigns) + 1)
        campaigns[cid] = {'name': request.form.get('name', 'Unnamed'), 'template': request.form.get('template', '')}
        helpers.write_json('campaigns.json', campaigns)
        return redirect(url_for('index'))
    return render_template('landing.html')

@app.route('/<campaign_id>')
def landing(campaign_id):
    logs = helpers.read_json('logs.json')
    logs.setdefault(campaign_id, []).append({'ip': request.remote_addr, 'path': request.path})
    helpers.write_json('logs.json', logs)
    return render_template('landing.html', campaign_id=campaign_id)

if __name__ == '__main__':
    # Ensure data directory exists when running from package root
    os.makedirs('data', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)