from django.db import models

# Create your models here.


class Epidemicinfo(models.Model):
    username = models.CharField(max_length=20, primary_key=True, unique=True, null=False, verbose_name='用户名')
    password = models.CharField(max_length=32, null=False, verbose_name='登录密码')
    real_name = models.CharField(max_length=500, verbose_name='真实姓名')
    tel = models.CharField(max_length=11, unique=True, verbose_name='电话号码')
    random_code = models.IntegerField(max_length=20)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'Epidemic_info'  # 表名
# class BoardModel(db.Model):
#     __tablename__ = 'board'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name = db.Column(db.String(20),nullable=False)
#     leibie = db.Column(db.String(100),nullable=False)
#     url = db.Column(db.String(255), nullable=False)
#     urlone = db.Column(db.String(255), nullable=False)
#     create_time = db.Column(db.DateTime,default=datetime.now)
#
# class AllNewsModel(db.Model):
#     __tablename__ = 'allnews'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(500),nullable=False)
#     url = db.Column(db.String(500),nullable=False)
#     source = db.Column(db.String(255),nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#     evenname = db.Column(db.String(255),nullable=False)
#     board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
#     board = db.relationship("BoardModel", backref="posts")
#
# class NewsModel(db.Model):
#     __tablename__ = 'spider_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     url = db.Column(db.String(500), nullable=False)
#     source = db.Column(db.String(255), nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#
# class News_one_Model(db.Model):
#     __tablename__ = 'one_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     url = db.Column(db.String(500), nullable=False)
#     source = db.Column(db.String(255), nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#
# class News_two_Model(db.Model):
#     __tablename__ = 'two_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     url = db.Column(db.String(500), nullable=False)
#     source = db.Column(db.String(255), nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#
# class News_three_Model(db.Model):
#     __tablename__ = 'three_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     url = db.Column(db.String(500), nullable=False)
#     source = db.Column(db.String(255), nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#
# class News_four_Model(db.Model):
#     __tablename__ = 'four_news'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     url = db.Column(db.String(500), nullable=False)
#     source = db.Column(db.String(255), nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#
# class ClassifyModel(db.Model):
#     __tablename__ = 'classify'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(500), nullable=False)
#     explain = db.Column(db.String(500), nullable=False)
