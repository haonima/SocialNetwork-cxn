import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.web

from geetest import geetest

import time

class baseHandler(tornado.web.RequestHandler):
    def render_method(self, html, **kwarg):
        if self.get_secure_cookie('name'):
            name = self.current_user
        else:
            name = None
        self.render(html, name = name ,**kwarg)
        
class indexHandler(baseHandler):
    def get_current_user(self):
        return self.get_secure_cookie('name')
    
    @tornado.web.authenticated
    def get(self):
        #self.clear_cookie(name='uname')
        if not self.get_secure_cookie('name') :
            self.redirect('register')         
        else:
            headline = {
                'title':'headline',
                'description':'haonima headline',
                'pic':r'../static/usrimg/a.jpg',
                'author':'haost',
                'time': time.strftime('%Y-%m-%d %H:%M'),
                'visit':'0' 
            }
            toys = [
                {
                    'title':'haonima1',
                    'description':'haonima first article',
                    'pic':r'../static/usrimg/a.jpg',
                    'author':'haost',
                    'time': time.strftime('%Y-%m-%d %H:%M'),
                    'visit':'0'
                },
                {
                    'title':'haonima2',
                    'description':'haonima second article',
                    'pic':r'../static/usrimg/a.jpg',
                    'author':'haost',
                    'time': time.strftime('%Y-%m-%d %H:%M'),
                    'visit':'0'
                },                
            ]
            self.render_method('index.html',title = 'index', toy=toys, headline=headline, )
            #self.render(r'index.html',name = self.current_user)
            
    
class uploadHandler(baseHandler):
    def get(self):
        self.render_method('upload.html',title = 'upload')
        
    def post(self):
        import time
        fname = time.time()
        
        f = self.request.files['imgfile'][0]['body']
        nm = self.get_argument('title')
#        print self.request.files['imgfile']
        with open(r'static/img/%f.jpg'%fname,'wb') as up:
            up.write(f)
            
        self.redirect('success')
        
    
class loginHandler(baseHandler):
    BASE_URL = "api.geetest.com/get.php?gt="
    captcha_id = "ab41ef907b0100ee902ab84d8a9a793e"
    private_key = "af370804764f58962a256f6d71da5be4"
    product = "" 
    def get(self):
        '''
        gt = geetest.geetest(self.captcha_id, self.private_key)
        url = ''
        try:
            challenge = gt.geetest_register()
        except:
            challenge = ''
        if len(challenge)==32:
            url = "http://%s%s&challenge=%s&product=%s" % (self.BASE_URL, self.captcha_id, challenge, self.product)
        ''' 
        #self.render_method('login.html',title = 'login', url = url)
        self.render_method('login.html',title = 'login', url = 'a')
        #self.write('login')        
                
    def post(self):
        name = self.get_argument('username')
        passwd = self.get_argument('passwd')
        '''
        challenge = self.get_argument("geetest_challenge")
        validate = self.get_argument("geetest_validate")
        seccode = self.get_argument("geetest_seccode")
        #print 'challenge:',challenge
        #print 'seccode:',seccode
        #print 'validate:',validate
        gt = geetest.geetest(self.captcha_id, self.private_key)
        ckresult = gt.geetest_validate(challenge, validate, seccode)        
        '''
        
        ##########test###########
        ckresult=1
        
        if name and passwd and ckresult:
            self.set_secure_cookie(name = 'name', value =name , expires_days=3)
            self.redirect(r'/')
        else:
            self.redirect(r'/login')
    
class registerHandler(baseHandler):
    BASE_URL = "api.geetest.com/get.php?gt="
    captcha_id = "ab41ef907b0100ee902ab84d8a9a793e"
    private_key = "af370804764f58962a256f6d71da5be4"
    product = ""        
    
    def get(self):
        gt = geetest.geetest(self.captcha_id, self.private_key)
        url = ''
        
        try:
            challenge = gt.geetest_register()
        except:
            challenge = ''
            
        if len(challenge)==32:
            url = "http://%s%s&challenge=%s&product=%s" % (self.BASE_URL, self.captcha_id, challenge, self.product)
        
        #self.render(r'register.html', title='register', url = url)        
        self.render_method(r'register.html', title = 'register', url = url)
        
    def post(self):
        name = self.get_argument('username')        
        passwd1 = self.get_argument('password1')
        passwd2 = self.get_argument('password2')
        challenge = self.get_argument("geetest_challenge")
        validate = self.get_argument("geetest_validate")
        seccode = self.get_argument("geetest_seccode")
        #print 'challenge:',challenge
        #print 'seccode:',seccode
        #print 'validate:',validate
        gt = geetest.geetest(self.captcha_id, self.private_key)
        ckresult = gt.geetest_validate(challenge, validate, seccode)        
        
        #########test############
        ckresult=1
        
        if not self.check(name, passwd1, passwd2, ckresult):
            #self.redirect('error')
            self.write_error(404)
        else:
            self.set_secure_cookie('name',name,3) 
            self.redirect(r'/')        
            
    def check(self,name, passwd1, passwd2, ckresult):
        if not ckresult :
            return False
        if passwd1 == passwd2 :
            return True
        return False
        
    def write_error(self, status_code):
        self.redirect('error')
    
class usrHandler(baseHandler):
    def get(self, usr):
        
        u = {
            'name':'haost',
            'pic':'../static/usrimg/haost.png',
            'description':'haonima from gx203',
            'tel':'10086',
            'email':'13sthao@stu.edu.cn',
            'years':'2',
            'exp':'1232',
        }
        self.render_method('member.html',title = usr,u = u)
        
class errorHandler(baseHandler):
    def get(self):
        self.write('error')        
        
class succHandler(baseHandler):
    def get(self):
        self.write('success')
        