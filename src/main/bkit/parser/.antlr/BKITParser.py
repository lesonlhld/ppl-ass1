# Generated from d:\PPL\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u01a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\7\2f\n\2")
        buf.write("\f\2\16\2i\13\2\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\7\2r\n")
        buf.write("\2\f\2\16\2u\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3~\n\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u0084\n\3\7\3\u0086\n\3\f\3\16\3")
        buf.write("\u0089\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u0092\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009a\n\5\3\5\3\5\5\5\u009e")
        buf.write("\n\5\3\6\3\6\3\6\7\6\u00a3\n\6\f\6\16\6\u00a6\13\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7\u00ae\n\7\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00bc\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\7\r\u00c5\n\r\f\r\16\r\u00c8\13")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00d7\n\16\3\17\7\17\u00da\n\17\f\17\16")
        buf.write("\17\u00dd\13\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00ed\n\21\f\21\16")
        buf.write("\21\u00f0\13\21\3\21\3\21\5\21\u00f4\n\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u0121\n")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\5\31\u0128\n\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\5\32\u012f\n\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0138\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u0141\n\34\f\34\16\34\u0144\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u014d\n\35\f\35\16")
        buf.write("\35\u0150\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36")
        buf.write("\u0159\n\36\f\36\16\36\u015c\13\36\3\37\3\37\3\37\5\37")
        buf.write("\u0161\n\37\3 \3 \3 \3 \5 \u0167\n \3!\3!\3!\3!\3!\7!")
        buf.write("\u016e\n!\f!\16!\u0171\13!\3\"\3\"\5\"\u0175\n\"\3#\3")
        buf.write("#\3#\7#\u017a\n#\f#\16#\u017d\13#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\5$\u0186\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u019e\n+\3,\3,\5,\u01a2")
        buf.write("\n,\3,\2\6\668:@-\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\t\4\2\3\3F")
        buf.write("F\3\2\26\27\3\2!%\3\2\35 \3\2\37 \3\2&(\4\2)/\61\63\2")
        buf.write("\u01ab\2[\3\2\2\2\4x\3\2\2\2\6\u0091\3\2\2\2\b\u009d\3")
        buf.write("\2\2\2\n\u009f\3\2\2\2\f\u00ad\3\2\2\2\16\u00af\3\2\2")
        buf.write("\2\20\u00b1\3\2\2\2\22\u00b4\3\2\2\2\24\u00b7\3\2\2\2")
        buf.write("\26\u00bd\3\2\2\2\30\u00c1\3\2\2\2\32\u00d6\3\2\2\2\34")
        buf.write("\u00db\3\2\2\2\36\u00de\3\2\2\2 \u00e3\3\2\2\2\"\u00f8")
        buf.write("\3\2\2\2$\u0101\3\2\2\2&\u0109\3\2\2\2(\u0110\3\2\2\2")
        buf.write("*\u0117\3\2\2\2,\u011a\3\2\2\2.\u011d\3\2\2\2\60\u0125")
        buf.write("\3\2\2\2\62\u012b\3\2\2\2\64\u0137\3\2\2\2\66\u0139\3")
        buf.write("\2\2\28\u0145\3\2\2\2:\u0151\3\2\2\2<\u0160\3\2\2\2>\u0166")
        buf.write("\3\2\2\2@\u0168\3\2\2\2B\u0174\3\2\2\2D\u0176\3\2\2\2")
        buf.write("F\u0185\3\2\2\2H\u0187\3\2\2\2J\u0189\3\2\2\2L\u018b\3")
        buf.write("\2\2\2N\u018d\3\2\2\2P\u018f\3\2\2\2R\u0191\3\2\2\2T\u019d")
        buf.write("\3\2\2\2V\u01a1\3\2\2\2XZ\7G\2\2YX\3\2\2\2Z]\3\2\2\2[")
        buf.write("Y\3\2\2\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\4\3\2_^")
        buf.write("\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bg\3\2\2\2ca\3\2")
        buf.write("\2\2df\7G\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2")
        buf.write("hm\3\2\2\2ig\3\2\2\2jl\5\22\n\2kj\3\2\2\2lo\3\2\2\2mk")
        buf.write("\3\2\2\2mn\3\2\2\2ns\3\2\2\2om\3\2\2\2pr\7G\2\2qp\3\2")
        buf.write("\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2")
        buf.write("vw\7\2\2\3w\3\3\2\2\2xy\7\4\2\2yz\7\65\2\2z}\5\6\4\2{")
        buf.write("|\7>\2\2|~\5\n\6\2}{\3\2\2\2}~\3\2\2\2~\u0087\3\2\2\2")
        buf.write("\177\u0080\7\67\2\2\u0080\u0083\5\6\4\2\u0081\u0082\7")
        buf.write(">\2\2\u0082\u0084\5\n\6\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0086\3\2\2\2\u0085\177\3\2\2\2\u0086\u0089")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7\64\2")
        buf.write("\2\u008b\5\3\2\2\2\u008c\u0092\7\3\2\2\u008d\u0092\7F")
        buf.write("\2\2\u008e\u008f\t\2\2\2\u008f\u0090\7\67\2\2\u0090\u0092")
        buf.write("\5\6\4\2\u0091\u008c\3\2\2\2\u0091\u008d\3\2\2\2\u0091")
        buf.write("\u008e\3\2\2\2\u0092\7\3\2\2\2\u0093\u009e\7\3\2\2\u0094")
        buf.write("\u009e\7F\2\2\u0095\u009e\5\20\t\2\u0096\u009a\7\3\2\2")
        buf.write("\u0097\u009a\7F\2\2\u0098\u009a\5\20\t\2\u0099\u0096\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\u009c\7\67\2\2\u009c\u009e\5\6\4\2\u009d")
        buf.write("\u0093\3\2\2\2\u009d\u0094\3\2\2\2\u009d\u0095\3\2\2\2")
        buf.write("\u009d\u0099\3\2\2\2\u009e\t\3\2\2\2\u009f\u00a4\5\f\7")
        buf.write("\2\u00a0\u00a1\7\67\2\2\u00a1\u00a3\5\f\7\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\13\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7")
        buf.write("\u00ae\7E\2\2\u00a8\u00ae\7?\2\2\u00a9\u00ae\7B\2\2\u00aa")
        buf.write("\u00ae\5\16\b\2\u00ab\u00ae\7D\2\2\u00ac\u00ae\7\3\2\2")
        buf.write("\u00ad\u00a7\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3")
        buf.write("\2\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\r\3\2\2\2\u00af\u00b0\t\3\2\2\u00b0\17")
        buf.write("\3\2\2\2\u00b1\u00b2\7\3\2\2\u00b2\u00b3\5T+\2\u00b3\21")
        buf.write("\3\2\2\2\u00b4\u00b5\5\24\13\2\u00b5\u00b6\5\30\r\2\u00b6")
        buf.write("\23\3\2\2\2\u00b7\u00b8\7\20\2\2\u00b8\u00b9\7\65\2\2")
        buf.write("\u00b9\u00bb\7\3\2\2\u00ba\u00bc\5\26\f\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\25\3\2\2\2\u00bd\u00be")
        buf.write("\7\22\2\2\u00be\u00bf\7\65\2\2\u00bf\u00c0\5\6\4\2\u00c0")
        buf.write("\27\3\2\2\2\u00c1\u00c2\7\5\2\2\u00c2\u00c6\7\65\2\2\u00c3")
        buf.write("\u00c5\5\4\3\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\5\34\17\2\u00ca")
        buf.write("\u00cb\7\13\2\2\u00cb\u00cc\7\66\2\2\u00cc\31\3\2\2\2")
        buf.write("\u00cd\u00d7\5\36\20\2\u00ce\u00d7\5 \21\2\u00cf\u00d7")
        buf.write("\5\"\22\2\u00d0\u00d7\5&\24\2\u00d1\u00d7\5(\25\2\u00d2")
        buf.write("\u00d7\5*\26\2\u00d3\u00d7\5,\27\2\u00d4\u00d7\5.\30\2")
        buf.write("\u00d5\u00d7\5\60\31\2\u00d6\u00cd\3\2\2\2\u00d6\u00ce")
        buf.write("\3\2\2\2\u00d6\u00cf\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6")
        buf.write("\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\33\3\2")
        buf.write("\2\2\u00d8\u00da\5\32\16\2\u00d9\u00d8\3\2\2\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\35\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5\b\5\2\u00df")
        buf.write("\u00e0\7>\2\2\u00e0\u00e1\5\64\33\2\u00e1\u00e2\7\64\2")
        buf.write("\2\u00e2\37\3\2\2\2\u00e3\u00e4\7\21\2\2\u00e4\u00e5\5")
        buf.write("\64\33\2\u00e5\u00e6\7\24\2\2\u00e6\u00ee\5\34\17\2\u00e7")
        buf.write("\u00e8\7\n\2\2\u00e8\u00e9\5\64\33\2\u00e9\u00ea\7\24")
        buf.write("\2\2\u00ea\u00eb\5\34\17\2\u00eb\u00ed\3\2\2\2\u00ec\u00e7")
        buf.write("\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f3\3\2\2\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f1\u00f2\7\t\2\2\u00f2\u00f4\5\34\17\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f6\7\f\2\2\u00f6\u00f7\7\66\2\2\u00f7!\3\2\2\2\u00f8")
        buf.write("\u00f9\7\17\2\2\u00f9\u00fa\78\2\2\u00fa\u00fb\5$\23\2")
        buf.write("\u00fb\u00fc\79\2\2\u00fc\u00fd\7\b\2\2\u00fd\u00fe\5")
        buf.write("\34\17\2\u00fe\u00ff\7\r\2\2\u00ff\u0100\7\66\2\2\u0100")
        buf.write("#\3\2\2\2\u0101\u0102\7\3\2\2\u0102\u0103\7>\2\2\u0103")
        buf.write("\u0104\5\64\33\2\u0104\u0105\7\67\2\2\u0105\u0106\5\64")
        buf.write("\33\2\u0106\u0107\7\67\2\2\u0107\u0108\5\64\33\2\u0108")
        buf.write("%\3\2\2\2\u0109\u010a\7\25\2\2\u010a\u010b\5\64\33\2\u010b")
        buf.write("\u010c\7\b\2\2\u010c\u010d\5\34\17\2\u010d\u010e\7\16")
        buf.write("\2\2\u010e\u010f\7\66\2\2\u010f\'\3\2\2\2\u0110\u0111")
        buf.write("\7\b\2\2\u0111\u0112\5\34\17\2\u0112\u0113\7\25\2\2\u0113")
        buf.write("\u0114\5\64\33\2\u0114\u0115\7\30\2\2\u0115\u0116\7\66")
        buf.write("\2\2\u0116)\3\2\2\2\u0117\u0118\7\6\2\2\u0118\u0119\7")
        buf.write("\64\2\2\u0119+\3\2\2\2\u011a\u011b\7\7\2\2\u011b\u011c")
        buf.write("\7\64\2\2\u011c-\3\2\2\2\u011d\u011e\7\3\2\2\u011e\u0120")
        buf.write("\78\2\2\u011f\u0121\5D#\2\u0120\u011f\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\79\2\2\u0123")
        buf.write("\u0124\7\64\2\2\u0124/\3\2\2\2\u0125\u0127\7\23\2\2\u0126")
        buf.write("\u0128\5\64\33\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2")
        buf.write("\2\u0128\u0129\3\2\2\2\u0129\u012a\7\64\2\2\u012a\61\3")
        buf.write("\2\2\2\u012b\u012c\7\3\2\2\u012c\u012e\78\2\2\u012d\u012f")
        buf.write("\5D#\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0131\79\2\2\u0131\63\3\2\2\2\u0132\u0133")
        buf.write("\5\66\34\2\u0133\u0134\5P)\2\u0134\u0135\5\66\34\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0138\5\66\34\2\u0137\u0132\3\2\2")
        buf.write("\2\u0137\u0136\3\2\2\2\u0138\65\3\2\2\2\u0139\u013a\b")
        buf.write("\34\1\2\u013a\u013b\58\35\2\u013b\u0142\3\2\2\2\u013c")
        buf.write("\u013d\f\4\2\2\u013d\u013e\5N(\2\u013e\u013f\58\35\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u013c\3\2\2\2\u0141\u0144\3\2\2\2")
        buf.write("\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\67\3\2")
        buf.write("\2\2\u0144\u0142\3\2\2\2\u0145\u0146\b\35\1\2\u0146\u0147")
        buf.write("\5:\36\2\u0147\u014e\3\2\2\2\u0148\u0149\f\4\2\2\u0149")
        buf.write("\u014a\5J&\2\u014a\u014b\5:\36\2\u014b\u014d\3\2\2\2\u014c")
        buf.write("\u0148\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f9\3\2\2\2\u0150\u014e\3\2\2")
        buf.write("\2\u0151\u0152\b\36\1\2\u0152\u0153\5<\37\2\u0153\u015a")
        buf.write("\3\2\2\2\u0154\u0155\f\4\2\2\u0155\u0156\5H%\2\u0156\u0157")
        buf.write("\5<\37\2\u0157\u0159\3\2\2\2\u0158\u0154\3\2\2\2\u0159")
        buf.write("\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b;\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7&\2\2")
        buf.write("\u015e\u0161\5<\37\2\u015f\u0161\5> \2\u0160\u015d\3\2")
        buf.write("\2\2\u0160\u015f\3\2\2\2\u0161=\3\2\2\2\u0162\u0163\5")
        buf.write("L\'\2\u0163\u0164\5> \2\u0164\u0167\3\2\2\2\u0165\u0167")
        buf.write("\5@!\2\u0166\u0162\3\2\2\2\u0166\u0165\3\2\2\2\u0167?")
        buf.write("\3\2\2\2\u0168\u0169\b!\1\2\u0169\u016a\5B\"\2\u016a\u016f")
        buf.write("\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016e\5T+\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170A\3\2\2\2\u0171\u016f\3\2\2\2\u0172")
        buf.write("\u0175\5\62\32\2\u0173\u0175\5F$\2\u0174\u0172\3\2\2\2")
        buf.write("\u0174\u0173\3\2\2\2\u0175C\3\2\2\2\u0176\u017b\5\64\33")
        buf.write("\2\u0177\u0178\7\67\2\2\u0178\u017a\5\64\33\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017cE\3\2\2\2\u017d\u017b\3\2\2\2\u017e")
        buf.write("\u0186\5\f\7\2\u017f\u0180\78\2\2\u0180\u0181\5\64\33")
        buf.write("\2\u0181\u0182\79\2\2\u0182\u0186\3\2\2\2\u0183\u0186")
        buf.write("\5R*\2\u0184\u0186\7F\2\2\u0185\u017e\3\2\2\2\u0185\u017f")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("G\3\2\2\2\u0187\u0188\t\4\2\2\u0188I\3\2\2\2\u0189\u018a")
        buf.write("\t\5\2\2\u018aK\3\2\2\2\u018b\u018c\t\6\2\2\u018cM\3\2")
        buf.write("\2\2\u018d\u018e\t\7\2\2\u018eO\3\2\2\2\u018f\u0190\t")
        buf.write("\b\2\2\u0190Q\3\2\2\2\u0191\u0192\5V,\2\u0192\u0193\5")
        buf.write("T+\2\u0193S\3\2\2\2\u0194\u0195\7:\2\2\u0195\u0196\5\64")
        buf.write("\33\2\u0196\u0197\7;\2\2\u0197\u019e\3\2\2\2\u0198\u0199")
        buf.write("\7:\2\2\u0199\u019a\5\64\33\2\u019a\u019b\7;\2\2\u019b")
        buf.write("\u019c\5T+\2\u019c\u019e\3\2\2\2\u019d\u0194\3\2\2\2\u019d")
        buf.write("\u0198\3\2\2\2\u019eU\3\2\2\2\u019f\u01a2\7\3\2\2\u01a0")
        buf.write("\u01a2\5\62\32\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2")
        buf.write("\2\u01a2W\3\2\2\2$[agms}\u0083\u0087\u0091\u0099\u009d")
        buf.write("\u00a4\u00ad\u00bb\u00c6\u00d6\u00db\u00ee\u00f3\u0120")
        buf.write("\u0127\u012e\u0137\u0142\u014e\u015a\u0160\u0166\u016f")
        buf.write("\u0174\u017b\u0185\u019d\u01a1")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Var'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'int'", "'float'", 
                     "'boolean'", "'string'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'>='", "'<='", 
                     "'=/='", "'<.'", "'>.'", "'>=.'", "'<=.'", "';'", "':'", 
                     "'.'", "','", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "ADD", "ADD_F", "SUB", "SUB_F", "MULTI", "MULTI_F", 
                      "DIV", "DIV_F", "MOD", "NOT", "ANDAND", "OROR", "EQUAL", 
                      "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "NOT_EQUAL_F", "LESS_THAN_F", "GREATER_THAN_F", 
                      "GREATER_EQUAL_F", "LESS_EQUAL_F", "SEMI", "COLON", 
                      "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "ASSIGN", 
                      "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", "FLOAT", 
                      "BOOLEAN", "STRING", "ARRAY", "ARRAY_DECL", "SKIP_", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_variable_decl = 1
    RULE_variable_list = 2
    RULE_var_list = 3
    RULE_init_value = 4
    RULE_literal = 5
    RULE_boolean_literal = 6
    RULE_array_index = 7
    RULE_body_decl = 8
    RULE_init_body = 9
    RULE_parameter = 10
    RULE_body = 11
    RULE_stmt = 12
    RULE_stmt_list = 13
    RULE_assign_stmt = 14
    RULE_if_stmt = 15
    RULE_for_stmt = 16
    RULE_for_condition = 17
    RULE_while_stmt = 18
    RULE_do_while_stmt = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_call_stmt = 22
    RULE_return_stmt = 23
    RULE_function_call = 24
    RULE_exp = 25
    RULE_exp1 = 26
    RULE_exp2 = 27
    RULE_exp3 = 28
    RULE_exp4 = 29
    RULE_exp5 = 30
    RULE_exp6 = 31
    RULE_exp7 = 32
    RULE_exp_list = 33
    RULE_operands = 34
    RULE_multiplying_operators = 35
    RULE_adding_operators = 36
    RULE_sign_operators = 37
    RULE_boolean_operators = 38
    RULE_relational_operators = 39
    RULE_element_exp = 40
    RULE_index_operators = 41
    RULE_expr_index = 42

    ruleNames =  [ "program", "variable_decl", "variable_list", "var_list", 
                   "init_value", "literal", "boolean_literal", "array_index", 
                   "body_decl", "init_body", "parameter", "body", "stmt", 
                   "stmt_list", "assign_stmt", "if_stmt", "for_stmt", "for_condition", 
                   "while_stmt", "do_while_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "function_call", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp_list", 
                   "operands", "multiplying_operators", "adding_operators", 
                   "sign_operators", "boolean_operators", "relational_operators", 
                   "element_exp", "index_operators", "expr_index" ]

    EOF = Token.EOF
    ID=1
    VAR=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    FUNCTION=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    INT_TYPE=23
    FLOAT_TYPE=24
    BOOLEAN_TYPE=25
    STRING_TYPE=26
    ADD=27
    ADD_F=28
    SUB=29
    SUB_F=30
    MULTI=31
    MULTI_F=32
    DIV=33
    DIV_F=34
    MOD=35
    NOT=36
    ANDAND=37
    OROR=38
    EQUAL=39
    NOT_EQUAL=40
    LESS_THAN=41
    GREATER_THAN=42
    GREATER_EQUAL=43
    LESS_EQUAL=44
    NOT_EQUAL_F=45
    LESS_THAN_F=46
    GREATER_THAN_F=47
    GREATER_EQUAL_F=48
    LESS_EQUAL_F=49
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    LEFT_PAREN=54
    RIGHT_PAREN=55
    LEFT_BRACKET=56
    RIGHT_BRACKET=57
    LEFT_BRACE=58
    RIGHT_BRACE=59
    ASSIGN=60
    DECIMAL_INTEGER=61
    HEX_INTEGER=62
    OCT_INTEGER=63
    FLOAT=64
    BOOLEAN=65
    STRING=66
    ARRAY=67
    ARRAY_DECL=68
    SKIP_=69
    ERROR_CHAR=70
    UNCLOSE_STRING=71
    ILLEGAL_ESCAPE=72
    UNTERMINATED_COMMENT=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def SKIP_(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SKIP_)
            else:
                return self.getToken(BKITParser.SKIP_, i)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def body_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Body_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Body_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(BKITParser.SKIP_) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 92
                self.variable_decl()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.match(BKITParser.SKIP_) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 104
                self.body_decl()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SKIP_:
                self.state = 110
                self.match(BKITParser.SKIP_)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_listContext,i)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def init_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Init_valueContext)
            else:
                return self.getTypedRuleContext(BKITParser.Init_valueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_decl




    def variable_decl(self):

        localctx = BKITParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKITParser.VAR)
            self.state = 119
            self.match(BKITParser.COLON)
            self.state = 120
            self.variable_list()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 121
                self.match(BKITParser.ASSIGN)
                self.state = 122
                self.init_value()


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 125
                self.match(BKITParser.COMMA)
                self.state = 126
                self.variable_list()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 127
                    self.match(BKITParser.ASSIGN)
                    self.state = 128
                    self.init_value()


                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ARRAY_DECL(self):
            return self.getToken(BKITParser.ARRAY_DECL, 0)

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_list




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(BKITParser.ARRAY_DECL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                _la = self._input.LA(1)
                if not(_la==BKITParser.ID or _la==BKITParser.ARRAY_DECL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.match(BKITParser.COMMA)
                self.state = 142
                self.variable_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ARRAY_DECL(self):
            return self.getToken(BKITParser.ARRAY_DECL, 0)

        def array_index(self):
            return self.getTypedRuleContext(BKITParser.Array_indexContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_list)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(BKITParser.ARRAY_DECL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.array_index()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 148
                    self.match(BKITParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 149
                    self.match(BKITParser.ARRAY_DECL)
                    pass

                elif la_ == 3:
                    self.state = 150
                    self.array_index()
                    pass


                self.state = 153
                self.match(BKITParser.COMMA)
                self.state = 154
                self.variable_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_init_value




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.literal()
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 158
                    self.match(BKITParser.COMMA)
                    self.state = 159
                    self.literal() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKITParser.ARRAY, 0)

        def DECIMAL_INTEGER(self):
            return self.getToken(BKITParser.DECIMAL_INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(BKITParser.Boolean_literalContext,0)


        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(BKITParser.ARRAY)
                pass
            elif token in [BKITParser.DECIMAL_INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BKITParser.DECIMAL_INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.boolean_literal()
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.match(BKITParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_literal




    def boolean_literal(self):

        localctx = BKITParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_index




    def array_index(self):

        localctx = BKITParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(BKITParser.ID)
            self.state = 176
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_body(self):
            return self.getTypedRuleContext(BKITParser.Init_bodyContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_decl




    def body_decl(self):

        localctx = BKITParser.Body_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.init_body()
            self.state = 179
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_body




    def init_body(self):

        localctx = BKITParser.Init_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_init_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKITParser.FUNCTION)
            self.state = 182
            self.match(BKITParser.COLON)
            self.state = 183
            self.match(BKITParser.ID)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 184
                self.parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKITParser.PARAMETER)
            self.state = 188
            self.match(BKITParser.COLON)
            self.state = 189
            self.variable_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKITParser.BODY)
            self.state = 192
            self.match(BKITParser.COLON)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 193
                self.variable_decl()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.stmt_list()
            self.state = 200
            self.match(BKITParser.ENDBODY)
            self.state = 201
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 208
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 210
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 211
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self.stmt() 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.var_list()
            self.state = 221
            self.match(BKITParser.ASSIGN)
            self.state = 222
            self.exp()
            self.state = 223
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(BKITParser.IF)
            self.state = 226
            self.exp()
            self.state = 227
            self.match(BKITParser.THEN)
            self.state = 228
            self.stmt_list()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 229
                self.match(BKITParser.ELSEIF)
                self.state = 230
                self.exp()
                self.state = 231
                self.match(BKITParser.THEN)
                self.state = 232
                self.stmt_list()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 239
                self.match(BKITParser.ELSE)
                self.state = 240
                self.stmt_list()


            self.state = 243
            self.match(BKITParser.ENDIF)
            self.state = 244
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKITParser.FOR)
            self.state = 247
            self.match(BKITParser.LEFT_PAREN)
            self.state = 248
            self.for_condition()
            self.state = 249
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 250
            self.match(BKITParser.DO)
            self.state = 251
            self.stmt_list()
            self.state = 252
            self.match(BKITParser.ENDFOR)
            self.state = 253
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(BKITParser.ID)
            self.state = 256
            self.match(BKITParser.ASSIGN)
            self.state = 257
            self.exp()
            self.state = 258
            self.match(BKITParser.COMMA)
            self.state = 259
            self.exp()
            self.state = 260
            self.match(BKITParser.COMMA)
            self.state = 261
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(BKITParser.WHILE)
            self.state = 264
            self.exp()
            self.state = 265
            self.match(BKITParser.DO)
            self.state = 266
            self.stmt_list()
            self.state = 267
            self.match(BKITParser.ENDWHILE)
            self.state = 268
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BKITParser.DO)
            self.state = 271
            self.stmt_list()
            self.state = 272
            self.match(BKITParser.WHILE)
            self.state = 273
            self.exp()
            self.state = 274
            self.match(BKITParser.ENDDO)
            self.state = 275
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(BKITParser.BREAK)
            self.state = 278
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(BKITParser.CONTINUE)
            self.state = 281
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKITParser.ID)
            self.state = 284
            self.match(BKITParser.LEFT_PAREN)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.DECIMAL_INTEGER))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.ARRAY - 64)) | (1 << (BKITParser.ARRAY_DECL - 64)))) != 0):
                self.state = 285
                self.exp_list()


            self.state = 288
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 289
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKITParser.RETURN)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.DECIMAL_INTEGER))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.ARRAY - 64)) | (1 << (BKITParser.ARRAY_DECL - 64)))) != 0):
                self.state = 292
                self.exp()


            self.state = 295
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKITParser.ID)
            self.state = 298
            self.match(BKITParser.LEFT_PAREN)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.DECIMAL_INTEGER))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.ARRAY - 64)) | (1 << (BKITParser.ARRAY_DECL - 64)))) != 0):
                self.state = 299
                self.exp_list()


            self.state = 302
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def relational_operators(self):
            return self.getTypedRuleContext(BKITParser.Relational_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.exp1(0)
                self.state = 305
                self.relational_operators()
                self.state = 306
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def boolean_operators(self):
            return self.getTypedRuleContext(BKITParser.Boolean_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    self.boolean_operators()
                    self.state = 316
                    self.exp2(0) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def adding_operators(self):
            return self.getTypedRuleContext(BKITParser.Adding_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    self.adding_operators()
                    self.state = 328
                    self.exp3(0) 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def multiplying_operators(self):
            return self.getTypedRuleContext(BKITParser.Multiplying_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    self.multiplying_operators()
                    self.state = 340
                    self.exp4() 
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp4)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(BKITParser.NOT)
                self.state = 348
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUB_F, BKITParser.LEFT_PAREN, BKITParser.DECIMAL_INTEGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.ARRAY_DECL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_operators(self):
            return self.getTypedRuleContext(BKITParser.Sign_operatorsContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp5)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUB_F]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.sign_operators()
                self.state = 353
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LEFT_PAREN, BKITParser.DECIMAL_INTEGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.ARRAY_DECL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.exp6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.index_operators() 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp7)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_exp_list




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.exp()
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 373
                self.match(BKITParser.COMMA)
                self.state = 374
                self.exp()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def element_exp(self):
            return self.getTypedRuleContext(BKITParser.Element_expContext,0)


        def ARRAY_DECL(self):
            return self.getToken(BKITParser.ARRAY_DECL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operands)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(BKITParser.LEFT_PAREN)
                self.state = 382
                self.exp()
                self.state = 383
                self.match(BKITParser.RIGHT_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.element_exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.match(BKITParser.ARRAY_DECL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplying_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(BKITParser.MULTI, 0)

        def MULTI_F(self):
            return self.getToken(BKITParser.MULTI_F, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIV_F(self):
            return self.getToken(BKITParser.DIV_F, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying_operators




    def multiplying_operators(self):

        localctx = BKITParser.Multiplying_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplying_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MULTI) | (1 << BKITParser.MULTI_F) | (1 << BKITParser.DIV) | (1 << BKITParser.DIV_F) | (1 << BKITParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding_operators




    def adding_operators(self):

        localctx = BKITParser.Adding_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_adding_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.ADD_F) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sign_operators




    def sign_operators(self):

        localctx = BKITParser.Sign_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sign_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==BKITParser.SUB or _la==BKITParser.SUB_F):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def ANDAND(self):
            return self.getToken(BKITParser.ANDAND, 0)

        def OROR(self):
            return self.getToken(BKITParser.OROR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_operators




    def boolean_operators(self):

        localctx = BKITParser.Boolean_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_boolean_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.NOT) | (1 << BKITParser.ANDAND) | (1 << BKITParser.OROR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKITParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(BKITParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(BKITParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(BKITParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(BKITParser.LESS_EQUAL, 0)

        def NOT_EQUAL_F(self):
            return self.getToken(BKITParser.NOT_EQUAL_F, 0)

        def LESS_EQUAL_F(self):
            return self.getToken(BKITParser.LESS_EQUAL_F, 0)

        def GREATER_THAN_F(self):
            return self.getToken(BKITParser.GREATER_THAN_F, 0)

        def GREATER_EQUAL_F(self):
            return self.getToken(BKITParser.GREATER_EQUAL_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational_operators




    def relational_operators(self):

        localctx = BKITParser.Relational_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_relational_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL) | (1 << BKITParser.LESS_THAN) | (1 << BKITParser.GREATER_THAN) | (1 << BKITParser.GREATER_EQUAL) | (1 << BKITParser.LESS_EQUAL) | (1 << BKITParser.NOT_EQUAL_F) | (1 << BKITParser.GREATER_THAN_F) | (1 << BKITParser.GREATER_EQUAL_F) | (1 << BKITParser.LESS_EQUAL_F))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_index(self):
            return self.getTypedRuleContext(BKITParser.Expr_indexContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element_exp




    def element_exp(self):

        localctx = BKITParser.Element_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_element_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expr_index()
            self.state = 400
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_index_operators)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 403
                self.exp()
                self.state = 404
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 407
                self.exp()
                self.state = 408
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 409
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr_index




    def expr_index(self):

        localctx = BKITParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr_index)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.exp1_sempred
        self._predicates[27] = self.exp2_sempred
        self._predicates[28] = self.exp3_sempred
        self._predicates[31] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




