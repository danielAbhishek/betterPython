from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
from lib.stringtools import get_random_string


def register_new_user(name: str, password: str, email: str):
    user = create_user(name, password, email)

    post_slack_message(
        "sales",
        f"{user.name} has registered with email address {user.email}. Please\
        spam this person incessantly"
    )

    send_email(
        user.name, user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The DevNotes"
    )

    log(f"User registered with email address {user.email}")


def password_forgotten(email: str):
    user = find_user(email)

    user.reset_code = get_random_string(16)

    send_email(
        user.name,
        user.email,
        "Reset your password",
        f"To reset your password, use this very secure code: {user.reset_code}"
    )

    log(f"User with email address {user.email} request a password reset")
