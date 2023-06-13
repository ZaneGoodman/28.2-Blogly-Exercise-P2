from models import User, db
from app import app


db.drop_all()
db.create_all()


User.query.delete()

# Add users
john = User(
    first_name="John",
    last_name="Wintenburg",
    img_url="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80",
)

sally = User(
    first_name="Sally",
    last_name="Clara",
    img_url="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
)

fredrick = User(
    first_name="Fredrick",
    last_name="Geress",
    img_url="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80",
)


db.session.add(john)
db.session.add(sally)
db.session.add(fredrick)


db.session.commit()
