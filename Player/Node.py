
# this class is to construct a node so as to eventually form a tree
class Node():
    def __init__(self,position,board_data):
        self.nodeid=position
        self.board_data=board_data.copy()
        self.childNones=list()
        self.value=None
        self.parent=None
        self.name=""
        self.depth=float("inf")

    def getChildNodes(self):
        return self.childNones

    def getParent(self):
        return self.parent

    def addChildNode(self,child):
        self.childNones.append(child)

    def getNodeid(self):
        return self.nodeid

    def setParent(self,node):
        self.parent=node

    def setBoarddata(self,board_data):
        self.board_data=board_data.copy()

    def getBoarddata(self):
        return self.board_data.copy()

    def getName(self):
        return self.name

    def setname(self,addTag):
        self.name=self.name,addTag

    def setDepth(self,depth):
        self.depth=depth

    def getDepth(self):
        return self.depth


