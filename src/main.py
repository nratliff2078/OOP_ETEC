import asyncio
import tornado.web
import index
import quote

def makeApp():
    endpoints=[
        ("/",index.Handler),
        ("/quote",quote.Handler)
    ]
    app = tornado.web.Application(endpoints)
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()