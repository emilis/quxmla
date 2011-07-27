#!/usr/bin/python

#
#    QuXmlA - Quick Xml Analyzer
#
#    Copyright (C) 2011 Emilis Dambauskas <emilis.d@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import xml.sax
import xml.sax.handler


class QuxmlaElementStats():
    """Stats for a path"""

    def __init__(self):
        
        self.times_total = 1
        self.times_min = 0
        self.times_max = 0
        self.children = dict()
    
    
    def printMe(self):

        print "     {0}\t{1}\t{2}".format(
                self.times_total,
                self.times_min,
                self.times_max)
        for p in self.children:
            print "     {0}\t{1}".format(
                    p,
                    str(self.children[p]))


class QuxmlaStats():
    """Stats for all elements"""

    def __init__(self):

        self.stats = dict()


    def startElement(self, path, parentPath):

        #print("startElement", path, parentPath)

        # Increase times_total an null all children counters:
        if self.stats.has_key(path):
            el = self.stats[path]
            el.times_total += 1
            for p in el.children:
                el.children[p] = 0
        else:
            self.stats[path] = QuxmlaElementStats()

        # Increase children counter on parent:
        if parentPath:
            pchildren = self.stats[parentPath].children
            if pchildren.has_key(path):
                pchildren[path] += 1
            else:
                pchildren[path] = 1
        else:
            el = self.stats[path]
            el.times_min = None
            el.times_max = None

    
    def endElement(self, path):

        el = self.stats[path]
        #print("endElement    ", path, el.times_total, len(el.children))

        if el.times_total == 1:
            for p in el.children:
                self_child = self.stats[p]
                el_child_count = el.children[p]
                #print("endElement-child", el.times_total, p, el_child_count)
                self_child.times_min = el_child_count;
                self_child.times_max = el_child_count;
        else:
            for p in el.children:
                self_child = self.stats[p]
                el_child_count = el.children[p]
                #print("endElement-child", el.times_total, p, el_child_count)
                self_child.times_min = min(self_child.times_min, el_child_count)
                self_child.times_max = max(self_child.times_max, el_child_count)




class QuxmlaHandler(xml.sax.handler.ContentHandler):
    """Quick XML ContentHandler"""

    def __init__(self):

        self.path = []
        self.pathStr = ""
        self.parentPathStr = ""
        self.stats = QuxmlaStats()

    def startDocument(self):

        self.stats.startElement("/", False)

    def endDocument(self):

        self.stats.endElement("/")

    
    def startElement(self, name, attrs):

        self.parentPathStr = "/" + "/".join(self.path)
        self.path.append(name)
        self.pathStr = "/" + "/".join(self.path)

        self.stats.startElement(self.pathStr, self.parentPathStr)

    
    def endElement(self, name):

        self.stats.endElement(self.pathStr)
        last = self.path.pop()

        if last != name:
            raise AssertionError("Closing and opening tags do not match.")

        self.pathStr = "/" + "/".join(self.path)

    
    def printResults(self):

        print "Results:"
        print ""
        print "{0}\t{1}\t{2}\t{3}".format(
                "path",
                "found total",
                "min(found in parent)",
                "max(found in parent)")

        keys = self.stats.stats.keys()
        keys.sort()
        for p in keys:
            el = self.stats.stats[p]
            print "{0}\t{1}\t{2}\t{3}".format(
                    p,
                    el.times_total,
                    el.times_min,
                    el.times_max)
        
        # Some debugging:
        #for p in keys:
        #    print(p)
        #    self.stats.stats[p].printMe()



def main(argv):

    # Create XmlReader:
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_validation, False)
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setFeature(xml.sax.handler.feature_external_pes, False)
    
    # Create an assign a handler to the parser:
    handler = QuxmlaHandler()
    parser.setContentHandler(handler)

    # process all arguments as filenames:
    for f in argv:
        print "Processing {0}...".format(f)
        parser.parse(f)
    
    print ""
    handler.printResults()


def usage():

    print "Usage: $ python quxmla.py FILE [FILE] [FILE] ..."



if __name__ == "__main__":

    print "QuXmlA - Quick Xml Analyzer  Copyright (C) 2011 Emilis Dambauskas"
    print "This program comes with ABSOLUTELY NO WARRANTY."
    print "This is free software, and you are welcome to redistribute it under certain conditions; see LICENSE.txt for details."
    print ""
    
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        usage()
        
