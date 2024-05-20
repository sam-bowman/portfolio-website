from flask import Flask, url_for
import pyvibe as pv
from pf_components import global_components

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page(
        title='Home - SB',
        description="Homepage",
        navbar=global_components.get_navbar("Homepage"),
        footer=None,
        sidebar=global_components.get_sidebar()
    )
    page.add_header("You're here too early! This page will be updated soon(tm)")
    return page.to_html()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)