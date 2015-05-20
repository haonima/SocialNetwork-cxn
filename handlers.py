import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.web


class indexHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('name')
    
    @tornado.web.authenticated
    def get(self):
        #self.clear_cookie(name='uname')
        if not self.get_secure_cookie('name') :
            self.redirect('register')         
        else:
            self.render(r'index.html',name = self.current_user)
    
class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write('this is upload page')        
        self.render('upload.html')
        
    def post(self):
        import time
        fname = time.time()
        
        f = self.request.files['imgfile'][0]['body']
        print self.request.files['imgfile']
        with open(r'img/%f.jpg'%fname,'wb') as up:
            up.write(f)
            
        up = open(r'img/%f.jpg'%fname,'wb')
        up.write(f)
        up.close()
    
class loginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
        #self.write('login')        
                
    def post(self):
        name = self.get_argument('username')
        passwd = self.get_argument('passwd')
        
        if name and passwd :
            self.set_secure_cookie(name = 'name', value =name , expires_days=3)
            self.redirect(r'/')
        else:
            self.redirect(r'/login')
    
class registerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r'register.html')        
    def post(self):
        name = self.get_argument('username')        
        passwd1 = self.get_argument('password1')        
        passwd2 = self.get_argument('password2')
        if not self.check(name, passwd1, passwd2):
            #self.redirect('error')
            self.write_error(404)
        else:
            self.set_secure_cookie('uname',name,3) 
            self.redirect(r'/')        
    def check(self,name, passwd1, passwd2):
        if passwd1 == passwd2 :
            return True
        return False
        
    def write_error(self, status_code):
        self.redirect('error')
    
class errorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('error')        
        
        
class newHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('new page')