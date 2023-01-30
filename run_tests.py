import subprocess
import datetime

# Run your test suite
subprocess.run(["pytest", "--cov=mymodule"])

# Generate a code coverage HTML report
subprocess.run(["coverage", "html"])

# Add and commit the report to git
subprocess.run(["git", "add", "htmlcov/"])
subprocess.run(["git", "commit", "-m", "Update coverage report",datetime.datetime.today()])

# Push the report to GitHub
subprocess.run(["git", "push", "origin", "main"])