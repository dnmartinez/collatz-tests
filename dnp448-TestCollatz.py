#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        src = "1 10\n"
        i, j = collatz_read(src)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        src = "100 200\n"
        i, j = collatz_read(src)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        src = "201 210\n"
        i, j = collatz_read(src)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_read_4(self):
        src = "1 10\n"
        i, j = collatz_read(src)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        val = collatz_eval(999999, 999999)
        self.assertEqual(val, 258)

    def test_eval_6(self):
        val = collatz_eval(29, 5)
        self.assertEqual(val, 112)

    def test_eval_7(self):
        val = collatz_eval(89098, 210)
        self.assertEqual(val, 351)

    # -----
    # print
    # -----

    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "1 10 89\n")

    def test_print_4(self):
        writer = StringIO()
        collatz_print(writer, 900, 1000, 174)
        self.assertEqual(writer.getvalue(), "1 10 174\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 25\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("108 45789\n29 5\n89098 210\n88 34\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "108 45789 324\n29 5 112\n89098 210 351\n88 34 116\n")
    
    def test_solve_3(self):
        reader = StringIO("5 10\n783729 784000\n2016 1994\n2 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "5 10 20\n83729 784000 331\n2016 1994 144\n2 1 2\n")
"""
Name             Stmts   Miss Branch BrPart  Cover
--------------------------------------------------
Collatz.py          44     18     24     11    49%
TestCollatz.py      78      1      2      1    98%
--------------------------------------------------
TOTAL              122     19     26     12    75%
"""

# ----
# main
# ----

if __name__ == "__main__":
    main()
