from celery.task.schedules import crontab
from celery.decorators import perodic_task


@periodic_task(run_every=(crontab(minute='*/1')), name='random_message', ignore_result=True)
def random_message():
    """Generate a random message in the chat rooms"""

