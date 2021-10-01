# Generated from e:\Study\Sem7\PPL\Assignment\A2\Second try\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4W\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4_\n\4\3\4\5\4b\n\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5h\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6q\n")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6w\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u0080\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0088\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u0094\n\n")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u009a\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00a2\n\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00ab\n\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00b5\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00be\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00d3\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00dd\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00f7\n\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0102\n\22")
        buf.write("\f\22\16\22\u0105\13\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u010c\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u0113\n\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\5\25\u011b\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0125\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u012a\n\27\3\27\3\27\3\30\3\30\5\30\u0130")
        buf.write("\n\30\3\30\3\30\5\30\u0134\n\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u013a\n\31\3\32\3\32\5\32\u013e\n\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0156\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0164\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u017c\n\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u018a\n\"\3#\3")
        buf.write("#\3#\3#\3#\3#\5#\u0192\n#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u019d\n#\3#\3#\5#\u01a1\n#\3#\2\3\"$\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2")
        buf.write("\n\7\2\13\13\22\22\24\24\26\26##\7\2\13\13\22\22\24\24")
        buf.write("\26\26\34\34\3\2$%\3\2&)\3\2\60\61\3\2*+\3\2,/\3\2!\"")
        buf.write("\2\u01c8\2F\3\2\2\2\4M\3\2\2\2\6a\3\2\2\2\bg\3\2\2\2\n")
        buf.write("v\3\2\2\2\f\177\3\2\2\2\16\u0087\3\2\2\2\20\u0089\3\2")
        buf.write("\2\2\22\u0093\3\2\2\2\24\u0099\3\2\2\2\26\u009b\3\2\2")
        buf.write("\2\30\u009d\3\2\2\2\32\u00a6\3\2\2\2\34\u00b4\3\2\2\2")
        buf.write("\36\u00b6\3\2\2\2 \u00bd\3\2\2\2\"\u00dc\3\2\2\2$\u010b")
        buf.write("\3\2\2\2&\u010d\3\2\2\2(\u011a\3\2\2\2*\u0124\3\2\2\2")
        buf.write(",\u0126\3\2\2\2.\u012f\3\2\2\2\60\u0139\3\2\2\2\62\u013d")
        buf.write("\3\2\2\2\64\u0143\3\2\2\2\66\u0155\3\2\2\28\u0163\3\2")
        buf.write("\2\2:\u0165\3\2\2\2<\u017b\3\2\2\2>\u017d\3\2\2\2@\u0180")
        buf.write("\3\2\2\2B\u0189\3\2\2\2D\u01a0\3\2\2\2FG\5\4\3\2GH\7\2")
        buf.write("\2\3H\3\3\2\2\2IJ\5\6\4\2JK\5\4\3\2KN\3\2\2\2LN\5\6\4")
        buf.write("\2MI\3\2\2\2ML\3\2\2\2N\5\3\2\2\2OP\7\r\2\2PQ\7#\2\2Q")
        buf.write("R\7\21\2\2RS\7#\2\2SV\7\66\2\2TW\5\b\5\2UW\3\2\2\2VT\3")
        buf.write("\2\2\2VU\3\2\2\2WX\3\2\2\2Xb\7\67\2\2YZ\7\r\2\2Z[\7#\2")
        buf.write("\2[^\7\66\2\2\\_\5\b\5\2]_\3\2\2\2^\\\3\2\2\2^]\3\2\2")
        buf.write("\2_`\3\2\2\2`b\7\67\2\2aO\3\2\2\2aY\3\2\2\2b\7\3\2\2\2")
        buf.write("cd\5\n\6\2de\5\b\5\2eh\3\2\2\2fh\5\n\6\2gc\3\2\2\2gf\3")
        buf.write("\2\2\2h\t\3\2\2\2ij\5\f\7\2jk\5\16\b\2kl\5\22\n\2lm\7")
        buf.write("<\2\2mw\3\2\2\2nq\7 \2\2oq\3\2\2\2pn\3\2\2\2po\3\2\2\2")
        buf.write("qr\3\2\2\2rs\5\26\f\2st\5\30\r\2tw\3\2\2\2uw\5\32\16\2")
        buf.write("vi\3\2\2\2vp\3\2\2\2vu\3\2\2\2w\13\3\2\2\2xy\7 \2\2y\u0080")
        buf.write("\7\37\2\2z{\7\37\2\2{\u0080\7 \2\2|\u0080\7 \2\2}\u0080")
        buf.write("\7\37\2\2~\u0080\3\2\2\2\177x\3\2\2\2\177z\3\2\2\2\177")
        buf.write("|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\r\3\2\2\2\u0081")
        buf.write("\u0088\7\24\2\2\u0082\u0088\7\22\2\2\u0083\u0088\7\13")
        buf.write("\2\2\u0084\u0088\7\26\2\2\u0085\u0088\7#\2\2\u0086\u0088")
        buf.write("\5\20\t\2\u0087\u0081\3\2\2\2\u0087\u0082\3\2\2\2\u0087")
        buf.write("\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\17\3\2\2\2\u0089\u008a\t\2")
        buf.write("\2\2\u008a\u008b\7:\2\2\u008b\u008c\7\6\2\2\u008c\u008d")
        buf.write("\7;\2\2\u008d\21\3\2\2\2\u008e\u008f\5\24\13\2\u008f\u0090")
        buf.write("\7?\2\2\u0090\u0091\5\22\n\2\u0091\u0094\3\2\2\2\u0092")
        buf.write("\u0094\5\24\13\2\u0093\u008e\3\2\2\2\u0093\u0092\3\2\2")
        buf.write("\2\u0094\23\3\2\2\2\u0095\u0096\7#\2\2\u0096\u0097\7\65")
        buf.write("\2\2\u0097\u009a\5\"\22\2\u0098\u009a\7#\2\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\25\3\2\2\2\u009b\u009c")
        buf.write("\t\3\2\2\u009c\27\3\2\2\2\u009d\u009e\7#\2\2\u009e\u00a1")
        buf.write("\78\2\2\u009f\u00a2\5\34\17\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\79\2\2\u00a4\u00a5\5,\27\2\u00a5\31\3\2\2")
        buf.write("\2\u00a6\u00a7\7#\2\2\u00a7\u00aa\78\2\2\u00a8\u00ab\5")
        buf.write("\34\17\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\79\2\2")
        buf.write("\u00ad\u00ae\5,\27\2\u00ae\33\3\2\2\2\u00af\u00b0\5\36")
        buf.write("\20\2\u00b0\u00b1\7<\2\2\u00b1\u00b2\5\34\17\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b5\5\36\20\2\u00b4\u00af\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\35\3\2\2\2\u00b6\u00b7\5\16\b\2\u00b7")
        buf.write("\u00b8\5 \21\2\u00b8\37\3\2\2\2\u00b9\u00ba\7#\2\2\u00ba")
        buf.write("\u00bb\7?\2\2\u00bb\u00be\5 \21\2\u00bc\u00be\7#\2\2\u00bd")
        buf.write("\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be!\3\2\2\2\u00bf")
        buf.write("\u00c0\b\22\1\2\u00c0\u00c1\78\2\2\u00c1\u00c2\5\"\22")
        buf.write("\2\u00c2\u00c3\79\2\2\u00c3\u00dd\3\2\2\2\u00c4\u00dd")
        buf.write("\7\6\2\2\u00c5\u00dd\7\7\2\2\u00c6\u00dd\7\b\2\2\u00c7")
        buf.write("\u00dd\7\t\2\2\u00c8\u00dd\7\n\2\2\u00c9\u00dd\7\36\2")
        buf.write("\2\u00ca\u00dd\7#\2\2\u00cb\u00dd\5&\24\2\u00cc\u00cd")
        buf.write("\7#\2\2\u00cd\u00ce\7>\2\2\u00ce\u00cf\7#\2\2\u00cf\u00d2")
        buf.write("\78\2\2\u00d0\u00d3\5$\23\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00dd\79\2\2\u00d5\u00d6\7#\2\2\u00d6\u00d7\7>")
        buf.write("\2\2\u00d7\u00dd\7#\2\2\u00d8\u00d9\t\4\2\2\u00d9\u00dd")
        buf.write("\5\"\22\n\u00da\u00db\7\62\2\2\u00db\u00dd\5\"\22\t\u00dc")
        buf.write("\u00bf\3\2\2\2\u00dc\u00c4\3\2\2\2\u00dc\u00c5\3\2\2\2")
        buf.write("\u00dc\u00c6\3\2\2\2\u00dc\u00c7\3\2\2\2\u00dc\u00c8\3")
        buf.write("\2\2\2\u00dc\u00c9\3\2\2\2\u00dc\u00ca\3\2\2\2\u00dc\u00cb")
        buf.write("\3\2\2\2\u00dc\u00cc\3\2\2\2\u00dc\u00d5\3\2\2\2\u00dc")
        buf.write("\u00d8\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u0103\3\2\2\2")
        buf.write("\u00de\u00df\f\b\2\2\u00df\u00e0\7\63\2\2\u00e0\u0102")
        buf.write("\5\"\22\t\u00e1\u00e2\f\7\2\2\u00e2\u00e3\t\5\2\2\u00e3")
        buf.write("\u0102\5\"\22\b\u00e4\u00e5\f\6\2\2\u00e5\u00e6\t\4\2")
        buf.write("\2\u00e6\u0102\5\"\22\7\u00e7\u00e8\f\5\2\2\u00e8\u00e9")
        buf.write("\t\6\2\2\u00e9\u0102\5\"\22\6\u00ea\u00eb\f\4\2\2\u00eb")
        buf.write("\u00ec\t\7\2\2\u00ec\u0102\5\"\22\5\u00ed\u00ee\f\3\2")
        buf.write("\2\u00ee\u00ef\t\b\2\2\u00ef\u0102\5\"\22\4\u00f0\u00f1")
        buf.write("\f\17\2\2\u00f1\u00f2\7>\2\2\u00f2\u00f3\7#\2\2\u00f3")
        buf.write("\u00f6\78\2\2\u00f4\u00f7\5$\23\2\u00f5\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3")
        buf.write("\2\2\2\u00f8\u0102\79\2\2\u00f9\u00fa\f\r\2\2\u00fa\u00fb")
        buf.write("\7>\2\2\u00fb\u0102\7#\2\2\u00fc\u00fd\f\13\2\2\u00fd")
        buf.write("\u00fe\7:\2\2\u00fe\u00ff\5\"\22\2\u00ff\u0100\7;\2\2")
        buf.write("\u0100\u0102\3\2\2\2\u0101\u00de\3\2\2\2\u0101\u00e1\3")
        buf.write("\2\2\2\u0101\u00e4\3\2\2\2\u0101\u00e7\3\2\2\2\u0101\u00ea")
        buf.write("\3\2\2\2\u0101\u00ed\3\2\2\2\u0101\u00f0\3\2\2\2\u0101")
        buf.write("\u00f9\3\2\2\2\u0101\u00fc\3\2\2\2\u0102\u0105\3\2\2\2")
        buf.write("\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104#\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0106\u0107\5\"\22\2\u0107\u0108")
        buf.write("\7?\2\2\u0108\u0109\5$\23\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u010c\5\"\22\2\u010b\u0106\3\2\2\2\u010b\u010a\3\2\2")
        buf.write("\2\u010c%\3\2\2\2\u010d\u010e\7\25\2\2\u010e\u010f\7#")
        buf.write("\2\2\u010f\u0112\78\2\2\u0110\u0113\5$\23\2\u0111\u0113")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0115\79\2\2\u0115\'\3\2\2\2\u0116")
        buf.write("\u0117\5*\26\2\u0117\u0118\5(\25\2\u0118\u011b\3\2\2\2")
        buf.write("\u0119\u011b\5*\26\2\u011a\u0116\3\2\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011b)\3\2\2\2\u011c\u0125\5,\27\2\u011d\u0125")
        buf.write("\5\64\33\2\u011e\u0125\58\35\2\u011f\u0125\5:\36\2\u0120")
        buf.write("\u0125\5> \2\u0121\u0125\5@!\2\u0122\u0125\5B\"\2\u0123")
        buf.write("\u0125\5D#\2\u0124\u011c\3\2\2\2\u0124\u011d\3\2\2\2\u0124")
        buf.write("\u011e\3\2\2\2\u0124\u011f\3\2\2\2\u0124\u0120\3\2\2\2")
        buf.write("\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123\3")
        buf.write("\2\2\2\u0125+\3\2\2\2\u0126\u0129\7\66\2\2\u0127\u012a")
        buf.write("\5.\30\2\u0128\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7\67\2")
        buf.write("\2\u012c-\3\2\2\2\u012d\u0130\5\60\31\2\u012e\u0130\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u0134\5(\25\2\u0132\u0134\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134/\3\2\2\2\u0135")
        buf.write("\u0136\5\62\32\2\u0136\u0137\5\60\31\2\u0137\u013a\3\2")
        buf.write("\2\2\u0138\u013a\5\62\32\2\u0139\u0135\3\2\2\2\u0139\u0138")
        buf.write("\3\2\2\2\u013a\61\3\2\2\2\u013b\u013e\7\37\2\2\u013c\u013e")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0140\5\16\b\2\u0140\u0141\5\22\n")
        buf.write("\2\u0141\u0142\7<\2\2\u0142\63\3\2\2\2\u0143\u0144\5\66")
        buf.write("\34\2\u0144\u0145\7\64\2\2\u0145\u0146\5\"\22\2\u0146")
        buf.write("\u0147\7<\2\2\u0147\65\3\2\2\2\u0148\u0156\7#\2\2\u0149")
        buf.write("\u014a\5\"\22\2\u014a\u014b\7>\2\2\u014b\u014c\7#\2\2")
        buf.write("\u014c\u0156\3\2\2\2\u014d\u014e\7#\2\2\u014e\u014f\7")
        buf.write(">\2\2\u014f\u0156\7#\2\2\u0150\u0151\5\"\22\2\u0151\u0152")
        buf.write("\7:\2\2\u0152\u0153\5\"\22\2\u0153\u0154\7;\2\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u0148\3\2\2\2\u0155\u0149\3\2\2\2")
        buf.write("\u0155\u014d\3\2\2\2\u0155\u0150\3\2\2\2\u0156\67\3\2")
        buf.write("\2\2\u0157\u0158\7\23\2\2\u0158\u0159\5\"\22\2\u0159\u015a")
        buf.write("\7\27\2\2\u015a\u015b\5*\26\2\u015b\u015c\7\20\2\2\u015c")
        buf.write("\u015d\5*\26\2\u015d\u0164\3\2\2\2\u015e\u015f\7\23\2")
        buf.write("\2\u015f\u0160\5\"\22\2\u0160\u0161\7\27\2\2\u0161\u0162")
        buf.write("\5*\26\2\u0162\u0164\3\2\2\2\u0163\u0157\3\2\2\2\u0163")
        buf.write("\u015e\3\2\2\2\u01649\3\2\2\2\u0165\u0166\7\30\2\2\u0166")
        buf.write("\u0167\5<\37\2\u0167\u0168\7\64\2\2\u0168\u0169\5\"\22")
        buf.write("\2\u0169\u016a\t\t\2\2\u016a\u016b\5\"\22\2\u016b\u016c")
        buf.write("\7\17\2\2\u016c\u016d\5*\26\2\u016d;\3\2\2\2\u016e\u017c")
        buf.write("\7#\2\2\u016f\u0170\5\"\22\2\u0170\u0171\7>\2\2\u0171")
        buf.write("\u0172\7#\2\2\u0172\u017c\3\2\2\2\u0173\u0174\7#\2\2\u0174")
        buf.write("\u0175\7>\2\2\u0175\u017c\7#\2\2\u0176\u0177\5\"\22\2")
        buf.write("\u0177\u0178\7:\2\2\u0178\u0179\5\"\22\2\u0179\u017a\7")
        buf.write(";\2\2\u017a\u017c\3\2\2\2\u017b\u016e\3\2\2\2\u017b\u016f")
        buf.write("\3\2\2\2\u017b\u0173\3\2\2\2\u017b\u0176\3\2\2\2\u017c")
        buf.write("=\3\2\2\2\u017d\u017e\7\f\2\2\u017e\u017f\7<\2\2\u017f")
        buf.write("?\3\2\2\2\u0180\u0181\7\16\2\2\u0181\u0182\7<\2\2\u0182")
        buf.write("A\3\2\2\2\u0183\u0184\7\31\2\2\u0184\u0185\5\"\22\2\u0185")
        buf.write("\u0186\7<\2\2\u0186\u018a\3\2\2\2\u0187\u0188\7\31\2\2")
        buf.write("\u0188\u018a\7<\2\2\u0189\u0183\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u018aC\3\2\2\2\u018b\u018c\5\"\22\2\u018c\u018d")
        buf.write("\7>\2\2\u018d\u018e\7#\2\2\u018e\u0191\78\2\2\u018f\u0192")
        buf.write("\5$\23\2\u0190\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\79\2\2")
        buf.write("\u0194\u0195\7<\2\2\u0195\u01a1\3\2\2\2\u0196\u0197\7")
        buf.write("#\2\2\u0197\u0198\7>\2\2\u0198\u0199\7#\2\2\u0199\u019c")
        buf.write("\78\2\2\u019a\u019d\5$\23\2\u019b\u019d\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\79\2\2\u019f\u01a1\7<\2\2\u01a0\u018b\3\2")
        buf.write("\2\2\u01a0\u0196\3\2\2\2\u01a1E\3\2\2\2&MV^agpv\177\u0087")
        buf.write("\u0093\u0099\u00a1\u00aa\u00b4\u00bd\u00d2\u00dc\u00f6")
        buf.write("\u0101\u0103\u010b\u0112\u011a\u0124\u0129\u012f\u0133")
        buf.write("\u0139\u013d\u0155\u0163\u017b\u0189\u0191\u019c\u01a0")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'''", "'/'", "'%'", "'!='", "'=='", 
                     "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
                     "'^'", "':='", "'='", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
                      "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", 
                      "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                      "FINAL", "STATIC", "TO", "DOWNTO", "ID", "ADD", "SUB", 
                      "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", 
                      "GREATER", "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", 
                      "ASSIGN", "INIT", "LP", "RP", "LB", "RB", "LQ", "RQ", 
                      "SEMI", "COLON", "DOT", "COMMA", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDeclList = 1
    RULE_classDecl = 2
    RULE_memberList = 3
    RULE_member = 4
    RULE_attrKeyword = 5
    RULE_attrType = 6
    RULE_arrayType = 7
    RULE_attrList = 8
    RULE_attribute = 9
    RULE_returnType = 10
    RULE_method = 11
    RULE_constructor = 12
    RULE_paramList = 13
    RULE_param = 14
    RULE_idList = 15
    RULE_exp = 16
    RULE_argList = 17
    RULE_obj_create = 18
    RULE_stmtList = 19
    RULE_stmt = 20
    RULE_blockStmt = 21
    RULE_blockBody = 22
    RULE_declList = 23
    RULE_decl = 24
    RULE_assignStmt = 25
    RULE_lhs = 26
    RULE_ifStmt = 27
    RULE_forStmt = 28
    RULE_scalarVar = 29
    RULE_breakStmt = 30
    RULE_continueStmt = 31
    RULE_returnStmt = 32
    RULE_methodInvokeStmt = 33

    ruleNames =  [ "program", "classDeclList", "classDecl", "memberList", 
                   "member", "attrKeyword", "attrType", "arrayType", "attrList", 
                   "attribute", "returnType", "method", "constructor", "paramList", 
                   "param", "idList", "exp", "argList", "obj_create", "stmtList", 
                   "stmt", "blockStmt", "blockBody", "declList", "decl", 
                   "assignStmt", "lhs", "ifStmt", "forStmt", "scalarVar", 
                   "breakStmt", "continueStmt", "returnStmt", "methodInvokeStmt" ]

    EOF = Token.EOF
    WS=1
    BLOCK_CMT=2
    LINE_CMT=3
    INTLIT=4
    FLOATLIT=5
    BOOLLIT=6
    STRINGLIT=7
    ARRAYLIT=8
    BOOLEAN=9
    BREAK=10
    CLASS=11
    CONTINUE=12
    DO=13
    ELSE=14
    EXTENDS=15
    FLOAT=16
    IF=17
    INT=18
    NEW=19
    STRING=20
    THEN=21
    FOR=22
    RETURN=23
    TRUE=24
    FALSE=25
    VOID=26
    NIL=27
    THIS=28
    FINAL=29
    STATIC=30
    TO=31
    DOWNTO=32
    ID=33
    ADD=34
    SUB=35
    MUL=36
    DIV=37
    DIVF=38
    MOD=39
    NEQ=40
    EQ=41
    LESS=42
    GREATER=43
    LEQ=44
    GREQ=45
    OR=46
    AND=47
    NOT=48
    CONCAT=49
    ASSIGN=50
    INIT=51
    LP=52
    RP=53
    LB=54
    RB=55
    LQ=56
    RQ=57
    SEMI=58
    COLON=59
    DOT=60
    COMMA=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.classDeclList()
            self.state = 69
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,0)


        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDeclList




    def classDeclList(self):

        localctx = BKOOLParser.ClassDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclList)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.classDecl()
                self.state = 72
                self.classDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.classDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def memberList(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(BKOOLParser.CLASS)
                self.state = 78
                self.match(BKOOLParser.ID)
                self.state = 79
                self.match(BKOOLParser.EXTENDS)
                self.state = 80
                self.match(BKOOLParser.ID)
                self.state = 81
                self.match(BKOOLParser.LP)
                self.state = 84
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                    self.state = 82
                    self.memberList()
                    pass
                elif token in [BKOOLParser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 86
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(BKOOLParser.CLASS)
                self.state = 88
                self.match(BKOOLParser.ID)
                self.state = 89
                self.match(BKOOLParser.LP)
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                    self.state = 90
                    self.memberList()
                    pass
                elif token in [BKOOLParser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 94
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def memberList(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberList




    def memberList(self):

        localctx = BKOOLParser.MemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberList)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.member()
                self.state = 98
                self.memberList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrKeyword(self):
            return self.getTypedRuleContext(BKOOLParser.AttrKeywordContext,0)


        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def returnType(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnTypeContext,0)


        def method(self):
            return self.getTypedRuleContext(BKOOLParser.MethodContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.attrKeyword()
                self.state = 104
                self.attrType()
                self.state = 105
                self.attrList()
                self.state = 106
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 108
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 112
                self.returnType()
                self.state = 113
                self.method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrKeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attrKeyword




    def attrKeyword(self):

        localctx = BKOOLParser.AttrKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrKeyword)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(BKOOLParser.STATIC)
                self.state = 119
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(BKOOLParser.FINAL)
                self.state = 121
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrType




    def attrType(self):

        localctx = BKOOLParser.AttrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrType)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.arrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayType




    def arrayType(self):

        localctx = BKOOLParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 136
            self.match(BKOOLParser.LQ)
            self.state = 137
            self.match(BKOOLParser.INTLIT)
            self.state = 138
            self.match(BKOOLParser.RQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrList




    def attrList(self):

        localctx = BKOOLParser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrList)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.attribute()
                self.state = 141
                self.match(BKOOLParser.COMMA)
                self.state = 142
                self.attrList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.attribute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT(self):
            return self.getToken(BKOOLParser.INIT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(BKOOLParser.ID)
                self.state = 148
                self.match(BKOOLParser.INIT)
                self.state = 149
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnType




    def returnType(self):

        localctx = BKOOLParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BKOOLParser.ID)
            self.state = 156
            self.match(BKOOLParser.LB)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.state = 157
                self.paramList()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(BKOOLParser.RB)
            self.state = 162
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKOOLParser.ID)
            self.state = 165
            self.match(BKOOLParser.LB)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.state = 166
                self.paramList()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 170
            self.match(BKOOLParser.RB)
            self.state = 171
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.param()
                self.state = 174
                self.match(BKOOLParser.SEMI)
                self.state = 175
                self.paramList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.attrType()
            self.state = 181
            self.idList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idList




    def idList(self):

        localctx = BKOOLParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idList)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(BKOOLParser.ID)
                self.state = 184
                self.match(BKOOLParser.COMMA)
                self.state = 185
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(BKOOLParser.ID)
                pass


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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def ARRAYLIT(self):
            return self.getToken(BKOOLParser.ARRAYLIT, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def obj_create(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_createContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKOOLParser.DIVF, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(BKOOLParser.LEQ, 0)

        def GREQ(self):
            return self.getToken(BKOOLParser.GREQ, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 190
                self.match(BKOOLParser.LB)
                self.state = 191
                self.exp(0)
                self.state = 192
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.state = 194
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 195
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 196
                self.match(BKOOLParser.BOOLLIT)
                pass

            elif la_ == 5:
                self.state = 197
                self.match(BKOOLParser.STRINGLIT)
                pass

            elif la_ == 6:
                self.state = 198
                self.match(BKOOLParser.ARRAYLIT)
                pass

            elif la_ == 7:
                self.state = 199
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 8:
                self.state = 200
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 9:
                self.state = 201
                self.obj_create()
                pass

            elif la_ == 10:
                self.state = 202
                self.match(BKOOLParser.ID)
                self.state = 203
                self.match(BKOOLParser.DOT)
                self.state = 204
                self.match(BKOOLParser.ID)
                self.state = 205
                self.match(BKOOLParser.LB)
                self.state = 208
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 206
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 11:
                self.state = 211
                self.match(BKOOLParser.ID)
                self.state = 212
                self.match(BKOOLParser.DOT)
                self.state = 213
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 12:
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.exp(8)
                pass

            elif la_ == 13:
                self.state = 216
                self.match(BKOOLParser.NOT)
                self.state = 217
                self.exp(7)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 255
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 220
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 221
                        self.match(BKOOLParser.CONCAT)
                        self.state = 222
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 223
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.DIVF) | (1 << BKOOLParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.exp(5)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 229
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 231
                        self.exp(4)
                        pass

                    elif la_ == 5:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 232
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 233
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 234
                        self.exp(3)
                        pass

                    elif la_ == 6:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 235
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 236
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GREQ))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 237
                        self.exp(2)
                        pass

                    elif la_ == 7:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 238
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 239
                        self.match(BKOOLParser.DOT)
                        self.state = 240
                        self.match(BKOOLParser.ID)
                        self.state = 241
                        self.match(BKOOLParser.LB)
                        self.state = 244
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                            self.state = 242
                            self.argList()
                            pass
                        elif token in [BKOOLParser.RB]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 246
                        self.match(BKOOLParser.RB)
                        pass

                    elif la_ == 8:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 247
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 248
                        self.match(BKOOLParser.DOT)
                        self.state = 249
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 9:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 250
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 251
                        self.match(BKOOLParser.LQ)
                        self.state = 252
                        self.exp(0)
                        self.state = 253
                        self.match(BKOOLParser.RQ)
                        pass

             
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_argList




    def argList(self):

        localctx = BKOOLParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argList)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.exp(0)
                self.state = 261
                self.match(BKOOLParser.COMMA)
                self.state = 262
                self.argList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_create




    def obj_create(self):

        localctx = BKOOLParser.Obj_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_obj_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKOOLParser.NEW)
            self.state = 268
            self.match(BKOOLParser.ID)
            self.state = 269
            self.match(BKOOLParser.LB)
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                self.state = 270
                self.argList()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 274
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(BKOOLParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtList




    def stmtList(self):

        localctx = BKOOLParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmtList)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.stmt()
                self.state = 277
                self.stmtList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.stmt()
                pass


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

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def methodInvokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 287
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 289
                self.methodInvokeStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def blockBody(self):
            return self.getTypedRuleContext(BKOOLParser.BlockBodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKOOLParser.LP)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 293
                self.blockBody()
                pass

            elif la_ == 2:
                pass


            self.state = 297
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(BKOOLParser.DeclListContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(BKOOLParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockBody




    def blockBody(self):

        localctx = BKOOLParser.BlockBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 299
                self.declList()
                pass

            elif la_ == 2:
                pass


            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LP, BKOOLParser.LB]:
                self.state = 303
                self.stmtList()
                pass
            elif token in [BKOOLParser.RP]:
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


    class DeclListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def declList(self):
            return self.getTypedRuleContext(BKOOLParser.DeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declList




    def declList(self):

        localctx = BKOOLParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_declList)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.decl()
                self.state = 308
                self.declList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.state = 313
                self.match(BKOOLParser.FINAL)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 317
            self.attrType()
            self.state = 318
            self.attrList()
            self.state = 319
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.lhs()
            self.state = 322
            self.match(BKOOLParser.ASSIGN)
            self.state = 323
            self.exp(0)
            self.state = 324
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.exp(0)
                self.state = 328
                self.match(BKOOLParser.DOT)
                self.state = 329
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.match(BKOOLParser.ID)
                self.state = 332
                self.match(BKOOLParser.DOT)
                self.state = 333
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                self.exp(0)
                self.state = 335
                self.match(BKOOLParser.LQ)
                self.state = 336
                self.exp(0)
                self.state = 337
                self.match(BKOOLParser.RQ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifStmt)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(BKOOLParser.IF)
                self.state = 342
                self.exp(0)
                self.state = 343
                self.match(BKOOLParser.THEN)
                self.state = 344
                self.stmt()
                self.state = 345
                self.match(BKOOLParser.ELSE)
                self.state = 346
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(BKOOLParser.IF)
                self.state = 349
                self.exp(0)
                self.state = 350
                self.match(BKOOLParser.THEN)
                self.state = 351
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalarVar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(BKOOLParser.FOR)
            self.state = 356
            self.scalarVar()
            self.state = 357
            self.match(BKOOLParser.ASSIGN)
            self.state = 358
            self.exp(0)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 360
            self.exp(0)
            self.state = 361
            self.match(BKOOLParser.DO)
            self.state = 362
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarVar




    def scalarVar(self):

        localctx = BKOOLParser.ScalarVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_scalarVar)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.exp(0)
                self.state = 366
                self.match(BKOOLParser.DOT)
                self.state = 367
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.match(BKOOLParser.ID)
                self.state = 370
                self.match(BKOOLParser.DOT)
                self.state = 371
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.exp(0)
                self.state = 373
                self.match(BKOOLParser.LQ)
                self.state = 374
                self.exp(0)
                self.state = 375
                self.match(BKOOLParser.RQ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(BKOOLParser.BREAK)
            self.state = 380
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(BKOOLParser.CONTINUE)
            self.state = 383
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnStmt)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(BKOOLParser.RETURN)
                self.state = 386
                self.exp(0)
                self.state = 387
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(BKOOLParser.RETURN)
                self.state = 390
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvokeStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvokeStmt




    def methodInvokeStmt(self):

        localctx = BKOOLParser.MethodInvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_methodInvokeStmt)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.exp(0)
                self.state = 394
                self.match(BKOOLParser.DOT)
                self.state = 395
                self.match(BKOOLParser.ID)
                self.state = 396
                self.match(BKOOLParser.LB)
                self.state = 399
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 397
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 401
                self.match(BKOOLParser.RB)
                self.state = 402
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(BKOOLParser.ID)
                self.state = 405
                self.match(BKOOLParser.DOT)
                self.state = 406
                self.match(BKOOLParser.ID)
                self.state = 407
                self.match(BKOOLParser.LB)
                self.state = 410
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 408
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 412
                self.match(BKOOLParser.RB)
                self.state = 413
                self.match(BKOOLParser.SEMI)
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
        self._predicates[16] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 9)
         




