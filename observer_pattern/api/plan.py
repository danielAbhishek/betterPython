from lib.email import send_email
from lib.db import find_user
from lib.log import log
from lib.slack import post_slack_message


def upgrade_plan(email: str):
    # find the find_user
    user = find_user(email)

    user.plan = "paid"

    post_slack_message("sales", f"{user.name} has upgraded their plan")

    send_email(
        user.name, user.email, "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it."
    )

    log(f"User with email {user.email} had upgraded their plan")
