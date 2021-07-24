from user import User
from post import Post

# Creating an object
app_user_one = User("harry@example.com", "Harry Li", "pw1234", "DevOps Engineer")
app_user_one.get_user_infor()

app_user_two = User("james@example.com", "James Bond", "pw5678", "Java Developer")
app_user_one.get_user_infor()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_infor()
