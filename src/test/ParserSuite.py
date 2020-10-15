import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test1(self):
        """Miss variable"""
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test2(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    #Test expression
    def test3(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            c = [a+3];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test4(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = -.a;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test5(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = !a; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test6(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a * 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test7(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a + 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test8(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a && b; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test9(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = a >= 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test10(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = a < 4;
            c = !a; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    #Test statement
    def test11(self):
        """ Test assign statement """
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            a = 3 + 5 ; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test12(self):
        """ Test if statement """
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test13(self):
        """ Test if elseif else statement """
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            If a==5 Then b = 5;
            ElseIf a==6 Then c=6; 
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test14(self):
        """ Test if else statement """
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; 
            Else c=5; 
            EndIf. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test15(self):
        """ For Statement """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test16(self):
        """ For Statement """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            foo(2 + x, 4. \. y); 
            goo ();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test17(self):
        """ test simple function """
        input = """Function: foo 
        Parameter: n 
        Body: 
        x = 10; 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def test18(self):
        """ test empty body function """
        input = """Function: foo 
        Parameter: n 
        Body: 
        
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test19(self):
        """ test empty body, list parameter function """
        input = """Function: foo 
        Parameter: n, a[10]
        Body: 
        
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test21(self):
        """ test return_stmt in function """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test22(self):
        """ test call function """
        input = """Function: foo 
        Parameter: n
        Body: 
            x = 10;
            fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test23(self):
        """ test while function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test24(self):
        """ test index operator function """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test25(self):
        """ test  """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test26(self):
        """ test do while stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                x= x+1;
            While x>1 
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test27(self):
        """ test break stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test28(self):
        """ test conitnue stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test29(self):
        """ test Global variable declaration """
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test30(self):
        """ test comment in function """
        input = """Function: foo 
        Parameter: n
        Body: ** Xin chao**
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test31(self):
        """ test return type of value function """
        input = """
        Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            Else
                Return True;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 23: True"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test32(self):
        """ test var declare function """
        input = """
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[5] = {1,2,3};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    
    def test33(self):
        """ test many else """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test34(self):
        """ test no else """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test35(self):
        """ test assign_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test36(self):
        """ test var declare with function"""
        input = """
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test37(self):
        """ test var not at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody."""
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test38(self):
        """ test var not at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 1.0;
                Var: k = 10;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test39(self):
        """ test var at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test40(self):
        """ test nested if """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    Return 1;
                Else 
                    Return 2;
                EndIf.
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test41(self):
        """ test for_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test42(self):
        """ test multi function """
        input = """Function: foo 
        Parameter: n
        Body: 
        EndBody.
        Function: goo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test42(self):
        """ test null stmt while_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do

            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test43(self):
        """ test miss Do in While_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "Error on line 4 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test44(self):
        """ test error break """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break abc;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 6 col 27: abc"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test45(self):
        """ test error continue """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue absd;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 6 col 30: absd"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test46(self):
        """ test error call_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            fact (x) + 3;
        EndBody."""
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test47(self):
        """ test error return_stmt"""
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 
                If n > 10 Then Return x=3;
                EndIf.
                ;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 16: If"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test48(self):
        """ test var_decl function """
        input = """Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v;
            r = 10., v;
        EndBody."""
        expect = "Error on line 5 col 19: ,"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test49(self):
        """ test error for_stmt """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test50(self):
        """ test error scala-type in for_stmt """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (a[i] = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test51(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test52(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, , i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test53(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, i != 5,) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 29: )"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test54(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (,,) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    
    def test20(self):
        input= """Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5)
        a[i] = b +. 1.0;
        i = i + 1;
        EndWhile.
        EndBody."""
        expect = "Error on line 5 col 8: While"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test3411(self):
        """ test noelse """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test35111(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,257))

######################################################################
    # ARRAY TEST: 7 testcases

    def test01_valid_normal_array(self):
        """Valid normal array"""
        input = """Var: x[123] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test02_empty_array(self):
        """Check empty array"""
        input = """Var: x[0] = {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test03_array_contains_array(self):
        """Check array contains arrays"""
        input = \
"""Var: x[0] = {{}};
Var: y = {"asd", 0, {123, 12.3}, 1.23};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test04_array_contains_comment(self):
        """Check array contains comment"""
        input = """Var: x = {{1,2,3}, **asdkhasd!@#!@$!@** "abc"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test05_array_contains_id(self):
        """Check array contains id"""
        input = """Var: x[0] = {abc};"""
        expect = "Error on line 1 col 13: abc"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test06_unclosed_array(self):
        """Check unclosed array"""
        input = """Var: x[0] = {1,2,3 ;"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test07_array_with_ws(self):
        """Check array with various white space"""
        input = """Var: x[0] = {   1,  2,3 
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))


    ######################################################################
    # VAR DECL TEST: 14 testcases

    def test11_simple_var_decl(self):
        """Check simple var decl"""
        input = \
"""Var  :       anyid;
Var:a = 123.321e-123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test12_multiple_var_decl(self):
        """Check var decl with multiple ids"""
        input = """Var  :       anyid, moreid,  mUchm0r31d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test13_single_var_decl_assign(self):
        """Check single var decl with assignment"""
        input = """Var:someid=True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test14_multiple_var_decl_assign(self):
        """Check multiple var decl, some has assignment"""
        input = """Var:someid, mor3Id= "SomeSTRING",   some_more_id,muchmoreID = 123.321e-2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test15_multiple_var_decl_ws(self):
        """Check multiple var decl, some has assignment with various white spaces"""
        input = """Var :         someid, mor3Id
        = "SomeSTRING"
        ,
    some_more_id,muchmoreID = {"str","s"},  lots_m0rE_1D = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test16_multiple_var_decl_ws_composites(self):
        """Check multiple var decl, add some composite ids"""
        input = """Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test17_composite_var_no_dim(self):
        """Check composite id with no literal in brackets"""
        input = """Var: someid[] = {"w","h","oops"};"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test18_composite_var_wrong_dim(self):
        """Check composite id with wrong literal in dimension"""
        input = """Var: someid[1.23E-2] = {"w","h","oops"};"""
        expect = "Error on line 1 col 12: 1.23E-2"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test19_var_decl_wrong_keyword(self):
        """Check var decl with wrong keyword"""
        input = """vAr: someid;"""
        expect = "Error on line 1 col 0: vAr"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test20_var_decl_missing_comma(self):
        """Check var decl missing comma"""
        input = """Var someid;"""
        expect = "Error on line 1 col 4: someid"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test21_var_decl_no_id(self):
        """Check var decl without id"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test22_var_decl_missing_semi(self):
        """Check var decl missing semicolon"""
        input = """Var: someid = 123"""
        expect = "Error on line 1 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test23_var_decl_assign_exp(self):
        """Check var decl with expression assignment"""
        input = """Var: someid = 1+2+3;"""
        expect = "Error on line 1 col 15: +"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test24_var_decl_comment(self):
        """Check var decl with expression assignment"""
        input = """Var **some COMMENT**: ****someid = 3
        **more more**;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    ######################################################################
    # FUNC DECL TEST: xx testcases

    def test31_simple_func_decl(self):
        """Check simple func decl"""
        input = \
"""Function: foo
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test32_simple_func_decl_param(self):
        """Check simple func decl with some param"""
        input = \
"""Function: foo
    Parameter: a, b,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test33_simple_func_decl_param_no_id(self):
        """Check simple func decl with some param"""
        input = \
"""Function: foo
    Parameter:
    Body:
    EndBody."""
        expect = "Error on line 3 col 4: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test34_simple_func_decl_param_assign(self):
        """Check simple func decl with some params have assignment"""
        input = \
"""Function: foo
    Parameter: a, b = 123,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody."""
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test35_func_param_semi(self):
        """Check simple func decl param has semicolon"""
        input = \
"""Function: foo
    Parameter: abc;
    Body:
    EndBody."""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test36_func_miss_dot(self):
        """Check simple func decl without dot at the end"""
        input = \
"""Function: foo
    Parameter: abc
    Body:
    EndBody"""
        expect = "Error on line 4 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test37_func_with_comment(self):
        """Check simple func decl with comments"""
        input = \
"""** some comment **
Function: foo ** some more comment **
    Parameter: abc ** MuchM0re comment **
    Body:  ** LOTS of comment !@#$%^^&%&*() **
    EndBody **Here some too**. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test38_multiple_func_decl(self):
        """Check multiple func decl"""
        input = """Function: foo Parameter: abc Body: EndBody. Function: foo Body: EndBody.
Function: goo Parameter: abc Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test38_multiple_func_decl1(self):
        """Check multiple func decl"""
        input = """Var: a=False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test1233(self):
        input="""**hihihaha
*hihi
*"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test1233321(self):
        input="""**hihihaha
*hihi
** Hihi"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))