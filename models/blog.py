from app import db
import datetime


# 类名定义 collection
class Blog(db.Document):
    title = db.StringField(required=True)
    content = db.StringField()
    created_time = db.DateTimeField(default=datetime.datetime.now(), required=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'created_time': self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
