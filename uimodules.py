import tornado.web

class listModule(tornado.web.UIModule):
    def render(self, toy):
        return self.render_string('modules/list.html',toy = toy)