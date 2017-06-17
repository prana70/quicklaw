import web


render=web.template.render('templates')

urls = (
    '/article','article',
    '/index','index',
    '/blog/\d+','blog',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        query=web.input()
        return query

class blog:
    def GET(self):
        return web.ctx.env
    def POST(self):
        data=web.input()
        return data

class hello:        
    def GET(self, name):
        return web.seeother('http://news.ifeng.com')

class article:
    def GET(self):
        r=['wangbin','caiwei','wangyunqi']
        return render.article(r)

if __name__ == "__main__":
    app.run()


