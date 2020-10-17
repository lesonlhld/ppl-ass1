import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Created automatically"""
        input = r"""Var: x;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,200))
    def test_201(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_202(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n""" 
        output = r"""Error on line 2 col 20: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_203(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            a = 3 + 5 ; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_204(self):
        """Created automatically"""
        input = r""" Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; EndIf.
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_205(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_206(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_207(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_208(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_209(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
        x = 10; 
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_210(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
        
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_211(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n, a[10]
        Body: 
        
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_212(self):
        """Created automatically"""
        input = r"""Var: ;""" 
        output = r"""Error on line 1 col 5: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_213(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return break;
            EndIf.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_214(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_215(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x = 10;
            fact (x);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_216(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_217(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_218(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_219(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_220(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_223(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            c = [a+3];
        EndBody.
        """ 
        output = r"""Error on line 5 col 16: ["""
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_224(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: ** Xin chao**
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_225(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_226(self):
        """Created automatically"""
        input = r"""
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[5] = {1,2,3};
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_227(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            EndIf.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_228(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_229(self):
        """Created automatically"""
        input = r"""
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_230(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody.""" 
        output = r"""Error on line 5 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_231(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_232(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_233(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = -.a;
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_234(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_235(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_236(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do

            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_237(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_238(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_239(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_240(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            fact (x) + 3;
        EndBody.""" 
        output = r"""Error on line 4 col 21: +"""
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_241(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_242(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v;
            r = 10., v;
        EndBody.""" 
        output = r"""Error on line 5 col 19: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_243(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 19: =="""
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_244(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = !a; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_245(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (a[i] = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 18: ["""
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_246(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 17: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_247(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, , i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 22: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_248(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, i != 5,) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 29: )"""
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_249(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: n 
        Body: 
            For (,,) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Error on line 5 col 17: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_250(self):
        """Created automatically"""
        input = r"""Var: x;
                   Var: a,b,c;
                   Var: a[100];
                """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_251(self):
        """Created automatically"""
        input = r"""Var: a[100];
                   Var: b[10][200], c[9999], e[];
                """ 
        output = r"""Error on line 2 col 47: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_252(self):
        """Created automatically"""
        input = r"""Var: e[5];
                   Var: decArray[987654321], hexArray[0x123456789][0XABCDEF], octArray[0o1234567][0O5731321];
                """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_253(self):
        """Created automatically"""
        input = r""" Function: main
                        Body:
                        Var: a, b, c;
                        a = False;
                        b = True;
                        c = a || b;
                        a = (!(b && c)||!(a && c)||!(a&&b)); 
                        EndBody.
                    """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_254(self):
        """Created automatically"""
        input = r""" Function: main
                    Body:
                        Var: a[5][5][9], b = 1.55, c = -10;
                    EndBody.
                    """ 
        output = r"""Error on line 3 col 55: -"""
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_255(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a * 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_256(self):
        """Created automatically"""
        input = r""" Function: testIfStatement
                        Parameter: x, a, b, c
                        Body:
                            If(x == ((False||True) && (a > b + c))) Then
                                a = b - c;
                            Else
                                a = b + c;
                                x = True;
                            EndIf.
                        EndBody.
                    """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_257(self):
        """Created automatically"""
        input = r"""Function: foo
                        Parameter: x
                        Body:
                            For (i = 1, i <= x*x*x,i + x ) Do
                                writeln(i);
                            EndFor.
                        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_258(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While(1) Do
                While(!x) Do
                    x = True;
                EndWhile.
            EndWhile.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_259(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While((x > a) && (x < b)) Do
                While((x >= b) || (x >= a)) Do
                    While((x > c * b) && (x < b*b)) Do
                        x = x - 1;
                        c = 2 * c;
                        While( !False ) Do
                            a = a * 1;
                        EndWhile.
                    EndWhile.
                EndWhile.
        EndBody.""" 
        output = r"""Error on line 14 col 8: EndBody"""
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_260(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Do
                x = a + b;
                writeln(x);
            While(True || False || True || (a > b))
        EndBody.""" 
        output = r"""Error on line 8 col 8: EndBody"""
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_261(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Do
            While();
            EndDo.
        EndBody.""" 
        output = r"""Error on line 5 col 18: )"""
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_262(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Do
                Do
                    While(b!=4);
                While(a!=3);
                EndDo.
            EndDo.
        EndBody.""" 
        output = r"""Error on line 6 col 31: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_263(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Break;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_264(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Continue;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_265(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            test(a,3*7,y[1],z[2] + 5,"string",True);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_266(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a + 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_267(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Do  
                Return foo(x,y);
            While (True)
            EndDo.
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_268(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a= (a==b)!= c ;
            x= (x =/= y) <. z >.t;
        EndBody.""" 
        output = r"""Error on line 5 col 30: >."""
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_269(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x= (y+3)+. 0.e3 - (z -. -9);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_270(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x= (x*3)*. 0x3E \ (y \. 0.123) % 5;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_271(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body:
            a= -3;
            b= -0x123;
            c= -0o77;
            d= -a;
            c= -foo(x); 
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_272(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x = !(True);
            y = (False || True) && True;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_273(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            x = !(!(!(y) && z) || (x > 3) !(y < 2));
        EndBody.""" 
        output = r"""Error on line 4 col 42: !"""
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_274(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_275(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a= foo(a,b) + goo (x);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_276(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            foo(2.34,"string",-9.2e11);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_277(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c =a && b; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_278(self):
        """Created automatically"""
        input = r"""Function: foo 
            Parameter: n
            Body: 
            Var : a;
            EndBody.

            Function: program1
            Parameter: e
            Body:
            EndBody.

            Function: main
            Body:
            EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_279(self):
        """Created automatically"""
        input = r"""
            Function: main
            Body:
            EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_280(self):
        """Created automatically"""
        input = r"""
        Function: foo 
        Parameter: 
        Body: 
        EndBody.""" 
        output = r"""Error on line 4 col 8: Body"""
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_281(self):
        """Created automatically"""
        input = r"""
            Function: main
            Body:
            EndBody.
            Var:x=10;""" 
        output = r"""Error on line 5 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_282(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[123]= {1,2,3};
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_283(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[12] = { 1 ,2 , 3};
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_284(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[12] = {"abc",123};
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_285(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[123]={};
            b[1]={{{}}};
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_286(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a[12]={{1,2,3},{"abc"},{0.12e3,0X12F,0o456}};
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_287(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            array[12]={a,b,c};
        EndBody.""" 
        output = r"""Error on line 4 col 23: a"""
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_288(self):
        """Created automatically"""
        input = r""" 
        Function: foo 
        Parameter: n 
        Body: 
            c = a >= 5; 
        EndBody.
        """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_289(self):
        """Created automatically"""
        input = r""" """ 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_290(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If (x == y) || (x != y) Then
                x = ((a >=. 2.3e-13) || (x =/= 2e-35));
            EndIf.
            z = (x < 3) && (y > 4);
            a = (x != z);
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_291(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            a =(foo(3) != foo(4))* 0.e2;
        EndBody.""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_292(self):
        """Created automatically"""
        input = r"""Var: x = {{1,2,3}, **Comment here** "abc"};""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_293(self):
        """Created automatically"""
        input = r"""
        Var: x[]=1;
        """ 
        output = r"""Error on line 2 col 15: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_294(self):
        """Created automatically"""
        input = r"""
        Var: x[12.e3]=1;
        """ 
        output = r"""Error on line 2 col 15: 12.e3"""
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_295(self):
        """Created automatically"""
        input = r"""Var:x[1]=1+2;""" 
        output = r"""Error on line 1 col 10: +"""
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_296(self):
        """Created automatically"""
        input = r"""Var **some COMMENT**: ****someid = 3
        **more more**;""" 
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_297(self):
        """Created automatically"""
        input = r""" Function: testfuncallexpression
                    Parameter: a,b,c
                    Body:
                        foo;
                    EndBody.""" 
        output = r"""Error on line 4 col 27: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_298(self):
        """Created automatically"""
        input = r"""Function:
        Parameter: n
        Body: 
        EndBody.""" 
        output = r"""Error on line 2 col 8: Parameter"""
        self.assertTrue(TestParser.checkParser(input,expect,298))