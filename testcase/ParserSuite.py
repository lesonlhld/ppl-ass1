import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    ###########################################################
	# Test variable declare
    def test1(self):
        input = """Var: faji342F__324dADS;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test2(self):
        input = """Var: 
        
        """
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test3(self):
        input = """
        Var:                ;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test4(self):
        input = """ 
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test5(self):
        input = """ 
        Var: decimal[108], hexadecimal[0X5456A][0x205F], octdecimal[0o413215][0O123];
        Var: array[5][13456];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test6(self):
        input = """ 
        Var: dsa[432][0X364][0o95721], b = 20.e5, c = "mot con vit xoe ra 2 \\n cai canh";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test7(self):
        input = """ 
        Var: x = {**comment trong array**{34221}, {"fsd\\h" **cmt**},2};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test8(self):
        input = """ 
        Var **COMMENT**: ****id = 465632
        **dsfhfsdhjnc^#%#@@~!**
    vAr: sss;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test9(self):
        input = """ 
        Var: ppl[20.e5]=56508;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test10(self):
        input = """ 
        Var: nvh[   ]=20052000;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test11(self):
        input = """
            Var: emptyvardecl, arr[]"""
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    ###########################################################
	# Test function declare
    def test11(self):
        input = """ 
        Function: test_lan_1 
        Parameter: global_var
        Body: 
            dayLA1_teNbIen = 25+6-.2.5%3\\100 ; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test12(self):
        input = """ Function: lan2
        Parameter: var
        Body: 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test13(self):
        input = """ 
        Function: **comment chut da**funcinfunc 
        Body: 
            x=20;
            Function: foo 
            Parameter: n
            Body: 
                x=100.0;
            EndBody.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test14(self):
        input = """ Function: nobody
            If x==i Then Break;
            EndIf. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test15(self):
        input = """
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test16(self):
        input = """
        Function: parameter 
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body: 
            a=1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test17(self):
        input = """Function: double__PARAM
        Parameter: n
        Parameter: n
        Body: 
        x = 10; 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test18(self):
        input = """Function: testn


        Parameter: themdauchamphay ;
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test19(self):
        input = """Function: initvalueparam 
        Parameter: n = 20, arr[5]
        Body: 
            Var: r = 10., v;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test20(self):
        input = """Function: foo"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test21(self):
        input = """Function: varinstmtlist
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                i = i + 1;
            While i <= 10 
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    ###########################################################
	# Test comment
    def test22(self):
        input = """**sau day la 1 ham \\\\ main\\n**
Function:**het y r** main ** test ne;**
**cmt tum lum ~!$()>?:{}**    Body: a=**235**865;
    EndBody **Body**."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test23(self):
        input = """** This is a single-line comment. **
