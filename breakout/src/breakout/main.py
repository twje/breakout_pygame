from core.application import Application
from .breakout import Breakout


def main():
    application = Application(
        listener=Breakout(),
        caption="Hello World",
        width=600,
        height=400
    )
    application.run()
