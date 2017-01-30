# Add the app directory to the path
import sys
sys.path.insert(0, '/var/www/awesome-rdv')

# Source the virtualenv
activate_this = '/var/www/awesome-rdv/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Run the app
from app import app as application
