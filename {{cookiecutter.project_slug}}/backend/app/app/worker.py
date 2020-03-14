import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration

from app.core import config
from app.core.celery_app import celery_app

import logging

sentry_sdk.init(config.SENTRY_DSN, integrations=[CeleryIntegration()])

@celery_app.task(acks_late=True)
def test_celery(word: str):
    logging.info(f"start test celery {word}")
    return f"test task return {word}"
