import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/bkit/parser/' in sys.path:
    sys.path.append('./main/bkit/parser/')
if os.path.isdir('../target/main/bkit/parser') and not '../target/main/bkit/parser/' in sys.path:
    sys.path.append('../target/main/bkit/parser/')
from BKITLexer import BKITLexer
from BKITParser import BKITParser
from lexererr import *

testcase = "./test/testLexer.txt"
testfile = open(testcase,"a")
testfile.write("""import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):""")
testfile.close()

testcase = "./test/testParser.txt"
testfile = open(testcase,"a")
testfile.write("""import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):""")
testfile.close()

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        """tmp = repr(inputStr)
        file.write(tmp[1:-1])"""
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        testcase = "./test/testLexer.txt"
        testfile = open(testcase,"a")
        testfile.write("""
    def test_""" + str(num)+"""(self):
        \"\"\"Created automatically\"\"\"
        input = r\"\"\"""" + input + """\"\"\" 
        output = r\"\"\"""")
        
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except LexerError as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()

        testfile.write(line + """\"\"\"
        self.assertTrue(TestLexer.checkLexeme(input,output,"""+str(num)+"""))""")
        testfile.close()

        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        testcase = "./test/testParser.txt"
        testfile = open(testcase,"a")
        testfile.write("""
    def test_""" + str(num)+"""(self):
        \"\"\"Created automatically\"\"\"
        input = r\"\"\"""" + input + """\"\"\" 
        expect = r\"\"\"""")

        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = BKITParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        
        testfile.write(line+"""\"\"\"
        self.assertTrue(TestParser.checkParser(input,expect,"""+str(num)+"""))""")
        testfile.close()

        return line == expect
