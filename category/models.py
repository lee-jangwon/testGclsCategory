from django.db import models


class CategoryDepth1(models.Model):
    class Meta:
        verbose_name = "Category (Depth 1)"
        verbose_name_plural = "Categories (Depth 1)"

    korean_name = models.CharField(
        verbose_name="카테고리 국문 명칭", help_text="카테고리 국문 명칭", max_length=100
    )
    english_name = models.CharField(
        verbose_name="카테고리 영문 명칭", help_text="카테고리 영문 명칭", max_length=100
    )
    is_esri = models.BooleanField(default=True)
    code = models.CharField(max_length=2, unique=True, editable=False)
    needs_review = models.BooleanField("검토필요", default=False, help_text="체크하면 회의에서 검토")
    note = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.code == "":
            super().save()
            self.code = f"{self.id:02}"
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.code}] {self.korean_name}({self.english_name})"


class CategoryDepth2(models.Model):
    class Meta:
        verbose_name = "Category (Depth 2)"
        verbose_name_plural = "Categories (Depth 2)"

    korean_name = models.CharField(
        verbose_name="카테고리 국문 명칭", help_text="카테고리 국문 명칭", max_length=100
    )
    english_name = models.CharField(
        verbose_name="카테고리 영문 명칭", help_text="카테고리 영문 명칭", max_length=100
    )
    is_esri = models.BooleanField(default=True)
    depth1 = models.ForeignKey(
        CategoryDepth1,
        verbose_name="상위 카테고리",
        related_name="categories_depth2",
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=5, unique=True, editable=False)
    needs_review = models.BooleanField("검토필요", default=False, help_text="체크하면 회의에서 검토")
    note = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.code == "":
            super().save()
            self.code = f"{self.depth1.code}{self.pk:03}"
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.code}] {self.korean_name}({self.english_name})"


class CategoryDepth3(models.Model):
    class Meta:
        verbose_name = "Category (Depth 3)"
        verbose_name_plural = "Categories (Depth 3)"

    korean_name = models.CharField(
        verbose_name="카테고리 국문 명칭", help_text="카테고리 국문 명칭", max_length=100
    )
    english_name = models.CharField(
        verbose_name="카테고리 영문 명칭", help_text="카테고리 영문 명칭", max_length=100
    )
    depth2 = models.ForeignKey(
        CategoryDepth2,
        verbose_name="상위 카테고리",
        related_name="categories_depth3",
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=10, unique=True, editable=False)
    needs_review = models.BooleanField("검토필요", default=False, help_text="체크하면 회의에서 검토")
    note = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.code == "":
            super().save()
            self.code = f"{self.depth2.code}{self.pk:05}"
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.code}] {self.korean_name}({self.english_name})"
