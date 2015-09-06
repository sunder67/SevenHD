# -*- coding: utf-8 -*-
# Written by .:TBX:.
# This Plugin is free Software!!!
# General imports

from GlobalImport import *

class Update():
        
        def __init__(self, session):
		self.session = session
		self.onClose = [ ]
		self.msgBox = None                                                    
                self.do_update()   
        
        def do_update(self):
                self.version = config.plugins.SevenHD.version.value

                try:
                   self.new_version = urlopen('http://www.gigablue-support.org/skins/SevenHD/update/version.txt').read()
                   self.dl_version = self.new_version
                   self.ipk_url = 'http://www.gigablue-support.org/skins/SevenHD/update/enigma2-plugin-skins-sevenhd_%s_all.ipk' % str(self.dl_version)
                   self.filename = '/tmp/enigma2-plugin-skins-sevenhd_%s_all.ipk' % str(self.dl_version)
                   self.debug('Found new Version -> enigma2-plugin-skins-sevenhd_%s_all.ipk' % str(self.dl_version))
                   self.debug(self.ipk_url)

                except:
                   self.new_version = '0.0.0'
                   self.debug('URL/Server Error!!')

                self.version = ''.join(self.version.replace('.',''))
                self.new_version = ''.join(self.new_version.replace('.',''))

                self.debug('%s - %s' % (str(len(self.version)), str(len(self.new_version))))

                if str(len(self.version)) <= str('3'): 
                   self.version = self.version + str('0')
                   if str(len(self.version)) < str('4'): 
                      self.version = self.version + str('0')
                if str(len(self.new_version)) <= str('3'): 
                   self.new_version = self.new_version + str('0')
                   if str(len(self.new_version)) < str('4'): 
                      self.new_version = self.new_version + str('0')

                self.debug('%s - %s' % (str(self.version), str(self.new_version)))

                if int(self.version) < int(self.new_version):

                   if config.plugins.SevenHD.AutoUpdate.value:

                      if not self.session.in_exec:
                         self.download_ipk(True)
                         Notifications.AddNotification(MessageBox, _("GUI needs a restart after download Plugin.\n"), MessageBox.TYPE_INFO, timeout=5) 

                      else:
                         self.download_ipk(True)
                         self.msgBox = self.session.open(MessageBox, _("GUI needs a restart after download Plugin.\n"), MessageBox.TYPE_INFO, timeout=5)
                   else:

                      if not self.session.in_exec:
                         message = 'Found new Version -> enigma2-plugin-skins-sevenhd_%s_all.ipk\nDownload, Install and Reboot?' % str(self.dl_version)
                         Notifications.AddNotificationWithCallback(self.download_ipk, MessageBox, message, MessageBox.TYPE_YESNO, timeout=15)

                      else:
                         message = 'Found new Version -> enigma2-plugin-skins-sevenhd_%s_all.ipk\nDownload, Install and Reboot?' % str(self.dl_version)
                         self.msgBox = self.session.openWithCallback(self.download_ipk, MessageBox, message, MessageBox.TYPE_YESNO, timeout=15)

                else:
                   self.debug('No new Version found')
        
        
        def download_ipk(self, answer):
            if answer is True:
               self.debug('Try to download and install new Version')
               downloadPage(self.ipk_url, self.filename).addCallback(self.on_finish).addErrback(self.Error)


        def on_finish(self, fake):       
               self.debug('Download and Install new Version finished')
               self.msgBox = self.session.openWithCallback(self.reboot, MessageBox, _("GUI needs a restart after download Plugin."), MessageBox.TYPE_YESNO, timeout=10)
               os.system('opkg install %s' % str(self.filename))


        def reboot(self, answer):
               if answer is True:
                  self.session.open(TryQuitMainloop, 3)	


        def Error(self, error):
                if not self.session.in_exec:
                   Notifications.AddNotification(MessageBox, _("Download failed"), MessageBox.TYPE_ERROR)          
                else:
                   self.msgBox = self.session.open(MessageBox, _("Download failed"), MessageBox.TYPE_ERROR)
                self.debug(error)               
        
        
        def debug(self, what):        
                if config.plugins.SevenHD.debug.value:
                   f = open('/tmp/kraven_debug.txt', 'a+')
                   f.write('[AutoUpdate]' + str(what) + '\n')
                   f.close()
