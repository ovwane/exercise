# -*- coding:utf-8 -*-
import datetime
import log
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:  #如果小于60分，表格输出时标红
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>'% (name,score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' %(name,score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<caption>'
print u"表格标题"
print '</caption>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
