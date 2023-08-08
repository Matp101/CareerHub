'''
main.py
'''
from website import create_app

app = create_app() # Creates the app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)