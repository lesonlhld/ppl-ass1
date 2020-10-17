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
        self.assertTrue(TestLexer.checkLexeme(""" "String ket thuc bang '" ""","""Unclosed String: acnv EOF """,134))
    def test_unclosed_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n ""","""Unclosed String: abc\\n """,135))
    def test_unclosed_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "khok '" 1" "dong song~~~ 
        newline" " ""","""a,+,11.2,+,mam.123,12,Unclosed String: %^&""",136))
    def test_unclosed_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " """,""", ,Unclosed String:  """,137))
    def test_unclosed_string_8(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: assignment Body: str = "Hello World!!! \\" Endbody.""",""",Unclosed String:  """,138))
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
        self.assertTrue(TestLexer.checkLexeme("Body Break  Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False EndDo","For,brEaK,Continue,km,<EOF>",151))
    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme("if thEn ElsE Then ","Do,if,thEn,Error Token E",152))
    def test_keyword_3(self):
        self.assertTrue(TestLexer.checkLexeme("EndFor EndIff EndDoOO EndGame","Var,r,Error Token V",153))
    def test_keyword_4(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter: x[123],n","Parameter,:,x,<EOF>",154))
    def test_keyword_5(self):
        self.assertTrue(TestLexer.checkLexeme(" int var_ =. int(1.12)*1.0 12and","Error Token B",155))
    def test_keyword_6(self):
        self.assertTrue(TestLexer.checkLexeme("x oR y assign !k","oR,diVModNTEGER,Error Token M",156))
    def test_keyword_7(self):
        self.assertTrue(TestLexer.checkLexeme("If a == true then Return 1. elseIf a = False Returnn 0","If,then,else,false,<EOF>",157))
    def test_keyword_8(self):
        self.assertTrue(TestLexer.checkLexeme("""If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf.""","anD,then,false,<EOF>",158))
    def test_keyword_9(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5)
a[i] = b +. 1.0;
i = i + 1;
EndWhile.
EndBody.""","sTRIng,False,<EOF>",159))
    def test_keyword_10(self):
        self.assertTrue(TestLexer.checkLexeme("IfaThenbElseWhile(x>0)Thena++EndWhileEndIF","EndDo,EndFor,Error Token W",160))

	###########################################################
	# Test operator
    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("25+6-.2.5%3\\100","a,+,bas,+.,asdf,-,ddas,-.,<EOF>",161))
    def test_operator_2(self):
        self.assertTrue(TestLexer.checkLexeme("2e-5*.41+-18","a,+,+,bcds,-,-,cd,<EOF>",162))
    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("test&&lexer||parser&h=4/5","asdf,*,dsf,*.,123,Error Token /",163))
    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("=<=<>>=>=.=/===>.<<.!=","a,*.,0.123e12,<EOF>",164))
    def test_operator_5(self):
        self.assertTrue(TestLexer.checkLexeme("!x&&a<=.b\\.d*","!,a,%,5,&&,b,||,c,<EOF>",165))

    ###########################################################
	# Test comment
    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a single-line comment. **","<EOF>",166))
    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("***** *** **","*,<EOF>",167))
    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a
