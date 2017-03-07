class People(object):
    tool = None

    def __init__(self, name):
        self.name = name

    def setTool(self, tool):
        self.tool = tool

    def write(self, text):
        self.tool.write(self.name, text)


class ToolBase:

    def write(self, name, text):
        raise NotImplementedError

class PenTool(ToolBase):

    def write(self, name, text):
        print(u'%s (pen) %s' % (name, text))


class BrushTool(ToolBase):

    def write(self, name, text):
        print(u'%s (brush) %s' % (name, text))


class Student(People):
    tool = PenTool()


class Painter(People):
    tool = BrushTool()


student = Student(u'Student')
student.write(u'write text')

artist = Painter(u'Artist')
artist.write(u'draw the picture')
