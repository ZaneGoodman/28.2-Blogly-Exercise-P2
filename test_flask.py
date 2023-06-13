from unittest import TestCase

from app import app
from models import db, User

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test_db"
app.config["SQLALCHEMY_ECHO"] = False

app.config["TESTING"] = True

app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

db.drop_all()
db.create_all()


class UserTestCase(TestCase):
    """Test for views for Users"""

    def setUp(self):
        """Add sample user"""

        User.query.delete()

        user = User(
            first_name="Lacey",
            last_name="grace",
            img_url="https://images.pexels.com/photos/2773977/pexels-photo-2773977.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        )
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up an db for each test"""

        db.session.rollback()

    def test_user_details(self):
        with app.test_client() as client:
            resp = client.get(f"/user-details/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Lacey grace</h1>", html)

    def test_edit_user(self):
        with app.test_client() as client:
            resp = client.get(f"/user-details/{self.user_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<label for='first_name'>First Name</label>", html)

    def test_user_edit_form(self):
        with app.test_client() as client:
            data = {
                "first_name": "Sally",
                "last_name": "brooks",
                "img_url": "https://images.pexels.com/photos/634021/pexels-photo-634021.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            }
            resp = client.post(
                f"/user-details/{self.user_id}/edit", data=data, follow_redirects=True
            )
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Sally brooks</h1>", html)

    def test_delete_user(self):
        with app.test_client() as client:
            resp = client.get(f"/user-details/{self.user_id}/delete")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            self.assertNotIn("Lacey", html)
