import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Created automatically"""
        input = r"""Var: x[123] = {1,2,3};""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1))
    def test_2(self):
        """Created automatically"""
        input = r"""Var: x[0] = {};""" 
        output = r"""Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,2))
    def test_3(self):
        """Created automatically"""
        input = r"""Var: x[0] = {{}};
Var: y = {"asd", 0, {123, 12.3}, 1.23};""" 
        output = r"""Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,3))
    def test_4(self):
        """Created automatically"""
        input = r"""Var: x = {{1,2,3}, **asdkhasd!@#!@$!@** "abc"};""" 
        output = r"""Error on line 1 col 9: {"""
        self.assertTrue(TestParser.checkParser(input,expect,4))
    def test_5(self):
        """Created automatically"""
        input = r"""Var: x[0] = {abc};""" 
        output = r"""Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,5))
    def test_6(self):
        """Created automatically"""
        input = r"""Var: x[0] = {1,2,3 ;""" 
        output = r"""Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,6))
    def test_7(self):
        """Created automatically"""
        input = r"""Var: x[0] = {   1,  2,3 
        };""" 
        output = r"""Error on line 1 col 12: {"""
        self.assertTrue(TestParser.checkParser(input,expect,7))
    def test_8(self):
        """Created automatically"""
        input = r"""Var: x;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,8))
    def test_9(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = a < 4;
            c = !a; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,9))
    def test_10(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            a = 3 + 5 ; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,10))
    def test_11(self):
        """Created automatically"""
        input = r"""Var  :       anyid;
