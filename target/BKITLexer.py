# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u025a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\5\13\u00cf\n\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00d9\n\f\3\r\3\r\5\r\u00dd\n")
        buf.write("\r\3\r\3\r\3\16\6\16\u00e2\n\16\r\16\16\16\u00e3\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00ea\n\17\f\17\16\17\u00ed\13\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\5\20\u00f4\n\20\3\20\5\20\u00f7")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0101")
        buf.write("\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u010b")
        buf.write("\n\25\3\26\3\26\7\26\u010f\n\26\f\26\16\26\u0112\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*")
        buf.write("\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3")
        buf.write("O\3P\3P\3Q\3Q\3R\3R\7R\u0207\nR\fR\16R\u020a\13R\3R\5")
        buf.write("R\u020d\nR\3S\3S\3S\3S\7S\u0213\nS\fS\16S\u0216\13S\3")
        buf.write("T\3T\3T\3T\7T\u021c\nT\fT\16T\u021f\13T\3U\3U\5U\u0223")
        buf.write("\nU\3V\3V\5V\u0227\nV\3W\3W\7W\u022b\nW\fW\16W\u022e\13")
        buf.write("W\3W\3W\3W\3X\3X\3X\5X\u0236\nX\3X\3X\3Y\3Y\3Z\3Z\7Z\u023e")
        buf.write("\nZ\fZ\16Z\u0241\13Z\3Z\5Z\u0244\nZ\3Z\3Z\3[\3[\7[\u024a")
        buf.write("\n[\f[\16[\u024d\13[\3[\3[\3[\3\\\3\\\3\\\3\\\7\\\u0256")
        buf.write("\n\\\f\\\16\\\u0259\13\\\5\u00eb\u022c\u0257\2]\3\2\5")
        buf.write("\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2")
        buf.write("\35\2\37\2!\2#\2%\2\'\2)\2+\3-\4/\5\61\6\63\7\65\b\67")
        buf.write("\t9\n;\13=\f?\rA\16C\17E\20G\21I\22K\23M\24O\25Q\26S\27")
        buf.write("U\30W\31Y\32[\33]\34_\35a\36c\37e g!i\"k#m$o%q&s\'u(w")
        buf.write(")y*{+},\177-\u0081.\u0083/\u0085\60\u0087\61\u0089\62")
        buf.write("\u008b\63\u008d\64\u008f\65\u0091\66\u0093\67\u00958\u0097")
        buf.write("9\u0099:\u009b;\u009d<\u009f=\u00a1>\u00a3?\u00a5@\u00a7")
        buf.write("A\u00a9B\u00abC\u00adD\u00afE\u00b1F\u00b3G\u00b5H\u00b7")
        buf.write("I\3\2\27\4\2C\\c|\3\2\62;\3\2\63;\3\2\629\3\2\639\4\2")
        buf.write("\62;CH\4\2\63;CH\4\2GGgg\4\2--//\5\2\13\f\16\17\"\"\3")
        buf.write("\2$$\3\2))\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2")
        buf.write("^^\3\2c|\6\2\62;C\\aac|\3\2\62\62\4\2ZZzz\4\2QQqq\5\3")
        buf.write("\n\f\16\17^^\2\u025d\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
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
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9\3\2\2\2\5\u00bb")
        buf.write("\3\2\2\2\7\u00bd\3\2\2\2\t\u00bf\3\2\2\2\13\u00c1\3\2")
        buf.write("\2\2\r\u00c3\3\2\2\2\17\u00c5\3\2\2\2\21\u00c7\3\2\2\2")
        buf.write("\23\u00c9\3\2\2\2\25\u00cc\3\2\2\2\27\u00d8\3\2\2\2\31")
        buf.write("\u00dc\3\2\2\2\33\u00e1\3\2\2\2\35\u00e5\3\2\2\2\37\u00f6")
        buf.write("\3\2\2\2!\u00f8\3\2\2\2#\u00fa\3\2\2\2%\u0100\3\2\2\2")
        buf.write("\'\u0102\3\2\2\2)\u010a\3\2\2\2+\u010c\3\2\2\2-\u0113")
        buf.write("\3\2\2\2/\u0117\3\2\2\2\61\u011c\3\2\2\2\63\u0122\3\2")
        buf.write("\2\2\65\u012b\3\2\2\2\67\u012e\3\2\2\29\u0133\3\2\2\2")
        buf.write(";\u013a\3\2\2\2=\u0142\3\2\2\2?\u0148\3\2\2\2A\u014f\3")
        buf.write("\2\2\2C\u0158\3\2\2\2E\u015c\3\2\2\2G\u0165\3\2\2\2I\u0168")
        buf.write("\3\2\2\2K\u0172\3\2\2\2M\u0179\3\2\2\2O\u017e\3\2\2\2")
        buf.write("Q\u0184\3\2\2\2S\u0189\3\2\2\2U\u018f\3\2\2\2W\u0195\3")
        buf.write("\2\2\2Y\u0199\3\2\2\2[\u019f\3\2\2\2]\u01a7\3\2\2\2_\u01ae")
        buf.write("\3\2\2\2a\u01b0\3\2\2\2c\u01b3\3\2\2\2e\u01b5\3\2\2\2")
        buf.write("g\u01b8\3\2\2\2i\u01ba\3\2\2\2k\u01bd\3\2\2\2m\u01bf\3")
        buf.write("\2\2\2o\u01c2\3\2\2\2q\u01c4\3\2\2\2s\u01c6\3\2\2\2u\u01c9")
        buf.write("\3\2\2\2w\u01cc\3\2\2\2y\u01cf\3\2\2\2{\u01d2\3\2\2\2")
        buf.write("}\u01d4\3\2\2\2\177\u01d6\3\2\2\2\u0081\u01d9\3\2\2\2")
        buf.write("\u0083\u01dc\3\2\2\2\u0085\u01e0\3\2\2\2\u0087\u01e3\3")
        buf.write("\2\2\2\u0089\u01e6\3\2\2\2\u008b\u01ea\3\2\2\2\u008d\u01ee")
        buf.write("\3\2\2\2\u008f\u01f0\3\2\2\2\u0091\u01f2\3\2\2\2\u0093")
        buf.write("\u01f4\3\2\2\2\u0095\u01f6\3\2\2\2\u0097\u01f8\3\2\2\2")
        buf.write("\u0099\u01fa\3\2\2\2\u009b\u01fc\3\2\2\2\u009d\u01fe\3")
        buf.write("\2\2\2\u009f\u0200\3\2\2\2\u00a1\u0202\3\2\2\2\u00a3\u020c")
        buf.write("\3\2\2\2\u00a5\u020e\3\2\2\2\u00a7\u0217\3\2\2\2\u00a9")
        buf.write("\u0222\3\2\2\2\u00ab\u0226\3\2\2\2\u00ad\u0228\3\2\2\2")
        buf.write("\u00af\u0235\3\2\2\2\u00b1\u0239\3\2\2\2\u00b3\u023b\3")
        buf.write("\2\2\2\u00b5\u0247\3\2\2\2\u00b7\u0251\3\2\2\2\u00b9\u00ba")
        buf.write("\t\2\2\2\u00ba\4\3\2\2\2\u00bb\u00bc\t\3\2\2\u00bc\6\3")
        buf.write("\2\2\2\u00bd\u00be\t\4\2\2\u00be\b\3\2\2\2\u00bf\u00c0")
        buf.write("\t\5\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\t\6\2\2\u00c2\f\3")
        buf.write("\2\2\2\u00c3\u00c4\t\7\2\2\u00c4\16\3\2\2\2\u00c5\u00c6")
        buf.write("\t\b\2\2\u00c6\20\3\2\2\2\u00c7\u00c8\5\u00a3R\2\u00c8")
        buf.write("\22\3\2\2\2\u00c9\u00ca\5\u0091I\2\u00ca\u00cb\5\u00a3")
        buf.write("R\2\u00cb\24\3\2\2\2\u00cc\u00ce\t\t\2\2\u00cd\u00cf\t")
        buf.write("\n\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\5\u00a3R\2\u00d1\26\3\2\2\2\u00d2")
        buf.write("\u00d3\5\21\t\2\u00d3\u00d4\5\23\n\2\u00d4\u00d9\3\2\2")
        buf.write("\2\u00d5\u00d6\5\21\t\2\u00d6\u00d7\5\u0091I\2\u00d7\u00d9")
        buf.write("\3\2\2\2\u00d8\u00d2\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d9")
        buf.write("\30\3\2\2\2\u00da\u00dd\5\21\t\2\u00db\u00dd\5\27\f\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3")
        buf.write("\2\2\2\u00de\u00df\5\25\13\2\u00df\32\3\2\2\2\u00e0\u00e2")
        buf.write("\t\13\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\34\3\2\2\2\u00e5")
        buf.write("\u00e6\7,\2\2\u00e6\u00e7\7,\2\2\u00e7\u00eb\3\2\2\2\u00e8")
        buf.write("\u00ea\13\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2")
        buf.write("\2\u00eb\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ee")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\36\3\2\2\2\u00f1\u00f3\7\17\2\2\u00f2")
        buf.write("\u00f4\7\f\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2")
        buf.write("\u00f4\u00f7\3\2\2\2\u00f5\u00f7\7\f\2\2\u00f6\u00f1\3")
        buf.write("\2\2\2\u00f6\u00f5\3\2\2\2\u00f7 \3\2\2\2\u00f8\u00f9")
        buf.write("\t\f\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\t\r\2\2\u00fb$\3")
        buf.write("\2\2\2\u00fc\u00fd\7)\2\2\u00fd\u0101\7$\2\2\u00fe\u0101")
        buf.write("\n\16\2\2\u00ff\u0101\5\'\24\2\u0100\u00fc\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101&\3\2\2\2\u0102")
        buf.write("\u0103\7^\2\2\u0103\u0104\t\17\2\2\u0104(\3\2\2\2\u0105")
        buf.write("\u0106\7^\2\2\u0106\u010b\n\17\2\2\u0107\u010b\n\20\2")
        buf.write("\2\u0108\u0109\7)\2\2\u0109\u010b\n\f\2\2\u010a\u0105")
        buf.write("\3\2\2\2\u010a\u0107\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("*\3\2\2\2\u010c\u0110\t\21\2\2\u010d\u010f\t\22\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111,\3\2\2\2\u0112\u0110\3\2\2")
        buf.write("\2\u0113\u0114\7X\2\2\u0114\u0115\7c\2\2\u0115\u0116\7")
        buf.write("t\2\2\u0116.\3\2\2\2\u0117\u0118\7D\2\2\u0118\u0119\7")
        buf.write("q\2\2\u0119\u011a\7f\2\2\u011a\u011b\7{\2\2\u011b\60\3")
        buf.write("\2\2\2\u011c\u011d\7D\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7c\2\2\u0120\u0121\7m\2\2\u0121\62")
        buf.write("\3\2\2\2\u0122\u0123\7E\2\2\u0123\u0124\7q\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7v\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7w\2\2\u0129\u012a\7g\2\2\u012a\64")
        buf.write("\3\2\2\2\u012b\u012c\7F\2\2\u012c\u012d\7q\2\2\u012d\66")
        buf.write("\3\2\2\2\u012e\u012f\7G\2\2\u012f\u0130\7n\2\2\u0130\u0131")
        buf.write("\7u\2\2\u0131\u0132\7g\2\2\u01328\3\2\2\2\u0133\u0134")
        buf.write("\7G\2\2\u0134\u0135\7n\2\2\u0135\u0136\7u\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137\u0138\7K\2\2\u0138\u0139\7h\2\2\u0139:\3")
        buf.write("\2\2\2\u013a\u013b\7G\2\2\u013b\u013c\7p\2\2\u013c\u013d")
        buf.write("\7f\2\2\u013d\u013e\7D\2\2\u013e\u013f\7q\2\2\u013f\u0140")
        buf.write("\7f\2\2\u0140\u0141\7{\2\2\u0141<\3\2\2\2\u0142\u0143")
        buf.write("\7G\2\2\u0143\u0144\7p\2\2\u0144\u0145\7f\2\2\u0145\u0146")
        buf.write("\7K\2\2\u0146\u0147\7h\2\2\u0147>\3\2\2\2\u0148\u0149")
        buf.write("\7G\2\2\u0149\u014a\7p\2\2\u014a\u014b\7f\2\2\u014b\u014c")
        buf.write("\7H\2\2\u014c\u014d\7q\2\2\u014d\u014e\7t\2\2\u014e@\3")
        buf.write("\2\2\2\u014f\u0150\7G\2\2\u0150\u0151\7p\2\2\u0151\u0152")
        buf.write("\7f\2\2\u0152\u0153\7Y\2\2\u0153\u0154\7j\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7n\2\2\u0156\u0157\7g\2\2\u0157B\3")
        buf.write("\2\2\2\u0158\u0159\7H\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015bD\3\2\2\2\u015c\u015d\7H\2\2\u015d\u015e")
        buf.write("\7w\2\2\u015e\u015f\7p\2\2\u015f\u0160\7e\2\2\u0160\u0161")
        buf.write("\7v\2\2\u0161\u0162\7k\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164F\3\2\2\2\u0165\u0166\7K\2\2\u0166\u0167")
        buf.write("\7h\2\2\u0167H\3\2\2\2\u0168\u0169\7R\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7t\2\2\u016b\u016c\7c\2\2\u016c\u016d")
        buf.write("\7o\2\2\u016d\u016e\7g\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7g\2\2\u0170\u0171\7t\2\2\u0171J\3\2\2\2\u0172\u0173")
        buf.write("\7T\2\2\u0173\u0174\7g\2\2\u0174\u0175\7v\2\2\u0175\u0176")
        buf.write("\7w\2\2\u0176\u0177\7t\2\2\u0177\u0178\7p\2\2\u0178L\3")
        buf.write("\2\2\2\u0179\u017a\7V\2\2\u017a\u017b\7j\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7p\2\2\u017dN\3\2\2\2\u017e\u017f")
        buf.write("\7Y\2\2\u017f\u0180\7j\2\2\u0180\u0181\7k\2\2\u0181\u0182")
        buf.write("\7n\2\2\u0182\u0183\7g\2\2\u0183P\3\2\2\2\u0184\u0185")
        buf.write("\7V\2\2\u0185\u0186\7t\2\2\u0186\u0187\7w\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188R\3\2\2\2\u0189\u018a\7H\2\2\u018a\u018b")
        buf.write("\7c\2\2\u018b\u018c\7n\2\2\u018c\u018d\7u\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018eT\3\2\2\2\u018f\u0190\7G\2\2\u0190\u0191")
        buf.write("\7p\2\2\u0191\u0192\7f\2\2\u0192\u0193\7F\2\2\u0193\u0194")
        buf.write("\7q\2\2\u0194V\3\2\2\2\u0195\u0196\7k\2\2\u0196\u0197")
        buf.write("\7p\2\2\u0197\u0198\7v\2\2\u0198X\3\2\2\2\u0199\u019a")
        buf.write("\7h\2\2\u019a\u019b\7n\2\2\u019b\u019c\7q\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7v\2\2\u019eZ\3\2\2\2\u019f\u01a0")
        buf.write("\7d\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3")
        buf.write("\7n\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6\\\3\2\2\2\u01a7\u01a8\7u\2\2\u01a8\u01a9")
        buf.write("\7v\2\2\u01a9\u01aa\7t\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac")
        buf.write("\7p\2\2\u01ac\u01ad\7i\2\2\u01ad^\3\2\2\2\u01ae\u01af")
        buf.write("\7-\2\2\u01af`\3\2\2\2\u01b0\u01b1\7-\2\2\u01b1\u01b2")
        buf.write("\7\60\2\2\u01b2b\3\2\2\2\u01b3\u01b4\7/\2\2\u01b4d\3\2")
        buf.write("\2\2\u01b5\u01b6\7/\2\2\u01b6\u01b7\7\60\2\2\u01b7f\3")
        buf.write("\2\2\2\u01b8\u01b9\7,\2\2\u01b9h\3\2\2\2\u01ba\u01bb\7")
        buf.write(",\2\2\u01bb\u01bc\7\60\2\2\u01bcj\3\2\2\2\u01bd\u01be")
        buf.write("\7^\2\2\u01bel\3\2\2\2\u01bf\u01c0\7^\2\2\u01c0\u01c1")
        buf.write("\7\60\2\2\u01c1n\3\2\2\2\u01c2\u01c3\7\'\2\2\u01c3p\3")
        buf.write("\2\2\2\u01c4\u01c5\7#\2\2\u01c5r\3\2\2\2\u01c6\u01c7\7")
        buf.write("(\2\2\u01c7\u01c8\7(\2\2\u01c8t\3\2\2\2\u01c9\u01ca\7")
        buf.write("~\2\2\u01ca\u01cb\7~\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7")
        buf.write("?\2\2\u01cd\u01ce\7?\2\2\u01cex\3\2\2\2\u01cf\u01d0\7")
        buf.write("#\2\2\u01d0\u01d1\7?\2\2\u01d1z\3\2\2\2\u01d2\u01d3\7")
        buf.write(">\2\2\u01d3|\3\2\2\2\u01d4\u01d5\7@\2\2\u01d5~\3\2\2\2")
        buf.write("\u01d6\u01d7\7@\2\2\u01d7\u01d8\7?\2\2\u01d8\u0080\3\2")
        buf.write("\2\2\u01d9\u01da\7>\2\2\u01da\u01db\7?\2\2\u01db\u0082")
        buf.write("\3\2\2\2\u01dc\u01dd\7?\2\2\u01dd\u01de\7\61\2\2\u01de")
        buf.write("\u01df\7?\2\2\u01df\u0084\3\2\2\2\u01e0\u01e1\7>\2\2\u01e1")
        buf.write("\u01e2\7\60\2\2\u01e2\u0086\3\2\2\2\u01e3\u01e4\7@\2\2")
        buf.write("\u01e4\u01e5\7\60\2\2\u01e5\u0088\3\2\2\2\u01e6\u01e7")
        buf.write("\7@\2\2\u01e7\u01e8\7?\2\2\u01e8\u01e9\7\60\2\2\u01e9")
        buf.write("\u008a\3\2\2\2\u01ea\u01eb\7>\2\2\u01eb\u01ec\7?\2\2\u01ec")
        buf.write("\u01ed\7\60\2\2\u01ed\u008c\3\2\2\2\u01ee\u01ef\7=\2\2")
        buf.write("\u01ef\u008e\3\2\2\2\u01f0\u01f1\7<\2\2\u01f1\u0090\3")
        buf.write("\2\2\2\u01f2\u01f3\7\60\2\2\u01f3\u0092\3\2\2\2\u01f4")
        buf.write("\u01f5\7.\2\2\u01f5\u0094\3\2\2\2\u01f6\u01f7\7*\2\2\u01f7")
        buf.write("\u0096\3\2\2\2\u01f8\u01f9\7+\2\2\u01f9\u0098\3\2\2\2")
        buf.write("\u01fa\u01fb\7]\2\2\u01fb\u009a\3\2\2\2\u01fc\u01fd\7")
        buf.write("_\2\2\u01fd\u009c\3\2\2\2\u01fe\u01ff\7}\2\2\u01ff\u009e")
        buf.write("\3\2\2\2\u0200\u0201\7\177\2\2\u0201\u00a0\3\2\2\2\u0202")
        buf.write("\u0203\7?\2\2\u0203\u00a2\3\2\2\2\u0204\u0208\5\7\4\2")
        buf.write("\u0205\u0207\5\5\3\2\u0206\u0205\3\2\2\2\u0207\u020a\3")
        buf.write("\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020d")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d\t\23\2\2\u020c")
        buf.write("\u0204\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u00a4\3\2\2\2")
        buf.write("\u020e\u020f\t\23\2\2\u020f\u0210\t\24\2\2\u0210\u0214")
        buf.write("\5\17\b\2\u0211\u0213\5\r\7\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u00a6\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\t")
        buf.write("\23\2\2\u0218\u0219\t\25\2\2\u0219\u021d\5\13\6\2\u021a")
        buf.write("\u021c\5\t\5\2\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u00a8\3")
        buf.write("\2\2\2\u021f\u021d\3\2\2\2\u0220\u0223\5\27\f\2\u0221")
        buf.write("\u0223\5\31\r\2\u0222\u0220\3\2\2\2\u0222\u0221\3\2\2")
        buf.write("\2\u0223\u00aa\3\2\2\2\u0224\u0227\5Q)\2\u0225\u0227\5")
        buf.write("S*\2\u0226\u0224\3\2\2\2\u0226\u0225\3\2\2\2\u0227\u00ac")
        buf.write("\3\2\2\2\u0228\u022c\5!\21\2\u0229\u022b\5%\23\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c\3")
        buf.write("\2\2\2\u022f\u0230\5!\21\2\u0230\u0231\bW\2\2\u0231\u00ae")
        buf.write("\3\2\2\2\u0232\u0236\5\35\17\2\u0233\u0236\5\33\16\2\u0234")
        buf.write("\u0236\5\37\20\2\u0235\u0232\3\2\2\2\u0235\u0233\3\2\2")
        buf.write("\2\u0235\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0238")
        buf.write("\bX\3\2\u0238\u00b0\3\2\2\2\u0239\u023a\13\2\2\2\u023a")
        buf.write("\u00b2\3\2\2\2\u023b\u023f\7$\2\2\u023c\u023e\5%\23\2")
        buf.write("\u023d\u023c\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d\3")
        buf.write("\2\2\2\u023f\u0240\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f")
        buf.write("\3\2\2\2\u0242\u0244\t\26\2\2\u0243\u0242\3\2\2\2\u0244")
        buf.write("\u0245\3\2\2\2\u0245\u0246\bZ\4\2\u0246\u00b4\3\2\2\2")
        buf.write("\u0247\u024b\7$\2\2\u0248\u024a\5%\23\2\u0249\u0248\3")
        buf.write("\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u024f\5)\25\2\u024f\u0250\b[\5\2\u0250\u00b6\3\2\2\2")
        buf.write("\u0251\u0252\7,\2\2\u0252\u0253\7,\2\2\u0253\u0257\3\2")
        buf.write("\2\2\u0254\u0256\13\2\2\2\u0255\u0254\3\2\2\2\u0256\u0259")
        buf.write("\3\2\2\2\u0257\u0258\3\2\2\2\u0257\u0255\3\2\2\2\u0258")
        buf.write("\u00b8\3\2\2\2\u0259\u0257\3\2\2\2\31\2\u00ce\u00d8\u00dc")
        buf.write("\u00e3\u00eb\u00f3\u00f6\u0100\u010a\u0110\u0208\u020c")
        buf.write("\u0214\u021d\u0222\u0226\u022c\u0235\u023f\u0243\u024b")
        buf.write("\u0257\6\3W\2\b\2\2\3Z\3\3[\4")
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
    SKIP_ = 67
    ERROR_CHAR = 68
    UNCLOSE_STRING = 69
    ILLEGAL_ESCAPE = 70
    UNTERMINATED_COMMENT = 71

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
            "BOOLEAN", "STRING", "SKIP_", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LETTER", "DIGIT", "NON_ZERO_DIGIT", "OCT_DIGIT", "NON_OCT_DIGIT", 
                  "HEX_DIGIT", "NON_HEX_DIGIT", "INT_PART", "DEC_PART", 
                  "EXPONENT", "POINT_FLOAT", "EXPONENT_FLOAT", "WS", "COMMENT", 
                  "NEWLINE", "DOUBLE_QUOTE", "SINGLE_QUOTE", "STRING_CONTENT", 
                  "ESCAPE_SEQ", "ESCAPE_ILLEGAL", "ID", "VAR", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", "INT_TYPE", 
                  "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "ADD", "ADD_F", 
                  "SUB", "SUB_F", "MULTI", "MULTI_F", "DIV", "DIV_F", "MOD", 
                  "NOT", "ANDAND", "OROR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "GREATER_EQUAL", "LESS_EQUAL", "NOT_EQUAL_F", 
                  "LESS_THAN_F", "GREATER_THAN_F", "GREATER_EQUAL_F", "LESS_EQUAL_F", 
                  "SEMI", "COLON", "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                  "ASSIGN", "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", 
                  "FLOAT", "BOOLEAN", "STRING", "SKIP_", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            actions[85] = self.STRING_action 
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
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
            	
     


