import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	###########################################################
	# Test identifiers
	def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
	def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("day la 1 test","<EOF>",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("xin chao cac ban","kK,a10,1,Error Token A",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("co so dau tien 108NVH","asf,aso,Do,woad,<EOF>",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("viet hoa IDENTIFIERS","tuoitre,chuwa,trai,su,doi,<EOF>",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("vIet Lon XOn nE","dem123,123,dem,1,a,an,han,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("co ky tu dac biet @@","yud,al,gnaht,ugn,12,Error Token A",108))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x","Var,:,x,<EOF>",109))
    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("tu1 1a` le^ trun9 son!!!","1,cOn,viT,xOE,rA,Error Token H",110))

	###########################################################
	# Test integers
    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("0X5456A 0x205F 0XBCD 0X0 0X567 0x2","12.e5,10.e-3,10.e+3,10.,e,0.,e,<EOF>",112))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("01 8 0108 2000 000","0,1,10,0,0,1,100,<EOF>",113))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("0O0 0o1 0o413215","Var,x0,.,12e51,.,2,<EOF>",114))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0B2005","-,0,-,1,-,10,-.,e3,-,10.,e,-,10.e3,<EOF>",115))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0X54J54","0.3,0.123,.,123,123.,.,<EOF>",116))
    def test_integer_real6(self):
        self.assertTrue(TestLexer.checkLexeme("0.0 12.. 1..e.3 ..1..e","0.0,12.,.,1.,.,e,.,3,.,.,1.,.,e,<EOF>",117))
    def test_integer_real7(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5 10.e-3 10.e+3 10.e 0.e","0X12A,0x12B,0XFA,0XABC,0o567,0O2,<EOF>",118))
    def test_integer_real8(self):
        self.assertTrue(TestLexer.checkLexeme("-0 -1 -10 -.e3 -10.e -10.e3","0,Error Token B",119))
    def test_integer_real9(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",120))
	def test_integer_real5(self):
        self.assertTrue(TestLexer.checkLexeme("0.3 0.123 .123 123. .","0.3,0.123,.,123,123.,.,<EOF>",116))


	###########################################################
	# Test floats


	###########################################################
	# Test illegal escape

	###########################################################
	# Test unclosed string

	###########################################################
	# Test string

	###########################################################
	# Test keyword

	###########################################################
	# Test operator

	###########################################################
	# Test comment


	###########################################################
	# Test array

	###########################################################
	# Test boolean

	###########################################################
	# Test array

	###########################################################
	# Test array

	###########################################################
	# Test array


