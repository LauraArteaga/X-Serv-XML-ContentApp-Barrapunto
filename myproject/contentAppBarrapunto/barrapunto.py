#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.title = ""
        self.links = "<p><h1> TITULARES </h1></p>"
		
    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True
            
    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.title = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
				self.links += "<p><a href=" + self.theContent + ">" + self.title + "</a></p>"
				self.inContent = False
				self.theContent = ""
                
    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
            
	
if len(sys.argv)<2:
    print "Usage error: python barrapunto.py <document>"
    sys.exit(1)

theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)


xmlFile = open(sys.argv[1],"r")
theParser.parse(xmlFile)

out = open("out.html", "w")
out.write(theHandler.links.encode("utf-8"))