* multi-line
* comment.
** ""","*,<EOF>",168))
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("* * **** * *","asda,<EOF>",169))
    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("**Tui SaP Bj LAG luon r =.= (T.T) :v 2654^$$%!{><>~}{5}[789]!@#$%^&* \\v \\n   **","Unterminated Comment",170))
    def test_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("""hello **"be mo"** **cUG wa tr wa dat lun""","13,ek3,<,9,end,*,das,Unterminated Comment",171))
    def test_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme("**met xiu luon a* kok tie9 con bo","2,er,*,Error Token E",172))
    def test_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme("""**VI DU CO EOF TRONG CMT** "\\\\den day la oke\\n" ""","+,abc,<,>,xyzb,>,cv,<EOF>",173))
    def test_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**comment trong string nha \\haha**" oke hem???""","*,Unterminated Comment",174))
    def test_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme("""**sau day
        *la
        * **comment trong cmt**
        *
        **""","{,abc,},1.,abc,<EOF>",175))

	###########################################################
	# Test error token
    def test_error_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("""fjiwef883_Fef_GRWE4324 r3fe 23728DFRfdw""","{,abc,},1.,abc,<EOF>",176))
    def test_error_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("""__count in function""","{,abc,},1.,abc,<EOF>",177))
    def test_error_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("""iwqoue9432@#$8(!/da""","{,abc,},1.,abc,<EOF>",178))
    def test_error_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("""!!=x/y""","{,abc,},1.,abc,<EOF>",179))
    def test_error_token_5(self):
        self.assertTrue(TestLexer.checkLexeme(""""string nay co 2 \\' nha qui vi ^.^"' ""","{,abc,},1.,abc,<EOF>",180))
    
	###########################################################
	# Test array
    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme("""{996,712,216}""","""{1,2,3},<EOF>""",181))
    def test_array_2(self):
        self.assertTrue(TestLexer.checkLexeme("""{{867,345,987},{76,12,744}}""","""{{1},{1,2,3}},<EOF>""",182))
    def test_array_3(self):
        self.assertTrue(TestLexer.checkLexeme("""{y65,de3DEF,ca_rFE245_2E23}""","""{,a,,,b,,,c,},<EOF>""",183))
    def test_array_4(self):
        self.assertTrue(TestLexer.checkLexeme("""{"STRING","aRraY1","Array2"}""","""{"abc","asd"},<EOF>""",184))
    def test_array_5(self):
        self.assertTrue(TestLexer.checkLexeme("""{   20, 2   ,108  }""","""{1 , 2, 3},<EOF>""",185))
    def test_array_6(self):
        self.assertTrue(TestLexer.checkLexeme("""{10.e13, 0.123, 543.0e-6  }""","""{10.e13, 0.123},<EOF>""",186))
    def test_array_7(self):
        self.assertTrue(TestLexer.checkLexeme("""{{"xe mau xanh"},"xe mau do"}""","""{{"abc"},"asd"},<EOF>""",187))
    def test_array_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" {"duwat73\\r \\t", "@#&\\n rwFEW54", 54312}  ""","""{,3,,,2,,,3,,,4,},<EOF>""",188))
    def test_array_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" {**comment trong array**}  ""","""{,3,,,2,,,3,,,4,},<EOF>""",189))
    def test_array_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" {True,False}  ""","""{,3,,,2,,,3,,,4,},<EOF>""",190))
	###########################################################
	# Test Fucntion
    def test_function_1(self):
        self.assertTrue(TestLexer.checkLexeme("""** comment nha **
    Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""","""{1,2,3},<EOF>""",191))
    def test_function_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};""","""{{1},{1,2,3}},<EOF>""",192))
    def test_function_3(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5)
        a[i] = b +. 1.0;
        i = i + 1;
        EndWhile.
        EndBody.""","""{,a,,,b,,,c,},<EOF>""",193))
    def test_function_4(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo 
        Parameter: n
        Body: 
            While i < 5 
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.""","""{"abc","asd"},<EOF>""",194))
    def test_function_5(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.""","""{1 , 2, 3},<EOF>""",195))
    def test_function_6(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
    Parameter: abc;
    Body:
    Var **some COMMENT**: ****someid = 3
        **more more**
    vAr: someid;
    EndBody.""","""{10.e13, 0.123},<EOF>""",196))
    def test_function_7(self):
        self.assertTrue(TestLexer.checkLexeme("""Function:fooParameter:nBody:Ifn==0ThenReturn1;ElseReturnn*fact(n-1);ElseReturnn;EndIf.EndBody.""","""{{"abc"},"asd"},<EOF>""",197))
    def test_function_8(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    c =a && b;
                Else 
                    Do
                        x= x+1;
                        iF x==5 tHEN Break;
                    While x>1 
                    EndDo.
            EndIf.
        EndBody.""","""{,3,,,2,,,3,,,4,},<EOF>""",198))
    def test_function_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" **global declaration**  Var: a = 5;
        Varr: b[2][3] = {{2,3,4},{4,5,6}};
        Varrr: c, d = 6, e, f;
        Var: m, n[10];""","""{,3,,,2,,,3,,,4,},<EOF>""",199))
    def test_function_10(self):
        self.assertTrue(TestLexer.checkLexeme("""Function:testdjiDEW__214__wsaParameter:ne23Body:x1 = a[3-foo(3)];Var:x,y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};WhileTrueprint("Hello_World\\n");EndWhile.EndBody.""","""{,3,,,2,,,3,,,4,},<EOF>""",200))