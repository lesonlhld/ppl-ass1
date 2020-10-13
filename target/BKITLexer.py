# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u0294\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\5\13\u00d9\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00e3\n\f\3\r\3\r\5\r\u00e7\n\r\3\r\3\r\3\16\6\16\u00ec")
        buf.write("\n\16\r\16\16\16\u00ed\3\17\3\17\3\17\3\17\7\17\u00f4")
        buf.write("\n\17\f\17\16\17\u00f7\13\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\5\20\u00fe\n\20\3\20\5\20\u0101\n\20\3\21\3\21\3\22\3")
        buf.write("\22\3\23\3\23\3\23\3\23\5\23\u010b\n\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u0115\n\25\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u011b\n\26\f\26\16\26\u011e\13\26\3\27\7")
        buf.write("\27\u0121\n\27\f\27\16\27\u0124\13\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u012c\n\27\3\27\7\27\u012f\n\27\f\27")
        buf.write("\16\27\u0132\13\27\3\30\3\30\3\30\5\30\u0137\n\30\3\30")
        buf.write("\3\30\3\31\3\31\7\31\u013d\n\31\f\31\16\31\u0140\13\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3")
        buf.write("U\3U\7U\u0235\nU\fU\16U\u0238\13U\3U\5U\u023b\nU\3V\3")
        buf.write("V\3V\3V\7V\u0241\nV\fV\16V\u0244\13V\3W\3W\3W\3W\7W\u024a")
        buf.write("\nW\fW\16W\u024d\13W\3X\3X\5X\u0251\nX\3Y\3Y\5Y\u0255")
        buf.write("\nY\3Z\3Z\7Z\u0259\nZ\fZ\16Z\u025c\13Z\3Z\3Z\3Z\3[\3[")
        buf.write("\5[\u0263\n[\3[\3[\3\\\3\\\6\\\u0269\n\\\r\\\16\\\u026a")
        buf.write("\3]\3]\3]\5]\u0270\n]\3]\3]\3^\3^\3_\3_\7_\u0278\n_\f")
        buf.write("_\16_\u027b\13_\3_\5_\u027e\n_\3_\3_\3`\3`\7`\u0284\n")
        buf.write("`\f`\16`\u0287\13`\3`\3`\3`\3a\3a\3a\3a\7a\u0290\na\f")
        buf.write("a\16a\u0293\13a\5\u00f5\u025a\u0291\2b\3\2\5\2\7\2\t\2")
        buf.write("\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2")
        buf.write("!\2#\2%\2\'\2)\2+\2-\2/\2\61\3\63\4\65\5\67\69\7;\b=\t")
        buf.write("?\nA\13C\fE\rG\16I\17K\20M\21O\22Q\23S\24U\25W\26Y\27")
        buf.write("[\30]\31_\32a\33c\34e\35g\36i\37k m!o\"q#s$u%w&y\'{(}")
        buf.write(")\177*\u0081+\u0083,\u0085-\u0087.\u0089/\u008b\60\u008d")
        buf.write("\61\u008f\62\u0091\63\u0093\64\u0095\65\u0097\66\u0099")
        buf.write("\67\u009b8\u009d9\u009f:\u00a1;\u00a3<\u00a5=\u00a7>\u00a9")
        buf.write("?\u00ab@\u00adA\u00afB\u00b1C\u00b3D\u00b5E\u00b7F\u00b9")
        buf.write("G\u00bbH\u00bdI\u00bfJ\u00c1K\3\2\30\4\2C\\c|\3\2\62;")
        buf.write("\3\2\63;\3\2\629\3\2\639\4\2\62;CH\4\2\63;CH\4\2GGgg\4")
        buf.write("\2--//\5\2\13\f\16\17\"\"\3\2$$\3\2))\7\2\n\f\16\17$$")
        buf.write("))^^\n\2$$))^^ddhhppttvv\3\2^^\3\2\"\"\3\2c|\6\2\62;C")
        buf.write("\\aac|\3\2\62\62\4\2ZZzz\4\2QQqq\5\3\n\f\16\17^^\2\u029f")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\3\u00c3\3\2\2\2\5\u00c5\3\2\2\2\7\u00c7\3\2\2\2\t\u00c9")
        buf.write("\3\2\2\2\13\u00cb\3\2\2\2\r\u00cd\3\2\2\2\17\u00cf\3\2")
        buf.write("\2\2\21\u00d1\3\2\2\2\23\u00d3\3\2\2\2\25\u00d6\3\2\2")
        buf.write("\2\27\u00e2\3\2\2\2\31\u00e6\3\2\2\2\33\u00eb\3\2\2\2")
        buf.write("\35\u00ef\3\2\2\2\37\u0100\3\2\2\2!\u0102\3\2\2\2#\u0104")
        buf.write("\3\2\2\2%\u010a\3\2\2\2\'\u010c\3\2\2\2)\u0114\3\2\2\2")
        buf.write("+\u0116\3\2\2\2-\u0122\3\2\2\2/\u0133\3\2\2\2\61\u013a")
        buf.write("\3\2\2\2\63\u0141\3\2\2\2\65\u0145\3\2\2\2\67\u014a\3")
        buf.write("\2\2\29\u0150\3\2\2\2;\u0159\3\2\2\2=\u015c\3\2\2\2?\u0161")
        buf.write("\3\2\2\2A\u0168\3\2\2\2C\u0170\3\2\2\2E\u0176\3\2\2\2")
        buf.write("G\u017d\3\2\2\2I\u0186\3\2\2\2K\u018a\3\2\2\2M\u0193\3")
        buf.write("\2\2\2O\u0196\3\2\2\2Q\u01a0\3\2\2\2S\u01a7\3\2\2\2U\u01ac")
        buf.write("\3\2\2\2W\u01b2\3\2\2\2Y\u01b7\3\2\2\2[\u01bd\3\2\2\2")
        buf.write("]\u01c3\3\2\2\2_\u01c7\3\2\2\2a\u01cd\3\2\2\2c\u01d5\3")
        buf.write("\2\2\2e\u01dc\3\2\2\2g\u01de\3\2\2\2i\u01e1\3\2\2\2k\u01e3")
        buf.write("\3\2\2\2m\u01e6\3\2\2\2o\u01e8\3\2\2\2q\u01eb\3\2\2\2")
        buf.write("s\u01ed\3\2\2\2u\u01f0\3\2\2\2w\u01f2\3\2\2\2y\u01f4\3")
        buf.write("\2\2\2{\u01f7\3\2\2\2}\u01fa\3\2\2\2\177\u01fd\3\2\2\2")
        buf.write("\u0081\u0200\3\2\2\2\u0083\u0202\3\2\2\2\u0085\u0204\3")
        buf.write("\2\2\2\u0087\u0207\3\2\2\2\u0089\u020a\3\2\2\2\u008b\u020e")
        buf.write("\3\2\2\2\u008d\u0211\3\2\2\2\u008f\u0214\3\2\2\2\u0091")
        buf.write("\u0218\3\2\2\2\u0093\u021c\3\2\2\2\u0095\u021e\3\2\2\2")
        buf.write("\u0097\u0220\3\2\2\2\u0099\u0222\3\2\2\2\u009b\u0224\3")
        buf.write("\2\2\2\u009d\u0226\3\2\2\2\u009f\u0228\3\2\2\2\u00a1\u022a")
        buf.write("\3\2\2\2\u00a3\u022c\3\2\2\2\u00a5\u022e\3\2\2\2\u00a7")
        buf.write("\u0230\3\2\2\2\u00a9\u023a\3\2\2\2\u00ab\u023c\3\2\2\2")
        buf.write("\u00ad\u0245\3\2\2\2\u00af\u0250\3\2\2\2\u00b1\u0254\3")
        buf.write("\2\2\2\u00b3\u0256\3\2\2\2\u00b5\u0260\3\2\2\2\u00b7\u0266")
        buf.write("\3\2\2\2\u00b9\u026f\3\2\2\2\u00bb\u0273\3\2\2\2\u00bd")
        buf.write("\u0275\3\2\2\2\u00bf\u0281\3\2\2\2\u00c1\u028b\3\2\2\2")
        buf.write("\u00c3\u00c4\t\2\2\2\u00c4\4\3\2\2\2\u00c5\u00c6\t\3\2")
        buf.write("\2\u00c6\6\3\2\2\2\u00c7\u00c8\t\4\2\2\u00c8\b\3\2\2\2")
        buf.write("\u00c9\u00ca\t\5\2\2\u00ca\n\3\2\2\2\u00cb\u00cc\t\6\2")
        buf.write("\2\u00cc\f\3\2\2\2\u00cd\u00ce\t\7\2\2\u00ce\16\3\2\2")
        buf.write("\2\u00cf\u00d0\t\b\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\5")
        buf.write("\u00a9U\2\u00d2\22\3\2\2\2\u00d3\u00d4\5\u0097L\2\u00d4")
        buf.write("\u00d5\5\u00a9U\2\u00d5\24\3\2\2\2\u00d6\u00d8\t\t\2\2")
        buf.write("\u00d7\u00d9\t\n\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\5\u00a9U\2\u00db")
        buf.write("\26\3\2\2\2\u00dc\u00dd\5\21\t\2\u00dd\u00de\5\23\n\2")
        buf.write("\u00de\u00e3\3\2\2\2\u00df\u00e0\5\21\t\2\u00e0\u00e1")
        buf.write("\5\u0097L\2\u00e1\u00e3\3\2\2\2\u00e2\u00dc\3\2\2\2\u00e2")
        buf.write("\u00df\3\2\2\2\u00e3\30\3\2\2\2\u00e4\u00e7\5\21\t\2\u00e5")
        buf.write("\u00e7\5\27\f\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2")
        buf.write("\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\5\25\13\2\u00e9\32")
        buf.write("\3\2\2\2\u00ea\u00ec\t\13\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\34\3\2\2\2\u00ef\u00f0\7,\2\2\u00f0\u00f1\7,\2")
        buf.write("\2\u00f1\u00f5\3\2\2\2\u00f2\u00f4\13\2\2\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f8\u00f9\7,\2\2\u00f9\u00fa\7,\2\2\u00fa\36\3\2\2")
        buf.write("\2\u00fb\u00fd\7\17\2\2\u00fc\u00fe\7\f\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write("\u0101\7\f\2\2\u0100\u00fb\3\2\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101 \3\2\2\2\u0102\u0103\t\f\2\2\u0103\"\3\2\2\2\u0104")
        buf.write("\u0105\t\r\2\2\u0105$\3\2\2\2\u0106\u0107\7)\2\2\u0107")
        buf.write("\u010b\7$\2\2\u0108\u010b\n\16\2\2\u0109\u010b\5\'\24")
        buf.write("\2\u010a\u0106\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u0109")
        buf.write("\3\2\2\2\u010b&\3\2\2\2\u010c\u010d\7^\2\2\u010d\u010e")
        buf.write("\t\17\2\2\u010e(\3\2\2\2\u010f\u0110\7^\2\2\u0110\u0115")
        buf.write("\n\17\2\2\u0111\u0115\n\20\2\2\u0112\u0113\7)\2\2\u0113")
        buf.write("\u0115\n\f\2\2\u0114\u010f\3\2\2\2\u0114\u0111\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0115*\3\2\2\2\u0116\u011c\5-\27")
        buf.write("\2\u0117\u0118\5\u0099M\2\u0118\u0119\5-\27\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0117\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d,\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0121\t\21\2\2\u0120\u011f\3\2\2")
        buf.write("\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u012b\3\2\2\2\u0124\u0122\3\2\2\2\u0125")
        buf.write("\u012c\5\u00a9U\2\u0126\u012c\5\u00b3Z\2\u0127\u012c\5")
        buf.write("\u00b1Y\2\u0128\u012c\5\u00afX\2\u0129\u012c\5\u00b5[")
        buf.write("\2\u012a\u012c\5\35\17\2\u012b\u0125\3\2\2\2\u012b\u0126")
        buf.write("\3\2\2\2\u012b\u0127\3\2\2\2\u012b\u0128\3\2\2\2\u012b")
        buf.write("\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c\u0130\3\2\2\2")
        buf.write("\u012d\u012f\t\21\2\2\u012e\u012d\3\2\2\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write(".\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0136\5\u009fP\2\u0134")
        buf.write("\u0137\5\u00a9U\2\u0135\u0137\5\61\31\2\u0136\u0134\3")
        buf.write("\2\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139")
        buf.write("\5\u00a1Q\2\u0139\60\3\2\2\2\u013a\u013e\t\22\2\2\u013b")
        buf.write("\u013d\t\23\2\2\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2")
        buf.write("\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\62\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7X\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7t\2\2\u0144\64\3\2\2\2\u0145\u0146")
        buf.write("\7D\2\2\u0146\u0147\7q\2\2\u0147\u0148\7f\2\2\u0148\u0149")
        buf.write("\7{\2\2\u0149\66\3\2\2\2\u014a\u014b\7D\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7g\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7m\2\2\u014f8\3\2\2\2\u0150\u0151\7E\2\2\u0151\u0152")
        buf.write("\7q\2\2\u0152\u0153\7p\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7p\2\2\u0156\u0157\7w\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158:\3\2\2\2\u0159\u015a\7F\2\2\u015a\u015b")
        buf.write("\7q\2\2\u015b<\3\2\2\2\u015c\u015d\7G\2\2\u015d\u015e")
        buf.write("\7n\2\2\u015e\u015f\7u\2\2\u015f\u0160\7g\2\2\u0160>\3")
        buf.write("\2\2\2\u0161\u0162\7G\2\2\u0162\u0163\7n\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\u0165\7g\2\2\u0165\u0166\7K\2\2\u0166\u0167")
        buf.write("\7h\2\2\u0167@\3\2\2\2\u0168\u0169\7G\2\2\u0169\u016a")
        buf.write("\7p\2\2\u016a\u016b\7f\2\2\u016b\u016c\7D\2\2\u016c\u016d")
        buf.write("\7q\2\2\u016d\u016e\7f\2\2\u016e\u016f\7{\2\2\u016fB\3")
        buf.write("\2\2\2\u0170\u0171\7G\2\2\u0171\u0172\7p\2\2\u0172\u0173")
        buf.write("\7f\2\2\u0173\u0174\7K\2\2\u0174\u0175\7h\2\2\u0175D\3")
        buf.write("\2\2\2\u0176\u0177\7G\2\2\u0177\u0178\7p\2\2\u0178\u0179")
        buf.write("\7f\2\2\u0179\u017a\7H\2\2\u017a\u017b\7q\2\2\u017b\u017c")
        buf.write("\7t\2\2\u017cF\3\2\2\2\u017d\u017e\7G\2\2\u017e\u017f")
        buf.write("\7p\2\2\u017f\u0180\7f\2\2\u0180\u0181\7Y\2\2\u0181\u0182")
        buf.write("\7j\2\2\u0182\u0183\7k\2\2\u0183\u0184\7n\2\2\u0184\u0185")
        buf.write("\7g\2\2\u0185H\3\2\2\2\u0186\u0187\7H\2\2\u0187\u0188")
        buf.write("\7q\2\2\u0188\u0189\7t\2\2\u0189J\3\2\2\2\u018a\u018b")
        buf.write("\7H\2\2\u018b\u018c\7w\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7e\2\2\u018e\u018f\7v\2\2\u018f\u0190\7k\2\2\u0190\u0191")
        buf.write("\7q\2\2\u0191\u0192\7p\2\2\u0192L\3\2\2\2\u0193\u0194")
        buf.write("\7K\2\2\u0194\u0195\7h\2\2\u0195N\3\2\2\2\u0196\u0197")
        buf.write("\7R\2\2\u0197\u0198\7c\2\2\u0198\u0199\7t\2\2\u0199\u019a")
        buf.write("\7c\2\2\u019a\u019b\7o\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\7v\2\2\u019d\u019e\7g\2\2\u019e\u019f\7t\2\2\u019fP\3")
        buf.write("\2\2\2\u01a0\u01a1\7T\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3")
        buf.write("\7v\2\2\u01a3\u01a4\7w\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6R\3\2\2\2\u01a7\u01a8\7V\2\2\u01a8\u01a9")
        buf.write("\7j\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab\7p\2\2\u01abT\3")
        buf.write("\2\2\2\u01ac\u01ad\7Y\2\2\u01ad\u01ae\7j\2\2\u01ae\u01af")
        buf.write("\7k\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1\7g\2\2\u01b1V\3")
        buf.write("\2\2\2\u01b2\u01b3\7V\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5")
        buf.write("\7w\2\2\u01b5\u01b6\7g\2\2\u01b6X\3\2\2\2\u01b7\u01b8")
        buf.write("\7H\2\2\u01b8\u01b9\7c\2\2\u01b9\u01ba\7n\2\2\u01ba\u01bb")
        buf.write("\7u\2\2\u01bb\u01bc\7g\2\2\u01bcZ\3\2\2\2\u01bd\u01be")
        buf.write("\7G\2\2\u01be\u01bf\7p\2\2\u01bf\u01c0\7f\2\2\u01c0\u01c1")
        buf.write("\7F\2\2\u01c1\u01c2\7q\2\2\u01c2\\\3\2\2\2\u01c3\u01c4")
        buf.write("\7k\2\2\u01c4\u01c5\7p\2\2\u01c5\u01c6\7v\2\2\u01c6^\3")
        buf.write("\2\2\2\u01c7\u01c8\7h\2\2\u01c8\u01c9\7n\2\2\u01c9\u01ca")
        buf.write("\7q\2\2\u01ca\u01cb\7c\2\2\u01cb\u01cc\7v\2\2\u01cc`\3")
        buf.write("\2\2\2\u01cd\u01ce\7d\2\2\u01ce\u01cf\7q\2\2\u01cf\u01d0")
        buf.write("\7q\2\2\u01d0\u01d1\7n\2\2\u01d1\u01d2\7g\2\2\u01d2\u01d3")
        buf.write("\7c\2\2\u01d3\u01d4\7p\2\2\u01d4b\3\2\2\2\u01d5\u01d6")
        buf.write("\7u\2\2\u01d6\u01d7\7v\2\2\u01d7\u01d8\7t\2\2\u01d8\u01d9")
        buf.write("\7k\2\2\u01d9\u01da\7p\2\2\u01da\u01db\7i\2\2\u01dbd\3")
        buf.write("\2\2\2\u01dc\u01dd\7-\2\2\u01ddf\3\2\2\2\u01de\u01df\7")
        buf.write("-\2\2\u01df\u01e0\7\60\2\2\u01e0h\3\2\2\2\u01e1\u01e2")
        buf.write("\7/\2\2\u01e2j\3\2\2\2\u01e3\u01e4\7/\2\2\u01e4\u01e5")
        buf.write("\7\60\2\2\u01e5l\3\2\2\2\u01e6\u01e7\7,\2\2\u01e7n\3\2")
        buf.write("\2\2\u01e8\u01e9\7,\2\2\u01e9\u01ea\7\60\2\2\u01eap\3")
        buf.write("\2\2\2\u01eb\u01ec\7^\2\2\u01ecr\3\2\2\2\u01ed\u01ee\7")
        buf.write("^\2\2\u01ee\u01ef\7\60\2\2\u01eft\3\2\2\2\u01f0\u01f1")
        buf.write("\7\'\2\2\u01f1v\3\2\2\2\u01f2\u01f3\7#\2\2\u01f3x\3\2")
        buf.write("\2\2\u01f4\u01f5\7(\2\2\u01f5\u01f6\7(\2\2\u01f6z\3\2")
        buf.write("\2\2\u01f7\u01f8\7~\2\2\u01f8\u01f9\7~\2\2\u01f9|\3\2")
        buf.write("\2\2\u01fa\u01fb\7?\2\2\u01fb\u01fc\7?\2\2\u01fc~\3\2")
        buf.write("\2\2\u01fd\u01fe\7#\2\2\u01fe\u01ff\7?\2\2\u01ff\u0080")
        buf.write("\3\2\2\2\u0200\u0201\7>\2\2\u0201\u0082\3\2\2\2\u0202")
        buf.write("\u0203\7@\2\2\u0203\u0084\3\2\2\2\u0204\u0205\7@\2\2\u0205")
        buf.write("\u0206\7?\2\2\u0206\u0086\3\2\2\2\u0207\u0208\7>\2\2\u0208")
        buf.write("\u0209\7?\2\2\u0209\u0088\3\2\2\2\u020a\u020b\7?\2\2\u020b")
        buf.write("\u020c\7\61\2\2\u020c\u020d\7?\2\2\u020d\u008a\3\2\2\2")
        buf.write("\u020e\u020f\7>\2\2\u020f\u0210\7\60\2\2\u0210\u008c\3")
        buf.write("\2\2\2\u0211\u0212\7@\2\2\u0212\u0213\7\60\2\2\u0213\u008e")
        buf.write("\3\2\2\2\u0214\u0215\7@\2\2\u0215\u0216\7?\2\2\u0216\u0217")
        buf.write("\7\60\2\2\u0217\u0090\3\2\2\2\u0218\u0219\7>\2\2\u0219")
        buf.write("\u021a\7?\2\2\u021a\u021b\7\60\2\2\u021b\u0092\3\2\2\2")
        buf.write("\u021c\u021d\7=\2\2\u021d\u0094\3\2\2\2\u021e\u021f\7")
        buf.write("<\2\2\u021f\u0096\3\2\2\2\u0220\u0221\7\60\2\2\u0221\u0098")
        buf.write("\3\2\2\2\u0222\u0223\7.\2\2\u0223\u009a\3\2\2\2\u0224")
        buf.write("\u0225\7*\2\2\u0225\u009c\3\2\2\2\u0226\u0227\7+\2\2\u0227")
        buf.write("\u009e\3\2\2\2\u0228\u0229\7]\2\2\u0229\u00a0\3\2\2\2")
        buf.write("\u022a\u022b\7_\2\2\u022b\u00a2\3\2\2\2\u022c\u022d\7")
        buf.write("}\2\2\u022d\u00a4\3\2\2\2\u022e\u022f\7\177\2\2\u022f")
        buf.write("\u00a6\3\2\2\2\u0230\u0231\7?\2\2\u0231\u00a8\3\2\2\2")
        buf.write("\u0232\u0236\5\7\4\2\u0233\u0235\5\5\3\2\u0234\u0233\3")
        buf.write("\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u023b\3\2\2\2\u0238\u0236\3\2\2\2\u0239")
        buf.write("\u023b\t\24\2\2\u023a\u0232\3\2\2\2\u023a\u0239\3\2\2")
        buf.write("\2\u023b\u00aa\3\2\2\2\u023c\u023d\t\24\2\2\u023d\u023e")
        buf.write("\t\25\2\2\u023e\u0242\5\17\b\2\u023f\u0241\5\r\7\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u00ac\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0245\u0246\t\24\2\2\u0246\u0247\t\26\2\2\u0247")
        buf.write("\u024b\5\13\6\2\u0248\u024a\5\t\5\2\u0249\u0248\3\2\2")
        buf.write("\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u00ae\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u0251\5\27\f\2\u024f\u0251\5\31\r\2\u0250\u024e\3\2\2")
        buf.write("\2\u0250\u024f\3\2\2\2\u0251\u00b0\3\2\2\2\u0252\u0255")
        buf.write("\5W,\2\u0253\u0255\5Y-\2\u0254\u0252\3\2\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255\u00b2\3\2\2\2\u0256\u025a\5!\21\2\u0257")
        buf.write("\u0259\5%\23\2\u0258\u0257\3\2\2\2\u0259\u025c\3\2\2\2")
        buf.write("\u025a\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025d\3")
        buf.write("\2\2\2\u025c\u025a\3\2\2\2\u025d\u025e\5!\21\2\u025e\u025f")
        buf.write("\bZ\2\2\u025f\u00b4\3\2\2\2\u0260\u0262\5\u00a3R\2\u0261")
        buf.write("\u0263\5+\26\2\u0262\u0261\3\2\2\2\u0262\u0263\3\2\2\2")
        buf.write("\u0263\u0264\3\2\2\2\u0264\u0265\5\u00a5S\2\u0265\u00b6")
        buf.write("\3\2\2\2\u0266\u0268\5\61\31\2\u0267\u0269\5/\30\2\u0268")
        buf.write("\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u0268\3\2\2\2")
        buf.write("\u026a\u026b\3\2\2\2\u026b\u00b8\3\2\2\2\u026c\u0270\5")
        buf.write("\35\17\2\u026d\u0270\5\33\16\2\u026e\u0270\5\37\20\2\u026f")
        buf.write("\u026c\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u026e\3\2\2\2")
        buf.write("\u0270\u0271\3\2\2\2\u0271\u0272\b]\3\2\u0272\u00ba\3")
        buf.write("\2\2\2\u0273\u0274\13\2\2\2\u0274\u00bc\3\2\2\2\u0275")
        buf.write("\u0279\7$\2\2\u0276\u0278\5%\23\2\u0277\u0276\3\2\2\2")
        buf.write("\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a\3")
        buf.write("\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3\2\2\2\u027c\u027e")
        buf.write("\t\27\2\2\u027d\u027c\3\2\2\2\u027e\u027f\3\2\2\2\u027f")
        buf.write("\u0280\b_\4\2\u0280\u00be\3\2\2\2\u0281\u0285\7$\2\2\u0282")
        buf.write("\u0284\5%\23\2\u0283\u0282\3\2\2\2\u0284\u0287\3\2\2\2")
        buf.write("\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0288\3")
        buf.write("\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289\5)\25\2\u0289\u028a")
        buf.write("\b`\5\2\u028a\u00c0\3\2\2\2\u028b\u028c\7,\2\2\u028c\u028d")
        buf.write("\7,\2\2\u028d\u0291\3\2\2\2\u028e\u0290\13\2\2\2\u028f")
        buf.write("\u028e\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u0292\3\2\2\2")
        buf.write("\u0291\u028f\3\2\2\2\u0292\u00c2\3\2\2\2\u0293\u0291\3")
        buf.write("\2\2\2 \2\u00d8\u00e2\u00e6\u00ed\u00f5\u00fd\u0100\u010a")
        buf.write("\u0114\u011c\u0122\u012b\u0130\u0136\u013e\u0236\u023a")
        buf.write("\u0242\u024b\u0250\u0254\u025a\u0262\u026a\u026f\u0279")
        buf.write("\u027d\u0285\u0291\6\3Z\2\b\2\2\3_\3\3`\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    VAR = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSEIF = 8
    ENDBODY = 9
    ENDIF = 10
    ENDFOR = 11
    ENDWHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    WHILE = 19
    TRUE = 20
    FALSE = 21
    ENDDO = 22
    INT_TYPE = 23
    FLOAT_TYPE = 24
    BOOLEAN_TYPE = 25
    STRING_TYPE = 26
    ADD = 27
    ADD_F = 28
    SUB = 29
    SUB_F = 30
    MULTI = 31
    MULTI_F = 32
    DIV = 33
    DIV_F = 34
    MOD = 35
    NOT = 36
    ANDAND = 37
    OROR = 38
    EQUAL = 39
    NOT_EQUAL = 40
    LESS_THAN = 41
    GREATER_THAN = 42
    GREATER_EQUAL = 43
    LESS_EQUAL = 44
    NOT_EQUAL_F = 45
    LESS_THAN_F = 46
    GREATER_THAN_F = 47
    GREATER_EQUAL_F = 48
    LESS_EQUAL_F = 49
    SEMI = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    LEFT_PAREN = 54
    RIGHT_PAREN = 55
    LEFT_BRACKET = 56
    RIGHT_BRACKET = 57
    LEFT_BRACE = 58
    RIGHT_BRACE = 59
    ASSIGN = 60
    DECIMAL_INTEGER = 61
    HEX_INTEGER = 62
    OCT_INTEGER = 63
    FLOAT = 64
    BOOLEAN = 65
    STRING = 66
    ARRAY = 67
    ARRAY_DECL = 68
    SKIP_ = 69
    ERROR_CHAR = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72
    UNTERMINATED_COMMENT = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'True'", "'False'", "'EndDo'", "'int'", "'float'", 
            "'boolean'", "'string'", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
            "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'>'", "'>='", "'<='", "'=/='", "'<.'", "'>.'", 
            "'>=.'", "'<=.'", "';'", "':'", "'.'", "','", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "TRUE", "FALSE", 
            "ENDDO", "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
            "ADD", "ADD_F", "SUB", "SUB_F", "MULTI", "MULTI_F", "DIV", "DIV_F", 
            "MOD", "NOT", "ANDAND", "OROR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
            "GREATER_THAN", "GREATER_EQUAL", "LESS_EQUAL", "NOT_EQUAL_F", 
            "LESS_THAN_F", "GREATER_THAN_F", "GREATER_EQUAL_F", "LESS_EQUAL_F", 
            "SEMI", "COLON", "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", 
            "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
            "ASSIGN", "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", "FLOAT", 
            "BOOLEAN", "STRING", "ARRAY", "ARRAY_DECL", "SKIP_", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LETTER", "DIGIT", "NON_ZERO_DIGIT", "OCT_DIGIT", "NON_OCT_DIGIT", 
                  "HEX_DIGIT", "NON_HEX_DIGIT", "INT_PART", "DEC_PART", 
                  "EXPONENT", "POINT_FLOAT", "EXPONENT_FLOAT", "WS", "COMMENT", 
                  "NEWLINE", "DOUBLE_QUOTE", "SINGLE_QUOTE", "STRING_CONTENT", 
                  "ESCAPE_SEQ", "ESCAPE_ILLEGAL", "ARRAY_LIST", "ARRAY_TYPE", 
                  "DIMENSION", "ID", "VAR", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", "INT_TYPE", 
                  "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "ADD", "ADD_F", 
                  "SUB", "SUB_F", "MULTI", "MULTI_F", "DIV", "DIV_F", "MOD", 
                  "NOT", "ANDAND", "OROR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "GREATER_EQUAL", "LESS_EQUAL", "NOT_EQUAL_F", 
                  "LESS_THAN_F", "GREATER_THAN_F", "GREATER_EQUAL_F", "LESS_EQUAL_F", 
                  "SEMI", "COLON", "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                  "ASSIGN", "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", 
                  "FLOAT", "BOOLEAN", "STRING", "ARRAY", "ARRAY_DECL", "SKIP_", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[88] = self.STRING_action 
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		self.text = y[1:]
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		self.text = y[1:]
            	
     


