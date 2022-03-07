from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan


register_new_user("Arjan", "BestPasswordEva", "hi@arjaneggs.com")

password_forgotten("hi@arjaneggs.com")

upgrade_plan("hi@arjaneggs.com")
