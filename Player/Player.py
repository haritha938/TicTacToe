#----------------------------------------------------------------------------------------
#   Player object contains different kind of players
#    This code has been updated on the initial code given by  professor,Arjang Fahim
#   Name: Haritha Nimmagadda#
#   Date: 8/7/2020
#   email: haritha.nimmagadda@student.csulb.edu
#   version: 1.1.0
#----------------------------------------------------------------------------------------


import math
import random
import Player.Node as NodeClass

class Player():
    def __init__(self, board):
        self.board = board

class RandomComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        
    
    def next_move(self):
        available_space = self.board.available_space()

        
        square = random.choice(available_space)
        self.board.board_data[square] = self.board.c_letter


class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        

    def next_move(self):
        print ("Please enter your move ", end = " ")
        square = input()
        if int(square)-1 not in self.board.available_space():
            print("postion '",square,"' is already used. Please enter a valid postion")
            square=input()
        self.board.board_data[int(square)-1] = self.board.h_letter
        
class SmartPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        self.Nodes=self.board.available_space().copy()
        self.bd=board
        self.MinMaxBoardData=board.board_data.copy()




    def next_move(self):
        self.Nodes = self.board.available_space().copy()
        self.MinMaxBoardData = self.bd.board_data.copy()
        rootNodeid = -1
        root = NodeClass.Node(rootNodeid, self.MinMaxBoardData.copy())
        turn = self.board.c_letter
        self.constructTree(root, 0, root.board_data)

        root.value=float("-inf")
        self.MiniMax(root, 0)
        values = list()
        positions = list()
        max = float("-inf")
        pos = None
        self.verify(root,0)
        for childNode in root.getChildNodes():
            val = childNode.value
            values.append(val)
            positions.append(childNode.nodeid)
            if val > max:
                max = val
                pos = childNode.nodeid
        #print("list:", values, "postions:", positions, "pos:", pos)
        self.board.board_data[pos] = self.board.c_letter


    #construct tree with all scenarios
    def constructTree(self,root,depth,Board_data):
        turn=None

        if depth%2==0:
            turn=self.board.c_letter
            if self.is_winner(self.board.h_letter, root.getBoarddata()):
               return

        else:
            turn = self.board.h_letter
            if self.is_winner(self.board.c_letter, root.getBoarddata()):
               return


        #if self.is_winner(turn, root.getBoarddata()):
         #   return


        for nodeId in self.Temp_available_space(root.getBoarddata()):
            ChildNodeBoard_data=root.getBoarddata().copy()
            ChildNodeBoard_data[nodeId]=turn
            mainNode=NodeClass.Node(nodeId,ChildNodeBoard_data.copy())
            root.addChildNode(mainNode)
            mainNode.setParent(root)
            if root.getName()=="":
                root.setname("d-"+str(depth)+":"+str(mainNode.nodeid))
            else:
                root.setname("-"+str(mainNode.nodeid))
            if  self.is_winner(turn, mainNode.getBoarddata()):
                continue

            blankSpaceCount=len(self.Temp_available_space(ChildNodeBoard_data))
            if blankSpaceCount>0:
                if not self.is_winner(turn, mainNode.getBoarddata()):
                    self.constructTree(mainNode,depth+1,ChildNodeBoard_data.copy())

    # just for verification and can be ignored
    def verify(self,root,depth):
        if depth%2==0:
            flag="max"
        else:
            flag="min"

        for child in root.getChildNodes():
            self.verify(child,depth+1)
        childernId=list()
        util=list()
        for childNode in root.getChildNodes():
            childernId.append(childNode.nodeid)
            util.append(childNode.value)

        #print("flag:",flag,"RootUtil:",root.value,"depth:",depth,"NodeId:",root.nodeid,"ChildId:",childernId,"util:",util)

    # to draw the board
    def draw_temp_board(self,currentBoard_data):

        print("\n\n")
        index = 0

        for i in range(3):
            print("\t\t\t  %s | %s  | %s  \n" % (
            currentBoard_data[index], currentBoard_data[index + 1], currentBoard_data[index + 2]))
            index += 3

    def Temp_available_space(self,boarddata):
        return [i for i, x in enumerate(boarddata) if x == 0]

    #implemented miniMax algorithm
    def MiniMax(self,root,depth):
        flag=None

        if depth % 2 != 0:
            flag="min"
            if root.value==None:
                root.value=float("inf")

        else:
            flag = "max"
            if root.value==None:
                root.value = float("-inf")

        if len(root.getChildNodes()) == 0:
            #root.value = self.utility(root,flag)
            root.value = self.utility1(root)
            return root.value
        else:

            for childNode in root.getChildNodes():

                if depth % 2 != 0:
                    root.value = min(root.value, self.MiniMax(childNode, depth + 1))

                else:
                    root.value = max(root.value,self.MiniMax(childNode, depth + 1))

            return root.value







    # calculating the utility function
    def utility1(self, node):
        t = 0
        blankspaces = len(self.Temp_available_space(node.getBoarddata()))

        if self.is_winner(self.board.c_letter, node.getBoarddata()):
            t = blankspaces + 1
        elif self.is_winner(self.board.h_letter, node.getBoarddata()):
            t = -1*(blankspaces + 1)
        else:
            if blankspaces==0:
                t = 0
            else:
                print("blankspaces:",blankspaces,"Boarddata:",node.getBoarddata())

        return t




    # is if letter is the winner
    def is_winner(self, letter,board_data):
        index = 0
        # checking for the row similarity
        for i in range(3):

            row_set = set(board_data[index: index + 3])
            if len(row_set) == 1 and (letter in row_set):
                return True
            index += 3

        # checking for the column similarity
        for i in range(3):
            if (board_data[i] == letter and board_data[i + 3] == letter and board_data[i + 6] == letter):
                return True

        if (board_data[0] == letter and board_data[4] == letter and board_data[8] == letter):
            return True

        if (board_data[2] == letter and board_data[4] == letter and board_data[6] == letter):
            return True

        return False



        
