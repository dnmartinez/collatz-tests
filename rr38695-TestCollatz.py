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

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "90 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  90)
        self.assertEqual(j, 10)

    def test_read_3(self):
        s = "11100 22220\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  11100)
        self.assertEqual(j, 22220)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_4(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # cycle_length
    # -----
    def test_cycle_length_1(self):
        # collatz eval needs to be called for cycle length to work
        v = collatz_eval(900, 1000)
        cycle = cycle_length(5)
        self.assertEqual(cycle, 6)

    def test_cycle_length_2(self):
        # collatz eval needs to be called for cycle length to work
        v = collatz_eval(900, 1000)
        cycle = cycle_length(2)
        self.assertEqual(cycle, 2)

    def test_cycle_length_3(self):
        # collatz eval needs to be called for cycle length to work
        v = collatz_eval(900, 1000)
        cycle = cycle_length(4)
        self.assertEqual(cycle, 3)
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 70)
        self.assertEqual(w.getvalue(), "900 1000 70\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("10 1\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n1000 900 174\n")

    def test_solve_3(self):
        r = StringIO("500 2500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "500 2500 209\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
