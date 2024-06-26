import invoke


@invoke.task
def format(c: invoke.Context):
    c.run("autoflake .")
    c.run("black .")


@invoke.task
def run_notifications(c: invoke.Context):
    c.run("flask --app notifications --debug run")


@invoke.task
def run_sfc(c: invoke.Context):
    c.run("flask --app sfc_report_424 --debug run")
