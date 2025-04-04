from django.db import models
#import models used from academic procedure and academic information  modules and globals
from applications.academic_information.models import Student, Curriculum
from applications.programme_curriculum.models import Course as Courses, CourseInstructor
from applications.globals.models import ExtraInfo

#the modules for containing course content
class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_name

#the documents in the course (slides , ppt) added by the faculty  and can be downloaded by the students
class CourseDocuments(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    module_id = models.ForeignKey(Modules, on_delete=models.CASCADE, default = 1)
    upload_time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100)
    document_name = models.CharField(max_length=40)
    document_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} - {}'.format(self.course_id, self.document_name)
    
#the attendance files added by the faculty and can be downloaded by the students
class AttendanceFiles(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=40)
    file_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} - {}'.format(self.course_id, self.file_name)

#videos added by the faculty and can be downloaded by students
class CourseVideo(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100)
    video_name = models.CharField(max_length=40)
    video_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} - {}'.format(self.course_id, self.video_name)

#For storing the questions topic wise
class Topics(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    topic_name = models.TextField(max_length=200)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.course_id, self.topic_name)

#details of a question bank of which course it is 
class QuestionBank(models.Model):
    instructor_id = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  #name of question bank

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.instructor_id, self.name)

#question can be stored to question bank  and then added to quiz
class Question(models.Model):
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)
    options1 = models.CharField(null=True, max_length=100)
    options2 = models.CharField(null=True, max_length=100)
    options3 = models.CharField(null=True, max_length=100)
    options4 = models.CharField(null=True, max_length=100)
    options5 = models.CharField(null=True, max_length=100)
    answer = models.IntegerField()
    image = models.TextField(max_length=1000, null=True)
    marks = models.IntegerField()

    # def __str__(self):
    #     return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(
    #         self.pk, self.question_bank, self.question, self.topic, self.options1,
    #         self.options2, self.options3, self.options4,
    #         self.options5, self.answer)

 #details of quiz are stored
class Quiz(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=20)
    end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    d_day = models.CharField(max_length=2)
    d_hour = models.CharField(max_length=2)
    d_minute = models.CharField(max_length=2)
    negative_marks = models.FloatField(default=0)
    number_of_question = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    rules = models.TextField(max_length=2000)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
                self.pk, self.course_id,
                self.start_time, self.end_time,
                self.negative_marks)

#questions of the quiz are stored separately
class QuizQuestion(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(
            self.pk, self.question)

#the details of practice quiz (objective assignment)---- under development
class Practice(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    prac_quiz_name = models.CharField(max_length=20)
    negative_marks = models.FloatField(default=0)
    number_of_question = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
                self.pk, self.course_id,
                self.negative_marks)

#the details of questions for the practice quiz (objective assignment) 
class PracticeQuestion(models.Model):
    prac_quiz_id = models.ForeignKey(Practice, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)
    options1 = models.CharField(null=True, max_length=100)
    options2 = models.CharField(null=True, max_length=100)
    options3 = models.CharField(null=True, max_length=100)
    options4 = models.CharField(null=True, max_length=100)
    options5 = models.CharField(null=True, max_length=100)
    answer = models.IntegerField()
    image = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(
            self.pk, self.quiz_id, self.options1,
            self.options2, self.options3, self.options4,
            self.options5, self.answer, self.announcement)

#answer given by the student in the quiz is stored here to check properly the answers
class StudentAnswer(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    choice = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
                self.pk, self.student_id,
                self.quiz_id, self.question_id,
                self.choice)

#details of the assignment uploaded by the faculty
class Assignment(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now=True)
    submit_date = models.DateTimeField()
    assignment_name = models.CharField(max_length=100)
    assignment_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.course_id, self.assignment_name)

#details of the solution uploaded by the student
class StudentAssignment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now=True)
    upload_url = models.TextField(max_length=200)
    score = models.IntegerField(null=True)        #score is submitted by faculty 
    feedback = models.CharField(max_length=100, null=True)  #feedback by the faculty for the solution of the assignment submitted
    assign_name = models.CharField(max_length=100) 

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
                self.pk, self.student_id,
                self.assignment_id, self.score,
                self.feedback)

#the score of quiz of each student 
class QuizResult(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
                self.pk, self.student_id,
                self.quiz_id, self.score,
                self.finished)

#to store the comment of student and lecturer
class Forum(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    commenter_id = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=2000)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.pk, self.course_id,
            self.commenter_id,
            self.comment)

#reply of particular comment is stored in this table
class ForumReply(models.Model):
    #the original comment(questions) 
    forum_ques = models.ForeignKey(Forum, on_delete=models.CASCADE,   
                                   related_name='forum_ques')
    #the reply of the questions
    forum_reply = models.ForeignKey(Forum, on_delete=models.CASCADE,
                                    related_name='forum_reply')

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.forum_ques, self.forum_reply)
    
class GradingScheme(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    # quiz = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # assignment = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # midsem = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # endsem = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # projects = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    type_of_evaluation = models.CharField(max_length=100)
    weightage = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return '{} - {}'.format(
                self.pk, self.course_id)
    
class GradingScheme_grades(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    O_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    O_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    A_plus_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    A_plus_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    A_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    A_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    B_plus_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    B_plus_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    B_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    B_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    C_plus_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    C_plus_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    C_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    C_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    D_plus_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    D_plus_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    D_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    D_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    F_Lower = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    F_Upper = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.course_id)

class Student_grades(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.IntegerField(default=1)
    year = models.IntegerField(default=2016)
    roll_no = models.TextField(max_length=2000)
    total_marks = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grade = models.TextField(max_length=2000)
    batch = models.IntegerField(default=2021)
 
    def __str__(self):
        return '{} - {}'.format(self.pk, self.course_id)

class Attendance(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
#    course_id = models.ForeignKey(Course)
#    attend = models.CharField(max_length=6, choices=Constants.ATTEND_CHOICES)
    instructor_id = models.ForeignKey(CourseInstructor, on_delete=models.CASCADE)
#    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.IntegerField(default=0)
    no_of_attendance = models.IntegerField(default=1)
 
    def __str__(self):
        return self.course_id
    
class StudentEvaluation(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    evaluation_id = models.ForeignKey(GradingScheme, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    total_marks = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
                self.pk, self.student_id,
                self.evaluation_id, self.marks)