** This is a
* multi-line
* comment.
**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test24(self):
        input = """**Function: main 
        Parameter: x, a
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody.**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test25(self):
        input = """Function: multivscmt 
        Body: 
            Var: a = 100, b;
            b = (6\\2)*8*b* **b**b*b;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test26(self):
        input = """Var **test comment**: **bien = "STRING"**
        ****fu={0X74365,0o86523**cmt**}****;****"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    ###########################################################
	# Test keyword
    def test27(self):
        input = """Function: iDenTIfier_SS__ 
        Parameter: varrr
        Body: 
            **Do
                x= x+1;
            While x>1 
            EndDo.
            **
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test28(self):
        input = """Function: keyword 
        Body: 
            Iff=1 Then Return;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test29(self):
        input = """Function: keyword_fail 
        parameter: k
        body:
        endbody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test30(self):
        input = """Function:mainParameter:xBody:If!aThenbElseWhile(x>0)Thena++EndWhileEndIfEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test31(self):
        input = """Function: special~!@#$%^& 
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    ###########################################################
	# Test operators
    def test32(self):
        input = """Function: hellomoinguoi 
        Parameter: n
        Body: 
            If n <=. 1.2E-4 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test33(self):
        input = """Function: testop 
        Body: 
            If ((k==1)&&(i!=0))||(k==5)||!j Then
                f=f%3;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test34(self):
        input = """Function: calculate 
        Parameter: n
        Body: 
            Var: a = {1,2,3}, b[2][3] = 5, c[2] = {{1,3},{,5,7}};
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test35(self):
        input = """Function: test_precedence___ 
        Parameter: n
        Body: 
            x = !(!(!a && b) || (c >. 3.e+3) !(d < 2);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test36(self):
        input = """
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: testttt 
        Body: 
            var = (x==123)!= xonxon ;
            x = (var =/= ilv) <. nvh >.h;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test37(self):
        input = """Function: stmtcallinindex 
        Parameter: n
        Body: 
            a = 3*.4.5\\.0e-2+arr[3-function("call")];
        EndBody."""
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test38(self):
        input = """Function: precedence 
        Body: 
            x = -(-15.e-1+(-.45.1*.2.3)*(35+108+a[4]));
        EndBody."""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test39(self):
        input = """Function: array 
        Parameter: i , j, arr[1001]
        Body: 
            a[i] = arr[c[2+j][b[i]*3]] + 4;
            i = i + 1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test40(self):
        input = """Function: positionoflogicalop 
        Parameter: n
        Body: 
            While (True) Do
                logic=[e+3]&&var!variable;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test41(self):
        input = """Function: signop
        Parameter: n
        Body:
            a = -1082000;
            b = -0X123BCD;
            c = -0o21345;
            d = -a;
            c = -call(a);
            b = -.352.4E-12 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test42(self):
        input = """Function: indexop
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody."""
        expect = "Error on line 4 col 42: !"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test43(self):
        input = """Function: indexerror
        Body: 
            x=[a+6];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test44(self):
        input = """Function: misspareninop 
        Body: 
             x = ((a >=. 2.3e-13 || (x =/= 2e-35));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test45(self):
        input = """
        Function: test
        Body:
            Var: x=1;
            If x > 10 Then
                x=25+6-.2.5%3\\100*x;
            Else
                x=x+2;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 23: True"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    ###########################################################
	# Test statement
    def test46(self):
        input = """Function: var_decl 
        Parameter: naybingeohuhu
        Body:
Var: r = 10., v;
v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test47(self):
        input = """Function: assign 
        Parameter: n
        Body: a = {1,2,3}, b[2][3] = 5
        c[2] = {{1,3},{,5,7}}
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test48(self):
        input = """Function: ifOKE 
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test49(self):
        input = """Function: if__more_Else 
        Parameter: khaibaobien
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 4 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test50(self):
        input = """Function: iFElseIFNotElse 
        Parameter: n
        Body: 
            If bool_of_string("True") Then
                a = int_of_string (read ());
            ElseIf n =/= 1.08 Then
                b = float_of_int (a) +. 2.0;
            ElseIf False Then
                Return n;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 27: abc"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test51(self):
        input = """Function: fullIf 
        Body: 
            If (x == (b!=c && (a > b + c))) Then Return;
            ElseIf (x=="Chung Xon@@") Break;
            Else 
            x="successful";
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 30: absd"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test52(self):
        input = """Function: ifELSEelseif
        Body: 
            If i <. 4.5 Then
                print(i);
            Else
                i=i-1;
            ElseIf n > 10 Then 
                Break;
            EndIf.
            EndBody."""
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test53(self):
        input = """Function: iflongnhau
        Parameter: a, b
        Body:
        Var: id[4312][867][9856][i812], stringID[108] = "day la \\\\ 1 chuoi !!",
,literal = 120000e-1,  array[2][3] = {{867,345,987},{76,12,744}};
            If n > 10 Then
                If n <. 20.5 Then Return x=3;
                EndIf.
                printStrLn(arg);
            Else fact(x) + 3;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 16: If"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test54(self):
        input = """Function: nothen
        Body:
            If e==True 
                print("Hello cac cau\\n");
            EndIf.
        EndBody."""
        expect = "Error on line 5 col 19: ,"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test55(self):
        input = """
        Function: foroke
        Body: 
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test56(self):
        input = """
        Function: forinitfail 
        Parameter: n[5]
        Body: 
            For (n[i] = 0, i < 10, i=i+1) Do
                n[i]=n+i;
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test57(self):
        input = """
        Function: formissing
        Body: 
            For (, i < k, i=i*i) Do
            goo();
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test58(self):
        input = """
        Function: foofail
        Parameter: x
        Body: 
            For (, ,                    
            ) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test59(self):
        input = """
        Function: fornotendfor
        Body: 
            For (i = 1, i <= x*x*x,i=i*i+.1.5)
            Do x=x+1;
            EndDo.
        EndBody."""
        expect = "Error on line 5 col 29: )"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test60(self):
        input = """
        Function: forinfor
        Parameter: row,col,sum,arr[5][9]
        Body:
            Var: sum=0;
            For( i=0,i<=row,i=i+1) Do
                For(j=0,j<col,j=j+1) Do
                    sum=sum+arr[i][j]
                EndFor.
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test61(self):
        input = """Function: whileoke
        Body: 
            Var: i = 0,k=10;
            While i !=k Do
                a[i] = b + i +. 15.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test62(self):
        input = """Function: whileandif 
        Body:
            Var: x=20;
            While True Do
                If x==0 Then Break;
                ElseIf x%2==0 Then
                    x=x\\2;
                Else writeln(x);
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 2 col 47: ]"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test63(self):
        input = """Function: whilenullstmt
        Body:
            While i < 5 Do EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test64(self):
        input = """Function: whileinwhile 
        Parameter: x
        Body: 
            While (True) Do
                While (x>=0) Do
                    x = x+-1;
                EndWhile.
                If ((x<0)) Then Break; EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test65(self):
        input = """Function: whilenotendwhile 
        Parameter: n
        Body: 
            While True Do
                Whilen>=1 Do
                    Whilen<.69.96 Do
                        While n%3==1 Do
                            n = n \\ 5;
                        EndWhile
                    .EndWhile.
                EndWhile.
        EndBody."""
        expect = "Error on line 3 col 55: -"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test66(self):
        input = """
        Function: main
        Body:
            While True print("Hello World"); EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test67(self):
        input = """Function: whileindowhile
        Parameter: x
        Body:
            Do
                While a<100 Do
                    a=a-30;
                EndWhile.
            While (a>1);
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test68(self):
        input = """Function: miss_one_do 
        Body:
            While a<100 Do
                a=a-30;
                While (a>1);
                EndDo.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test69(self):
        input = """Function: testdowhile
        Parameter: x,a,b
        Body: 
            Do x = a + b;
            While(x<1000.e5)
            EndDo.
        EndBody."""
        expect = "Error on line 14 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test70(self):
        input = """Function: notexpr 
        Parameter: n
        Body: 
            Do  
                Return 1;
            While EndDo.
        EndBody."""
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test71(self):
        input = """Function: breaktest 
        Parameter: x
        Body: 
            While x >= 1 Do
                If y<100 Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 18: )"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test72(self):
        input = """Function: breakwithoutsemi
        Body: 
            For((i=0), i!=9, i=i*.2.0) Do
                If i>=10 Then Breakk;
                EndIf.
            EndFor.
        EndBody."""
        expect = "Error on line 6 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test73(self):
        input = """Function: continue 
        Body: 
            For((i=0), i!=9, i=i*.2.0) Do
                If i==10 Then Continue;
                EndIf.
                foo();
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test74(self):
        input = """Function: breakandcontinuealone
        Body: 
            Continue;
            Break;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test75(self):
        input = """Function: callstmt 
        Parameter: x,y
        Body:
            foo(2 + x, 4. \. y);
            goo();
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test76(self):
        input = """Function: callmore
        Body: 
            call(a,876,var*.65e-1,arr[3],True,"chuoi~~\\n");
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test77(self):
        input = """Var: callnotinfunction
            goo(x,y*2,z+3.00000003);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test78(self):
        input = """Function: callwithoutsemi
        Body: 
            iden__TI_FIerOf_Function(a,b_,c+.3.e-2)
        EndBody."""
        expect = "Error on line 5 col 30: >."
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test79(self):
        input = """Function: testreturn 
        Parameter: n
        Body: 
            Var: t=False;
            If n<100 Then t=True
            EndIf.
            Return t;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test80(self):
        input = """Var: returnwithoutfunction
        Var: t=0
        Return t;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test81(self):
        input = """Function: returnnull 
        Parameter: i
        Body: 
            If i==0 Then Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test82(self):
        input = """Function: returnstring
            Body:
                Return "String'""
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test83(self):
        input = """
            Function: returnboolean
            Body:
            If str == "Chung Xon" Then
                Return True;
            Else
                Return False;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test84(self):
        input = """
        Function: funccallfail 
        Body:
        foo(x)+a+2;
        EndBody."""
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    ###########################################################
	# Test array
    def test85(self):
        input = """Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test86(self):
        input = """Function: arrayinarray 
                Parameter: x[2][3]
        Body:
            Var: i = 0;
            x[2][3]={{867,345,987},{76,12,744}};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test87(self):
        input = """Function: idinarray 
        Parameter: n
        Body: 
            x[123]={y65,de3DEF,ca_rFE245_2E23};
        EndBody."""
        expect = "Error on line 4 col 42: !"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test88(self):
        input = """
        Var: stringinarray, x[123]={"STRING","aRraY1","Array2"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test89(self):
        input = """Function: arrayhavespace
        Body: 
            Var  : x[123]={   20, 2   ,108  };
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test90(self):
        input = """Function: complexarray
            Body: x[123]={"duwat73\r \t", "@#&\n rwFEW54",54312,10.e13, 0.123, 543.0e-6  ,{"xe mau xanh"},"xe mau do"};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test91(self):
        input = """Function: arraynull
        Body: 
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test92(self):
        input = """Function: multicallstmt
        Body:
            a =-((func1(a)+23) * -func2(4)+arr[3])\. 0.5;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test93(self):
        input = """Function: callincall
        Body:
            a =func1(foo(3))+23) - func2(goo(foo(a)));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    ###########################################################
	# Test more function
    def test94(self):
        input = """Function: a Parameter: a Body: Var: a=False;EndBody. Function: b Body: EndBody.
Function: d**Here some too**Parameter: d Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test95(self):
        input = """Function: foo 
        Parameter: n
        Body:
            Var: i = 0;
            While i!=423 Do
                fact (i);
                i = i + 3; **cmt**
                If i==212 Then Break;
                a = (!(b && c)||!(a&&b)); 
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "Error on line 2 col 15: ]"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test96(self):
        input = """Function: mmmmm
        Body: 
            Do
                While(1) Do
                foo (2 + x, 4. \. y);goo ();
            EndWhile.
            EndDo.
        EndBody."""
        expect = "Error on line 1 col 10: +"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test297(self):
        input= """Function: more1
        Parameter: a[5], b
        Body:
        Var: x = {{1,2,3}, **Comment here** "abc"};
        Var: i = 0;
        While (i < 5)
        If i == 3 ThenReturn 1;EndIf.
        i = i + 1;
        EndWhile.
        EndBody."""
        expect = "Error on line 5 col 8: While"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test98(self):
        input = """Function: factorialOfNumber
        Parameter: n
        Body:
        Var:factorial=1;
        print("Enter integer: ")
        read();
        For i=0, i<=n, i=i+1 Do(
            factorial=factorial*i
        )
        EndFor.
        print(factorial);
        return factorial;
        EndBody."""
        expect = "Error on line 4 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test99(self):
        input = """Function: fibo
        Parameter: n
        Body:
            Var: n, t1 = 0, t2 = 1, nextTerm = 0;
            print("Enter the number of terms: ");
            getline(n);
            print("Fibonacci Series: ");
            For (i = 1, i <= n, i=i+1) Do
                If(i == 1) Then(
                print(" " + t1);
                Continue;
                EndIf.
            )
            If(i == 2) Then
                cout << t2 << " ";
        Continue;
        EndIf.
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        
        print(nextTerm + " ");
    )
    EndFor.
    return 0;
    EndBody."""
        expect = "Error on line 2 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test100(self):
        input = """Function: octalToDecimal
        Parameter: octalNumber
        Body:
        Var: decimalNumber = 0, i = 0, rem;
        While (octalNumber != 0) Do
            rem = octalNumber % 10;
            octalNumber =octalNumber \\ 10;
            decimalNumber =decimalNumber  + rem * pow({8,i});
            i=i+1;;
        EndWhile.
    Return decimalNumber;
    EndBody."""
        expect = "Error on line 2 col 20: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,300))