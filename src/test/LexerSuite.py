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
        self.assertTrue(TestLexer.checkLexeme("0X54J54","0.3,0.123,.,123,123.,.,<EOF>",111))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("0X5456A 0x205F 0XBCD 0X0 0X567 0x2","12.e5,10.e-3,10.e+3,10.,e,0.,e,<EOF>",112))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("01 8 0108 2000 000","0,1,10,0,0,1,100,<EOF>",113))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0O0 0o1 0o413215","Var,x0,.,12e51,.,2,<EOF>",114))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0B2005","-,0,-,1,-,10,-.,e3,-,10.,e,-,10.e3,<EOF>",115))

	###########################################################
	# Test floats
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("20.e5 18.E9 9.e+3 33.e-3 0.e ","0.3,0.123,.,123,123.,.,<EOF>",116))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("0.0 52.. 43124. 120000e-1","0.0,12.,.,1.,.,e,.,3,.,.,1.,.,e,<EOF>",117))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("0.4254 654.321 .7582 87867. .","0X12A,0x12B,0XFA,0XABC,0o567,0O2,<EOF>",118))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("4.e.6 -0 -404 -.e3 -10.e -10.e3","0,Error Token B",119))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("e97 E-66 16e 30E4 12.0e3","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",120))

	###########################################################
	# Test illegal escape
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",121))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\'\\myfriend" ""","""Illegal Escape In String: bac\\m""",122))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "chao cac ban nhaaa \\Hom\\nay cac ban the nao" ""","""Illegal Escape In String: bad game toDay\\H""",123))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "24 naif ^%$^% cdasjh\\Fncueyew" ""","""Illegal Escape In String: ,dls\\F""",124))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "To la Chung Xon \\Ne" ""","""Illegal Escape In String: ado\\m""",125))
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" xin chao "phan thanh truong\\haha" 456""","""123,abc,Illegal Escape In String: xyz\\k""",126))
    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ahihi do ngoc\\\\" ""","""" Illegal Escape In String: aa\" """,127))
    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Day la ' illegal" ""","""Illegal Escape In String: This is '""",128))
    def test_illegal_escape_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Test met qua troi \\Wa dat luon ne""","""Illegal Escape In String: This is \\W""",129))
    def test_illegal_escape_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ngoi TAo \\\\tESt eScapE '" ne ' \\r" ""","""Illegal Escape In String: This is a test '" asdsadasd '""",130))

	###########################################################
	# Test unclosed string
    def test_unclosed_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,131))
    def test_unclosed_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hi Chau Thanh""Tan ""","""bac,Unclosed String: xyc """,132))
    def test_unclosed_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "vi su nghiep qua PPL \\n" ""","""Unclosed String: adsfa \\n""",133))
    def test_unclosed_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "String ket thuc bang EOF" ""","""Unclosed String: acnv EOF """,134))
    def test_unclosed_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n ""","""Unclosed String: abc\\n """,135))
    def test_unclosed_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "khok '" 1" "dong song~~~ EOF""","""a,+,11.2,+,mam.123,12,Unclosed String: %^&""",136))
    def test_unclosed_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " """,""", ,Unclosed String:  """,137))
    def test_unclosed_string_8(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: assignment Body: str = "Hello World!!! Endbody.""",""",Unclosed String:  """,138))
    def test_unclosed_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "8n[#F*`~.~+C_D""","""Unclosed String: ULxhskjdhfkja2""",139))
    def test_unclosed_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""""fe23%$.81r " {"abc"} 123"abc""","""Nk8U;,rA,@Y3*,oV,Unclosed String: bh1""",140))

	###########################################################
	# Test normal string
    def test_normal_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Day la 1 string nha Dang Huynh Minh Tri"  ""","""ab'"c\\n def,<EOF>""",141))
    def test_normal_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t"  ""","""This is a string containing tab \\t,<EOF>""",142))
    def test_normal_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'""  ""","""He asked me: '"Where is John?'",<EOF>""",143))
    def test_normal_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "String nay chua cac ky tu dac biet !@#$%^^&*()?/|~!%>:P{}<> :)))"  ""","""Illegal Escape In String:  This is a test '" asdsadasd '""",144))
    def test_normal_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""Illegal Escape In String: ab'"c\\ """,145))
    def test_normal_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Sau day la 1 string rong" ""  ""","""Illegal Escape In String: ab'"c\\ """,146))
    def test_normal_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bool_of_string ('"True'")"  ""","""Illegal Escape In String: ab'"c\\ """,147))
    def test_normal_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "** cai nay hong phai comment nha **"  ""","""Illegal Escape In String: ab'"c\\ """,148))
    def test_normal_string_9(self):
        self.assertTrue(TestLexer.checkLexeme("""" This is a test 0925919727 \\' PHONE" abc 
"YKYUUD '" \\f fsgre " ""","""Illegal Escape In String: ab'"c\\ """,149))
    def test_normal_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b\\f\\r\\n\\t\\'\\\\"  ""","""Illegal Escape In String: ab'"c\\ """,150))
    
	###########################################################
	# Test keyword
    def test_keyword_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc For 12 BreaK Continue dot","For,brEaK,Continue,km,<EOF>",151))
    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme("if thEn ElSE Then ","Do,if,thEn,Error Token E",152))
    def test_keyword_3(self):
        self.assertTrue(TestLexer.checkLexeme("Varr VaR","Var,r,Error Token V",153))
    def test_keyword_4(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter: x","Parameter,:,x,<EOF>",154))
    def test_keyword_5(self):
        self.assertTrue(TestLexer.checkLexeme("BODY int 1.12INTEGER 12and","Error Token B",155))
    def test_keyword_6(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Error Token M",156))
    def test_keyword_7(self):
        self.assertTrue(TestLexer.checkLexeme("If then else false","If,then,else,false,<EOF>",157))
    def test_keyword_8(self):
        self.assertTrue(TestLexer.checkLexeme("anD then false","anD,then,false,<EOF>",158))
    def test_keyword_9(self):
        self.assertTrue(TestLexer.checkLexeme("sTRIng False","sTRIng,False,<EOF>",159))
    def test_keyword_10(self):
        self.assertTrue(TestLexer.checkLexeme("EndDoEndForWhWhileileWhileWhile","EndDo,EndFor,Error Token W",160))

	###########################################################
	# Test operator
    def test_truong1(self):
        self.assertTrue(TestLexer.checkLexeme("truong_555!","",161))
    def test_truong2(self):
        self.assertTrue(TestLexer.checkLexeme("0123p","",162))
    def test_truong3(self):
        self.assertTrue(TestLexer.checkLexeme("0000000","",163))
    def test_truong4(self):
        self.assertTrue(TestLexer.checkLexeme("**truong**","",164))
    def test_truong5(self):
        self.assertTrue(TestLexer.checkLexeme("** truong **","",165))
    def test_truong6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "phan thanh truong" ""","",166))
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