Var:a = 123.321e-123;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,11))
    def test_12(self):
        """Created automatically"""
        input = r""" Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; EndIf.
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,12))
    def test_13(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            While True print("Hello World"); EndWhile.
        EndBody.""" 
        output = r"""Error on line 4 col 12: While"""
        self.assertTrue(TestParser.checkParser(input,expect,13))
    def test_14(self):
        """Created automatically"""
        input = r"""Var: a = {1,2,3}, b[2][3] = 5, c[2] = {{1,3},{,5,7}}""" 
        output = r"""Error on line 1 col 38: {"""
        self.assertTrue(TestParser.checkParser(input,expect,14))
    def test_15(self):
        """Created automatically"""
        input = r"""Var  :       anyid, moreid,  mUchm0r31d;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,15))
    def test_16(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            If a==5 Then b = 5;
            ElseIf a==6 Then c=6; 
            EndIf.
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,16))
    def test_17(self):
        """Created automatically"""
        input = r"""Var:someid=True;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,17))
    def test_18(self):
        """Created automatically"""
        input = r""" Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; 
            Else c=5; 
            EndIf. 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,18))
    def test_19(self):
        """Created automatically"""
        input = r"""Var:someid, mor3Id= "SomeSTRING",   some_more_id,muchmoreID = 123.321e-2;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,19))
    def test_20(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,20))
    def test_21(self):
        """Created automatically"""
        input = r"""Var :         someid, mor3Id
        = "SomeSTRING"
        ,
    some_more_id,muchmoreID = {"str","s"},  lots_m0rE_1D = False;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,21))
    def test_22(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            foo(2 + x, 4. \. y); 
            goo ();
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,22))
    def test_23(self):
        """Created automatically"""
        input = r"""Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,23))
    def test_24(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
        x = 10; 
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,24))
    def test_25(self):
        """Created automatically"""
        input = r"""Var: someid[] = {"w","h","oops"};""" 
        output = r"""Error on line 1 col 11: ["""
        self.assertTrue(TestParser.checkParser(input,expect,25))
    def test_26(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
        
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,26))
    def test_27(self):
        """Created automatically"""
        input = r"""Var: someid[1.23E-2] = {"w","h","oops"};""" 
        output = r"""Error on line 1 col 11: ["""
        self.assertTrue(TestParser.checkParser(input,expect,27))
    def test_28(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n, a[10]
        Body: 
        
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,28))
    def test_29(self):
        """Created automatically"""
        input = r"""vAr: someid;""" 
        output = r"""Error on line 1 col 0: vAr"""
        self.assertTrue(TestParser.checkParser(input,expect,29))
    def test_30(self):
        """Created automatically"""
        input = r"""Var: ;""" 
        output = r"""Error on line 1 col 5: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,30))
    def test_31(self):
        """Created automatically"""
        input = r"""Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5)
        a[i] = b +. 1.0;
        i = i + 1;
        EndWhile.
        EndBody.""" 
        output = r"""Error on line 5 col 8: While"""
        self.assertTrue(TestParser.checkParser(input,expect,31))
    def test_32(self):
        """Created automatically"""
        input = r"""Var someid;""" 
        output = r"""Error on line 1 col 4: someid"""
        self.assertTrue(TestParser.checkParser(input,expect,32))
    def test_33(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,33))
    def test_34(self):
        """Created automatically"""
        input = r"""Var: ;""" 
        output = r"""Error on line 1 col 5: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,34))
    def test_35(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x = 10;
            fact (x);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,35))
    def test_36(self):
        """Created automatically"""
        input = r"""Var: someid = 123""" 
        output = r"""Error on line 1 col 17: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,36))
    def test_37(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,37))
    def test_38(self):
        """Created automatically"""
        input = r"""Var: someid = 1+2+3;""" 
        output = r"""Error on line 1 col 15: +"""
        self.assertTrue(TestParser.checkParser(input,expect,38))
    def test_39(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,39))
    def test_40(self):
        """Created automatically"""
        input = r"""Var **some COMMENT**: ****someid = 3
        **more more**;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,40))
    def test_41(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,41))
    def test_42(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Do
                x= x+1;
            While x>1 
            EndDo.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,42))
    def test_43(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,43))
    def test_44(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,44))
    def test_45(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,45))
    def test_46(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            c = [a+3];
        EndBody.
        """ 
        output = r"""Error on line 5 col 16: ["""
        self.assertTrue(TestParser.checkParser(input,expect,46))
    def test_47(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: ** Xin chao**
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,47))
    def test_48(self):
        """Created automatically"""
        input = r"""
        Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            Else
                Return True;
            EndIf.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,48))
    def test_49(self):
        """Created automatically"""
        input = r"""Function: foo
    Body:
    EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,49))
    def test_50(self):
        """Created automatically"""
        input = r"""
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[5] = {1,2,3};
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,50))
    def test_51(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: a, b,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,51))
    def test_52(self):
        """Created automatically"""
        input = r"""Function: foo 
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
        output = r"""Error on line 8 col 12: Else"""
        self.assertTrue(TestParser.checkParser(input,expect,52))
    def test_53(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter:
    Body:
    EndBody.""" 
        output = r"""Error on line 3 col 4: Body"""
        self.assertTrue(TestParser.checkParser(input,expect,53))
    def test_54(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            EndIf.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,54))
    def test_55(self):
        """Created automatically"""
        input = r"""Function: foo 
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
        output = r"""Error on line 8 col 12: Else"""
        self.assertTrue(TestParser.checkParser(input,expect,55))
    def test_56(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: a, b = 123,c[123] ,d[123][234][0]  ,e
    Body:
    EndBody.""" 
        output = r"""Error on line 2 col 20: ="""
        self.assertTrue(TestParser.checkParser(input,expect,56))
    def test_57(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,57))
    def test_58(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 5 col 16: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,58))
    def test_59(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: abc;
    Body:
    EndBody.""" 
        output = r"""Error on line 2 col 18: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,59))
    def test_60(self):
        """Created automatically"""
        input = r"""
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody.""" 
        output = r"""Error on line 2 col 24: {"""
        self.assertTrue(TestParser.checkParser(input,expect,60))
    def test_61(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: abc
    Body:
    EndBody""" 
        output = r"""Error on line 4 col 11: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,61))
    def test_62(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody.""" 
        output = r"""Error on line 5 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,62))
    def test_63(self):
        """Created automatically"""
        input = r"""** some comment **
Function: foo ** some more comment **
    Parameter: abc ** MuchM0re comment **
    Body:  ** LOTS of comment !@#$%^^&%&*() **
    EndBody **Here some too**. """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,63))
    def test_64(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 1.0;
                Var: k = 10;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 7 col 16: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,64))
    def test_65(self):
        """Created automatically"""
        input = r"""Function: foo Parameter: abc Body: EndBody. Function: foo Body: EndBody.
Function: goo Parameter: abc Body: EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,65))
    def test_66(self):
        """Created automatically"""
        input = r"""Var: a=False;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,66))
    def test_67(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 6 col 16: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,67))
    def test_68(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = -.a;
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,68))
    def test_69(self):
        """Created automatically"""
        input = r"""Function: foo 
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
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,69))
    def test_70(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,70))
    def test_71(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do

            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,71))
    def test_72(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While i < 5 
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 4 col 12: While"""
        self.assertTrue(TestParser.checkParser(input,expect,72))
    def test_73(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break abc;
                EndIf.
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 6 col 27: abc"""
        self.assertTrue(TestParser.checkParser(input,expect,73))
    def test_74(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue absd;
                EndIf.
            EndWhile.
        EndBody.""" 
        output = r"""Error on line 6 col 30: absd"""
        self.assertTrue(TestParser.checkParser(input,expect,74))
    def test_75(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            fact (x) + 3;
        EndBody.""" 
        output = r"""Error on line 4 col 21: +"""
        self.assertTrue(TestParser.checkParser(input,expect,75))
    def test_76(self):
        """Created automatically"""
        input = r"""Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 
                If n > 10 Then Return x=3;
                EndIf.
                ;
            EndIf.
        EndBody.""" 
        output = r"""Error on line 6 col 16: If"""
        self.assertTrue(TestParser.checkParser(input,expect,76))
    def test_77(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v;
            r = 10., v;
        EndBody.""" 
        output = r"""Error on line 5 col 19: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,77))
    def test_78(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 19: =="""
        self.assertTrue(TestParser.checkParser(input,expect,78))
    def test_79(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = !a; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,79))
    def test_80(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (a[i] = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 17: a[i]"""
        self.assertTrue(TestParser.checkParser(input,expect,80))
    def test_81(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 17: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,81))
    def test_82(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, , i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 22: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,82))
    def test_83(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, i != 5,) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 29: )"""
        self.assertTrue(TestParser.checkParser(input,expect,83))
    def test_84(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (,,) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 17: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,84))
    def test_85(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a * 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,85))
    def test_86(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a + 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,86))
    def test_87(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a && b; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,87))
    def test_88(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = a >= 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,88))