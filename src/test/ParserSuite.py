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
            Else b=0;
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
        self.assertTrue(TestParser.checkParser(input,expect,220))

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
        """ test empty parameter function """
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
        """ test empty parameter function """
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
        """ test empty parameter function """
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
    
    def test34(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test35(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,235))