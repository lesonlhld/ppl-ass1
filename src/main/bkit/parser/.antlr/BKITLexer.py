# Generated from d:\PPL\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u028f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\26\3\26\7\26\u011b\n\26\f\26\16\26\u011e\13\26\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u0124\n\27\3\30\3\30\3\30\5\30\u0129")
        buf.write("\n\30\3\30\3\30\3\31\3\31\7\31\u012f\n\31\f\31\16\31\u0132")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3")
        buf.write(">\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3")
        buf.write("E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3")
        buf.write("S\3T\3T\3U\3U\7U\u0227\nU\fU\16U\u022a\13U\3U\5U\u022d")
        buf.write("\nU\3V\3V\3V\3V\7V\u0233\nV\fV\16V\u0236\13V\3W\3W\3W")
        buf.write("\3W\7W\u023c\nW\fW\16W\u023f\13W\3X\3X\5X\u0243\nX\3Y")
        buf.write("\3Y\5Y\u0247\nY\3Z\3Z\7Z\u024b\nZ\fZ\16Z\u024e\13Z\3Z")
        buf.write("\3Z\3Z\3[\3[\3[\3[\3[\7[\u0258\n[\f[\16[\u025b\13[\3[")
        buf.write("\3[\3[\5[\u0260\n[\3\\\3\\\6\\\u0264\n\\\r\\\16\\\u0265")
        buf.write("\3]\3]\3]\5]\u026b\n]\3]\3]\3^\3^\3_\3_\7_\u0273\n_\f")
        buf.write("_\16_\u0276\13_\3_\5_\u0279\n_\3_\3_\3`\3`\7`\u027f\n")
        buf.write("`\f`\16`\u0282\13`\3`\3`\3`\3a\3a\3a\3a\7a\u028b\na\f")
        buf.write("a\16a\u028e\13a\5\u00f5\u024c\u028c\2b\3\2\5\2\7\2\t\2")
        buf.write("\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2")
        buf.write("!\2#\2%\2\'\2)\2+\2-\2/\2\61\3\63\4\65\5\67\69\7;\b=\t")
        buf.write("?\nA\13C\fE\rG\16I\17K\20M\21O\22Q\23S\24U\25W\26Y\27")
        buf.write("[\30]\31_\32a\33c\34e\35g\36i\37k m!o\"q#s$u%w&y\'{(}")
        buf.write(")\177*\u0081+\u0083,\u0085-\u0087.\u0089/\u008b\60\u008d")
        buf.write("\61\u008f\62\u0091\63\u0093\64\u0095\65\u0097\66\u0099")
        buf.write("\67\u009b8\u009d9\u009f:\u00a1;\u00a3<\u00a5=\u00a7>\u00a9")
        buf.write("?\u00ab@\u00adA\u00afB\u00b1C\u00b3D\u00b5E\u00b7F\u00b9")
        buf.write("G\u00bbH\u00bdI\u00bfJ\u00c1K\3\2\27\4\2C\\c|\3\2\62;")
        buf.write("\3\2\63;\3\2\629\3\2\639\4\2\62;CH\4\2\63;CH\4\2GGgg\4")
        buf.write("\2--//\5\2\13\f\16\17\"\"\3\2$$\3\2))\7\2\n\f\16\17$$")
        buf.write("))^^\n\2$$))^^ddhhppttvv\3\2^^\3\2c|\6\2\62;C\\aac|\3")
        buf.write("\2\62\62\4\2ZZzz\4\2QQqq\5\3\n\f\16\17^^\2\u0297\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\3\u00c3")
        buf.write("\3\2\2\2\5\u00c5\3\2\2\2\7\u00c7\3\2\2\2\t\u00c9\3\2\2")
        buf.write("\2\13\u00cb\3\2\2\2\r\u00cd\3\2\2\2\17\u00cf\3\2\2\2\21")
        buf.write("\u00d1\3\2\2\2\23\u00d3\3\2\2\2\25\u00d6\3\2\2\2\27\u00e2")
        buf.write("\3\2\2\2\31\u00e6\3\2\2\2\33\u00eb\3\2\2\2\35\u00ef\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0102\3\2\2\2#\u0104\3\2\2\2")
        buf.write("%\u010a\3\2\2\2\'\u010c\3\2\2\2)\u0114\3\2\2\2+\u0116")
        buf.write("\3\2\2\2-\u0123\3\2\2\2/\u0125\3\2\2\2\61\u012c\3\2\2")
        buf.write("\2\63\u0133\3\2\2\2\65\u0137\3\2\2\2\67\u013c\3\2\2\2")
        buf.write("9\u0142\3\2\2\2;\u014b\3\2\2\2=\u014e\3\2\2\2?\u0153\3")
        buf.write("\2\2\2A\u015a\3\2\2\2C\u0162\3\2\2\2E\u0168\3\2\2\2G\u016f")
        buf.write("\3\2\2\2I\u0178\3\2\2\2K\u017c\3\2\2\2M\u0185\3\2\2\2")
        buf.write("O\u0188\3\2\2\2Q\u0192\3\2\2\2S\u0199\3\2\2\2U\u019e\3")
        buf.write("\2\2\2W\u01a4\3\2\2\2Y\u01a9\3\2\2\2[\u01af\3\2\2\2]\u01b5")
        buf.write("\3\2\2\2_\u01b9\3\2\2\2a\u01bf\3\2\2\2c\u01c7\3\2\2\2")
        buf.write("e\u01ce\3\2\2\2g\u01d0\3\2\2\2i\u01d3\3\2\2\2k\u01d5\3")
        buf.write("\2\2\2m\u01d8\3\2\2\2o\u01da\3\2\2\2q\u01dd\3\2\2\2s\u01df")
        buf.write("\3\2\2\2u\u01e2\3\2\2\2w\u01e4\3\2\2\2y\u01e6\3\2\2\2")
        buf.write("{\u01e9\3\2\2\2}\u01ec\3\2\2\2\177\u01ef\3\2\2\2\u0081")
        buf.write("\u01f2\3\2\2\2\u0083\u01f4\3\2\2\2\u0085\u01f6\3\2\2\2")
        buf.write("\u0087\u01f9\3\2\2\2\u0089\u01fc\3\2\2\2\u008b\u0200\3")
        buf.write("\2\2\2\u008d\u0203\3\2\2\2\u008f\u0206\3\2\2\2\u0091\u020a")
        buf.write("\3\2\2\2\u0093\u020e\3\2\2\2\u0095\u0210\3\2\2\2\u0097")
        buf.write("\u0212\3\2\2\2\u0099\u0214\3\2\2\2\u009b\u0216\3\2\2\2")
        buf.write("\u009d\u0218\3\2\2\2\u009f\u021a\3\2\2\2\u00a1\u021c\3")
        buf.write("\2\2\2\u00a3\u021e\3\2\2\2\u00a5\u0220\3\2\2\2\u00a7\u0222")
        buf.write("\3\2\2\2\u00a9\u022c\3\2\2\2\u00ab\u022e\3\2\2\2\u00ad")
        buf.write("\u0237\3\2\2\2\u00af\u0242\3\2\2\2\u00b1\u0246\3\2\2\2")
        buf.write("\u00b3\u0248\3\2\2\2\u00b5\u025f\3\2\2\2\u00b7\u0261\3")
        buf.write("\2\2\2\u00b9\u026a\3\2\2\2\u00bb\u026e\3\2\2\2\u00bd\u0270")
        buf.write("\3\2\2\2\u00bf\u027c\3\2\2\2\u00c1\u0286\3\2\2\2\u00c3")
        buf.write("\u00c4\t\2\2\2\u00c4\4\3\2\2\2\u00c5\u00c6\t\3\2\2\u00c6")
        buf.write("\6\3\2\2\2\u00c7\u00c8\t\4\2\2\u00c8\b\3\2\2\2\u00c9\u00ca")
        buf.write("\t\5\2\2\u00ca\n\3\2\2\2\u00cb\u00cc\t\6\2\2\u00cc\f\3")
        buf.write("\2\2\2\u00cd\u00ce\t\7\2\2\u00ce\16\3\2\2\2\u00cf\u00d0")
        buf.write("\t\b\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\5\u00a9U\2\u00d2")
        buf.write("\22\3\2\2\2\u00d3\u00d4\5\u0097L\2\u00d4\u00d5\5\u00a9")
        buf.write("U\2\u00d5\24\3\2\2\2\u00d6\u00d8\t\t\2\2\u00d7\u00d9\t")
        buf.write("\n\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\5\u00a9U\2\u00db\26\3\2\2\2\u00dc")
        buf.write("\u00dd\5\21\t\2\u00dd\u00de\5\23\n\2\u00de\u00e3\3\2\2")
        buf.write("\2\u00df\u00e0\5\21\t\2\u00e0\u00e1\5\u0097L\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00dc\3\2\2\2\u00e2\u00df\3\2\2\2\u00e3")
        buf.write("\30\3\2\2\2\u00e4\u00e7\5\21\t\2\u00e5\u00e7\5\27\f\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\u00e9\5\25\13\2\u00e9\32\3\2\2\2\u00ea\u00ec")
        buf.write("\t\13\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\34\3\2\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\u00f1\7,\2\2\u00f1\u00f5\3\2\2\2\u00f2")
        buf.write("\u00f4\13\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7\3\2\2")
        buf.write("\2\u00f5\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f8")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\7,\2\2\u00f9")
        buf.write("\u00fa\7,\2\2\u00fa\36\3\2\2\2\u00fb\u00fd\7\17\2\2\u00fc")
        buf.write("\u00fe\7\f\2\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u0101\7\f\2\2\u0100\u00fb\3")
        buf.write("\2\2\2\u0100\u00ff\3\2\2\2\u0101 \3\2\2\2\u0102\u0103")
        buf.write("\t\f\2\2\u0103\"\3\2\2\2\u0104\u0105\t\r\2\2\u0105$\3")
        buf.write("\2\2\2\u0106\u0107\7)\2\2\u0107\u010b\7$\2\2\u0108\u010b")
        buf.write("\n\16\2\2\u0109\u010b\5\'\24\2\u010a\u0106\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b&\3\2\2\2\u010c")
        buf.write("\u010d\7^\2\2\u010d\u010e\t\17\2\2\u010e(\3\2\2\2\u010f")
        buf.write("\u0110\7^\2\2\u0110\u0115\n\17\2\2\u0111\u0115\n\20\2")
        buf.write("\2\u0112\u0113\7)\2\2\u0113\u0115\n\f\2\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("*\3\2\2\2\u0116\u011c\5-\27\2\u0117\u0118\5\u0099M\2\u0118")
        buf.write("\u0119\5-\27\2\u0119\u011b\3\2\2\2\u011a\u0117\3\2\2\2")
        buf.write("\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d,\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0124")
        buf.write("\5\u00a9U\2\u0120\u0124\5\u00b3Z\2\u0121\u0124\5\u00b1")
        buf.write("Y\2\u0122\u0124\5\u00afX\2\u0123\u011f\3\2\2\2\u0123\u0120")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write(".\3\2\2\2\u0125\u0128\5\u009fP\2\u0126\u0129\5\u00a9U")
        buf.write("\2\u0127\u0129\5\61\31\2\u0128\u0126\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\5\u00a1Q\2\u012b")
        buf.write("\60\3\2\2\2\u012c\u0130\t\21\2\2\u012d\u012f\t\22\2\2")
        buf.write("\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\62\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0133\u0134\7X\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7t\2\2\u0136\64\3\2\2\2\u0137\u0138\7D\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7f\2\2\u013a\u013b\7{\2\2\u013b\66")
        buf.write("\3\2\2\2\u013c\u013d\7D\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7m\2\2\u01418\3")
        buf.write("\2\2\2\u0142\u0143\7E\2\2\u0143\u0144\7q\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7v\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7p\2\2\u0148\u0149\7w\2\2\u0149\u014a\7g\2\2\u014a:\3")
        buf.write("\2\2\2\u014b\u014c\7F\2\2\u014c\u014d\7q\2\2\u014d<\3")
        buf.write("\2\2\2\u014e\u014f\7G\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7u\2\2\u0151\u0152\7g\2\2\u0152>\3\2\2\2\u0153\u0154")
        buf.write("\7G\2\2\u0154\u0155\7n\2\2\u0155\u0156\7u\2\2\u0156\u0157")
        buf.write("\7g\2\2\u0157\u0158\7K\2\2\u0158\u0159\7h\2\2\u0159@\3")
        buf.write("\2\2\2\u015a\u015b\7G\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7f\2\2\u015d\u015e\7D\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7f\2\2\u0160\u0161\7{\2\2\u0161B\3\2\2\2\u0162\u0163")
        buf.write("\7G\2\2\u0163\u0164\7p\2\2\u0164\u0165\7f\2\2\u0165\u0166")
        buf.write("\7K\2\2\u0166\u0167\7h\2\2\u0167D\3\2\2\2\u0168\u0169")
        buf.write("\7G\2\2\u0169\u016a\7p\2\2\u016a\u016b\7f\2\2\u016b\u016c")
        buf.write("\7H\2\2\u016c\u016d\7q\2\2\u016d\u016e\7t\2\2\u016eF\3")
        buf.write("\2\2\2\u016f\u0170\7G\2\2\u0170\u0171\7p\2\2\u0171\u0172")
        buf.write("\7f\2\2\u0172\u0173\7Y\2\2\u0173\u0174\7j\2\2\u0174\u0175")
        buf.write("\7k\2\2\u0175\u0176\7n\2\2\u0176\u0177\7g\2\2\u0177H\3")
        buf.write("\2\2\2\u0178\u0179\7H\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017bJ\3\2\2\2\u017c\u017d\7H\2\2\u017d\u017e")
        buf.write("\7w\2\2\u017e\u017f\7p\2\2\u017f\u0180\7e\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7k\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184L\3\2\2\2\u0185\u0186\7K\2\2\u0186\u0187")
        buf.write("\7h\2\2\u0187N\3\2\2\2\u0188\u0189\7R\2\2\u0189\u018a")
        buf.write("\7c\2\2\u018a\u018b\7t\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7o\2\2\u018d\u018e\7g\2\2\u018e\u018f\7v\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7t\2\2\u0191P\3\2\2\2\u0192\u0193")
        buf.write("\7T\2\2\u0193\u0194\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196")
        buf.write("\7w\2\2\u0196\u0197\7t\2\2\u0197\u0198\7p\2\2\u0198R\3")
        buf.write("\2\2\2\u0199\u019a\7V\2\2\u019a\u019b\7j\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019c\u019d\7p\2\2\u019dT\3\2\2\2\u019e\u019f")
        buf.write("\7Y\2\2\u019f\u01a0\7j\2\2\u01a0\u01a1\7k\2\2\u01a1\u01a2")
        buf.write("\7n\2\2\u01a2\u01a3\7g\2\2\u01a3V\3\2\2\2\u01a4\u01a5")
        buf.write("\7V\2\2\u01a5\u01a6\7t\2\2\u01a6\u01a7\7w\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8X\3\2\2\2\u01a9\u01aa\7H\2\2\u01aa\u01ab")
        buf.write("\7c\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7u\2\2\u01ad\u01ae")
        buf.write("\7g\2\2\u01aeZ\3\2\2\2\u01af\u01b0\7G\2\2\u01b0\u01b1")
        buf.write("\7p\2\2\u01b1\u01b2\7f\2\2\u01b2\u01b3\7F\2\2\u01b3\u01b4")
        buf.write("\7q\2\2\u01b4\\\3\2\2\2\u01b5\u01b6\7k\2\2\u01b6\u01b7")
        buf.write("\7p\2\2\u01b7\u01b8\7v\2\2\u01b8^\3\2\2\2\u01b9\u01ba")
        buf.write("\7h\2\2\u01ba\u01bb\7n\2\2\u01bb\u01bc\7q\2\2\u01bc\u01bd")
        buf.write("\7c\2\2\u01bd\u01be\7v\2\2\u01be`\3\2\2\2\u01bf\u01c0")
        buf.write("\7d\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2\7q\2\2\u01c2\u01c3")
        buf.write("\7n\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7c\2\2\u01c5\u01c6")
        buf.write("\7p\2\2\u01c6b\3\2\2\2\u01c7\u01c8\7u\2\2\u01c8\u01c9")
        buf.write("\7v\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb\7k\2\2\u01cb\u01cc")
        buf.write("\7p\2\2\u01cc\u01cd\7i\2\2\u01cdd\3\2\2\2\u01ce\u01cf")
        buf.write("\7-\2\2\u01cff\3\2\2\2\u01d0\u01d1\7-\2\2\u01d1\u01d2")
        buf.write("\7\60\2\2\u01d2h\3\2\2\2\u01d3\u01d4\7/\2\2\u01d4j\3\2")
        buf.write("\2\2\u01d5\u01d6\7/\2\2\u01d6\u01d7\7\60\2\2\u01d7l\3")
        buf.write("\2\2\2\u01d8\u01d9\7,\2\2\u01d9n\3\2\2\2\u01da\u01db\7")
        buf.write(",\2\2\u01db\u01dc\7\60\2\2\u01dcp\3\2\2\2\u01dd\u01de")
        buf.write("\7^\2\2\u01der\3\2\2\2\u01df\u01e0\7^\2\2\u01e0\u01e1")
        buf.write("\7\60\2\2\u01e1t\3\2\2\2\u01e2\u01e3\7\'\2\2\u01e3v\3")
        buf.write("\2\2\2\u01e4\u01e5\7#\2\2\u01e5x\3\2\2\2\u01e6\u01e7\7")
        buf.write("(\2\2\u01e7\u01e8\7(\2\2\u01e8z\3\2\2\2\u01e9\u01ea\7")
        buf.write("~\2\2\u01ea\u01eb\7~\2\2\u01eb|\3\2\2\2\u01ec\u01ed\7")
        buf.write("?\2\2\u01ed\u01ee\7?\2\2\u01ee~\3\2\2\2\u01ef\u01f0\7")
        buf.write("#\2\2\u01f0\u01f1\7?\2\2\u01f1\u0080\3\2\2\2\u01f2\u01f3")
        buf.write("\7>\2\2\u01f3\u0082\3\2\2\2\u01f4\u01f5\7@\2\2\u01f5\u0084")
        buf.write("\3\2\2\2\u01f6\u01f7\7@\2\2\u01f7\u01f8\7?\2\2\u01f8\u0086")
        buf.write("\3\2\2\2\u01f9\u01fa\7>\2\2\u01fa\u01fb\7?\2\2\u01fb\u0088")
        buf.write("\3\2\2\2\u01fc\u01fd\7?\2\2\u01fd\u01fe\7\61\2\2\u01fe")
        buf.write("\u01ff\7?\2\2\u01ff\u008a\3\2\2\2\u0200\u0201\7>\2\2\u0201")
        buf.write("\u0202\7\60\2\2\u0202\u008c\3\2\2\2\u0203\u0204\7@\2\2")
        buf.write("\u0204\u0205\7\60\2\2\u0205\u008e\3\2\2\2\u0206\u0207")
        buf.write("\7@\2\2\u0207\u0208\7?\2\2\u0208\u0209\7\60\2\2\u0209")
        buf.write("\u0090\3\2\2\2\u020a\u020b\7>\2\2\u020b\u020c\7?\2\2\u020c")
        buf.write("\u020d\7\60\2\2\u020d\u0092\3\2\2\2\u020e\u020f\7=\2\2")
        buf.write("\u020f\u0094\3\2\2\2\u0210\u0211\7<\2\2\u0211\u0096\3")
        buf.write("\2\2\2\u0212\u0213\7\60\2\2\u0213\u0098\3\2\2\2\u0214")
        buf.write("\u0215\7.\2\2\u0215\u009a\3\2\2\2\u0216\u0217\7*\2\2\u0217")
        buf.write("\u009c\3\2\2\2\u0218\u0219\7+\2\2\u0219\u009e\3\2\2\2")
        buf.write("\u021a\u021b\7]\2\2\u021b\u00a0\3\2\2\2\u021c\u021d\7")
        buf.write("_\2\2\u021d\u00a2\3\2\2\2\u021e\u021f\7}\2\2\u021f\u00a4")
        buf.write("\3\2\2\2\u0220\u0221\7\177\2\2\u0221\u00a6\3\2\2\2\u0222")
        buf.write("\u0223\7?\2\2\u0223\u00a8\3\2\2\2\u0224\u0228\5\7\4\2")
        buf.write("\u0225\u0227\5\5\3\2\u0226\u0225\3\2\2\2\u0227\u022a\3")
        buf.write("\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022d")
        buf.write("\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022d\t\23\2\2\u022c")
        buf.write("\u0224\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u00aa\3\2\2\2")
        buf.write("\u022e\u022f\t\23\2\2\u022f\u0230\t\24\2\2\u0230\u0234")
        buf.write("\5\17\b\2\u0231\u0233\5\r\7\2\u0232\u0231\3\2\2\2\u0233")
        buf.write("\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\u00ac\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\t")
        buf.write("\23\2\2\u0238\u0239\t\25\2\2\u0239\u023d\5\13\6\2\u023a")
        buf.write("\u023c\5\t\5\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u00ae\3")
        buf.write("\2\2\2\u023f\u023d\3\2\2\2\u0240\u0243\5\27\f\2\u0241")
        buf.write("\u0243\5\31\r\2\u0242\u0240\3\2\2\2\u0242\u0241\3\2\2")
        buf.write("\2\u0243\u00b0\3\2\2\2\u0244\u0247\5W,\2\u0245\u0247\5")
        buf.write("Y-\2\u0246\u0244\3\2\2\2\u0246\u0245\3\2\2\2\u0247\u00b2")
        buf.write("\3\2\2\2\u0248\u024c\5!\21\2\u0249\u024b\5%\23\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024d\u024f\3\2\2\2\u024e\u024c\3")
        buf.write("\2\2\2\u024f\u0250\5!\21\2\u0250\u0251\bZ\2\2\u0251\u00b4")
        buf.write("\3\2\2\2\u0252\u0253\5\u00a3R\2\u0253\u0259\5\u00b5[\2")
        buf.write("\u0254\u0255\5\u0099M\2\u0255\u0256\5\u00b5[\2\u0256\u0258")
        buf.write("\3\2\2\2\u0257\u0254\3\2\2\2\u0258\u025b\3\2\2\2\u0259")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025c\3\2\2\2")
        buf.write("\u025b\u0259\3\2\2\2\u025c\u025d\5\u00a5S\2\u025d\u0260")
        buf.write("\3\2\2\2\u025e\u0260\5+\26\2\u025f\u0252\3\2\2\2\u025f")
        buf.write("\u025e\3\2\2\2\u0260\u00b6\3\2\2\2\u0261\u0263\5\61\31")
        buf.write("\2\u0262\u0264\5/\30\2\u0263\u0262\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266")
        buf.write("\u00b8\3\2\2\2\u0267\u026b\5\35\17\2\u0268\u026b\5\33")
        buf.write("\16\2\u0269\u026b\5\37\20\2\u026a\u0267\3\2\2\2\u026a")
        buf.write("\u0268\3\2\2\2\u026a\u0269\3\2\2\2\u026b\u026c\3\2\2\2")
        buf.write("\u026c\u026d\b]\3\2\u026d\u00ba\3\2\2\2\u026e\u026f\13")
        buf.write("\2\2\2\u026f\u00bc\3\2\2\2\u0270\u0274\7$\2\2\u0271\u0273")
        buf.write("\5%\23\2\u0272\u0271\3\2\2\2\u0273\u0276\3\2\2\2\u0274")
        buf.write("\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0278\3\2\2\2")
        buf.write("\u0276\u0274\3\2\2\2\u0277\u0279\t\26\2\2\u0278\u0277")
        buf.write("\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u027b\b_\4\2\u027b")
        buf.write("\u00be\3\2\2\2\u027c\u0280\7$\2\2\u027d\u027f\5%\23\2")
        buf.write("\u027e\u027d\3\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e\3")
        buf.write("\2\2\2\u0280\u0281\3\2\2\2\u0281\u0283\3\2\2\2\u0282\u0280")
        buf.write("\3\2\2\2\u0283\u0284\5)\25\2\u0284\u0285\b`\5\2\u0285")
        buf.write("\u00c0\3\2\2\2\u0286\u0287\7,\2\2\u0287\u0288\7,\2\2\u0288")
        buf.write("\u028c\3\2\2\2\u0289\u028b\13\2\2\2\u028a\u0289\3\2\2")
        buf.write("\2\u028b\u028e\3\2\2\2\u028c\u028d\3\2\2\2\u028c\u028a")
        buf.write("\3\2\2\2\u028d\u00c2\3\2\2\2\u028e\u028c\3\2\2\2\37\2")
        buf.write("\u00d8\u00e2\u00e6\u00ed\u00f5\u00fd\u0100\u010a\u0114")
        buf.write("\u011c\u0123\u0128\u0130\u0228\u022c\u0234\u023d\u0242")
        buf.write("\u0246\u024c\u0259\u025f\u0265\u026a\u0274\u0278\u0280")
        buf.write("\u028c\6\3Z\2\b\2\2\3_\3\3`\4")
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
            	
     


