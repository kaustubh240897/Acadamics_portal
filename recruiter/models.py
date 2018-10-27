from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator

class Semester_1(models.Model):
    course_title=models.CharField(max_length=25)
    # ppts=models.FileField()
    # Video_link=models.CharField(max_length=100)
    # Syllabus=models.FileField()
    # pdfs=models.FileField()
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title


class Semester_2(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_3(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_4(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_5(models.Model):
    course_title=models.CharField(max_length=25)
    def get_absolute_url(self):
        return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_6(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_7(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Semester_8(models.Model):
    course_title=models.CharField(max_length=25)
    # def get_absolute_url(self):
    #     return reverse('recruiter:material',kwargs={'pk':self.pk})

    def __str__(self):
        return self.course_title

class Course1_sem1(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name


class Course2_sem1(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course3_sem1(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course4_sem1(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course5_sem1(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course1_sem2(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course2_sem2(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course3_sem2(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course4_sem2(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course5_sem2(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course1_sem3(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course2_sem3(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course3_sem3(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course4_sem3(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course5_sem3(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course1_sem4(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course2_sem4(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course3_sem4(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course4_sem4(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course5_sem4(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course1_sem5(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course2_sem5(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course3_sem5(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

class Course4_sem5(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course5_sem5(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course1_sem6(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course2_sem6(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course3_sem6(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course4_sem6(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course5_sem6(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course1_sem7(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course2_sem7(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course3_sem7(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course4_sem7(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course5_sem7(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name
class Course1_sem8(models.Model):
    course_title=models.ForeignKey(Semester_1, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30, null=True)
    file_pdfs=models.FileField(null=True)
    video_link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.course_name

