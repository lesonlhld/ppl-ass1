# Generated from d:\PPL\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u0278\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\u00c9")
        buf.write("\n\7\r\7\16\7\u00ca\3\b\3\b\6\b\u00cf\n\b\r\b\16\b\u00d0")
        buf.write("\3\t\3\t\5\t\u00d5\n\t\3\t\6\t\u00d8\n\t\r\t\16\t\u00d9")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00e2\n\n\3\13\3\13\5\13")
        buf.write("\u00e6\n\13\3\13\3\13\3\f\6\f\u00eb\n\f\r\f\16\f\u00ec")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u00f3\n\r\f\r\16\r\u00f6\13\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0103\n\20\3\21\3\21\3\21\3\22\3\22\3\22\5\22\u010b\n")
        buf.write("\22\3\23\3\23\3\23\3\23\7\23\u0111\n\23\f\23\16\23\u0114")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\5\24\u011b\n\24\3\25\3")
        buf.write("\25\3\25\5\25\u0120\n\25\3\25\3\25\3\26\3\26\7\26\u0126")
        buf.write("\n\26\f\26\16\26\u0129\13\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=")
        buf.write("\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\7R\u021e")
        buf.write("\nR\fR\16R\u0221\13R\3R\5R\u0224\nR\3S\3S\3S\6S\u0229")
        buf.write("\nS\rS\16S\u022a\3T\3T\3T\6T\u0230\nT\rT\16T\u0231\3U")
        buf.write("\3U\5U\u0236\nU\3V\3V\5V\u023a\nV\3W\3W\7W\u023e\nW\f")
        buf.write("W\16W\u0241\13W\3W\3W\3W\3X\3X\5X\u0248\nX\3X\3X\3Y\3")
        buf.write("Y\6Y\u024e\nY\rY\16Y\u024f\3Z\3Z\5Z\u0254\nZ\3Z\3Z\3[")
        buf.write("\3[\3\\\3\\\7\\\u025c\n\\\f\\\16\\\u025f\13\\\3\\\5\\")
        buf.write("\u0262\n\\\3\\\3\\\3]\3]\7]\u0268\n]\f]\16]\u026b\13]")
        buf.write("\3]\3]\3]\3^\3^\3^\3^\7^\u0274\n^\f^\16^\u0277\13^\5\u00f4")
        buf.write("\u023f\u0275\2_\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23")
        buf.write("\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\3-\4")
        buf.write("/\5\61\6\63\7\65\b\67\t9\n;\13=\f?\rA\16C\17E\20G\21I")
        buf.write("\22K\23M\24O\25Q\26S\27U\30W\31Y\32[\33]\34_\35a\36c\37")
        buf.write("e g!i\"k#m$o%q&s\'u(w)y*{+},\177-\u0081.\u0083/\u0085")
        buf.write("\60\u0087\61\u0089\62\u008b\63\u008d\64\u008f\65\u0091")
        buf.write("\66\u0093\67\u00958\u00979\u0099:\u009b;\u009d<\u009f")
        buf.write("=\u00a1>\u00a3?\u00a5@\u00a7A\u00a9B\u00abC\u00adD\u00af")
        buf.write("E\u00b1F\u00b3G\u00b5H\u00b7I\u00b9J\u00bbK\3\2\25\4\2")
        buf.write("C\\c|\3\2\62;\3\2\63;\3\2\629\5\2\62;CHch\4\2GGgg\4\2")
        buf.write("--//\5\2\13\f\16\17\"\"\3\2$$\3\2))\7\2\n\f\16\17$$))")
        buf.write("^^\n\2$$))^^ddhhppttvv\3\2^^\3\2c|\6\2\62;C\\aac|\3\2")
        buf.write("\62\62\4\2ZZzz\4\2QQqq\7\3\n\f\16\17$$))^^\2\u0282\2+")
        buf.write("\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2")
        buf.write("\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=")
        buf.write("\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2")
        buf.write("G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\3\u00bd\3\2\2\2\5\u00bf")
        buf.write("\3\2\2\2\7\u00c1\3\2\2\2\t\u00c3\3\2\2\2\13\u00c5\3\2")
        buf.write("\2\2\r\u00c8\3\2\2\2\17\u00cc\3\2\2\2\21\u00d2\3\2\2\2")
        buf.write("\23\u00e1\3\2\2\2\25\u00e5\3\2\2\2\27\u00ea\3\2\2\2\31")
        buf.write("\u00ee\3\2\2\2\33\u00fa\3\2\2\2\35\u00fc\3\2\2\2\37\u0102")
        buf.write("\3\2\2\2!\u0104\3\2\2\2#\u010a\3\2\2\2%\u010c\3\2\2\2")
        buf.write("\'\u011a\3\2\2\2)\u011c\3\2\2\2+\u0123\3\2\2\2-\u012a")
        buf.write("\3\2\2\2/\u012e\3\2\2\2\61\u0133\3\2\2\2\63\u0139\3\2")
        buf.write("\2\2\65\u0142\3\2\2\2\67\u0145\3\2\2\29\u014a\3\2\2\2")
        buf.write(";\u0151\3\2\2\2=\u0159\3\2\2\2?\u015f\3\2\2\2A\u0166\3")
        buf.write("\2\2\2C\u016f\3\2\2\2E\u0173\3\2\2\2G\u017c\3\2\2\2I\u017f")
        buf.write("\3\2\2\2K\u0189\3\2\2\2M\u0190\3\2\2\2O\u0195\3\2\2\2")
        buf.write("Q\u019b\3\2\2\2S\u01a0\3\2\2\2U\u01a6\3\2\2\2W\u01ac\3")
        buf.write("\2\2\2Y\u01b0\3\2\2\2[\u01b6\3\2\2\2]\u01be\3\2\2\2_\u01c5")
        buf.write("\3\2\2\2a\u01c7\3\2\2\2c\u01ca\3\2\2\2e\u01cc\3\2\2\2")
        buf.write("g\u01cf\3\2\2\2i\u01d1\3\2\2\2k\u01d4\3\2\2\2m\u01d6\3")
        buf.write("\2\2\2o\u01d9\3\2\2\2q\u01db\3\2\2\2s\u01dd\3\2\2\2u\u01e0")
        buf.write("\3\2\2\2w\u01e3\3\2\2\2y\u01e6\3\2\2\2{\u01e9\3\2\2\2")
        buf.write("}\u01eb\3\2\2\2\177\u01ed\3\2\2\2\u0081\u01f0\3\2\2\2")
        buf.write("\u0083\u01f3\3\2\2\2\u0085\u01f7\3\2\2\2\u0087\u01fa\3")
        buf.write("\2\2\2\u0089\u01fd\3\2\2\2\u008b\u0201\3\2\2\2\u008d\u0205")
        buf.write("\3\2\2\2\u008f\u0207\3\2\2\2\u0091\u0209\3\2\2\2\u0093")
        buf.write("\u020b\3\2\2\2\u0095\u020d\3\2\2\2\u0097\u020f\3\2\2\2")
        buf.write("\u0099\u0211\3\2\2\2\u009b\u0213\3\2\2\2\u009d\u0215\3")
        buf.write("\2\2\2\u009f\u0217\3\2\2\2\u00a1\u0219\3\2\2\2\u00a3\u0223")
        buf.write("\3\2\2\2\u00a5\u0225\3\2\2\2\u00a7\u022c\3\2\2\2\u00a9")
        buf.write("\u0235\3\2\2\2\u00ab\u0239\3\2\2\2\u00ad\u023b\3\2\2\2")
        buf.write("\u00af\u0245\3\2\2\2\u00b1\u024b\3\2\2\2\u00b3\u0253\3")
        buf.write("\2\2\2\u00b5\u0257\3\2\2\2\u00b7\u0259\3\2\2\2\u00b9\u0265")
        buf.write("\3\2\2\2\u00bb\u026f\3\2\2\2\u00bd\u00be\t\2\2\2\u00be")
        buf.write("\4\3\2\2\2\u00bf\u00c0\t\3\2\2\u00c0\6\3\2\2\2\u00c1\u00c2")
        buf.write("\t\4\2\2\u00c2\b\3\2\2\2\u00c3\u00c4\t\5\2\2\u00c4\n\3")
        buf.write("\2\2\2\u00c5\u00c6\t\6\2\2\u00c6\f\3\2\2\2\u00c7\u00c9")
        buf.write("\5\5\3\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\16\3\2\2\2\u00cc")
        buf.write("\u00ce\5\u0091I\2\u00cd\u00cf\5\5\3\2\u00ce\u00cd\3\2")
        buf.write("\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\20\3\2\2\2\u00d2\u00d4\t\7\2\2\u00d3\u00d5")
        buf.write("\t\b\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00d7\3\2\2\2\u00d6\u00d8\5\5\3\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\22\3\2\2\2\u00db\u00dc\5\r\7\2\u00dc\u00dd")
        buf.write("\5\17\b\2\u00dd\u00e2\3\2\2\2\u00de\u00df\5\r\7\2\u00df")
        buf.write("\u00e0\5\u0091I\2\u00e0\u00e2\3\2\2\2\u00e1\u00db\3\2")
        buf.write("\2\2\u00e1\u00de\3\2\2\2\u00e2\24\3\2\2\2\u00e3\u00e6")
        buf.write("\5\r\7\2\u00e4\u00e6\5\23\n\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\5\21\t")
        buf.write("\2\u00e8\26\3\2\2\2\u00e9\u00eb\t\t\2\2\u00ea\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\30\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef\u00f0")
        buf.write("\7,\2\2\u00f0\u00f4\3\2\2\2\u00f1\u00f3\13\2\2\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f7\u00f8\7,\2\2\u00f8\u00f9\7,\2\2\u00f9\32")
        buf.write("\3\2\2\2\u00fa\u00fb\t\n\2\2\u00fb\34\3\2\2\2\u00fc\u00fd")
        buf.write("\t\13\2\2\u00fd\36\3\2\2\2\u00fe\u0103\n\f\2\2\u00ff\u0100")
        buf.write("\7)\2\2\u0100\u0103\7$\2\2\u0101\u0103\5!\21\2\u0102\u00fe")
        buf.write("\3\2\2\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write(" \3\2\2\2\u0104\u0105\7^\2\2\u0105\u0106\t\r\2\2\u0106")
        buf.write("\"\3\2\2\2\u0107\u0108\7^\2\2\u0108\u010b\n\r\2\2\u0109")
        buf.write("\u010b\n\16\2\2\u010a\u0107\3\2\2\2\u010a\u0109\3\2\2")
        buf.write("\2\u010b$\3\2\2\2\u010c\u0112\5\'\24\2\u010d\u010e\5\u0093")
        buf.write("J\2\u010e\u010f\5\'\24\2\u010f\u0111\3\2\2\2\u0110\u010d")
        buf.write("\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113&\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u011b\5\u00a3R\2\u0116\u011b\5\u00adW\2\u0117\u011b\5")
        buf.write("\u00abV\2\u0118\u011b\5\u00a9U\2\u0119\u011b\5\u00afX")
        buf.write("\2\u011a\u0115\3\2\2\2\u011a\u0116\3\2\2\2\u011a\u0117")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b")
        buf.write("(\3\2\2\2\u011c\u011f\5\u0099M\2\u011d\u0120\5\u00a3R")
        buf.write("\2\u011e\u0120\5+\26\2\u011f\u011d\3\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\5\u009bN\2\u0122")
        buf.write("*\3\2\2\2\u0123\u0127\t\17\2\2\u0124\u0126\t\20\2\2\u0125")
        buf.write("\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128,\3\2\2\2\u0129\u0127\3\2\2")
        buf.write("\2\u012a\u012b\7X\2\2\u012b\u012c\7c\2\2\u012c\u012d\7")
        buf.write("t\2\2\u012d.\3\2\2\2\u012e\u012f\7D\2\2\u012f\u0130\7")
        buf.write("q\2\2\u0130\u0131\7f\2\2\u0131\u0132\7{\2\2\u0132\60\3")
        buf.write("\2\2\2\u0133\u0134\7D\2\2\u0134\u0135\7t\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7c\2\2\u0137\u0138\7m\2\2\u0138\62")
        buf.write("\3\2\2\2\u0139\u013a\7E\2\2\u013a\u013b\7q\2\2\u013b\u013c")
        buf.write("\7p\2\2\u013c\u013d\7v\2\2\u013d\u013e\7k\2\2\u013e\u013f")
        buf.write("\7p\2\2\u013f\u0140\7w\2\2\u0140\u0141\7g\2\2\u0141\64")
        buf.write("\3\2\2\2\u0142\u0143\7F\2\2\u0143\u0144\7q\2\2\u0144\66")
        buf.write("\3\2\2\2\u0145\u0146\7G\2\2\u0146\u0147\7n\2\2\u0147\u0148")
        buf.write("\7u\2\2\u0148\u0149\7g\2\2\u01498\3\2\2\2\u014a\u014b")
        buf.write("\7G\2\2\u014b\u014c\7n\2\2\u014c\u014d\7u\2\2\u014d\u014e")
        buf.write("\7g\2\2\u014e\u014f\7K\2\2\u014f\u0150\7h\2\2\u0150:\3")
        buf.write("\2\2\2\u0151\u0152\7G\2\2\u0152\u0153\7p\2\2\u0153\u0154")
        buf.write("\7f\2\2\u0154\u0155\7D\2\2\u0155\u0156\7q\2\2\u0156\u0157")
        buf.write("\7f\2\2\u0157\u0158\7{\2\2\u0158<\3\2\2\2\u0159\u015a")
        buf.write("\7G\2\2\u015a\u015b\7p\2\2\u015b\u015c\7f\2\2\u015c\u015d")
        buf.write("\7K\2\2\u015d\u015e\7h\2\2\u015e>\3\2\2\2\u015f\u0160")
        buf.write("\7G\2\2\u0160\u0161\7p\2\2\u0161\u0162\7f\2\2\u0162\u0163")
        buf.write("\7H\2\2\u0163\u0164\7q\2\2\u0164\u0165\7t\2\2\u0165@\3")
        buf.write("\2\2\2\u0166\u0167\7G\2\2\u0167\u0168\7p\2\2\u0168\u0169")
        buf.write("\7f\2\2\u0169\u016a\7Y\2\2\u016a\u016b\7j\2\2\u016b\u016c")
        buf.write("\7k\2\2\u016c\u016d\7n\2\2\u016d\u016e\7g\2\2\u016eB\3")
        buf.write("\2\2\2\u016f\u0170\7H\2\2\u0170\u0171\7q\2\2\u0171\u0172")
        buf.write("\7t\2\2\u0172D\3\2\2\2\u0173\u0174\7H\2\2\u0174\u0175")
        buf.write("\7w\2\2\u0175\u0176\7p\2\2\u0176\u0177\7e\2\2\u0177\u0178")
        buf.write("\7v\2\2\u0178\u0179\7k\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017bF\3\2\2\2\u017c\u017d\7K\2\2\u017d\u017e")
        buf.write("\7h\2\2\u017eH\3\2\2\2\u017f\u0180\7R\2\2\u0180\u0181")
        buf.write("\7c\2\2\u0181\u0182\7t\2\2\u0182\u0183\7c\2\2\u0183\u0184")
        buf.write("\7o\2\2\u0184\u0185\7g\2\2\u0185\u0186\7v\2\2\u0186\u0187")
        buf.write("\7g\2\2\u0187\u0188\7t\2\2\u0188J\3\2\2\2\u0189\u018a")
        buf.write("\7T\2\2\u018a\u018b\7g\2\2\u018b\u018c\7v\2\2\u018c\u018d")
        buf.write("\7w\2\2\u018d\u018e\7t\2\2\u018e\u018f\7p\2\2\u018fL\3")
        buf.write("\2\2\2\u0190\u0191\7V\2\2\u0191\u0192\7j\2\2\u0192\u0193")
        buf.write("\7g\2\2\u0193\u0194\7p\2\2\u0194N\3\2\2\2\u0195\u0196")
        buf.write("\7Y\2\2\u0196\u0197\7j\2\2\u0197\u0198\7k\2\2\u0198\u0199")
        buf.write("\7n\2\2\u0199\u019a\7g\2\2\u019aP\3\2\2\2\u019b\u019c")
        buf.write("\7V\2\2\u019c\u019d\7t\2\2\u019d\u019e\7w\2\2\u019e\u019f")
        buf.write("\7g\2\2\u019fR\3\2\2\2\u01a0\u01a1\7H\2\2\u01a1\u01a2")
        buf.write("\7c\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5")
        buf.write("\7g\2\2\u01a5T\3\2\2\2\u01a6\u01a7\7G\2\2\u01a7\u01a8")
        buf.write("\7p\2\2\u01a8\u01a9\7f\2\2\u01a9\u01aa\7F\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01abV\3\2\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae")
        buf.write("\7p\2\2\u01ae\u01af\7v\2\2\u01afX\3\2\2\2\u01b0\u01b1")
        buf.write("\7h\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4")
        buf.write("\7c\2\2\u01b4\u01b5\7v\2\2\u01b5Z\3\2\2\2\u01b6\u01b7")
        buf.write("\7d\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9\7q\2\2\u01b9\u01ba")
        buf.write("\7n\2\2\u01ba\u01bb\7g\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd")
        buf.write("\7p\2\2\u01bd\\\3\2\2\2\u01be\u01bf\7u\2\2\u01bf\u01c0")
        buf.write("\7v\2\2\u01c0\u01c1\7t\2\2\u01c1\u01c2\7k\2\2\u01c2\u01c3")
        buf.write("\7p\2\2\u01c3\u01c4\7i\2\2\u01c4^\3\2\2\2\u01c5\u01c6")
        buf.write("\7-\2\2\u01c6`\3\2\2\2\u01c7\u01c8\7-\2\2\u01c8\u01c9")
        buf.write("\7\60\2\2\u01c9b\3\2\2\2\u01ca\u01cb\7/\2\2\u01cbd\3\2")
        buf.write("\2\2\u01cc\u01cd\7/\2\2\u01cd\u01ce\7\60\2\2\u01cef\3")
        buf.write("\2\2\2\u01cf\u01d0\7,\2\2\u01d0h\3\2\2\2\u01d1\u01d2\7")
        buf.write(",\2\2\u01d2\u01d3\7\60\2\2\u01d3j\3\2\2\2\u01d4\u01d5")
        buf.write("\7^\2\2\u01d5l\3\2\2\2\u01d6\u01d7\7^\2\2\u01d7\u01d8")
        buf.write("\7\60\2\2\u01d8n\3\2\2\2\u01d9\u01da\7\'\2\2\u01dap\3")
        buf.write("\2\2\2\u01db\u01dc\7#\2\2\u01dcr\3\2\2\2\u01dd\u01de\7")
        buf.write("(\2\2\u01de\u01df\7(\2\2\u01dft\3\2\2\2\u01e0\u01e1\7")
        buf.write("~\2\2\u01e1\u01e2\7~\2\2\u01e2v\3\2\2\2\u01e3\u01e4\7")
        buf.write("?\2\2\u01e4\u01e5\7?\2\2\u01e5x\3\2\2\2\u01e6\u01e7\7")
        buf.write("#\2\2\u01e7\u01e8\7?\2\2\u01e8z\3\2\2\2\u01e9\u01ea\7")
        buf.write(">\2\2\u01ea|\3\2\2\2\u01eb\u01ec\7@\2\2\u01ec~\3\2\2\2")
        buf.write("\u01ed\u01ee\7@\2\2\u01ee\u01ef\7?\2\2\u01ef\u0080\3\2")
        buf.write("\2\2\u01f0\u01f1\7>\2\2\u01f1\u01f2\7?\2\2\u01f2\u0082")
        buf.write("\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5\7\61\2\2\u01f5")
        buf.write("\u01f6\7?\2\2\u01f6\u0084\3\2\2\2\u01f7\u01f8\7>\2\2\u01f8")
        buf.write("\u01f9\7\60\2\2\u01f9\u0086\3\2\2\2\u01fa\u01fb\7@\2\2")
        buf.write("\u01fb\u01fc\7\60\2\2\u01fc\u0088\3\2\2\2\u01fd\u01fe")
        buf.write("\7@\2\2\u01fe\u01ff\7?\2\2\u01ff\u0200\7\60\2\2\u0200")
        buf.write("\u008a\3\2\2\2\u0201\u0202\7>\2\2\u0202\u0203\7?\2\2\u0203")
        buf.write("\u0204\7\60\2\2\u0204\u008c\3\2\2\2\u0205\u0206\7=\2\2")
        buf.write("\u0206\u008e\3\2\2\2\u0207\u0208\7<\2\2\u0208\u0090\3")
        buf.write("\2\2\2\u0209\u020a\7\60\2\2\u020a\u0092\3\2\2\2\u020b")
        buf.write("\u020c\7.\2\2\u020c\u0094\3\2\2\2\u020d\u020e\7*\2\2\u020e")
        buf.write("\u0096\3\2\2\2\u020f\u0210\7+\2\2\u0210\u0098\3\2\2\2")
        buf.write("\u0211\u0212\7]\2\2\u0212\u009a\3\2\2\2\u0213\u0214\7")
        buf.write("_\2\2\u0214\u009c\3\2\2\2\u0215\u0216\7}\2\2\u0216\u009e")
        buf.write("\3\2\2\2\u0217\u0218\7\177\2\2\u0218\u00a0\3\2\2\2\u0219")
        buf.write("\u021a\7?\2\2\u021a\u00a2\3\2\2\2\u021b\u021f\5\7\4\2")
        buf.write("\u021c\u021e\5\5\3\2\u021d\u021c\3\2\2\2\u021e\u0221\3")
        buf.write("\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0224")
        buf.write("\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0224\t\21\2\2\u0223")
        buf.write("\u021b\3\2\2\2\u0223\u0222\3\2\2\2\u0224\u00a4\3\2\2\2")
        buf.write("\u0225\u0226\t\21\2\2\u0226\u0228\t\22\2\2\u0227\u0229")
        buf.write("\5\13\6\2\u0228\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u00a6\3\2\2\2")
        buf.write("\u022c\u022d\t\21\2\2\u022d\u022f\t\23\2\2\u022e\u0230")
        buf.write("\5\t\5\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u00a8\3\2\2\2")
        buf.write("\u0233\u0236\5\23\n\2\u0234\u0236\5\25\13\2\u0235\u0233")
        buf.write("\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u00aa\3\2\2\2\u0237")
        buf.write("\u023a\5Q)\2\u0238\u023a\5S*\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023a\u00ac\3\2\2\2\u023b\u023f\5\33\16")
        buf.write("\2\u023c\u023e\5\37\20\2\u023d\u023c\3\2\2\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u0240\3\2\2\2\u023f\u023d\3\2\2\2\u0240")
        buf.write("\u0242\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243\5\33\16")
        buf.write("\2\u0243\u0244\bW\2\2\u0244\u00ae\3\2\2\2\u0245\u0247")
        buf.write("\5\u009dO\2\u0246\u0248\5%\23\2\u0247\u0246\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\5\u009f")
        buf.write("P\2\u024a\u00b0\3\2\2\2\u024b\u024d\5+\26\2\u024c\u024e")
        buf.write("\5)\25\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u00b2\3\2\2\2")
        buf.write("\u0251\u0254\5\31\r\2\u0252\u0254\5\27\f\2\u0253\u0251")
        buf.write("\3\2\2\2\u0253\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255")
        buf.write("\u0256\bZ\3\2\u0256\u00b4\3\2\2\2\u0257\u0258\13\2\2\2")
        buf.write("\u0258\u00b6\3\2\2\2\u0259\u025d\7$\2\2\u025a\u025c\5")
        buf.write("\37\20\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2\2\2\u025d")
        buf.write("\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0261\3\2\2\2")
        buf.write("\u025f\u025d\3\2\2\2\u0260\u0262\t\24\2\2\u0261\u0260")
        buf.write("\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\b\\\4\2\u0264")
        buf.write("\u00b8\3\2\2\2\u0265\u0269\7$\2\2\u0266\u0268\5\37\20")
        buf.write("\2\u0267\u0266\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026c\3\2\2\2\u026b")
        buf.write("\u0269\3\2\2\2\u026c\u026d\5#\22\2\u026d\u026e\b]\5\2")
        buf.write("\u026e\u00ba\3\2\2\2\u026f\u0270\7,\2\2\u0270\u0271\7")
        buf.write(",\2\2\u0271\u0275\3\2\2\2\u0272\u0274\13\2\2\2\u0273\u0272")
        buf.write("\3\2\2\2\u0274\u0277\3\2\2\2\u0275\u0276\3\2\2\2\u0275")
        buf.write("\u0273\3\2\2\2\u0276\u00bc\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\37\2\u00ca\u00d0\u00d4\u00d9\u00e1\u00e5\u00ec\u00f4")
        buf.write("\u0102\u010a\u0112\u011a\u011f\u0127\u021f\u0223\u022a")
        buf.write("\u0231\u0235\u0239\u023f\u0247\u024f\u0253\u025d\u0261")
        buf.write("\u0269\u0275\6\3W\2\b\2\2\3\\\3\3]\4")
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

    ruleNames = [ "LETTER", "DIGIT", "NON_ZERO_DIGIT", "OCT_DIGIT", "HEX_DIGIT", 
                  "INT_PART", "DEC_PART", "EXPONENT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "WS", "COMMENT", "DOUBLE_QUOTE", "SINGLE_QUOTE", "STRING_CONTENT", 
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
        self.checkVersion("4.7.1")
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
            actions[85] = self.STRING_action 
            actions[90] = self.UNCLOSE_STRING_action 
            actions[91] = self.ILLEGAL_ESCAPE_action 
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
            	
     


