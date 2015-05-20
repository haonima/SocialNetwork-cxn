import os
import tornado.web
import tornado.ioloop

from handlers import *

def main():
    handlers = [
        (r'/',indexHandler),
        (r'/login',loginHandler),
        (r'/register',registerHandler),
        (r'/upload',uploadHandler),
        (r'/error',errorHandler),
        (r'/success',succHandler)
    ]
    
    settings = {
        r'static_path':os.path.join(os.path.dirname(__file__),'static'),
        r'template_path':os.path.join(os.path.dirname(__file__),'templates'),
        #############################################################
        #the code to generate cookie_secret:
        #import base64, uuid
        #base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        #############################################################
        r"cookie_secret":"SEzK+fStSMOyneFM9T4UqHmZwCrnkU+QvOS17ErWayQ=",
        r'login_url':'login'
    }
    
    app = tornado.web.Application(handlers,**settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    main()

