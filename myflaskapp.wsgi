import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/u640710737/public_html/senior_project")

from app import app as application
