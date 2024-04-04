from django.core.management import BaseCommand

from mail_tg.services import TGBot


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        bot = TGBot()
        bot.send_message('проверка связи')
