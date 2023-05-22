from waitress import serve

from flaskr import create_app

serve(create_app(), host='localhost', port=5000)