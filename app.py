#!/usr/bin/env Python

################################################################################
# Written by Ryan Cotter
#   For Unique Tattoos
#
#   Once complete, this shouldn't need to change unless further
#   app capabilities are required
#
#   Using web.py (http://webpy.org)
#
################################################################################

import web

ut_email = 'unique_tattoos@hotmail.com'
auto_respond = 'someemailImustmake@mailey.com'

render = web.template.render('templates/', base='layout')
render_plain = web.template.render('templates/')

urls = (
        '/','Index',
#        '/about','About',
#        '/contact','Contact',
#        '/gallery','Gallery',
#        '/thanks','Thanks',
        )


class Index:
    def GET(self):
        return render.index()

#class Contact:
#    form = web.form.Form(
#            web.form.Textbox('name', web.form.notnull,
#                size=30, description="Name:"),
#            web.form.Textbox('email', web.form.notnull,
#                size=30, description="email"),
#            web.form.Textarea('message:', web.form.notnull,
#                size=30, description="Message:"),
#            web.form.Textbox('url',
#                description="Don't type anything here"),
#            web.form.Button('submit', type="submit",
#                description="Submit"),
#            )
#
#    def GET(self):
#        form = self.form
#        return render.contact(form)
#
#    def POST(self):
#        i = web.input()
#        #if len(i.url) == 0 and i.url == '':
#            #web.sendmail(from_address=i.email, to_address=ut_email, subject=i.name, message=i.message)
#            #web.sendmail(from_address=auto_respond, to_address=i.email, subject='Email recieved', message=("Hello %s, Your message has been recieved.\n This is an automatically generated message, you do not need to reply" % (i.name))
#
#        raise web.seeother('/thanks')
#
#class Gallery:
#
#    def GET(self):
#        return render.gallery()
#
#class Thanks:
#    def GET(self):
#        return render.thanks()
#
if __name__=='__main__':
    app = web.application(urls, globals())
    app.run()
