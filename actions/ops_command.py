# encoding: utf-8
from st2actions.runners.pythonrunner import Action
from clicrud.device.generic import generic
import sys


class OPSCommand(Action):

    def run(self, host, command):
        self.method = self.config['method']
        self.username = self.config['username']
        self.password = self.config['password']
        self.enable = self.config['enable']
        try:
            utf8_command = command.encode('utf-8')
            utf8_host = host.encode('utf-8')
            transport = generic(host=utf8_host, username=self.username,
                                enable=self.enable, method=self.method,
                                password=self.password)

            return_value = transport.read(utf8_command, return_type="string")
            _return_value = unicode(return_value)
            transport.close()
            return _return_value
        except Exception, err:
            self.logger.info('FUBARd')
            self.logger.info(err)
            sys.exit(2)
