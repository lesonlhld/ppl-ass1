# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u0264\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\7\2\u00b3\n\2\f\2\16\2\u00b6")
        buf.write("\13\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\5@\u01b8\n@\3A\3A\3A\7A\u01bd\n")
        buf.write("A\fA\16A\u01c0\13A\5A\u01c2\nA\3B\3B\3B\3B\3C\3C\3C\3")
        buf.write("C\3D\3D\5D\u01ce\nD\3D\3D\3D\5D\u01d3\nD\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\7H\u01dd\nH\fH\16H\u01e0\13H\3I\3I\7I\u01e4")
        buf.write("\nI\fI\16I\u01e7\13I\3J\6J\u01ea\nJ\rJ\16J\u01eb\3K\3")
        buf.write("K\3K\7K\u01f1\nK\fK\16K\u01f4\13K\3L\3L\3L\5L\u01f9\n")
        buf.write("L\3L\6L\u01fc\nL\rL\16L\u01fd\3M\3M\7M\u0202\nM\fM\16")
        buf.write("M\u0205\13M\3M\3M\3M\3N\3N\3N\3N\5N\u020e\nN\3O\3O\3O")
        buf.write("\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u021e\nO\3P\3P\3")
        buf.write("P\3P\7P\u0224\nP\fP\16P\u0227\13P\3P\3P\3P\3P\3P\3Q\6")
        buf.write("Q\u022f\nQ\rQ\16Q\u0230\3Q\3Q\3R\3R\5R\u0237\nR\3R\5R")
        buf.write("\u023a\nR\3R\3R\3S\3S\3T\3T\7T\u0242\nT\fT\16T\u0245\13")
        buf.write("T\3T\5T\u0248\nT\3T\3T\3U\3U\7U\u024e\nU\fU\16U\u0251")
        buf.write("\13U\3U\3U\3U\3V\3V\3V\3V\5V\u025a\nV\3W\3W\3W\3W\7W\u0260")
        buf.write("\nW\fW\16W\u0263\13W\4\u0225\u0261\2X\3\3\5\2\7\4\t\5")
        buf.write("\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37")
        buf.write("\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33")
        buf.write("\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_")
        buf.write("\60a\61c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?\177@\u0081")
        buf.write("A\u0083B\u0085C\u0087D\u0089\2\u008b\2\u008d\2\u008f\2")
        buf.write("\u0091\2\u0093\2\u0095\2\u0097\2\u0099E\u009b\2\u009d")
        buf.write("\2\u009fF\u00a1G\u00a3H\u00a5I\u00a7J\u00a9K\u00ab\2\u00ad")
        buf.write("L\3\2\22\3\2c|\4\2ZZzz\4\2QQqq\5\2C\\aac|\3\2\62;\3\2")
        buf.write("\63;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\4\2GGgg\6\2\f")
        buf.write("\f$$))^^\5\2\13\f\16\17\"\"\3\3\f\f\t\2))^^ddhhppttvv")
        buf.write("\3\2$$\2\u0277\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\3\u00af\3\2\2\2\5\u00b7\3\2\2\2\7\u00b9\3\2\2\2\t\u00c2")
        buf.write("\3\2\2\2\13\u00c6\3\2\2\2\r\u00d0\3\2\2\2\17\u00d5\3\2")
        buf.write("\2\2\21\u00dd\3\2\2\2\23\u00e2\3\2\2\2\25\u00e8\3\2\2")
        buf.write("\2\27\u00ec\3\2\2\2\31\u00f3\3\2\2\2\33\u00f9\3\2\2\2")
        buf.write("\35\u0102\3\2\2\2\37\u0105\3\2\2\2!\u010b\3\2\2\2#\u0112")
        buf.write("\3\2\2\2%\u0118\3\2\2\2\'\u0121\3\2\2\2)\u0124\3\2\2\2")
        buf.write("+\u012a\3\2\2\2-\u012f\3\2\2\2/\u0136\3\2\2\2\61\u013b")
        buf.write("\3\2\2\2\63\u013d\3\2\2\2\65\u013f\3\2\2\2\67\u0141\3")
        buf.write("\2\2\29\u0143\3\2\2\2;\u0145\3\2\2\2=\u0148\3\2\2\2?\u014b")
        buf.write("\3\2\2\2A\u014e\3\2\2\2C\u0151\3\2\2\2E\u0153\3\2\2\2")
        buf.write("G\u0156\3\2\2\2I\u0159\3\2\2\2K\u015b\3\2\2\2M\u015e\3")
        buf.write("\2\2\2O\u0161\3\2\2\2Q\u0163\3\2\2\2S\u0165\3\2\2\2U\u0168")
        buf.write("\3\2\2\2W\u016b\3\2\2\2Y\u016f\3\2\2\2[\u0172\3\2\2\2")
        buf.write("]\u0175\3\2\2\2_\u0179\3\2\2\2a\u017d\3\2\2\2c\u017f\3")
        buf.write("\2\2\2e\u0181\3\2\2\2g\u0183\3\2\2\2i\u0185\3\2\2\2k\u0187")
        buf.write("\3\2\2\2m\u0189\3\2\2\2o\u018b\3\2\2\2q\u018d\3\2\2\2")
        buf.write("s\u018f\3\2\2\2u\u0191\3\2\2\2w\u0199\3\2\2\2y\u01a0\3")
        buf.write("\2\2\2{\u01a6\3\2\2\2}\u01ae\3\2\2\2\177\u01b7\3\2\2\2")
        buf.write("\u0081\u01c1\3\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01c7\3")
        buf.write("\2\2\2\u0087\u01d2\3\2\2\2\u0089\u01d4\3\2\2\2\u008b\u01d6")
        buf.write("\3\2\2\2\u008d\u01d8\3\2\2\2\u008f\u01da\3\2\2\2\u0091")
        buf.write("\u01e1\3\2\2\2\u0093\u01e9\3\2\2\2\u0095\u01ed\3\2\2\2")
        buf.write("\u0097\u01f5\3\2\2\2\u0099\u01ff\3\2\2\2\u009b\u020d\3")
        buf.write("\2\2\2\u009d\u021d\3\2\2\2\u009f\u021f\3\2\2\2\u00a1\u022e")
        buf.write("\3\2\2\2\u00a3\u0239\3\2\2\2\u00a5\u023d\3\2\2\2\u00a7")
        buf.write("\u023f\3\2\2\2\u00a9\u024b\3\2\2\2\u00ab\u0259\3\2\2\2")
        buf.write("\u00ad\u025b\3\2\2\2\u00af\u00b4\5\5\3\2\u00b0\u00b3\5")
        buf.write("\u0089E\2\u00b1\u00b3\5\u008bF\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\4\3\2\2\2\u00b6\u00b4\3\2\2")
        buf.write("\2\u00b7\u00b8\t\2\2\2\u00b8\6\3\2\2\2\u00b9\u00ba\7H")
        buf.write("\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7e\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\b\3\2\2\2\u00c2\u00c3")
        buf.write("\7X\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7t\2\2\u00c5\n")
        buf.write("\3\2\2\2\u00c6\u00c7\7R\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7o\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\f\3\2\2\2\u00d0\u00d1\7D\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7f\2\2\u00d3\u00d4\7{\2\2\u00d4\16")
        buf.write("\3\2\2\2\u00d5\u00d6\7G\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7f\2\2\u00db\u00dc\7{\2\2\u00dc\20\3\2\2\2\u00dd\u00de")
        buf.write("\7V\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\22\3\2\2\2\u00e2\u00e3\7H\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\24\3\2\2\2\u00e8\u00e9\7H\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7t\2\2\u00eb\26\3\2\2\2\u00ec\u00ed")
        buf.write("\7G\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0")
        buf.write("\7H\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\30")
        buf.write("\3\2\2\2\u00f3\u00f4\7Y\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7g\2\2\u00f8\32")
        buf.write("\3\2\2\2\u00f9\u00fa\7G\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7f\2\2\u00fc\u00fd\7Y\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7g\2\2\u0101\34")
        buf.write("\3\2\2\2\u0102\u0103\7F\2\2\u0103\u0104\7q\2\2\u0104\36")
        buf.write("\3\2\2\2\u0105\u0106\7G\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7f\2\2\u0108\u0109\7F\2\2\u0109\u010a\7q\2\2\u010a \3")
        buf.write("\2\2\2\u010b\u010c\7T\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7v\2\2\u010e\u010f\7w\2\2\u010f\u0110\7t\2\2\u0110\u0111")
        buf.write("\7p\2\2\u0111\"\3\2\2\2\u0112\u0113\7D\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7g\2\2\u0115\u0116\7c\2\2\u0116\u0117")
        buf.write("\7m\2\2\u0117$\3\2\2\2\u0118\u0119\7E\2\2\u0119\u011a")
        buf.write("\7q\2\2\u011a\u011b\7p\2\2\u011b\u011c\7v\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7w\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120&\3\2\2\2\u0121\u0122\7K\2\2\u0122\u0123")
        buf.write("\7h\2\2\u0123(\3\2\2\2\u0124\u0125\7G\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7f\2\2\u0127\u0128\7K\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129*\3\2\2\2\u012a\u012b\7G\2\2\u012b\u012c")
        buf.write("\7n\2\2\u012c\u012d\7u\2\2\u012d\u012e\7g\2\2\u012e,\3")
        buf.write("\2\2\2\u012f\u0130\7G\2\2\u0130\u0131\7n\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132\u0133\7g\2\2\u0133\u0134\7K\2\2\u0134\u0135")
        buf.write("\7h\2\2\u0135.\3\2\2\2\u0136\u0137\7V\2\2\u0137\u0138")
        buf.write("\7j\2\2\u0138\u0139\7g\2\2\u0139\u013a\7p\2\2\u013a\60")
        buf.write("\3\2\2\2\u013b\u013c\7-\2\2\u013c\62\3\2\2\2\u013d\u013e")
        buf.write("\7/\2\2\u013e\64\3\2\2\2\u013f\u0140\7,\2\2\u0140\66\3")
        buf.write("\2\2\2\u0141\u0142\7^\2\2\u01428\3\2\2\2\u0143\u0144\7")
        buf.write("\'\2\2\u0144:\3\2\2\2\u0145\u0146\7-\2\2\u0146\u0147\7")
        buf.write("\60\2\2\u0147<\3\2\2\2\u0148\u0149\7/\2\2\u0149\u014a")
        buf.write("\7\60\2\2\u014a>\3\2\2\2\u014b\u014c\7,\2\2\u014c\u014d")
        buf.write("\7\60\2\2\u014d@\3\2\2\2\u014e\u014f\7^\2\2\u014f\u0150")
        buf.write("\7\60\2\2\u0150B\3\2\2\2\u0151\u0152\7#\2\2\u0152D\3\2")
        buf.write("\2\2\u0153\u0154\7(\2\2\u0154\u0155\7(\2\2\u0155F\3\2")
        buf.write("\2\2\u0156\u0157\7~\2\2\u0157\u0158\7~\2\2\u0158H\3\2")
        buf.write("\2\2\u0159\u015a\7?\2\2\u015aJ\3\2\2\2\u015b\u015c\7?")
        buf.write("\2\2\u015c\u015d\7?\2\2\u015dL\3\2\2\2\u015e\u015f\7#")
        buf.write("\2\2\u015f\u0160\7?\2\2\u0160N\3\2\2\2\u0161\u0162\7>")
        buf.write("\2\2\u0162P\3\2\2\2\u0163\u0164\7@\2\2\u0164R\3\2\2\2")
        buf.write("\u0165\u0166\7>\2\2\u0166\u0167\7?\2\2\u0167T\3\2\2\2")
        buf.write("\u0168\u0169\7@\2\2\u0169\u016a\7?\2\2\u016aV\3\2\2\2")
        buf.write("\u016b\u016c\7?\2\2\u016c\u016d\7\61\2\2\u016d\u016e\7")
        buf.write("?\2\2\u016eX\3\2\2\2\u016f\u0170\7>\2\2\u0170\u0171\7")
        buf.write("\60\2\2\u0171Z\3\2\2\2\u0172\u0173\7@\2\2\u0173\u0174")
        buf.write("\7\60\2\2\u0174\\\3\2\2\2\u0175\u0176\7>\2\2\u0176\u0177")
        buf.write("\7?\2\2\u0177\u0178\7\60\2\2\u0178^\3\2\2\2\u0179\u017a")
        buf.write("\7@\2\2\u017a\u017b\7?\2\2\u017b\u017c\7\60\2\2\u017c")
        buf.write("`\3\2\2\2\u017d\u017e\7*\2\2\u017eb\3\2\2\2\u017f\u0180")
        buf.write("\7+\2\2\u0180d\3\2\2\2\u0181\u0182\7]\2\2\u0182f\3\2\2")
        buf.write("\2\u0183\u0184\7_\2\2\u0184h\3\2\2\2\u0185\u0186\7<\2")
        buf.write("\2\u0186j\3\2\2\2\u0187\u0188\7.\2\2\u0188l\3\2\2\2\u0189")
        buf.write("\u018a\7\60\2\2\u018an\3\2\2\2\u018b\u018c\7=\2\2\u018c")
        buf.write("p\3\2\2\2\u018d\u018e\7}\2\2\u018er\3\2\2\2\u018f\u0190")
        buf.write("\7\177\2\2\u0190t\3\2\2\2\u0191\u0192\7k\2\2\u0192\u0193")
        buf.write("\7p\2\2\u0193\u0194\7v\2\2\u0194\u0195\7g\2\2\u0195\u0196")
        buf.write("\7i\2\2\u0196\u0197\7g\2\2\u0197\u0198\7t\2\2\u0198v\3")
        buf.write("\2\2\2\u0199\u019a\7u\2\2\u019a\u019b\7v\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7i\2\2\u019fx\3\2\2\2\u01a0\u01a1\7h\2\2\u01a1\u01a2")
        buf.write("\7n\2\2\u01a2\u01a3\7q\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5")
        buf.write("\7v\2\2\u01a5z\3\2\2\2\u01a6\u01a7\7d\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad\7p\2\2\u01ad|\3")
        buf.write("\2\2\2\u01ae\u01af\7c\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1")
        buf.write("\7t\2\2\u01b1\u01b2\7c\2\2\u01b2\u01b3\7{\2\2\u01b3~\3")
        buf.write("\2\2\2\u01b4\u01b8\5\u0081A\2\u01b5\u01b8\5\u0085C\2\u01b6")
        buf.write("\u01b8\5\u0083B\2\u01b7\u01b4\3\2\2\2\u01b7\u01b5\3\2")
        buf.write("\2\2\u01b7\u01b6\3\2\2\2\u01b8\u0080\3\2\2\2\u01b9\u01c2")
        buf.write("\7\62\2\2\u01ba\u01be\5\u008dG\2\u01bb\u01bd\5\u008bF")
        buf.write("\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c2\u0082\3\2\2\2\u01c3\u01c4\7\62\2\2\u01c4\u01c5")
        buf.write("\t\3\2\2\u01c5\u01c6\5\u008fH\2\u01c6\u0084\3\2\2\2\u01c7")
        buf.write("\u01c8\7\62\2\2\u01c8\u01c9\t\4\2\2\u01c9\u01ca\5\u0091")
        buf.write("I\2\u01ca\u0086\3\2\2\2\u01cb\u01cd\5\u0095K\2\u01cc\u01ce")
        buf.write("\5\u0097L\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01d3\3\2\2\2\u01cf\u01d0\5\u0093J\2\u01d0\u01d1\5\u0097")
        buf.write("L\2\u01d1\u01d3\3\2\2\2\u01d2\u01cb\3\2\2\2\u01d2\u01cf")
        buf.write("\3\2\2\2\u01d3\u0088\3\2\2\2\u01d4\u01d5\t\5\2\2\u01d5")
        buf.write("\u008a\3\2\2\2\u01d6\u01d7\t\6\2\2\u01d7\u008c\3\2\2\2")
        buf.write("\u01d8\u01d9\t\7\2\2\u01d9\u008e\3\2\2\2\u01da\u01de\t")
        buf.write("\b\2\2\u01db\u01dd\t\t\2\2\u01dc\u01db\3\2\2\2\u01dd\u01e0")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u0090\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e5\t\n\2\2")
        buf.write("\u01e2\u01e4\t\13\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("\u0092\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea\5\u008b")
        buf.write("F\2\u01e9\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u0094\3\2\2\2\u01ed")
        buf.write("\u01ee\5\u0093J\2\u01ee\u01f2\5m\67\2\u01ef\u01f1\5\u0093")
        buf.write("J\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u0096\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f8\t\f\2\2\u01f6\u01f9\5\63\32")
        buf.write("\2\u01f7\u01f9\5\61\31\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa")
        buf.write("\u01fc\5\u008bF\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2")
        buf.write("\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0098")
        buf.write("\3\2\2\2\u01ff\u0203\7$\2\2\u0200\u0202\5\u009bN\2\u0201")
        buf.write("\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u0207\7$\2\2\u0207\u0208\bM\2\2\u0208\u009a")
        buf.write("\3\2\2\2\u0209\u020e\n\r\2\2\u020a\u020e\5\u009dO\2\u020b")
        buf.write("\u020c\7)\2\2\u020c\u020e\7$\2\2\u020d\u0209\3\2\2\2\u020d")
        buf.write("\u020a\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u009c\3\2\2\2")
        buf.write("\u020f\u0210\7^\2\2\u0210\u021e\7)\2\2\u0211\u0212\7^")
        buf.write("\2\2\u0212\u021e\7^\2\2\u0213\u0214\7^\2\2\u0214\u021e")
        buf.write("\7d\2\2\u0215\u0216\7^\2\2\u0216\u021e\7h\2\2\u0217\u0218")
        buf.write("\7^\2\2\u0218\u021e\7t\2\2\u0219\u021a\7^\2\2\u021a\u021e")
        buf.write("\7p\2\2\u021b\u021c\7^\2\2\u021c\u021e\7v\2\2\u021d\u020f")
        buf.write("\3\2\2\2\u021d\u0211\3\2\2\2\u021d\u0213\3\2\2\2\u021d")
        buf.write("\u0215\3\2\2\2\u021d\u0217\3\2\2\2\u021d\u0219\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021e\u009e\3\2\2\2\u021f\u0220\7")
        buf.write(",\2\2\u0220\u0221\7,\2\2\u0221\u0225\3\2\2\2\u0222\u0224")
        buf.write("\13\2\2\2\u0223\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0228\3\2\2\2")
        buf.write("\u0227\u0225\3\2\2\2\u0228\u0229\7,\2\2\u0229\u022a\7")
        buf.write(",\2\2\u022a\u022b\3\2\2\2\u022b\u022c\bP\3\2\u022c\u00a0")
        buf.write("\3\2\2\2\u022d\u022f\t\16\2\2\u022e\u022d\3\2\2\2\u022f")
        buf.write("\u0230\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0231\u0232\3\2\2\2\u0232\u0233\bQ\3\2\u0233\u00a2\3")
        buf.write("\2\2\2\u0234\u0236\7\17\2\2\u0235\u0237\7\f\2\2\u0236")
        buf.write("\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u023a\3\2\2\2")
        buf.write("\u0238\u023a\7\f\2\2\u0239\u0234\3\2\2\2\u0239\u0238\3")
        buf.write("\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c\bR\3\2\u023c\u00a4")
        buf.write("\3\2\2\2\u023d\u023e\13\2\2\2\u023e\u00a6\3\2\2\2\u023f")
        buf.write("\u0243\7$\2\2\u0240\u0242\5\u009bN\2\u0241\u0240\3\2\2")
        buf.write("\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0246")
        buf.write("\u0248\t\17\2\2\u0247\u0246\3\2\2\2\u0248\u0249\3\2\2")
        buf.write("\2\u0249\u024a\bT\4\2\u024a\u00a8\3\2\2\2\u024b\u024f")
        buf.write("\7$\2\2\u024c\u024e\5\u009bN\2\u024d\u024c\3\2\2\2\u024e")
        buf.write("\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2\u0252\u0253\5")
        buf.write("\u00abV\2\u0253\u0254\bU\5\2\u0254\u00aa\3\2\2\2\u0255")
        buf.write("\u0256\7^\2\2\u0256\u025a\n\20\2\2\u0257\u0258\7)\2\2")
        buf.write("\u0258\u025a\n\21\2\2\u0259\u0255\3\2\2\2\u0259\u0257")
        buf.write("\3\2\2\2\u025a\u00ac\3\2\2\2\u025b\u025c\7,\2\2\u025c")
        buf.write("\u025d\7,\2\2\u025d\u0261\3\2\2\2\u025e\u0260\13\2\2\2")
        buf.write("\u025f\u025e\3\2\2\2\u0260\u0263\3\2\2\2\u0261\u0262\3")
        buf.write("\2\2\2\u0261\u025f\3\2\2\2\u0262\u00ae\3\2\2\2\u0263\u0261")
        buf.write("\3\2\2\2\34\2\u00b2\u00b4\u01b7\u01be\u01c1\u01cd\u01d2")
        buf.write("\u01de\u01e5\u01eb\u01f2\u01f8\u01fd\u0203\u020d\u021d")
        buf.write("\u0225\u0230\u0236\u0239\u0243\u0247\u024f\u0259\u0261")
        buf.write("\6\3M\2\b\2\2\3T\3\3U\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    FUNCTION = 2
    VAR = 3
    PARAMETER = 4
    BODY = 5
    ENDBODY = 6
    TRUE = 7
    FALSE = 8
    FOR = 9
    ENDFOR = 10
    WHILE = 11
    ENDWHILE = 12
    DO = 13
    ENDDO = 14
    RETURN = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ENDIF = 19
    ELSE = 20
    ELSEIF = 21
    THEN = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    ADDFLOAT = 28
    SUBFLOAT = 29
    MULFLOAT = 30
    DIVFLOAT = 31
    NOT = 32
    AND = 33
    OR = 34
    ASSIGN = 35
    EQUAL = 36
    NOTEQUAL = 37
    LT = 38
    GT = 39
    LTE = 40
    GTE = 41
    NOTEQUALFLOAT = 42
    LTFLOAT = 43
    GTFLOAT = 44
    LTEFLOAT = 45
    GTEFLOAT = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    Colon = 51
    Comma = 52
    DOT = 53
    Semi = 54
    LCB = 55
    RCB = 56
    INTEGERTYPE = 57
    STRINGTYPE = 58
    FLOATTYPE = 59
    BOOLEANTYPE = 60
    ARRAYTYPE = 61
    IntegerLiteral = 62
    DecimalLiteral = 63
    HexadecimalLiteral = 64
    OctalLiteral = 65
    FloatLiteral = 66
    StringLiteral = 67
    COMMENT = 68
    Whitespace = 69
    Newline = 70
    ERROR_CHAR = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73
    UNTERMINATED_COMMENT = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Function'", "'Var'", "'Parameter'", "'Body'", "'EndBody'", 
            "'True'", "'False'", "'For'", "'EndFor'", "'While'", "'EndWhile'", 
            "'Do'", "'EndDo'", "'Return'", "'Break'", "'Continue'", "'If'", 
            "'EndIf'", "'Else'", "'ElseIf'", "'Then'", "'+'", "'-'", "'*'", 
            "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", "'&&'", 
            "'||'", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", 
            "']'", "':'", "','", "'.'", "';'", "'{'", "'}'", "'integer'", 
            "'string'", "'float'", "'boolean'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "FUNCTION", "VAR", "PARAMETER", "BODY", "ENDBODY", "TRUE", 
            "FALSE", "FOR", "ENDFOR", "WHILE", "ENDWHILE", "DO", "ENDDO", 
            "RETURN", "BREAK", "CONTINUE", "IF", "ENDIF", "ELSE", "ELSEIF", 
            "THEN", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDFLOAT", "SUBFLOAT", 
            "MULFLOAT", "DIVFLOAT", "NOT", "AND", "OR", "ASSIGN", "EQUAL", 
            "NOTEQUAL", "LT", "GT", "LTE", "GTE", "NOTEQUALFLOAT", "LTFLOAT", 
            "GTFLOAT", "LTEFLOAT", "GTEFLOAT", "LP", "RP", "LSB", "RSB", 
            "Colon", "Comma", "DOT", "Semi", "LCB", "RCB", "INTEGERTYPE", 
            "STRINGTYPE", "FLOATTYPE", "BOOLEANTYPE", "ARRAYTYPE", "IntegerLiteral", 
            "DecimalLiteral", "HexadecimalLiteral", "OctalLiteral", "FloatLiteral", 
            "StringLiteral", "COMMENT", "Whitespace", "Newline", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "LOWERCASELETTER", "FUNCTION", "VAR", "PARAMETER", 
                  "BODY", "ENDBODY", "TRUE", "FALSE", "FOR", "ENDFOR", "WHILE", 
                  "ENDWHILE", "DO", "ENDDO", "RETURN", "BREAK", "CONTINUE", 
                  "IF", "ENDIF", "ELSE", "ELSEIF", "THEN", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "ADDFLOAT", "SUBFLOAT", "MULFLOAT", 
                  "DIVFLOAT", "NOT", "AND", "OR", "ASSIGN", "EQUAL", "NOTEQUAL", 
                  "LT", "GT", "LTE", "GTE", "NOTEQUALFLOAT", "LTFLOAT", 
                  "GTFLOAT", "LTEFLOAT", "GTEFLOAT", "LP", "RP", "LSB", 
                  "RSB", "Colon", "Comma", "DOT", "Semi", "LCB", "RCB", 
                  "INTEGERTYPE", "STRINGTYPE", "FLOATTYPE", "BOOLEANTYPE", 
                  "ARRAYTYPE", "IntegerLiteral", "DecimalLiteral", "HexadecimalLiteral", 
                  "OctalLiteral", "FloatLiteral", "NONDIGIT", "DIGIT", "NONZERODIGIT", 
                  "HEXADECIMALDIGIT", "OCTALDIGIT", "DigitSequence", "Fractional", 
                  "Exponent", "StringLiteral", "STRING_CHAR", "ESC", "COMMENT", 
                  "Whitespace", "Newline", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT" ]

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
            actions[75] = self.StringLiteral_action 
            actions[82] = self.UNCLOSE_STRING_action 
            actions[83] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = (self.text)[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = (self.text)[1:]
                    if self.text[-1] == '\n':
                        self.text = (self.text)[:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = (self.text)[1:]
                
     


