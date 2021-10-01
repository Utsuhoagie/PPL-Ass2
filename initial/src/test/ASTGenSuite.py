import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_program2(self):
        """Simple program: class main {} """
        input = """
            class main {

            }
            class foo {
                
            }"""
        expect = str(Program([ClassDecl(Id("main"),[]), ClassDecl(Id("foo"),[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_program3(self):
        """Simple program: class main {} """
        input = """class main extends foo {}"""
        expect = str(Program([ClassDecl(Id("main"),[],Id("foo"))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,304))
   
    def test_class_with_sameline_decl_program(self):
        """More complex program"""
        input = """class main {
            int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_class_with_samelinediff_decl_program(self):
        """More complex program"""
        input = """class main {
            static int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def testBlock(self):
        """More complex program"""
        input = """class main {
            
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Static(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,306))