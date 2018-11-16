import web

urls = ("/", "index")

class index(object):
    def GET(self):
        return "HAHA"

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run("10.234.130.27:8888")

