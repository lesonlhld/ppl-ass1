import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        """Created automatically"""
        input = r"""{996,712,216}""" 
        output = r"""{996,712,216},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,1))
    def test_2(self):
        """Created automatically"""
        input = r""" {True,False}  """ 
        output = r"""{True,False},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,2))
    def test_3(self):
        """Created automatically"""
        input = r"""{{867,345,987},{76,12,744}}""" 
        output = r"""{{867,345,987},{76,12,744}},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,3))
    def test_4(self):
        """Created automatically"""
        input = r"""{y65,de3DEF,ca_rFE245_2E23}""" 
        output = r"""{,y65,,,de3DEF,,,ca_rFE245_2E23,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,4))
    def test_5(self):
        """Created automatically"""
        input = r"""{"STRING","aRraY1","Array2"}""" 
        output = r"""{"STRING","aRraY1","Array2"},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,5))
    def test_6(self):
        """Created automatically"""
        input = r"""{   20, 2   ,108  }""" 
        output = r"""{,20,,,2,,,108,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,6))
    def test_7(self):
        """Created automatically"""
        input = r"""{10.e13, 0.123, 543.0e-6  }""" 
        output = r"""{,10.e13,,,0.123,,,543.0e-6,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,7))
    def test_8(self):
        """Created automatically"""
        input = r"""{{"xe mau xanh"},"xe mau do"}""" 
        output = r"""{{"xe mau xanh"},"xe mau do"},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,8))
    def test_9(self):
        """Created automatically"""
        input = r""" {"duwat73\r \t", "@#&\n rwFEW54", 54312}  """ 
        output = r"""{,duwat73\r \t,,,@#&\n rwFEW54,,,54312,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,9))
    def test_10(self):
        """Created automatically"""
        input = r""" {**comment trong array**}  """ 
        output = r"""{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,10))
    def test_11(self):
        """Created automatically"""
        input = r"""** This is a single-line comment. **""" 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,11))
    def test_12(self):
        """Created automatically"""
        input = r"""**sau day
        *la
        * **comment trong cmt**
        *
        **""" 
        output = r"""comment,trong,cmt,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,12))
    def test_13(self):
        """Created automatically"""
        input = r"""***** *** **""" 
        output = r"""*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,13))
    def test_14(self):
        """Created automatically"""
        input = r"""** This is a
* multi-line
* comment.
** """ 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,14))
    def test_15(self):
        """Created automatically"""
        input = r"""* * **** * *""" 
        output = r"""*,*,*,*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,15))
    def test_16(self):
        """Created automatically"""
        input = r"""**Tui SaP Bj LAG luon r =.= (T.T) :v 2654^$$%!{><>~}{5}[789]!@#$%^&* \v \n   **""" 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,16))
    def test_17(self):
        """Created automatically"""
        input = r"""hello **"be mo"** **cUG wa tr wa dat lun""" 
        output = r"""hello,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input,output,17))
    def test_18(self):
        """Created automatically"""
        input = r"""**met xiu luon a* kok tie9 con bo""" 
        output = r"""Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input,output,18))
    def test_19(self):
        """Created automatically"""
        input = r"""**VI DU CO EOF TRONG CMT** "\\den day la oke\n" """ 
        output = r"""\\den day la oke\n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,19))
    def test_20(self):
        """Created automatically"""
        input = r""" "**comment trong string nha \haha**" oke hem???""" 
        output = r"""Illegal Escape In String: **comment trong string nha \h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,20))
    def test_21(self):
        """Created automatically"""
        input = r"""fjiwef883_Fef_GRWE4324 r3fe 23728DFRfdw""" 
        output = r"""fjiwef883_Fef_GRWE4324,r3fe,23728,Error Token D"""
        self.assertTrue(TestLexer.checkLexeme(input,output,21))
    def test_22(self):
        """Created automatically"""
        input = r"""__count in function""" 
        output = r"""Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input,output,22))
    def test_23(self):
        """Created automatically"""
        input = r"""iwqoue9432@#$8(!/da""" 
        output = r"""iwqoue9432,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(input,output,23))
    def test_24(self):
        """Created automatically"""
        input = r"""!!=x/y""" 
        output = r"""!,!=,x,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input,output,24))
    def test_25(self):
        """Created automatically"""
        input = r""""string nay co 2 \' nha qui vi ^.^"' """ 
        output = r"""string nay co 2 \' nha qui vi ^.^,Error Token '"""
        self.assertTrue(TestLexer.checkLexeme(input,output,25))
    def test_26(self):
        """Created automatically"""
        input = r"""20.e5 18.E9 9.e+3 33.e-3 0.e """ 
        output = r"""20.e5,18.E9,9.e+3,33.e-3,0.,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,26))
    def test_27(self):
        """Created automatically"""
        input = r"""0.0 52.. 43124. 120000e-1""" 
        output = r"""0.0,52.,.,43124.,120000e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,27))
    def test_28(self):
        """Created automatically"""
        input = r"""0.4254 654.321 .7582 87867. .""" 
        output = r"""0.4254,654.321,.,7582,87867.,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,28))
    def test_29(self):
        """Created automatically"""
        input = r"""4.e.6 -0 -404 -.e3 -10.e -10.e3""" 
        output = r"""4.,e,.,6,-,0,-,404,-.,e3,-,10.,e,-,10.e3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,29))
    def test_30(self):
        """Created automatically"""
        input = r"""e97 E-66 16e 30E4 12.0e3""" 
        output = r"""e97,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,30))
    def test_31(self):
        """Created automatically"""
        input = r"""** comment nha **
    Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,For,(,i,==,0,,,i,!=,5,,,i,*,1,),Do,x,=,6,;,EndFor,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,31))
    def test_32(self):
        """Created automatically"""
        input = r"""Function:testdjiDEW__214__wsaParameter:ne23Body:x1 = a[3-foo(3)];Var:x,y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};WhileTrueprint("Hello_World\n");EndWhile.EndBody.""" 
        output = r"""Function,:,testdjiDEW__214__wsaParameter,:,ne23Body,:,x1,=,a,[,3,-,foo,(,3,),],;,Var,:,x,,,y[1][3],=,{,{,{12,1},,,{,12.,,,12e3,},},,,{23},,,{13,32},},;,While,True,print,(,Hello_World\n,),;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,32))
    def test_33(self):
        """Created automatically"""
        input = r"""Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};""" 
        output = r"""Var,:,someid[0][1][123][999],,,mor3Id[1000],=,SomeSTRING,,,some_more_id[987],,,muchmoreID,=,123.321e-2,,,lots_m0rE_1D[123][123],=,{12,3},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,33))
    def test_34(self):
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
        output = r"""Function,:,foo,Parameter,:,a[5],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a[i],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,34))
    def test_35(self):
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
        output = r"""Function,:,foo,Parameter,:,n,Body,:,While,i,<,5,Var,:,k,=,10,;,a[i],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,35))
    def test_36(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,36))
    def test_37(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: abc;
    Body:
    Var **some COMMENT**: ****someid = 3
        **more more**
    vAr: someid;
    EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,abc,;,Body,:,Var,:,someid,=,3,vAr,:,someid,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,37))
    def test_38(self):
        """Created automatically"""
        input = r"""Function:fooParameter:nBody:Ifn==0ThenReturn1;ElseReturnn*fact(n-1);ElseReturnn;EndIf.EndBody.""" 
        output = r"""Function,:,fooParameter,:,nBody,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,Else,Return,n,;,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,38))
    def test_39(self):
        """Created automatically"""
        input = r"""Function: foo 
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
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,If,n,==,0,Then,If,n,!=,0,Then,c,=,a,&&,b,;,Else,Do,x,=,x,+,1,;,iF,x,==,5,tHEN,Break,;,While,x,>,1,EndDo,.,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,39))
    def test_40(self):
        """Created automatically"""
        input = r""" **global declaration**  Var: a = 5;
        Varr: b[2][3] = {{2,3,4},{4,5,6}};
        Varrr: c, d = 6, e, f;
        Var: m, n[10];""" 
        output = r"""Var,:,a,=,5,;,Var,r,:,b[2][3],=,{{2,3,4},{4,5,6}},;,Var,rr,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n[10],;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,40))
    def test_41(self):
        """Created automatically"""
        input = r"""abc""" 
        output = r"""abc,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,41))
    def test_42(self):
        """Created automatically"""
        input = r"""tu1 1a` le^ trun9 son!!!""" 
        output = r"""tu1,1,a,Error Token `"""
        self.assertTrue(TestLexer.checkLexeme(input,output,42))
    def test_43(self):
        """Created automatically"""
        input = r"""Var""" 
        output = r"""Var,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,43))
    def test_44(self):
        """Created automatically"""
        input = r"""day la 1 test""" 
        output = r"""day,la,1,test,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,44))
    def test_45(self):
        """Created automatically"""
        input = r"""xin chao cac ban""" 
        output = r"""xin,chao,cac,ban,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,45))
    def test_46(self):
        """Created automatically"""
        input = r"""co so dau tien 108NVH""" 
        output = r"""co,so,dau,tien,108,Error Token N"""
        self.assertTrue(TestLexer.checkLexeme(input,output,46))
    def test_47(self):
        """Created automatically"""
        input = r"""viet hoa IDENTIFIERS""" 
        output = r"""viet,hoa,Error Token I"""
        self.assertTrue(TestLexer.checkLexeme(input,output,47))
    def test_48(self):
        """Created automatically"""
        input = r"""vIet Lon XOn nE""" 
        output = r"""vIet,Error Token L"""
        self.assertTrue(TestLexer.checkLexeme(input,output,48))
    def test_49(self):
        """Created automatically"""
        input = r"""co ky tu dac biet @@""" 
        output = r"""co,ky,tu,dac,biet,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(input,output,49))
    def test_50(self):
        """Created automatically"""
        input = r"""Var: x""" 
        output = r"""Var,:,x,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,50))
    def test_51(self):
        """Created automatically"""
        input = r""" "abc\h def"  """ 
        output = r"""Illegal Escape In String: abc\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,51))
    def test_52(self):
        """Created automatically"""
        input = r""" "ngoi TAo \\tESt eScapE '" ne ' \r" """ 
        output = r"""Illegal Escape In String: ngoi TAo \\tESt eScapE '" ne ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,52))
    def test_53(self):
        """Created automatically"""
        input = r""" "hello\'\myfriend" """ 
        output = r"""Illegal Escape In String: hello\'\m"""
        self.assertTrue(TestLexer.checkLexeme(input,output,53))
    def test_54(self):
        """Created automatically"""
        input = r""" "chao cac ban nhaaa \Hom\nay cac ban the nao" """ 
        output = r"""Illegal Escape In String: chao cac ban nhaaa \H"""
        self.assertTrue(TestLexer.checkLexeme(input,output,54))
    def test_55(self):
        """Created automatically"""
        input = r""" "24 naif ^%$^% cdasjh\Fncueyew" """ 
        output = r"""Illegal Escape In String: 24 naif ^%$^% cdasjh\F"""
        self.assertTrue(TestLexer.checkLexeme(input,output,55))
    def test_56(self):
        """Created automatically"""
        input = r""" "To la Chung Xon \Ne" """ 
        output = r"""Illegal Escape In String: To la Chung Xon \N"""
        self.assertTrue(TestLexer.checkLexeme(input,output,56))
    def test_57(self):
        """Created automatically"""
        input = r""" xin chao "phan thanh truong\haha" 456""" 
        output = r"""xin,chao,Illegal Escape In String: phan thanh truong\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,57))
    def test_58(self):
        """Created automatically"""
        input = r""" "ahihi do ngoc\\" """ 
        output = r"""ahihi do ngoc\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,58))
    def test_59(self):
        """Created automatically"""
        input = r""" "Day la ' illegal" """ 
        output = r"""Illegal Escape In String: Day la ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,59))
    def test_60(self):
        """Created automatically"""
        input = r""" "Test met qua troi \Wa dat luon ne""" 
        output = r"""Illegal Escape In String: Test met qua troi \W"""
        self.assertTrue(TestLexer.checkLexeme(input,output,60))
    def test_61(self):
        """Created automatically"""
        input = r"""0X54J54""" 
        output = r"""0X54,Error Token J"""
        self.assertTrue(TestLexer.checkLexeme(input,output,61))
    def test_62(self):
        """Created automatically"""
        input = r"""0X5456A 0x205F 0XBCD 0X0 0X567 0x2""" 
        output = r"""0X5456A,0x205F,0XBCD,0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(input,output,62))
    def test_63(self):
        """Created automatically"""
        input = r"""01 8 0108 2000 000""" 
        output = r"""0,1,8,0,108,2000,0,0,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,63))
    def test_64(self):
        """Created automatically"""
        input = r"""0O0 0o1 0o413215""" 
        output = r"""0,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(input,output,64))
    def test_65(self):
        """Created automatically"""
        input = r"""0B2005""" 
        output = r"""0,Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(input,output,65))
    def test_66(self):
        """Created automatically"""
        input = r"""Body Break  Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False EndDo""" 
        output = r"""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,66))
    def test_67(self):
        """Created automatically"""
        input = r"""IfaThenbElseWhile(x>0)Thena++EndWhileEndIF""" 
        output = r"""If,aThenbElseWhile,(,x,>,0,),Then,a,+,+,EndWhile,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,67))
    def test_68(self):
        """Created automatically"""
        input = r"""if thEn ElsE Then """ 
        output = r"""if,thEn,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,68))
    def test_69(self):
        """Created automatically"""
        input = r"""EndFor EndIff EndDoOO EndGame""" 
        output = r"""EndFor,EndIf,f,EndDo,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(input,output,69))
    def test_70(self):
        """Created automatically"""
        input = r"""Parameter: x[123],n""" 
        output = r"""Parameter,:,x[123],,,n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,70))
    def test_71(self):
        """Created automatically"""
        input = r""" int var_ =. int(1.12)*1.0 12and""" 
        output = r"""int,var_,=,.,int,(,1.12,),*,1.0,12,and,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,71))
    def test_72(self):
        """Created automatically"""
        input = r"""x oR y assign !k""" 
        output = r"""x,oR,y,assign,!,k,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,72))
    def test_73(self):
        """Created automatically"""
        input = r"""If a == true then Return 1. elseIf a = False Returnn 0""" 
        output = r"""If,a,==,true,then,Return,1.,elseIf,a,=,False,Return,n,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,73))
    def test_74(self):
        """Created automatically"""
        input = r"""If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf.""" 
        output = r"""If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,74))
    def test_75(self):
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
        output = r"""Function,:,foo,Parameter,:,a[5],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a[i],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,75))
    def test_76(self):
        """Created automatically"""
        input = r""" "Day la 1 string nha Dang Huynh Minh Tri"  """ 
        output = r"""Day la 1 string nha Dang Huynh Minh Tri,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,76))
    def test_77(self):
        """Created automatically"""
        input = r""" "\b\f\r\n\t\'\\"  """ 
        output = r"""\b\f\r\n\t\'\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,77))
    def test_78(self):
        """Created automatically"""
        input = r""" "This is a string containing tab \t"  """ 
        output = r"""This is a string containing tab \t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,78))
    def test_79(self):
        """Created automatically"""
        input = r""" "He asked me: '"Where is John?'""  """ 
        output = r"""He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,79))
    def test_80(self):
        """Created automatically"""
        input = r""" "String nay chua cac ky tu dac biet !@#$%^^&*()?/|~!%>:P{}<> :)))"  """ 
        output = r"""String nay chua cac ky tu dac biet !@#$%^^&*()?/|~!%>:P{}<> :))),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,80))
    def test_81(self):
        """Created automatically"""
        input = r""" "ab'"c\n def"  """ 
        output = r"""ab'"c\n def,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,81))
    def test_82(self):
        """Created automatically"""
        input = r""" "Sau day la 1 string rong" ""  """ 
        output = r"""Sau day la 1 string rong,,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,82))
    def test_83(self):
        """Created automatically"""
        input = r""" "bool_of_string ('"True'")"  """ 
        output = r"""bool_of_string ('"True'"),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,83))
    def test_84(self):
        """Created automatically"""
        input = r""" "** cai nay hong phai comment nha **"  """ 
        output = r"""** cai nay hong phai comment nha **,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,84))
    def test_85(self):
        """Created automatically"""
        input = r"""" This is a test 0925919727 \' PHONE" abc 
"YKYUUD '" \f fsgre " """ 
        output = r""" This is a test 0925919727 \' PHONE,abc,YKYUUD '" \f fsgre ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,85))
    def test_86(self):
        """Created automatically"""
        input = r"""25+6-.2.5%3\100""" 
        output = r"""25,+,6,-.,2.5,%,3,\,100,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,86))
    def test_87(self):
        """Created automatically"""
        input = r"""2e-5*.41+-18""" 
        output = r"""2e-5,*.,41,+,-,18,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,87))
    def test_88(self):
        """Created automatically"""
        input = r"""test&&lexer||parser&h=4/5""" 
        output = r"""test,&&,lexer,||,parser,Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(input,output,88))
    def test_89(self):
        """Created automatically"""
        input = r"""=<=<>>=>=.=/===>.<<.!=""" 
        output = r"""=,<=,<,>,>=,>=.,=/=,==,>.,<,<.,!=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,89))
    def test_90(self):
        """Created automatically"""
        input = r"""!x&&a<=.b\.d*""" 
        output = r"""!,x,&&,a,<=.,b,\.,d,*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,90))
    def test_91(self):
        """Created automatically"""
        input = r""" "abc def  """ 
        output = r"""Unclosed String: abc def  """
        self.assertTrue(TestLexer.checkLexeme(input,output,91))
    def test_92(self):
        """Created automatically"""
        input = r""""fe23%$.81r " {"abc"} 123"abc""" 
        output = r"""fe23%$.81r ,{"abc"},123,Unclosed String: abc"""
        self.assertTrue(TestLexer.checkLexeme(input,output,92))
    def test_93(self):
        """Created automatically"""
        input = r""" "Hi Chau Thanh""Tan """ 
        output = r"""Hi Chau Thanh,Unclosed String: Tan """
        self.assertTrue(TestLexer.checkLexeme(input,output,93))
    def test_94(self):
        """Created automatically"""
        input = r""" "vi su nghiep qua PPL \n" """ 
        output = r"""vi su nghiep qua PPL \n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,94))
    def test_95(self):
        """Created automatically"""
        input = r""" "String ket thuc bang '" """ 
        output = r"""Unclosed String: String ket thuc bang '" """
        self.assertTrue(TestLexer.checkLexeme(input,output,95))
    def test_96(self):
        """Created automatically"""
        input = r""" "abc\n """ 
        output = r"""Unclosed String: abc\n """
        self.assertTrue(TestLexer.checkLexeme(input,output,96))
    def test_97(self):
        """Created automatically"""
        input = r""" "khok '" 1" "dong song~~~ 
        newline" " """ 
        output = r"""khok '" 1,Unclosed String: dong song~~~ 
"""
        self.assertTrue(TestLexer.checkLexeme(input,output,97))
    def test_98(self):
        """Created automatically"""
        input = r""" "" " """ 
        output = r""",Unclosed String:  """
        self.assertTrue(TestLexer.checkLexeme(input,output,98))
    def test_99(self):
        """Created automatically"""
        input = r"""Function: assignment Body: str = "Hello World!!! \" Endbody.""" 
        output = r"""Function,:,assignment,Body,:,str,=,Unclosed String: Hello World!!! \" Endbody."""
        self.assertTrue(TestLexer.checkLexeme(input,output,99))
    def test_100(self):
        """Created automatically"""
        input = r""" "8n[#F*`~.~+C_D""" 
        output = r"""Unclosed String: 8n[#F*`~.~+C_D"""
        self.assertTrue(TestLexer.checkLexeme(input,output,100))