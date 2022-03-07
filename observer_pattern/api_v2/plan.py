from lib.db import find_user
from .event import post_event


def upgrade_plan(email: str):
    user = find_user(email)

    user.plan = "paid"

    post_event("user_upgrade_plan", user)
