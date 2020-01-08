from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    Popen(
            ["streamlit", "run", "StreamlitApp/app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"],
            env=dict(os.environ, PYTHONPATH='StreamlitApp/')
