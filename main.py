import web

from handle import Handle
url = ('/wx','Handle')
app = web.application(url,globals())

if __name__ == "__main__":
    app.run()
