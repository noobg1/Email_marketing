from source import app
import logging

if __name__ == '__main__':
    # logging.basicConfig(filename='example.log',level=logging.DEBUG)
    app.run(host="0.0.0.0", port=5000, debug=True)
