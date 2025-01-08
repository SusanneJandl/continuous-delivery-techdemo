from invoke import task


@task
def lint(c):
    c.run("black .")
    c.run("flake8 .")
    c.run("black --check .")


@task
def test(c):
    c.run("pytest")


@task
def build(c):
    lint(c)
    test(c)
    c.run("docker build -t my-calculator-app .")
    c.run("docker run -p 5000:5000 my-calculator-app")
