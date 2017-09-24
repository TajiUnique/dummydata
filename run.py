__author__ = 'joe'

from app import createapp

app = createapp()

if __name__ == "__main__":
    app.run(debug=True)
