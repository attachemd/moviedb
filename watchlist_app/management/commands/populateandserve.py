from django.core.management.base import BaseCommand
from subprocess import Popen, run
from sys import stdout, stdin, stderr
import time
import os
import signal


class Command(BaseCommand):
    help = 'Run all commands'
    commands = {
        1: 'python manage.py migrate',
        2: 'python manage.py createdata',
        3: 'python manage.py runserver'
    }

    # commands = 'python manage.py migrate && python manage.py createdata && python manage.py runserver'

    def handle(self, *args, **options):
        proc_list = []

        for command in self.commands:
            print("$ " + self.commands[command])
            proc = run(self.commands[command], shell=True, stdin=stdin,
                       stdout=stdout, stderr=stderr)
            proc_list.append(proc)

        # try:
        #     while True:
        #         time.sleep(10)
        # except KeyboardInterrupt:
        #     for proc in proc_list:
        #         os.kill(proc.pid, signal.SIGTERM)
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            os.kill(os.getpid(), signal.SIGTERM)
        # Popen(self.commands, shell=True, stdin=stdin,
        #       stdout=stdout, stderr=stderr)
