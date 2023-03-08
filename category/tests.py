from django.test import TestCase

from .models import CategoryDepth1, CategoryDepth2, CategoryDepth3


class CategoryDepth1TestCase(TestCase):
    def setUp(self):
        self.c1 = CategoryDepth1(
            korean_name="시험1", english_name="test1", note="this is a teststring1"
        )
        self.c1.save()

    def test_c1_code(self):
        self.assertEqual(self.c1.code, "01")


class CategoryDepth2TestCase(TestCase):
    def setUp(self):
        self.c1 = CategoryDepth1(
            korean_name="시험1", english_name="test1", note="this is a teststring1"
        )
        self.c1.save()
        self.c2 = CategoryDepth2(
            korean_name="시험2",
            english_name="test2",
            note="this is a teststring2",
            depth1=self.c1,
        )
        self.c2.save()

    def test_c2_code(self):
        self.assertEqual(self.c1.code, "01")
        self.assertEqual(self.c2.code, "01001")


class CategoryDepth3TestCase(TestCase):
    def setUp(self):
        self.c1 = CategoryDepth1(
            korean_name="시험1", english_name="test1", note="this is a teststring1"
        )
        self.c1.save()
        self.c2 = CategoryDepth2(
            korean_name="시험2",
            english_name="test2",
            note="this is a teststring2",
            depth1=self.c1,
        )
        self.c2.save()
        self.c3 = CategoryDepth3(
            korean_name="시험3",
            english_name="test3",
            note="this is a teststring3",
            depth2=self.c2,
        )
        self.c3.save()

    def test_c3_code(self):
        self.assertEqual(self.c1.code, "01")
        self.assertEqual(self.c2.code, "01001")
        self.assertEqual(self.c3.code, "0100100001")
