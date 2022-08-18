from webapp import web_app
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':

    # Initialize Web App
    web_app()

    # Request API Data every Day
    schedular = BlockingScheduler()
    schedular.add_job(web_app, 'interval', days=1)
    schedular.start()
