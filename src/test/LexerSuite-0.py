import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("rdad 40oBhenK292aWfTSFLt6","rdad,40,oBhenK292aWfTSFLt6,<EOF>",103))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("kK a10 1AbCd naA","kK,a10,1,Error Token A",104))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("asf aso Dowoad ","asf,aso,Do,woad,<EOF>",105))
    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("tuoitre chuwa trai su doi","tuoitre,chuwa,trai,su,doi,<EOF>",106))
    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("dem123 123dem 1a an han","dem123,123,dem,1,a,an,han,<EOF>",107))
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("yud al gnaht ugn 12Ads","yud,al,gnaht,ugn,12,Error Token A",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x","Var,:,x,<EOF>",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("1 cOn viT xOE rA HAi caI canh","1,cOn,viT,xOE,rA,Error Token H",110))
    
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",111))
    def test_integer_real1(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5 10.e-3 10.e+3 10.e 0.e","12.e5,10.e-3,10.e+3,10.,e,0.,e,<EOF>",112))
    def test_integer_real2(self):
        self.assertTrue(TestLexer.checkLexeme("01 10 001 100","0,1,10,0,0,1,100,<EOF>",113))
    def test_integer_real3(self):
        self.assertTrue(TestLexer.checkLexeme("Var x0.12e51.2","Var,x0,.,12e51,.,2,<EOF>",114))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.checkLexeme("-0 -1 -10 -.e3 -10.e -10.e3","-,0,-,1,-,10,-.,e3,-,10.,e,-,10.e3,<EOF>",115))
    def test_integer_real5(self):
        self.assertTrue(TestLexer.checkLexeme("0.3 0.123 .123 123. .","0.3,0.123,.,123,123.,.,<EOF>",116))
    def test_integer_real6(self):
        self.assertTrue(TestLexer.checkLexeme("0.0 12.. 1..e.3 ..1..e","0.0,12.,.,1.,.,e,.,3,.,.,1.,.,e,<EOF>",117))
    def test_integer_real7(self):
        self.assertTrue(TestLexer.checkLexeme("0X12A 0x12B 0XFA 0XABC 0o567 0O2","0X12A,0x12B,0XFA,0XABC,0o567,0O2,<EOF>",118))
    def test_integer_real8(self):
        self.assertTrue(TestLexer.checkLexeme("0B123 0BFA","0,Error Token B",119))
    def test_integer_real9(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",120))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",121))
    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bac\\ma" ""","""Illegal Escape In String: bac\\m""",122))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bad game toDay\\How\\na win" ""","""Illegal Escape In String: bad game toDay\\H""",123))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ",dls\\F12" ""","""Illegal Escape In String: ,dls\\F""",124))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ado\\mado" ""","""Illegal Escape In String: ado\\m""",125))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123abc "xyz\\k" 456""","""123,abc,Illegal Escape In String: xyz\\k""",126))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aa\\" ""","""" Illegal Escape In String: aa\" """,127))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is ' illegal" ""","""Illegal Escape In String: This is '""",128))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is \\W illegal""","""Illegal Escape In String: This is \\W""",129))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a test '" asdsadasd ' \\f asdasd " ""","""Illegal Escape In String: This is a test '" asdsadasd '""",130))
    
    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,131))
    def test_unclose_String1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bac""xyc ""","""bac,Unclosed String: xyc """,132))
    def test_unclose_String2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "adsfa \n" ""","""Unclosed String: adsfa \n""",133))
    def test_unclose_String3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "acnv EOF ""","""Unclosed String: acnv EOF """,134))
    def test_unclose_String4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n ""","""Unclosed String: abc\\n """,135))
    def test_unclose_String5(self):
        self.assertTrue(TestLexer.checkLexeme(""" a+11.2+"mam.123" 12 "%^&""","""a,+,11.2,+,mam.123,12,Unclosed String: %^&""",136))
    def test_unclose_String6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " "" """,""", ,Unclosed String:  """,137))
    def test_unclose_String7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " """,""",Unclosed String:  """,138))
    def test_unclose_String8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ULxhskjdhfkja2""","""Unclosed String: ULxhskjdhfkja2""",139))
    def test_unclose_String9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Nk8U;"rA"@Y3*"oV"bh1""","""Nk8U;,rA,@Y3*,oV,Unclosed String: bh1""",140))


    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",141))
    def test_normal_string_with_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t"  ""","""This is a string containing tab \\t,<EOF>""",142))
    def test_normal_string_with_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'""  ""","""He asked me: '"Where is John?'",<EOF>""",143))
    def test_normal_string_with_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" " This is a test '" asdsadasd ' \\b asdasd "  ""","""Illegal Escape In String:  This is a test '" asdsadasd '""",144))
    def test_normal_string_with_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\ def"  ""","""Illegal Escape In String: ab'"c\\ """,145))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",146))
    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("Tabcd","Error Token T",147))
    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme("Continue BreAk","Continue,Error Token B",148))
    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("1++3","1,+,+,3,<EOF>",149))
    def test_wrong_token4(self):
        self.assertTrue(TestLexer.checkLexeme("a~bc","a,Error Token ~",150))

    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("For brEaK Continue km","For,brEaK,Continue,km,<EOF>",151))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("Do if thEn ElSE ","Do,if,thEn,Error Token E",152))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("Varr VaR","Var,r,Error Token V",153))
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter: x","Parameter,:,x,<EOF>",154))
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("BODY int 1.12INTEGER 12and","Error Token B",155))
    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Error Token M",156))
    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("If then else false","If,then,else,false,<EOF>",157))
    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("anD then false","anD,then,false,<EOF>",158))
    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("sTRIng False","sTRIng,False,<EOF>",159))
    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("EndDoEndForWhWhileileWhileWhile","EndDo,EndFor,Error Token W",160))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",161))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",162))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "John isn'"t me" ""","""John isn'"t me,<EOF>""",163))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",164))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",165))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**This is not a comment **" 12yz ""","""**This is not a comment **,12,yz,<EOF>""",166))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Var: x= 1+2;" ""","""Var: x= 1+2;,<EOF>""",167))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a normal string" ""","""This is a normal string,<EOF>""",168))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string with escape \\f " ""","""This is a string with escape \\f ,<EOF>""",169))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"\"\"\" """,""",,<EOF>""",170))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("a+bas+.asdf-ddas-.","a,+,bas,+.,asdf,-,ddas,-.,<EOF>",171))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("a++bcds--cd","a,+,+,bcds,-,-,cd,<EOF>",172))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("asdf*dsf*.123/123/.321","asdf,*,dsf,*.,123,Error Token /",173))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("a *.0.123e12","a,*.,0.123e12,<EOF>",174))
    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("!a%5&&b||c","!,a,%,5,&&,b,||,c,<EOF>",175))
    def test_operator6(self):
        self.assertTrue(TestLexer.checkLexeme("a==b==01234!=43210<3>4","a,==,b,==,0,1234,!=,43210,<,3,>,4,<EOF>",176))
    def test_operator7(self):
        self.assertTrue(TestLexer.checkLexeme("*and<=>mod</<=","*,and,<=,>,mod,<,Error Token /",177))
    def test_operator8(self):
        self.assertTrue(TestLexer.checkLexeme("=/=6==5<.abd>.0","=/=,6,==,5,<.,abd,>.,0,<EOF>",178))
    def test_operator9(self):
        self.assertTrue(TestLexer.checkLexeme("3>.123e","3,>.,123,e,<EOF>",179))
    def test_operator10(self):
        self.assertTrue(TestLexer.checkLexeme("0.123/.12.e3","0.123,Error Token /",180))


    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",181))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",182))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("* ****","*,<EOF>",183))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("**1.e0 - 101** asda","asda,<EOF>",184))
    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0\\nabc -101","Unterminated Comment",185))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9**e=9e**end*das***d1.nerE","13,ek3,<,9,end,*,das,Unterminated Comment",186))
    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("**dasd*1.n*dm**2er*E**","2,er,*,Error Token E",187))
    def test_comment8(self):
        self.assertTrue(TestLexer.checkLexeme("+abc<>xyzb>cv **12mds<>dsd=(*dsd*)*)**","+,abc,<,>,xyzb,>,cv,<EOF>",188))
    def test_comment9(self):
        self.assertTrue(TestLexer.checkLexeme(""" * **""","*,Unterminated Comment",189))
    def test_comment10(self):
        self.assertTrue(TestLexer.checkLexeme("{abc} 1.abc","{,abc,},1.,abc,<EOF>",190))
    
    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{1,2,3}""","""{1,2,3},<EOF>""",191))
    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{{1},{1,2,3}}""","""{{1},{1,2,3}},<EOF>""",192))
    def test_array2(self):
        self.assertTrue(TestLexer.checkLexeme("""{a,b,c}""","""{,a,,,b,,,c,},<EOF>""",193))
    def test_array3(self):
        self.assertTrue(TestLexer.checkLexeme("""{"abc","asd"}""","""{"abc","asd"},<EOF>""",194))
    def test_array4(self):
        self.assertTrue(TestLexer.checkLexeme("""{1 , 2, 3}""","""{1 , 2, 3},<EOF>""",195))
    def test_array5(self):
        self.assertTrue(TestLexer.checkLexeme("""{10.e13, 0.123}""","""{10.e13, 0.123},<EOF>""",196))
    def test_array6(self):
        self.assertTrue(TestLexer.checkLexeme("""{{"abc"},"asd"}""","""{{"abc"},"asd"},<EOF>""",197))
    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""True + False""","""True,+,False,<EOF>""",198))
    def test_boolean2(self):
        self.assertTrue(TestLexer.checkLexeme("""TruE avasd""","""Error Token T""",199))
    def test_boolean3(self):
        self.assertTrue(TestLexer.checkLexeme("""false False""","""false,False,<EOF>""",200))


    def test_lower_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",301))

    def test_lower_upper_id1(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",302))

    def test_if(self):
        self.assertTrue(TestLexer.checkLexeme("Else EndIf ElseIf","Else,EndIf,ElseIf,<EOF>",303))

    def test_illegal_escape_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "a'bc\\"  ""","""Unclosed String: a'""",304))

    def test_array111(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" {   1  ,  2,3  , 4}  ""","""{,3,,,2,,,3,,,4,},<EOF>""",305))
    
    def test_identifier81(self):
        self.assertTrue(TestLexer.checkLexeme("rdad 40oBhenK292aWfTSFLt6","rdad,40,oBhenK292aWfTSFLt6,<EOF>",306))
    def test_identifier91(self):
        self.assertTrue(TestLexer.checkLexeme("vJozdspl3p1iOcRiAI12 dUB 1.NM 2cY2","vJozdspl3p1iOcRiAI12,dUB,3.,Error Token N",307))
    def test_identifier101(self):
        self.assertTrue(TestLexer.checkLexeme("0gChhrlnd8xI1dsxd s dwdski6E","0,gChhrlnd8xI1dsxd,s,dwdski6E,<EOF>",308))


    def test_keyword1111(self):
        self.assertTrue(TestLexer.checkLexeme("01anc mds For c brEaK 21mc continuE km","0,3,anc,mds,For,c,brEaK,21,mc,continuE,km,<EOF>",309))
    def test_keyword2111(self):
        self.assertTrue(TestLexer.checkLexeme("tO doWnto Do if thEn elSE return1","tO,doWnto,Do,if,thEn,elSE,return1,<EOF>",310))
    def test_keyword3111(self):
        self.assertTrue(TestLexer.checkLexeme("reTuRn whILe beGin eND function o","reTuRn,whILe,beGin,eND,function,o,<EOF>",311))
    def test_keyword4111(self):
        self.assertTrue(TestLexer.checkLexeme("pROCEDURE TRUe 1.12VAR45 ARRay OF 12REAL","pROCEDURE,Error Token T",312))
    def test_keyword5111(self):
        self.assertTrue(TestLexer.checkLexeme("BOOLEAN int 1.12INTEGER sTRIng not 12and","Error Token B",313))
    def test_keyword6111(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Error Token M",314))
    def test_keyword7111(self):
        self.assertTrue(TestLexer.checkLexeme("If then else diMod 12String true ds false","If,then,else,diMod,32,Error Token S",315))
    def test_keyword8111(self):
        self.assertTrue(TestLexer.checkLexeme("anD then elsediMod doWnTO.1trueds false","anD,then,elsediMod,doWnTO,.,3,trueds,false,<EOF>",316))
    def test_keyword9111(self):
        self.assertTrue(TestLexer.checkLexeme("anD thadenelsediMod doWnTO.1truedsfalse BOOLEAN float 1.12INTEGER sTRIng noT d15s0and","anD,thadenelsediMod,doWnTO,.,3,truedsfalse,Error Token B",319))
    def test_keyword10111(self):
        self.assertTrue(TestLexer.checkLexeme("12while int 1.12 INTEGER oR 12function","12,while,int,3.12,Error Token I",317))

    def test_operator1111(self):
        self.assertTrue(TestLexer.checkLexeme("ddsls<l>02>=d1s<=123","ddsls,<,l,>,0,2,>=,d1s,<=,323,<EOF>",318))
    def test_operator2111(self):
        self.assertTrue(TestLexer.checkLexeme("dlsd+1ds-*dmdsa/<>mdks","dlsd,+,3,ds,-,*,dmdsa,Error Token /",319))
    def test_operator3111(self):
        self.assertTrue(TestLexer.checkLexeme("lsddl<>=1<>=112>=<=d1","lsddl,<,>=,3,<,>=,312,>=,<=,d1,<EOF>",320))
    def test_operator4111(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eend<>=Edasdndm<=>erE","13,ek3,<,9,e,=,9,eend,<,>=,Error Token E",321))
    def test_operator5111(self):
        self.assertTrue(TestLexer.checkLexeme("djeiwjd1A<=>12>=<=d","djeiwjd1A,<=,>,32,>=,<=,d,<EOF>",322))
    def test_operator6111(self):
        self.assertTrue(TestLexer.checkLexeme("<-mod>=not+mod+and+not","<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>",323))
    def test_operator7111(self):
        self.assertTrue(TestLexer.checkLexeme("*and<=>mod</<=","*,and,<=,>,mod,<,Error Token /",324))
    def test_operator8111(self):
        self.assertTrue(TestLexer.checkLexeme("=or<=<><>=-<=>","=,or,<=,<,>,<,>=,-,<=,>,<EOF>",325))
    def test_operator9111(self):
        self.assertTrue(TestLexer.checkLexeme("not<>=and>=mod<=-and","not,<,>=,and,>=,mod,<=,-,and,<EOF>",326))
    def test_operator10111(self):
        self.assertTrue(TestLexer.checkLexeme("mod<=<===mod/<=<","mod,<=,<=,==,mod,Error Token /",327))


    def test_illegal_escape111(self):
        self.assertTrue(TestLexer.checkLexeme("\"bac\\ma\"","Illegal Escape In String: bac\\m",328))
    def test_illegal_escape211(self):
        self.assertTrue(TestLexer.checkLexeme("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",329))
    def test_illegal_escape311(self):
        self.assertTrue(TestLexer.checkLexeme("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",330))
    def test_illegal_escape411(self):
        self.assertTrue(TestLexer.checkLexeme("\"ado\\mado\"","Illegal Escape In String: ado\\m",331))
    def test_illegal_escape511(self):
        self.assertTrue(TestLexer.checkLexeme("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\\k",332))
    def test_illegal_escape6111(self):
        self.assertTrue(TestLexer.checkLexeme("\"aa\wb\"","Illegal Escape In String: aa\\w",333))
    def test_illegal_escape711(self):
        self.assertTrue(TestLexer.checkLexeme("ba+12+\"na\"\"md+1.2-468\lb","ba,+,32,+,na,Illegal Escape In String: md+1.2-468\\l",334))
    def test_illegal_escape811(self):
        self.assertTrue(TestLexer.checkLexeme("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",335))
    def test_illegal_escape911(self):
        self.assertTrue(TestLexer.checkLexeme("**nac**+1.1 \"ba\\qm\f\"","+,3.1,Illegal Escape In String: ba\\q",336))
    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.checkLexeme("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",337))

    def test_unclose_String1111(self):
        self.assertTrue(TestLexer.checkLexeme("\"bacxyc","Unclosed String: bacxyc",338))
    def test_unclose_String2111(self):
        self.assertTrue(TestLexer.checkLexeme("NmkobYn{!}+I1+\"`YS2h.J(","Error Token N",339))
    def test_unclose_String3111(self):
        self.assertTrue(TestLexer.checkLexeme("\"acnv \" \"abc","acnv ,Unclosed String: abc",340))
    
    def test_unclose_String511(self):
        self.assertTrue(TestLexer.checkLexeme("a+11.2+\"mam.123\" 12 \"%^&","a,+,31.2,+,mam.123,32,Unclosed String: %^&",341))
    def test_unclose_String611(self):
        self.assertTrue(TestLexer.checkLexeme("38n\"[#Ffs?0ED\"0.\"T`#!7n","38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n",342))
    def test_unclose_String711(self):
        self.assertTrue(TestLexer.checkLexeme("\".Hub`22Y\"<{;}\"Y`=DxXhZKh",".Hub`22Y,<,{,;,},Unclosed String: Y`=DxXhZKh",343))
    def test_unclose_String811(self):
        self.assertTrue(TestLexer.checkLexeme("\"ULxM*`~.~+C_DISD2","Unclosed String: ULxM*`~.~+C_DISD2",344))
    def test_unclose_String911(self):
        self.assertTrue(TestLexer.checkLexeme("{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1","{,Error Token S",345))

    def test_integer_real11(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5","12.e5,<EOF>",346))
    def test_integer_real21(self):
        self.assertTrue(TestLexer.checkLexeme("01","0,1,<EOF>",347))
    def test_integer_real31(self):
        #TODO: fix -42
        self.assertTrue(TestLexer.checkLexeme("Var x0.12e51.2","Var,x0,.,32e51,.,2,<EOF>",348))
    def test_integer_real41(self):
        self.assertTrue(TestLexer.checkLexeme(".",".,<EOF>",349))
    def test_integer_real51(self):
        #TODO:  fix -15
        self.assertTrue(TestLexer.checkLexeme("e--12 e12 E-15 99e 1 1. 1","e,-,-,32,e12,Error Token E",350))
    def test_integer_real61(self):
        self.assertTrue(TestLexer.checkLexeme("e-12.1 11.e11 12..12 2. .2 11e11 .1e-3","e,-,32.1,31.e11,32.,.,32,2.,.,2,31e11,.,3e-3,<EOF>",351))
    def test_integer_real71(self):
        self.assertTrue(TestLexer.checkLexeme("12.e0 -101 11.E 11.1e2","12.e0,-,301,31.,Error Token E",352))


    def test_comment1111(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0 -101** 11.e 11.1e2","11.,e,31.1e2,<EOF>",353))
    def test_comment2111(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0} -101** 11.1e2","11.1e2,<EOF>",354))
    def test_comment3111(self):
        self.assertTrue(TestLexer.checkLexeme("{abc} 1.abc","{,abc,},3.,abc,<EOF>",355))
    def test_comment4111(self):
        self.assertTrue(TestLexer.checkLexeme("**1.e0 - 101** {11.E} //22.12\\n","{,31.,Error Token E",356))
    def test_comment5111(self):
        #TODO: Fix reallit , intlit
        self.assertTrue(TestLexer.checkLexeme("**12.e0\\nabc -101","Unterminated Comment",357))
    def test_comment6111(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eendE//dasd1.ndm<>d1.02erE","13,ek3,<,9,e,=,9,eendE,Error Token /",358))
    def test_comment7111(self):
        self.assertTrue(TestLexer.checkLexeme("//dasd1.ndm\\n<>d1.02erE","Error Token /",360))
    def test_comment8111(self):
        self.assertTrue(TestLexer.checkLexeme("{ +abc<>xyzb>cv } **12mds<>dsd=(*dsd*)*)**","{,+,abc,<,>,xyzb,>,cv,},<EOF>",361))
    def test_comment9111(self):
        self.assertTrue(TestLexer.checkLexeme(""" * **""","*,Unterminated Comment",362))
    def test_comment10111(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",363))
    def test_comment11(self):
        self.assertTrue(TestLexer.checkLexeme("***** \"\"\"","*,Unclosed String: ",364))

    def test_comment12(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",365))
    def test_comment13(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",366))

###################################################
    #   STRING
    def test_01_valid_string(self):
        """test valid string"""
        input = \
"""" This is a test !@#$%^^&*()?/|"
" 1234567890 \\' ASD" abc 
"KJFLDSK '" \\f asdasd "
"\\b\\f\\r\\n\\t\\'\\\\"
 """
        output = \
""" This is a test !@#$%^^&*()?/|, 1234567890 \\' ASD,abc,KJFLDSK '" \\f asdasd ,\\b\\f\\r\\n\\t\\'\\\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,367))

    def test_03_string_contains_illegal_escape_1(self):
        """test string which contains illegal escape: quote"""
        input = """" This is a test '" asdsadasd ' \\f asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,368))

    def test_04_string_contains_illegal_escape_2(self):
        """test string which contains illegal escape: unidentified backslash"""
        input = """" This is a test '" asdsadasd \\h asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,369))

    def test_05_string_contains_illegal_escape_3(self):
        """test string which contains illegal escape: lone backslash"""
        input = """" This is a test '" asdsadasd \\ asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\ """
        self.assertTrue(TestLexer.checkLexeme(input,output,370))

    def test_06_string_contains_newline(self):
        """test string which contains newline character"""
        input = """" This is a test '" asdsa\ndasd \\ asdasd " """
        output = """Unclosed String:  This is a test '" asdsa"""
        self.assertTrue(TestLexer.checkLexeme(input,output,371))

    def test_07_empty_string(self):
        """test empty string"""
        input = """"" """
        output = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,372))

    ###################################################
    #   COMMENT BLOCK
    def test_11_valid_block_comment(self):
        """test valid block comment"""
        self.assertTrue(TestLexer.checkLexeme("***dsa?dkjs\nah**abc**dkj!* *@#!@#%^^*%%&**","abc,<EOF>",373))

    def test_12_incomplete_block_comment(self):
        """test incomplete block comment"""
        self.assertTrue(TestLexer.checkLexeme("**dsadkjs\nahdkj!* *@#!@#%^^*\%\%&*","Unterminated Comment",374))


    ###################################################
    # IDENTIFIER
    def test_21_lower_id(self):
        """test valid lower identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",375))

    def test_22_lower_upper_id(self):
        """test valid lower uppercase id"""
        self.assertTrue(TestLexer.checkLexeme("vaRiab","vaRiab,<EOF>",376))

    def test_23_lower_upper_digit_id(self):
        """test valid lower uppercase digit id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng123","s0m3Th1ng123,<EOF>",377))

    def test_24_lower_upper_digit_underscore_id(self):
        """test valid lower uppercase digit underscore id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng___123_Som3THiN6","s0m3Th1ng___123_Som3THiN6,<EOF>",378))

    def test_25_wrong_token(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("ab?cde","ab,Error Token ?",379))

    def test_26_wrong_first_letter_upper_id(self):
        """test wrong id first upper letter of id"""
        self.assertTrue(TestLexer.checkLexeme("Wrong","Error Token W",380))
                      
    def test_27_wrong_first_letter_number(self):
        """test wrong id first number digit of id"""
        self.assertTrue(TestLexer.checkLexeme("9reat","9,reat,<EOF>",381))

    def test_28_wrong_first_letter_number(self):
        """test wrong id first letter underscore of id"""
        self.assertTrue(TestLexer.checkLexeme("_wrong","Error Token _",382))


    ###################################################
    #   INTLIT
    def test_31_valid_int_dec(self):
        """test valid decimal integer"""
        self.assertTrue(TestLexer.checkLexeme("123 0","123,0,<EOF>",383))

    def test_32_valid_int_hex(self):
        """test valid hex integer"""
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF12 0X100","0xABCDEF12,0X100,<EOF>",384))

    def test_33_valid_int_oct(self):
        """test valid oct integer"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O777","0o123,0O777,<EOF>",385))

    def test_34_invalid_int_dec_extra_0(self):
        """test invalid decimal integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0123","0,323,<EOF>",386))

    def test_35_invalid_int_hex_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0x0123","0,x0123,<EOF>",387))

    def test_36_invalid_int_oct_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0o0123","0,o0123,<EOF>",388))

    def test_37_invalid_int_prefix(self):
        """test invalid integer with wrong prefix"""
        self.assertTrue(TestLexer.checkLexeme("0a123","0,a123,<EOF>",389))

    def test_38_invalid_int_hex_letter(self):
        """test invalid hex integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0X123abc","0X123,abc,<EOF>",390))

    def test_39_invalid_int_oct_letter(self):
        """test invalid hex integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0o678","0o67,8,<EOF>",391))


    ###################################################
    #   FLOATLIT and BOOL
    def test_41_valid_float(self):
        """test valid float"""
        input = """12.0e3 12e3 12.e5 12.0e3 12000. 120000E-1"""
        output = """12.0e3,32e3,32.e5,32.0e3,32000.,320000E-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,392))

    def test_42_float_with_addition_0(self):
        """test float"""
        input = """00123.123"""
        output = """0,0,323.123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,393))

    def test_43_float_with_exp_missing_exp_number(self):
        """test float"""
        input = """123e"""
        output = """123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,394))

    def test_44_float_with_both_missing_exp_number(self):
        """test float"""
        input = """123.123e"""
        output = """123.123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,395))

    def test_45_float_dec_without_int_part(self):
        """test float"""
        input = """.123"""
        output = """.,323,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,396))

    def test_46_float_exp_without_int_part(self):
        input = """E123"""
        output = """Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,397))

    def test_47_valid_bool(self):
        """test valid bool"""
        input = """TrueFalse"""
        output = """True,False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,398))

    ###################################################
    #Various func test
    def test_51_varitest(self):
        input = \
"""Function: abc
    Body:
        s = "abc
    Endbody."""
        expect = "Function,:,abc,Body,:,s,=,Unclosed String: abc"
        self.assertTrue(TestLexer.checkLexeme(input, expect,399))

        
    def test_unclose_String411(self):
        self.assertTrue(TestLexer.checkLexeme("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,{,abc,},323,Unclosed String: abc",400))