import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_if(self):
        self.assertTrue(TestLexer.checkLexeme("Else EndIf ElseIf","Else,EndIf,ElseIf,<EOF>",104))

    def test_illegal_escape_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "a'bc\\"  ""","""Unclosed String: a'""",105))

    def test_array(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" {   1  ,  2,3  , 4}  ""","""{,1,,,2,,,3,,,4,},<EOF>""",106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("rdad 40oBhenK292aWfTSFLt6","rdad,40,oBhenK292aWfTSFLt6,<EOF>",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("vJozdspl3p1iOcRiAI12 dUB 1.NM 2cY2","vJozdspl3p1iOcRiAI12,dUB,1.,Error Token N",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("0gChhrlnd8xI1dsxd s dwdski6E","0,gChhrlnd8xI1dsxd,s,dwdski6E,<EOF>",110))


    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("01anc mds For c brEaK 21mc continuE km","0,1,anc,mds,For,c,brEaK,21,mc,continuE,km,<EOF>",111))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("tO doWnto Do if thEn elSE return1","tO,doWnto,Do,if,thEn,elSE,return1,<EOF>",112))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("reTuRn whILe beGin eND function o","reTuRn,whILe,beGin,eND,function,o,<EOF>",113))
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("pROCEDURE TRUe 1.12VAR45 ARRay OF 12REAL","pROCEDURE,Error Token T",114))
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("BOOLEAN int 1.12INTEGER sTRIng not 12and","Error Token B",115))
    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Error Token M",116))
    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("If then else diMod 12String true ds false","If,then,else,diMod,12,Error Token S",117))
    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("anD then elsediMod doWnTO.1trueds false","anD,then,elsediMod,doWnTO,.,1,trueds,false,<EOF>",118))
    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("anD thadenelsediMod doWnTO.1truedsfalse BOOLEAN float 1.12INTEGER sTRIng noT d15s0and","anD,thadenelsediMod,doWnTO,.,1,truedsfalse,Error Token B",119))
    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("12while int 1.12 INTEGER oR 12function","12,while,int,1.12,Error Token I",120))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",121))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("ddsls<l>02>=d1s<=123","ddsls,<,l,>,0,2,>=,d1s,<=,123,<EOF>",122))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("dlsd+1ds-*dmdsa/<>mdks","dlsd,+,1,ds,-,*,dmdsa,Error Token /",123))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("lsddl<>=1<>=112>=<=d1","lsddl,<,>=,1,<,>=,112,>=,<=,d1,<EOF>",124))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eend<>=Edasdndm<=>erE","13,ek3,<,9,e,=,9,eend,<,>=,Error Token E",125))
    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("djeiwjd1A<=>12>=<=d","djeiwjd1A,<=,>,12,>=,<=,d,<EOF>",126))
    def test_operator6(self):
        self.assertTrue(TestLexer.checkLexeme("<-mod>=not+mod+and+not","<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>",127))
    def test_operator7(self):
        self.assertTrue(TestLexer.checkLexeme("*and<=>mod</<=","*,and,<=,>,mod,<,Error Token /",128))
    def test_operator8(self):
        self.assertTrue(TestLexer.checkLexeme("=or<=<><>=-<=>","=,or,<=,<,>,<,>=,-,<=,>,<EOF>",129))
    def test_operator9(self):
        self.assertTrue(TestLexer.checkLexeme("not<>=and>=mod<=-and","not,<,>=,and,>=,mod,<=,-,and,<EOF>",130))
    def test_operator10(self):
        self.assertTrue(TestLexer.checkLexeme("mod<=<===mod/<=<","mod,<=,<=,==,mod,Error Token /",131))


    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bac\\ma\"","Illegal Escape In String: bac\\m",132))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",133))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",134))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme("\"ado\\mado\"","Illegal Escape In String: ado\\m",135))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\\k",136))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme("\"aa\wb\"","Illegal Escape In String: aa\\w",137))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\\l",138))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",139))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme("**nac**+1.1 \"ba\\qm\f\"","+,1.1,Illegal Escape In String: ba\\q",140))
    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.checkLexeme("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",141))

    def test_unclose_String1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bacxyc","Unclosed String: bacxyc",142))
    def test_unclose_String2(self):
        self.assertTrue(TestLexer.checkLexeme("NmkobYn{!}+I1+\"`YS2h.J(","Error Token N",143))
    def test_unclose_String3(self):
        self.assertTrue(TestLexer.checkLexeme("\"acnv \" \"abc","acnv ,Unclosed String: abc",144))
    
    # def test_unclose_String4(self):
    #     self.assertTrue(TestLexer.checkLexeme("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,{,abc,},123,Unclosed String: abc",154))
    def test_unclose_String5(self):
        self.assertTrue(TestLexer.checkLexeme("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",145))
    def test_unclose_String6(self):
        self.assertTrue(TestLexer.checkLexeme("38n\"[#Ffs?0ED\"0.\"T`#!7n","38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n",146))
    def test_unclose_String7(self):
        self.assertTrue(TestLexer.checkLexeme("\".Hub`22Y\"<{;}\"Y`=DxXhZKh",".Hub`22Y,<,{,;,},Unclosed String: Y`=DxXhZKh",147))
    def test_unclose_String8(self):
        self.assertTrue(TestLexer.checkLexeme("\"ULxM*`~.~+C_DISD2","Unclosed String: ULxM*`~.~+C_DISD2",148))
    def test_unclose_String9(self):
        self.assertTrue(TestLexer.checkLexeme("{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1","{,Error Token S",149))

    def test_integer_real1(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5","12.e5,<EOF>",150))
    def test_integer_real2(self):
        self.assertTrue(TestLexer.checkLexeme("01","0,1,<EOF>",151))
    def test_integer_real3(self):
        #TODO: fix -42
        self.assertTrue(TestLexer.checkLexeme("Var x0.12e51.2","Var,x0,.,12e51,.,2,<EOF>",152))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.checkLexeme(".",".,<EOF>",153))
    def test_integer_real5(self):
        #TODO:  fix -15
        self.assertTrue(TestLexer.checkLexeme("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,Error Token E",154))
    def test_integer_real6(self):
        self.assertTrue(TestLexer.checkLexeme("e-12.1 11.e11 12..12 2. .2 11e11 .1e-3","e,-,12.1,11.e11,12.,.,12,2.,.,2,11e11,.,1e-3,<EOF>",155))
    def test_integer_real7(self):
        self.assertTrue(TestLexer.checkLexeme("12.e0 -101 11.E 11.1e2","12.e0,-,101,11.,Error Token E",156))


    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0 -101** 11.e 11.1e2","11.,e,11.1e2,<EOF>",157))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0} -101** 11.1e2","11.1e2,<EOF>",158))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("{abc} 1.abc","{,abc,},1.,abc,<EOF>",159))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("**1.e0 - 101** {11.E} //22.12\\n","{,11.,Error Token E",160))
    def test_comment5(self):
        #TODO: Fix reallit , intlit
        self.assertTrue(TestLexer.checkLexeme("**12.e0\\nabc -101","Unterminated Comment",161))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eendE//dasd1.ndm<>d1.02erE","13,ek3,<,9,e,=,9,eendE,Error Token /",162))
    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("//dasd1.ndm\\n<>d1.02erE","Error Token /",163))
    def test_comment8(self):
        self.assertTrue(TestLexer.checkLexeme("{ +abc<>xyzb>cv } **12mds<>dsd=(*dsd*)*)**","{,+,abc,<,>,xyzb,>,cv,},<EOF>",164))
    def test_comment9(self):
        self.assertTrue(TestLexer.checkLexeme(""" * **""","*,Unterminated Comment",165))
    def test_comment10(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",166))
    def test_comment11(self):
        self.assertTrue(TestLexer.checkLexeme("***** \"\"\"","*,Unclosed String: ",167))

    def test_comment12(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",168))
    def test_comment13(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","<EOF>",169))

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
        self.assertTrue(TestLexer.checkLexeme(input,output,170))

    def test_03_string_contains_illegal_escape_1(self):
        """test string which contains illegal escape: quote"""
        input = """" This is a test '" asdsadasd ' \\f asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,171))

    def test_04_string_contains_illegal_escape_2(self):
        """test string which contains illegal escape: unidentified backslash"""
        input = """" This is a test '" asdsadasd \\h asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,172))

    def test_05_string_contains_illegal_escape_3(self):
        """test string which contains illegal escape: lone backslash"""
        input = """" This is a test '" asdsadasd \\ asdasd " """
        output = """Illegal Escape In String:  This is a test '" asdsadasd \\ """
        self.assertTrue(TestLexer.checkLexeme(input,output,173))

    def test_06_string_contains_newline(self):
        """test string which contains newline character"""
        input = """" This is a test '" asdsa\ndasd \\ asdasd " """
        output = """Unclosed String:  This is a test '" asdsa"""
        self.assertTrue(TestLexer.checkLexeme(input,output,174))

    def test_07_empty_string(self):
        """test empty string"""
        input = """"" """
        output = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,175))

    ###################################################
    #   COMMENT BLOCK
    def test_11_valid_block_comment(self):
        """test valid block comment"""
        self.assertTrue(TestLexer.checkLexeme("***dsa?dkjs\nah**abc**dkj!* *@#!@#%^^*%%&**","abc,<EOF>",176))

    def test_12_incomplete_block_comment(self):
        """test incomplete block comment"""
        self.assertTrue(TestLexer.checkLexeme("**dsadkjs\nahdkj!* *@#!@#%^^*\%\%&*","Unterminated Comment",177))


    ###################################################
    # IDENTIFIER
    def test_21_lower_id(self):
        """test valid lower identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",178))

    def test_22_lower_upper_id(self):
        """test valid lower uppercase id"""
        self.assertTrue(TestLexer.checkLexeme("vaRiab","vaRiab,<EOF>",179))

    def test_23_lower_upper_digit_id(self):
        """test valid lower uppercase digit id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng123","s0m3Th1ng123,<EOF>",180))

    def test_24_lower_upper_digit_underscore_id(self):
        """test valid lower uppercase digit underscore id"""
        self.assertTrue(TestLexer.checkLexeme("s0m3Th1ng___123_Som3THiN6","s0m3Th1ng___123_Som3THiN6,<EOF>",181))

    def test_25_wrong_token(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("ab?cde","ab,Error Token ?",182))

    def test_26_wrong_first_letter_upper_id(self):
        """test wrong id first upper letter of id"""
        self.assertTrue(TestLexer.checkLexeme("Wrong","Error Token W",183))
                      
    def test_27_wrong_first_letter_number(self):
        """test wrong id first number digit of id"""
        self.assertTrue(TestLexer.checkLexeme("9reat","9,reat,<EOF>",184))

    def test_28_wrong_first_letter_number(self):
        """test wrong id first letter underscore of id"""
        self.assertTrue(TestLexer.checkLexeme("_wrong","Error Token _",185))


    ###################################################
    #   INTLIT
    def test_31_valid_int_dec(self):
        """test valid decimal integer"""
        self.assertTrue(TestLexer.checkLexeme("123 0","123,0,<EOF>",186))

    def test_32_valid_int_hex(self):
        """test valid hex integer"""
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF12 0X100","0xABCDEF12,0X100,<EOF>",187))

    def test_33_valid_int_oct(self):
        """test valid oct integer"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O777","0o123,0O777,<EOF>",188))

    def test_34_invalid_int_dec_extra_0(self):
        """test invalid decimal integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0123","0,123,<EOF>",189))

    def test_35_invalid_int_hex_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0x0123","0,x0123,<EOF>",190))

    def test_36_invalid_int_oct_extra_0(self):
        """test invalid hex integer with extra 0"""
        self.assertTrue(TestLexer.checkLexeme("0o0123","0,o0123,<EOF>",191))

    def test_37_invalid_int_prefix(self):
        """test invalid integer with wrong prefix"""
        self.assertTrue(TestLexer.checkLexeme("0a123","0,a123,<EOF>",192))

    def test_38_invalid_int_hex_letter(self):
        """test invalid hex integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0X123abc","0X123,abc,<EOF>",193))

    def test_39_invalid_int_oct_letter(self):
        """test invalid hex integer with wrong letter"""
        self.assertTrue(TestLexer.checkLexeme("0o678","0o67,8,<EOF>",194))


    ###################################################
    #   FLOATLIT and BOOL
    def test_41_valid_float(self):
        """test valid float"""
        input = """12.0e3 12e3 12.e5 12.0e3 12000. 120000E-1"""
        output = """12.0e3,12e3,12.e5,12.0e3,12000.,120000E-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,195))

    def test_42_float_with_addition_0(self):
        """test float"""
        input = """00123.123"""
        output = """0,0,123.123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,196))

    def test_43_float_with_exp_missing_exp_number(self):
        """test float"""
        input = """123e"""
        output = """123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,197))

    def test_44_float_with_both_missing_exp_number(self):
        """test float"""
        input = """123.123e"""
        output = """123.123,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,198))

    def test_45_float_dec_without_int_part(self):
        """test float"""
        input = """.123"""
        output = """.,123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,199))

    def test_46_float_exp_without_int_part(self):
        """test float"""
        input = """E123"""
        output = """Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,301))

    def test_47_valid_bool(self):
        """test valid bool"""
        input = """TrueFalse"""
        output = """True,False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,302))

    ###################################################
    #Various func test
    def test_51_varitest(self):
        input = \
"""Function: abc
    Body:
        s = "abc
    Endbody."""
        expect = "Function,:,abc,Body,:,s,=,Unclosed String: abc"
        self.assertTrue(TestLexer.checkLexeme(input, expect,303))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",304))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",305))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,306))

    