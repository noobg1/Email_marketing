from source import app
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    app.run(debug=True)
