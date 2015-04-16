from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Resource
from django.views.decorators.csrf import csrf_exempt
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

out = ""

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.title = ""
        self.links = "<p><h2> TITULARES BARRAPUNTO </h2></p>"
		
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
            

def update(request):
    global out
    
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    theParser.parse("http://barrapunto.com/index.rss")
    
    out = theHandler.links
    return HttpResponse(">> Titulares barrapunto actualizados" + out)

@csrf_exempt

def serve(request, resource):
    verb = request.method
    
    if verb == "GET":
        try:
            entry = Resource.objects.get(key=resource)
            return HttpResponse("<p> " + str(entry.value) + "</p>" + out)
        except Resource.DoesNotExist:
            return HttpResponseNotFound("ERROR: Entrada no disponible")
    elif verb == "PUT":
        entry = Resource(key=resource, value=request.body)
        entry.save()
        return HttpResponse("Entrada insertada correctamente")
