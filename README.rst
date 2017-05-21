=========================
 Binly
=========================

Installation
------------
Server Setup Instructions::
        virtualenv --system-site-packages venv
        source venv/bin/activate
        # For the raspberry pi: (see: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
        sudo apt-get install -y python-smbus i2c-tools
        pip install -r requirements-pi.txt
        # else anything else:
        pip install -r requirements.txt

Client Setup Instructions::
        # Follow instructions in client/README.md

Run the tests::
        make test

Start the server::
        make run

Re-build the client files::
        make build
