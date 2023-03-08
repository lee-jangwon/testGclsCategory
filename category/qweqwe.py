from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Lvl1Category(models.Model):
    """
    대분류 카테고리
    """

    class Meta:
        ordering = ["code"]
        verbose_name = "Category (Lvl 1)"
        verbose_name_plural = "Categories (Lvl 1)"

    korean_name = models.CharField(max_length=100, verbose_name="카테고리 국문 명칭")
    english_name = models.CharField(max_length=100, verbose_name="카테고리 영문 명칭")
    is_esri = models.BooleanField(
        default=True, verbose_name="본사 카테고리 여부", help_text="본사 카테고리에 포함이 되어있으면 체크표시"
    )
    code = models.IntegerField(default=0)
    # full_code = models.CharField(max_length=8, default=0)
    full_code = models.CharField(max_length=2, editable=False)

    def get_code(self) -> str:
        """
        카테고리의 코드를 8자화 한다.
        """
        return f"{self.code:02}000000"

    # def save(self, *args, **kwargs):
    #     super(Lvl1Category, self).save(*args, **kwargs)
    #     self.code = self.id

    def save(self, *args, **kwargs):
        super(Lvl1Category, self).save(*args, **kwargs)
        self.code = self.id
        self.full_code = f"{self.code:02}"

    def __str__(self):
        return f"[{self.get_code()}] {self.korean_name}({self.english_name})"


class Lvl2Category(models.Model):
    """
    중분류 카테고리
    """

    class Meta:
        ordering = ["code"]
        verbose_name = "Category (Lvl 2)"
        verbose_name_plural = "Categories (Lvl 2)"

    korean_name = models.CharField(max_length=100, verbose_name="카테고리 국문 명칭")
    english_name = models.CharField(max_length=100, verbose_name="카테고리 영문 명칭")
    is_esri = models.BooleanField(
        default=True, verbose_name="본사 카테고리 여부", help_text="본사 카테고리에 포함이 되어있으면 체크표시"
    )
    code = models.IntegerField(blank=True, null=True)
    lvl1_category = models.ForeignKey(
        Lvl1Category, on_delete=models.PROTECT, related_name="lvl2_categories"
    )
    full_code = models.CharField(max_length=8, default=0)

    def save(self, *args, **kwargs):
        same_category = Lvl2Category.objects.filter(
            lvl1_category__code=self.lvl1_category.code
        )
        if len(same_category) == 0:
            self.code = 0
        else:
            latest_code = same_category.order_by("-id")[0].code
            self.code = latest_code + 1
        super(Lvl2Category, self).save(*args, **kwargs)

    def get_code(self):
        lvl1_code = f"{self.lvl1_category.code:02}"
        return f"{lvl1_code:02}{self.code:03}000"

    def __str__(self):
        return f"[{self.get_code()}] {self.korean_name}({self.english_name})"


# def get_default_lvl1_category():


class Lvl3Category(models.Model):
    """
    소분류
    """

    class Meta:
        ordering = ["code"]
        verbose_name = "Category (Lvl 3)"
        verbose_name_plural = "Categories (Lvl 3)"

    korean_name = models.CharField(max_length=100, verbose_name="카테고리 국문 명칭")
    english_name = models.CharField(max_length=100, verbose_name="카테고리 영문 명칭")
    code = models.IntegerField(blank=True, null=True)
    lvl2_category = models.ForeignKey(
        Lvl2Category, on_delete=models.PROTECT, related_name="lvl3_categories"
    )
    # lvl1_category = models.ForeignKey(
    #     Lvl1Category, on_delete=models.PROTECT, related_name="lvl3_categories"
    # )
    full_code = models.CharField(max_length=8, default=0)

    def get_lvl1_code(self):
        return self.lvl2_category.lvl1_category.code

    def get_code(self):
        lvl1_code = f"{self.get_lvl1_code:02}"
        lvl2_code = f"{self.lvl2_category.code:03}"
        return f"{lvl1_code:02}{lvl2_code:03}{self.code:03}"

    def save(self, *args, **kwargs):
        lvl2 = Lvl2Category.objects.filter(english_name=self.lvl2_category.english_name)
        if len(lvl2) == 0:
            print(lvl2)
            self.code = 0
        else:
            self.code = lvl2.order_by("-code")[0].code + 1
        super(Lvl3Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"[{self.get_code()}] {self.korean_name}({self.english_name})"
