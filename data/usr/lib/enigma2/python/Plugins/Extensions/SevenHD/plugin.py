# -*- coding: utf-8 -*-
#######################################################################
#
# SevenHD by Team Kraven
# 
# Thankfully inspired by:
# MyMetrix
# Coded by iMaxxx (c) 2013
#
# This plugin is licensed under the Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
# or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#######################################################################
from GlobalImport import *
from OnlineUpdate import *
from ChangeSkin import *
from SkinParts import SkinParts
from FontSettings import FontSettings
from MainSettings import MainSettings
from MenuSettings import MenuSettings
from PluginSettings import PluginSettings
from InfobarSettings import InfobarSettings
from InfobarExtraSettings import InfobarExtraSettings
from ChannelSettings import ChannelSettings
from SonstigeSettings import SonstigeSettings
from ShareSkinSettings import ShareSkinSettings

class MainMenuList(MenuList):
    def __init__(self, list, font0 = 24, font1 = 16, itemHeight = 50, enableWrapAround = True):
        MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
        screenwidth = getDesktop(0).size().width()
        if screenwidth and screenwidth == 1920:
            self.l.setFont(0, gFont("Regular", int(font0*1.5)))
            self.l.setFont(1, gFont("Regular", int(font1*1.5)))
            self.l.setItemHeight(int(itemHeight*1.5))
        else:
            self.l.setFont(0, gFont("Regular", font0))
            self.l.setFont(1, gFont("Regular", font1))
            self.l.setItemHeight(itemHeight)

#############################################################

def MenuEntryItem(itemDescription, key):
    res = [(itemDescription, key)]
    screenwidth = getDesktop(0).size().width()
    if screenwidth and screenwidth == 1920:
        res.append(MultiContentEntryText(pos=(15, 8), size=(660, 68), font=0, text=itemDescription))
    else:
        res.append(MultiContentEntryText(pos=(10, 5), size=(440, 45), font=0, text=itemDescription))
    return res

#############################################################
lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SevenHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SevenHD/locale/"))

def _(txt):
	t = gettext.dgettext("SevenHD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def translateBlock(block):
	for x in TranslationHelper:
		if block.__contains__(x[0]):
			block = block.replace(x[0], x[1])
	return block
#############################################################
class SevenHD(Screen):
    skin =  """
                  <screen name="SevenHD-Setup" position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="transparent">
                         <widget name="buttonRed" font="Regular; 20" foregroundColor="#00f23d21" backgroundColor="#00000000" halign="left" valign="center" position="64,662" size="148,48" transparent="1" />
                         <widget name="buttonGreen" font="Regular; 20" foregroundColor="#00389416" backgroundColor="#00000000" halign="left" valign="center" position="264,662" size="148,48" transparent="1" />
                         <widget name="buttonYellow" font="Regular; 20" foregroundColor="#00e5b243" backgroundColor="#00000000" halign="left" valign="center" position="464,662" size="148,48" transparent="1" />
                         <widget name="buttonBlue" font="Regular; 20" foregroundColor="#000064c7" backgroundColor="#00000000" halign="left" valign="center" position="664,662" size="148,48" transparent="1" />
                         <widget name="menuList" position="18,72" size="816,575" itemHeight="36" scrollbarMode="showOnDemand" transparent="1" zPosition="1" backgroundColor="#00000000" />
                         <widget name="titel" position="70,12" size="708,46" font="Regular; 35" valign="center" halign="center" transparent="1" backgroundColor="#00000000" foregroundColor="#00ffffff" />
                         <widget name="helperimage" position="891,274" size="372,209" zPosition="1" backgroundColor="#00000000" />
                         <widget backgroundColor="#00000000" font="Regular2; 34" foregroundColor="#00ffffff" position="70,12" render="Label" size="708,46" source="Title" transparent="1" halign="center" valign="center" noWrap="1" />
                         <eLabel backgroundColor="#00000000" position="6,6" size="842,708" transparent="0" zPosition="-9" foregroundColor="#00ffffff" />
                         <eLabel backgroundColor="#00ffffff" position="6,6" size="842,2" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="6,714" size="844,2" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="6,6" size="2,708" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="848,6" size="2,708" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="18,64" size="816,2" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="18,656" size="816,2" zPosition="2" />
                         <widget source="global.CurrentTime" render="Label" position="1154,16" size="100,28" font="Regular;26" halign="right" backgroundColor="#00000000" transparent="1" valign="center" foregroundColor="#00ffffff">
                                 <convert type="ClockToText">Default</convert>
                         </widget>
                         <eLabel backgroundColor="#00000000" position="878,6" size="396,708" transparent="0" zPosition="-9" />
                         <eLabel backgroundColor="#00ffffff" position="878,6" size="396,2" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="878,714" size="398,2" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="878,6" size="2,708" zPosition="2" />
                         <eLabel backgroundColor="#00ffffff" position="1274,6" size="2,708" zPosition="2" />
                         <widget source="session.CurrentService" render="Label" position="891,88" size="372,46" font="Regular2;35" halign="center" backgroundColor="#00000000" transparent="1" valign="center" foregroundColor="#00ffffff">
                                 <convert type="SevenHDUpdate">Version</convert>
                         </widget>
                         <widget source="session.CurrentService" render="Label" position="891,134" size="372,28" font="Regular;26" halign="center" backgroundColor="#00000000" transparent="1" valign="center" foregroundColor="#00B27708">
                                 <convert type="SevenHDUpdate">Update</convert>
                         </widget>
                         <eLabel position="891,274" size="372,2" backgroundColor="#00ffffff" zPosition="5" />
                         <eLabel position="891,481" size="372,2" backgroundColor="#00ffffff" zPosition="5" />
                         <eLabel position="891,274" size="2,208" backgroundColor="#00ffffff" zPosition="5" />
                         <eLabel position="1261,274" size="2,208" backgroundColor="#00ffffff" zPosition="5" />
                  </screen>
               """
                  
    def __init__(self, session, args = None):
        self.session = session
        
        Screen.__init__(self, session)
        
        self.Scale = AVSwitch().getFramebufferScale()
        self.PicLoad = ePicLoad()
        self["helperimage"] = Pixmap()
        self["buttonRed"] = Label()
        self["buttonGreen"] = Label()
        self["buttonYellow"] = Label()
        self["buttonBlue"] = Label()
        self["titel"] = Label()
        self["buttonRed"].setText(_("Cancel"))
        self["buttonGreen"].setText(_("Save"))
        self["buttonYellow"].setText(_("Restart"))
        self["buttonBlue"] = Label("Extras/FAQ")
        self["titel"].setText(_("SevenHD"))

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "InputActions",
                "ColorActions"
            ],
            {
                "ok": self.ok,
                "cancel": self.exit,
                "red": self.exit,
                "green": self.ask_for_save,
                "yellow": self.reboot,
                "blue": self.showInfo
                
            }, -1)	
           
        list = []  
        list.append(MenuEntryItem(_("main setting"), "MainSettings"))
        list.append(MenuEntryItem(_("menu setting"), "MenuSettings"))
        list.append(MenuEntryItem(_("plugin setting"), "PluginSettings"))
        list.append(MenuEntryItem(_("infobar and second infobar"), "InfobarSettings"))
        list.append(MenuEntryItem(_("infobar extras"), "InfobarExtraSettings"))
        list.append(MenuEntryItem(_("channel selection"), "ChannelSettings"))
        if fileExists(MAIN_SKIN_PATH + 'skin.xml'):
           list.append(MenuEntryItem(_("font setting"), "FontSettings"))
           if config.plugins.SevenHD.skin_mode.value == '1':
              list.append(MenuEntryItem(_("skinpart setting"), "SkinParts"))
        list.append(MenuEntryItem(_("other settings"), "SonstigeSettings"))
        list.append(MenuEntryItem(_("system osd settings"), "SystemOSDSettings"))
        if CREATOR != 'OpenMips':
           list.append(MenuEntryItem(_("system channel settings"), "SystemChannelSettings"))
        list.append(MenuEntryItem(_("system osd position setup"), "OSDPositionSetup"))
           
        self["menuList"] = MainMenuList([], font0=24, font1=16, itemHeight=50)
        self["menuList"].l.setList(list)

        if not self.__selectionChanged in self["menuList"].onSelectionChanged:
            self["menuList"].onSelectionChanged.append(self.__selectionChanged)

        self.onChangedEntry = []

        self.onLayoutFinish.append(self.UpdatePicture)

    def __del__(self):
        self["menuList"].onSelectionChanged.remove(self.__selectionChanged)

    def UpdatePicture(self):
        self.PicLoad.PictureData.get().append(self.DecodePicture)
        self.onLayoutFinish.append(self.ShowPicture)

    def ShowPicture(self):
        if self["helperimage"] is None or self["helperimage"].instance is None:
            return

        cur = self["menuList"].getCurrent()

        if cur:                
            selectedKey = cur[0][1]
            self.debug('def ShowPicture\nneed: ' + MAIN_IMAGE_PATH + str(selectedKey) + '.jpg\n')
            if selectedKey == "MainSettings":
               imageUrl = MAIN_IMAGE_PATH + str("MAINSETTINGS.jpg")
            elif selectedKey == "FontSettings":
               imageUrl = MAIN_IMAGE_PATH + str("MENU.jpg")
            elif selectedKey == "MenuSettings":
               imageUrl = MAIN_IMAGE_PATH + str("MENU.jpg")
            elif selectedKey == "PluginSettings":
               imageUrl = MAIN_IMAGE_PATH + str("PLUGIN.jpg")
            elif selectedKey == "InfobarSettings":
               imageUrl = MAIN_IMAGE_PATH + str("IB.jpg")
            elif selectedKey == "InfobarExtraSettings":
               imageUrl = MAIN_IMAGE_PATH + str("EXTRA.jpg")
            elif selectedKey == "ChannelSettings":
               imageUrl = MAIN_IMAGE_PATH + str("CS.jpg")
            elif selectedKey == "SonstigeSettings":
               imageUrl = MAIN_IMAGE_PATH + str("OTHER.jpg")
            elif selectedKey == "SystemOSDSettings":
               imageUrl = MAIN_IMAGE_PATH + str("OSD.jpg") 
            elif selectedKey == "SystemChannelSettings":
               imageUrl = MAIN_IMAGE_PATH + str("SCS.jpg")
            elif selectedKey == "SkinParts":
               imageUrl = MAIN_IMAGE_PATH + str("SP.jpg")
            elif selectedKey == "OSDPositionSetup":
               imageUrl = MAIN_IMAGE_PATH + str("OSDPositionSetup.jpg")
                           
        self.PicLoad.setPara([self["helperimage"].instance.size().width(),self["helperimage"].instance.size().height(),self.Scale[0],self.Scale[1],0,1,"#00000000"])
        self.PicLoad.startDecode(imageUrl)

    def DecodePicture(self, PicInfo = ""):
        ptr = self.PicLoad.getData()
        self["helperimage"].instance.setPixmap(ptr)

    def ok(self):
        cur = self["menuList"].getCurrent()
        
        if cur:
            selectedKey = cur[0][1]
            self.debug('def ok\ntry open: "' + selectedKey + '" Screen\n')
                               
            if selectedKey == "MainSettings":
                self.session.open(MainSettings)
            elif selectedKey == "FontSettings":
                self.session.open(FontSettings)
            elif selectedKey == "MenuSettings":
                self.session.open(MenuSettings)
            elif selectedKey == "PluginSettings":
                self.session.open(PluginSettings)
            elif selectedKey == "InfobarSettings":
                self.session.open(InfobarSettings)
            elif selectedKey == "InfobarExtraSettings":
                self.session.open(InfobarExtraSettings)
    	    elif selectedKey == "ChannelSettings":
                self.session.open(ChannelSettings)  
            elif selectedKey == "SonstigeSettings":
                self.session.open(SonstigeSettings)
            elif selectedKey == "SystemOSDSettings":
                self.session.open(Setup, "userinterface")   
            elif selectedKey == "SystemChannelSettings":
                self.session.open(Setup, "channelselection")
            elif selectedKey == "SkinParts":
                self.session.open(SkinParts)
            elif selectedKey == "OSDPositionSetup":
                if OSDScreenPosition_plugin:
                   self.session.open(OverscanWizard)
                else:
                   self.session.open(UserInterfacePositioner)
                                   
    def ask_for_save(self):
        if config.plugins.SevenHD.skin_mode.value == '1':
           self.server_dir = 'SevenHD'
           self.value = float(1)
        if config.plugins.SevenHD.skin_mode.value == '2':
           self.server_dir = 'SevenFHD'
           self.value = float(1.5)
        if config.plugins.SevenHD.skin_mode.value >= '3':
           if config.plugins.SevenHD.skin_mode.value == '3': 
              msg_text = '3840x2160 for UHD'
              self.server_dir = 'SevenUHD'
              self.value = float(3)
           if config.plugins.SevenHD.skin_mode.value == '4':
              msg_text = '4096x2160 for 4k'
              self.server_dir = 'Seven4k'
              self.value = float(3)
           if config.plugins.SevenHD.skin_mode.value == '5':
              msg_text = '7680x4320 for FUHD'
              self.server_dir = 'SevenFUHD'
              self.value = float(4.5)
           if config.plugins.SevenHD.skin_mode.value == '6':
              msg_text = '8192x4320 for 8k'
              self.server_dir = 'Seven8k'
              self.value = float(4.5)     
           if config.plugins.SevenHD.skin_mode.value == '7':
              msg_text = '%sx%s' % (str(int(config.plugins.SevenHD.skin_mode_x.value)), str(int(config.plugins.SevenHD.skin_mode_y.value)))
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '1280':
                 self.server_dir = 'SevenHD'
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '1920':
                 self.server_dir = 'SevenFHD'
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '3840':
                 self.server_dir = 'SevenUHD'
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '4096':
                 self.server_dir = 'Seven4k'
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '7680':
                 self.server_dir = 'SevenFUHD'
              if str(config.plugins.SevenHD.skin_mode_x.value) >= '8192':
                 self.server_dir = 'Seven8k'
                 
           self.session.openWithCallback(self.answer, MessageBox, _('Sure that your Box support\nyour Resolution %s?\n' % str(msg_text)), MessageBox.TYPE_YESNO, default = False)   
        else:
           self.save()
    
    def answer(self, what):
        if what is True:
           self.save()
        else:
           self.exit()
           
    def save(self):
        self.skin_lines = []        
        try:
                #global tag search and replace in all skin elements
		self.skinSearchAndReplace = []
                # Normal Font
                self.FontStyle_1 = config.plugins.SevenHD.FontStyle_1.value
                self.FontStyleHeight_1 = config.plugins.SevenHD.FontStyleHeight_1.value
                if self.FontStyle_1 != 'noto':
                   if self.FontStyle_1 == 'campton':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/Campton Light.otf" name="Regular" scale="%s" />' % str(self.FontStyleHeight_1)])
                   elif self.FontStyle_1 == 'handel':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/HandelGotD.ttf" name="Regular" scale="%s" />' % str(self.FontStyleHeight_1)])
                   elif self.FontStyle_1 == 'proxima':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/Proxima Nova Regular.otf" name="Regular" scale="%s" />' % str(self.FontStyleHeight_1)])
                   elif self.FontStyle_1 == 'opensans':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/setrixHD.ttf" name="Regular" scale="%s" />' % str(self.FontStyleHeight_1)])
                   elif '?systemfont' in self.FontStyle_1:
                      self.Font_1 = self.FontStyle_1.split('?')[0]
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/%s" name="Regular" scale="%s" />' % (str(self.Font_1),str(self.FontStyleHeight_1))])
                else:
                   self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="95" />', '<font filename="SevenHD/fonts/NotoSans-Regular.ttf" name="Regular" scale="%s" />' % str(self.FontStyleHeight_1)])
                   
                # Bold Font
                self.FontStyle_2 = config.plugins.SevenHD.FontStyle_2.value
                self.FontStyleHeight_2 = config.plugins.SevenHD.FontStyleHeight_2.value
                if self.FontStyle_2 != 'noto':
                   if self.FontStyle_2 == 'campton':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/Campton Medium.otf" name="Regular2" scale="%s" />' % str(self.FontStyleHeight_2)])
                   elif self.FontStyle_2 == 'handel':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/HandelGotDBol.ttf" name="Regular2" scale="%s" />' % str(self.FontStyleHeight_2)])
                   elif self.FontStyle_2 == 'proxima':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/Proxima Nova Bold.otf" name="Regular2" scale="%s" />' % str(self.FontStyleHeight_2)])
                   elif self.FontStyle_2 == 'opensans':
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/OpenSans-Regular.ttf" name="Regular2" scale="%s" />' % str(self.FontStyleHeight_2)])
                   elif '?systemfont' in self.FontStyle_2:
                      self.Font_2 = self.FontStyle_2.split('?')[0]
                      self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/%s" name="Regular2" scale="%s" />' % (str(self.Font_2),str(self.FontStyleHeight_2))])
                else:
                   self.skinSearchAndReplace.append(['<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="95" />', '<font filename="SevenHD/fonts/NotoSans-Bold.ttf" name="Regular2" scale="%s" />' % str(self.FontStyleHeight_2)])
                      
                self.BackgroundLeft = config.plugins.SevenHD.BackgroundLeft.value
                if self.BackgroundLeft.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/menumain.png","SevenHD/back/menumain_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menuplayer.png","SevenHD/back/menuplayer_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menuplayersmall.png","SevenHD/back/menuplayersmall_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menuquick.png","SevenHD/back/menuquick_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menusmall.png","SevenHD/back/menusmall_1.png"])
                   if self.BackgroundLeft.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackgroundLeft" value="#00000000"', 'name="SevenBackgroundLeft" value="#%s%s"' % (config.plugins.SevenHD.BackgroundLeftColorTrans.value, config.plugins.SevenHD.GradientMenuTop.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackgroundLeft" value="#00000000"', 'name="SevenFontBackgroundLeft" value="#%s%s"' % (config.plugins.SevenHD.BackgroundLeftColorTrans.value, config.plugins.SevenHD.GradientMenuTop.value[2:8])])
                else:  
                   self.skinSearchAndReplace.append(['name="SevenBackgroundLeft" value="#00000000"', 'name="SevenBackgroundLeft" value="#%s%s"' % (config.plugins.SevenHD.BackgroundLeftColorTrans.value, self.BackgroundLeft[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackgroundLeft" value="#00000000"', 'name="SevenFontBackgroundLeft" value="#%s%s"' % (config.plugins.SevenHD.BackgroundLeftColorTrans.value, self.BackgroundLeft[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menumain.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menuplayer.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menuplayersmall.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menuquick.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menusmall.png"',""])
                
                self.BackgroundRight = config.plugins.SevenHD.BackgroundRight.value
                if self.BackgroundRight.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/menuright.png","SevenHD/back/menuright_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menutop.png","SevenHD/back/menutop_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/menurightsmall.png","SevenHD/back/menurightsmall_1.png"])
                   if self.BackgroundRight.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackgroundRight" value="#00000000"', 'name="SevenBackgroundRight" value="#%s%s"' % (config.plugins.SevenHD.BackgroundRightColorTrans.value, config.plugins.SevenHD.GradientMenuRightTop.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackgroundRight" value="#00000000"', 'name="SevenFontBackgroundRight" value="#%s%s"' % (config.plugins.SevenHD.BackgroundRightColorTrans.value, config.plugins.SevenHD.GradientMenuRightTop.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackgroundRight" value="#00000000"', 'name="SevenBackgroundRight" value="#%s%s"' % (config.plugins.SevenHD.BackgroundRightColorTrans.value, self.BackgroundRight[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackgroundRight" value="#00000000"', 'name="SevenFontBackgroundRight" value="#%s%s"' % (config.plugins.SevenHD.BackgroundRightColorTrans.value, self.BackgroundRight[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menuright.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menutop.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/menurightsmall.png"',""])
                
                self.BackgroundIB1 = config.plugins.SevenHD.BackgroundIB1.value
                if self.BackgroundIB1.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/ibone.png","SevenHD/back/ibone_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sysinfo.png","SevenHD/back/sysinfo_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/ibtop.png","SevenHD/back/ibtop_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibleft.png","SevenHD/back/sibleft_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/weatherbig.png","SevenHD/back/weatherbig_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibleftmetrix.png","SevenHD/back/sibleftmetrix_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibleftdouble.png","SevenHD/back/sibleftdouble_1.png"])
                   if self.BackgroundIB1.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackgroundIB1" value="#00000000"', 'name="SevenBackgroundIB1" value="#%s%s"' % (config.plugins.SevenHD.IB1ColorTrans.value, config.plugins.SevenHD.GradientIB1Top.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackgroundIB1" value="#00000000"', 'name="SevenFontBackgroundIB1" value="#%s%s"' % (config.plugins.SevenHD.IB1ColorTrans.value, config.plugins.SevenHD.GradientIB1Top.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackgroundIB1" value="#00000000"', 'name="SevenBackgroundIB1" value="#%s%s"' % (config.plugins.SevenHD.IB1ColorTrans.value, self.BackgroundIB1[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackgroundIB1" value="#00000000"', 'name="SevenFontBackgroundIB1" value="#%s%s"' % (config.plugins.SevenHD.IB1ColorTrans.value, self.BackgroundIB1[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/ibone.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sysinfo.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/ibtop.png"',""]) 
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibleft.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/weatherbig.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibleftmetrix.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibleftdouble.png"',""])
                
                self.BackgroundIB2 = config.plugins.SevenHD.BackgroundIB2.value
                if self.BackgroundIB2.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/sibtop.png","SevenHD/back/sibtop_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibtopbig.png","SevenHD/back/sibtopbig_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibright.png","SevenHD/back/sibright_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibrightmetrix.png","SevenHD/back/sibrightmetrix_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/sibrightdouble.png","SevenHD/back/sibrightdouble_1.png"])
                   if self.BackgroundIB2.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackgroundIB2" value="#00000000"', 'name="SevenBackgroundIB2" value="#%s%s"' % (config.plugins.SevenHD.IB2ColorTrans.value, config.plugins.SevenHD.GradientIB2Top.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackgroundIB2" value="#00000000"', 'name="SevenFontBackgroundIB2" value="#%s%s"' % (config.plugins.SevenHD.IB2ColorTrans.value, config.plugins.SevenHD.GradientIB2Top.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackgroundIB2" value="#00000000"', 'name="SevenBackgroundIB2" value="#%s%s"' % (config.plugins.SevenHD.IB2ColorTrans.value, self.BackgroundIB2[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackgroundIB2" value="#00000000"', 'name="SevenFontBackgroundIB2" value="#%s%s"' % (config.plugins.SevenHD.IB2ColorTrans.value, self.BackgroundIB2[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibtop.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibtopbig.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibright.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibrightmetric.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/sibrightdouble.png"',""])
                
                self.ChannelBack1 = config.plugins.SevenHD.ChannelBack1.value
                if self.ChannelBack1.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/csleft.png","SevenHD/back/csleft_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/cssmall.png","SevenHD/back/cssmall_1.png"])
                   if self.ChannelBack1.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackCS" value="#00000000"', 'name="SevenBackCS" value="#%s%s"' % (config.plugins.SevenHD.CSLeftColorTrans.value, config.plugins.SevenHD.GradientCSLeftTop.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackCS" value="#00000000"', 'name="SevenFontBackCS" value="#%s%s"' % (config.plugins.SevenHD.CSLeftColorTrans.value, config.plugins.SevenHD.GradientCSLeftTop.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackCS" value="#00000000"', 'name="SevenBackCS" value="#%s%s"' % (config.plugins.SevenHD.CSLeftColorTrans.value, self.ChannelBack1[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackCS" value="#00000000"', 'name="SevenFontBackCS" value="#%s%s"' % (config.plugins.SevenHD.CSLeftColorTrans.value, self.ChannelBack1[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/csleft.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/cssmall.png"',""])
                
                self.ChannelBack2 = config.plugins.SevenHD.ChannelBack2.value
                if self.ChannelBack2.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/csright.png","SevenHD/back/csright_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/cstop.png","SevenHD/back/cstop_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/back/csrightsmall.png","SevenHD/back/csrightsmall_1.png"])
                   if self.ChannelBack2.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackRightCS" value="#00000000"', 'name="SevenBackRightCS" value="#%s%s"' % (config.plugins.SevenHD.CSRightColorTrans.value, config.plugins.SevenHD.GradientCSRightTop.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackRightCS" value="#00000000"', 'name="SevenFontBackRightCS" value="#%s%s"' % (config.plugins.SevenHD.CSRightColorTrans.value, config.plugins.SevenHD.GradientCSRightTop.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackRightCS" value="#00000000"', 'name="SevenBackRightCS" value="#%s%s"' % (config.plugins.SevenHD.CSRightColorTrans.value, self.ChannelBack2[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackRightCS" value="#00000000"', 'name="SevenFontBackRightCS" value="#%s%s"' % (config.plugins.SevenHD.CSRightColorTrans.value, self.ChannelBack2[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/csright.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/cstop.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/csrightsmall.png"',""])
                
                self.ChannelBack3 = config.plugins.SevenHD.ChannelBack3.value
                if self.ChannelBack3.startswith('back'):
                   self.skinSearchAndReplace.append(["SevenHD/back/csmiddle.png","SevenHD/back/csmiddle_1.png"])
                   if self.ChannelBack3.startswith('back_gradient'):
                      self.skinSearchAndReplace.append(['name="SevenBackMiddleCS" value="#00000000"', 'name="SevenBackMiddleCS" value="#%s%s"' % (config.plugins.SevenHD.CSMiddleColorTrans.value, config.plugins.SevenHD.GradientCSMiddleTop.value[2:8])])
                      self.skinSearchAndReplace.append(['name="SevenFontBackMiddleCS" value="#00000000"', 'name="SevenFontBackMiddleCS" value="#%s%s"' % (config.plugins.SevenHD.CSMiddleColorTrans.value, config.plugins.SevenHD.GradientCSMiddleTop.value[2:8])])
                else:
                   self.skinSearchAndReplace.append(['name="SevenBackMiddleCS" value="#00000000"', 'name="SevenBackMiddleCS" value="#%s%s"' % (config.plugins.SevenHD.CSMiddleColorTrans.value, self.ChannelBack3[2:8])])
                   self.skinSearchAndReplace.append(['name="SevenFontBackMiddleCS" value="#00000000"', 'name="SevenFontBackMiddleCS" value="#%s%s"' % (config.plugins.SevenHD.CSMiddleColorTrans.value, self.ChannelBack3[2:8])])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/back/csmiddle.png"',""])
                
		self.skinSearchAndReplace.append(['name="SevenBackground" value="#00000000"', 'name="SevenBackground" value="#%s%s"' % (config.plugins.SevenHD.BackgroundColorTrans.value, config.plugins.SevenHD.Background.value[2:8])])
		self.skinSearchAndReplace.append(['name="SevenFontBackground" value="#00000000"', 'name="SevenFontBackground" value="#%s%s"' % (config.plugins.SevenHD.BackgroundColorTrans.value, config.plugins.SevenHD.Background.value[2:8])])

		self.skinSearchAndReplace.append(["Seven_Selection", config.plugins.SevenHD.SelectionBackground.value])
		self.skinSearchAndReplace.append(["SevenFont_1", config.plugins.SevenHD.Font1.value])
		self.skinSearchAndReplace.append(["SevenFont_2", config.plugins.SevenHD.Font2.value])
		self.skinSearchAndReplace.append(["SevenSel_Font", config.plugins.SevenHD.SelectionFont.value])
		self.skinSearchAndReplace.append(["SevenButton_Text", config.plugins.SevenHD.ButtonText.value])
		if not config.plugins.SevenHD.Border.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorder"', '<eLabel backgroundColor="SevenBorder"'])
			self.skinSearchAndReplace.append(['zPosition="101" />-->', 'zPosition="101" />'])
		else:
			self.skinSearchAndReplace.append(['borderWidth="2" borderColor="SevenBorder"', ' '])
			self.skinSearchAndReplace.append(['borderColor="SevenBorder" borderWidth="2"', ' '])
			self.skinSearchAndReplace.append(['borderColor="SevenBorder" borderWidth="1"', ' '])
		self.skinSearchAndReplace.append(["Seven_Border", config.plugins.SevenHD.Border.value])
		if not config.plugins.SevenHD.Line.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLine"', '<eLabel backgroundColor="SevenLine"'])
			self.skinSearchAndReplace.append(['zPosition="108" />-->', 'zPosition="108" />'])
		self.skinSearchAndReplace.append(["Seven_Line", config.plugins.SevenHD.Line.value])
		if not config.plugins.SevenHD.BorderRight.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderRight"', '<eLabel backgroundColor="SevenBorderRight"'])
			self.skinSearchAndReplace.append(['zPosition="102" />-->', 'zPosition="102" />'])
		self.skinSearchAndReplace.append(["SevenBorder_Right", config.plugins.SevenHD.BorderRight.value])
		if not config.plugins.SevenHD.LineRight.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineRight"', '<eLabel backgroundColor="SevenLineRight"'])
			self.skinSearchAndReplace.append(['zPosition="109" />-->', 'zPosition="109" />'])
		self.skinSearchAndReplace.append(["SevenLine_Right", config.plugins.SevenHD.LineRight.value])

		self.skinSearchAndReplace.append(["SevenFont_ECM", config.plugins.SevenHD.SevenECM.value])
		self.skinSearchAndReplace.append(["SevenFont_Sat", config.plugins.SevenHD.SevenSat.value])
		self.skinSearchAndReplace.append(["SevenFont_Sys1", config.plugins.SevenHD.SevenSys1.value])
		self.skinSearchAndReplace.append(["SevenFont_Sys2", config.plugins.SevenHD.SevenSys2.value])
		self.skinSearchAndReplace.append(["SevenFont_Weather1", config.plugins.SevenHD.SevenWeather1.value])
		self.skinSearchAndReplace.append(["SevenFont_Weather2", config.plugins.SevenHD.SevenWeather2.value])
		self.skinSearchAndReplace.append(["SevenFont_Weather3", config.plugins.SevenHD.SevenWeather3.value])

		self.skinSearchAndReplace.append(["SevenMeteo_Font", config.plugins.SevenHD.MeteoColor.value])


		self.skinSearchAndReplace.append(["SevenProgress_BorderCS", config.plugins.SevenHD.ProgressBorderCS.value])
		self.skinSearchAndReplace.append(["SevenProgress_LineCS", config.plugins.SevenHD.ProgressLineCS.value])
		self.skinSearchAndReplace.append(["SevenProgress_LineIB", config.plugins.SevenHD.ProgressLineIB.value])
		self.skinSearchAndReplace.append(["SevenProgress_LinePlug", config.plugins.SevenHD.ProgressLinePlug.value])
		self.skinSearchAndReplace.append(["SevenProgress_LineVol", config.plugins.SevenHD.ProgressLineVol.value])


		self.skinSearchAndReplace.append(["SevenProgress_IB", config.plugins.SevenHD.ProgressIB.value])
		self.skinSearchAndReplace.append(["SevenProgress_Vol", config.plugins.SevenHD.ProgressVol.value])
		self.skinSearchAndReplace.append(["SevenProgress_CS", config.plugins.SevenHD.ProgressCS.value])
		self.skinSearchAndReplace.append(["SevenProgress_ListCS", config.plugins.SevenHD.ProgressListCS.value])


		self.skinSearchAndReplace.append(["SevenProgress_IB", config.plugins.SevenHD.ProgressIB.value])
		self.skinSearchAndReplace.append(["SevenProgress_Vol", config.plugins.SevenHD.ProgressVol.value])


		if not config.plugins.SevenHD.InfobarBorder.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderIB"', '<eLabel backgroundColor="SevenBorderIB"'])
			self.skinSearchAndReplace.append(['zPosition="103" />-->', 'zPosition="103" />'])
		else:
			self.skinSearchAndReplace.append(['borderWidth="2" borderColor="SevenBorderIB"', ' '])
		self.skinSearchAndReplace.append(["SevenBorder_IB", config.plugins.SevenHD.InfobarBorder.value])
		if not config.plugins.SevenHD.InfobarLine.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineIB"', '<eLabel backgroundColor="SevenLineIB"'])
			self.skinSearchAndReplace.append(['zPosition="110" />-->', 'zPosition="110" />'])
		self.skinSearchAndReplace.append(["SevenLine_IB", config.plugins.SevenHD.InfobarLine.value])
		if not config.plugins.SevenHD.InfobarBorder2.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderIB2"', '<eLabel backgroundColor="SevenBorderIB2"'])
			self.skinSearchAndReplace.append(['zPosition="104" />-->', 'zPosition="104" />'])
		self.skinSearchAndReplace.append(["SevenBorder2_IB", config.plugins.SevenHD.InfobarBorder2.value])
		if not config.plugins.SevenHD.InfobarLine2.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineIB2"', '<eLabel backgroundColor="SevenLineIB2"'])
			self.skinSearchAndReplace.append(['zPosition="111" />-->', 'zPosition="111" />'])
		self.skinSearchAndReplace.append(["SevenLine2_IB", config.plugins.SevenHD.InfobarLine2.value])
		self.skinSearchAndReplace.append(["SevenNext_IB", config.plugins.SevenHD.NextEvent.value])
		self.skinSearchAndReplace.append(["SevenNow_IB", config.plugins.SevenHD.NowEvent.value])
		self.skinSearchAndReplace.append(["SevenSNR_IB", config.plugins.SevenHD.SNR.value])
		self.skinSearchAndReplace.append(["SevenFont_CN", config.plugins.SevenHD.FontCN.value])


		self.skinSearchAndReplace.append(["SevenClock_Date", config.plugins.SevenHD.ClockDate.value])
		self.skinSearchAndReplace.append(["SevenClock_H", config.plugins.SevenHD.ClockTimeh.value])
		self.skinSearchAndReplace.append(["SevenClock_M", config.plugins.SevenHD.ClockTimem.value])
		self.skinSearchAndReplace.append(["SevenClock_S", config.plugins.SevenHD.ClockTimes.value])
		self.skinSearchAndReplace.append(["SevenClock_Time", config.plugins.SevenHD.ClockTime.value])
		self.skinSearchAndReplace.append(["SevenClock_Weather", config.plugins.SevenHD.ClockWeather.value])
		self.skinSearchAndReplace.append(["SevenClock_Weekday", config.plugins.SevenHD.ClockWeek.value])


		if not config.plugins.SevenHD.ChannelLine.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineCS"', '<eLabel backgroundColor="SevenLineCS"'])
			self.skinSearchAndReplace.append(['zPosition="112" />-->', 'zPosition="112" />'])
		self.skinSearchAndReplace.append(["SevenLine_CS", config.plugins.SevenHD.ChannelLine.value])
		if not config.plugins.SevenHD.ChannelLineRight.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineRightCS"', '<eLabel backgroundColor="SevenLineRightCS"'])
			self.skinSearchAndReplace.append(['zPosition="113" />-->', 'zPosition="113" />'])
		self.skinSearchAndReplace.append(["SevenLineRight_CS", config.plugins.SevenHD.ChannelLineRight.value])
		if not config.plugins.SevenHD.ChannelLineMiddle.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenLineMiddleCS"', '<eLabel backgroundColor="SevenLineMiddleCS"'])
			self.skinSearchAndReplace.append(['zPosition="114" />-->', 'zPosition="114" />'])
		self.skinSearchAndReplace.append(["SevenLineMiddle_CS", config.plugins.SevenHD.ChannelLineMiddle.value])
		if not config.plugins.SevenHD.ChannelBorder.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderCS"', '<eLabel backgroundColor="SevenBorderCS"'])
			self.skinSearchAndReplace.append(['zPosition="105" />-->', 'zPosition="105" />'])
		self.skinSearchAndReplace.append(["SevenBorder_CS", config.plugins.SevenHD.ChannelBorder.value])
		if not config.plugins.SevenHD.ChannelBorderRight.value == "ff000000":
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderRightCS"', '<eLabel backgroundColor="SevenBorderRightCS"'])
			self.skinSearchAndReplace.append(['zPosition="106" />-->', 'zPosition="106" />'])
		self.skinSearchAndReplace.append(["SevenBorderRight_CS", config.plugins.SevenHD.ChannelBorderRight.value])
		if not config.plugins.SevenHD.ChannelBorderMiddle.value == "ff000000":
			self.skinSearchAndReplace.append(["SevenBorderMiddle_CS", config.plugins.SevenHD.ChannelBorderMiddle.value])
			self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenBorderMiddleCS"', '<eLabel backgroundColor="SevenBorderMiddleCS"'])
			self.skinSearchAndReplace.append(['zPosition="107" />-->', 'zPosition="107" />'])
		self.skinSearchAndReplace.append(["SevenBorderMiddle_CS", config.plugins.SevenHD.ChannelBorderMiddle.value])
		self.skinSearchAndReplace.append(["SevenButtons_CS", config.plugins.SevenHD.ChannelColorButton.value])
		self.skinSearchAndReplace.append(["SevenBouquet_CS", config.plugins.SevenHD.ChannelColorBouquet.value])
		self.skinSearchAndReplace.append(["SevenChannel_CS", config.plugins.SevenHD.ChannelColorChannel.value])
		self.skinSearchAndReplace.append(["SevenNext_CS", config.plugins.SevenHD.ChannelColorNext.value])
		self.skinSearchAndReplace.append(["SevenDestcriptionNext_CS", config.plugins.SevenHD.ChannelColorDesciptionNext.value])
		self.skinSearchAndReplace.append(["SevenDestcriptionLater_CS", config.plugins.SevenHD.ChannelColorDesciptionLater.value])
		self.skinSearchAndReplace.append(["SevenRuntime_CS", config.plugins.SevenHD.ChannelColorRuntime.value])
		self.skinSearchAndReplace.append(["SevenProgram_CS", config.plugins.SevenHD.ChannelColorProgram.value])
		self.skinSearchAndReplace.append(["SevenTime_CS", config.plugins.SevenHD.ChannelColorTimeCS.value])
		self.skinSearchAndReplace.append(["SevenPrime_CS", config.plugins.SevenHD.ChannelColorPrimeTime.value])
		self.skinSearchAndReplace.append(["SevenDestcription_CS", config.plugins.SevenHD.ChannelColorDesciption.value])
		self.skinSearchAndReplace.append(["SevenName_List", config.plugins.SevenHD.ChannelColorChannelName.value])
		self.skinSearchAndReplace.append(["SevenNumber_List", config.plugins.SevenHD.ChannelColorChannelNumber.value])
		self.skinSearchAndReplace.append(["SevenProgram_List", config.plugins.SevenHD.ChannelColorEvent.value])
		
		# Weather Font
                provider = config.plugins.SevenHD.weather_server.value
                if provider == '_accu' or provider == '_realtek':
                   font = 'Meteo'   
                elif provider == '_owm':
                   font = 'Meteo2'
                
                if config.plugins.SevenHD.WeatherView.value == "meteo": 
                   self.skinSearchAndReplace.append(['size="50,50" path="WetterIcons" render="SevenHDWetterPicon" alphatest="blend"', 'size="50,50" render="Label" font="%s; 45" halign="center" valign="center" foregroundColor="SevenMeteoFont" backgroundColor="SevenFontBackgroundIB1" noWrap="1"' % font])
                   self.skinSearchAndReplace.append(['size="70,70" render="SevenHDWetterPicon" alphatest="blend" path="WetterIcons"', 'size="70,70" render="Label" font="%s; 70" halign="center" valign="center" foregroundColor="SevenMeteoFont" backgroundColor="SevenFontBackgroundIB1" noWrap="1"' % font])  
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_0,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_0,MeteoFont' % str(provider)])
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_1,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_1,MeteoFont' % str(provider)])
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_2,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_2,MeteoFont' % str(provider)])
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_3,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_3,MeteoFont' % str(provider)])
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_4,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_4,MeteoFont' % str(provider)])    
                   self.skinSearchAndReplace.append(['convert  type="SevenHDWeather%s">Day_5,MeteoIcon' % str(provider), 'convert  type="SevenHDWeather%s">Day_5,MeteoFont' % str(provider)])     
      
                ### Progress
                if config.plugins.SevenHD.Progress.value == "progress":
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress52.png","SevenHD/progress/progress52_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress300.png","SevenHD/progress/progress300_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress362.png","SevenHD/progress/progress362_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress535.png","SevenHD/progress/progress535_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress793.png","SevenHD/progress/progress793_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress858.png","SevenHD/progress/progress858_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress990.png","SevenHD/progress/progress990_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progress/progress1280.png","SevenHD/progress/progress1280_1.png"])
                else:
                   self.skinSearchAndReplace.append(["00fffff1", config.plugins.SevenHD.Progress.value])
                   self.skinSearchAndReplace.append(['picServiceEventProgressbar="SevenHD/progress/progress52.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress300.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress362.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress535.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress793.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress858.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress990.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progress/progress1280.png"',""])
                       
                ### ProgressIB
                if config.plugins.SevenHD.ProgressIB.value == "progressib":
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib621.png","SevenHD/progressib/progressib621_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib638.png","SevenHD/progressib/progressib638_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib770.png","SevenHD/progressib/progressib770_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib793.png","SevenHD/progressib/progressib793_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib812.png","SevenHD/progressib/progressib812_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib858.png","SevenHD/progressib/progressib858_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib1022.png","SevenHD/progressib/progressib1022_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib1045.png","SevenHD/progressib/progressib1045_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressib/progressib1280.png","SevenHD/progressib/progressib1280_1.png"])
                else:
                   self.skinSearchAndReplace.append(["00fffff2", config.plugins.SevenHD.ProgressIB.value])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib621.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib638.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib770.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib793.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib812.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib858.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib1022.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib1045.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressib/progressib1280.png"',""])
                       
                ### ProgressVol
                if config.plugins.SevenHD.ProgressVol.value == "progressvol":
                   self.skinSearchAndReplace.append(["SevenHD/progressvol/progressvol170.png","SevenHD/progressvol/progressvol170_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressvol/progressvol213.png","SevenHD/progressvol/progressvol213_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progressvol/progress213vvol.png","SevenHD/progressvol/progress213vvol_1.png"])
                else:
                   self.skinSearchAndReplace.append(["00fffff3", config.plugins.SevenHD.ProgressVol.value])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressvol/progressvol170.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressvol/progressvol213.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progressvol/progress213vvol.png"',""])
                       
                ### ProgressCS
                if config.plugins.SevenHD.ProgressCS.value == "progresscs":
                   self.skinSearchAndReplace.append(["SevenHD/progresscs/progresscs52.png","SevenHD/progresscs/progresscs52_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progresscs/progresscs362.png","SevenHD/progresscs/progresscs362_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progresscs/progresscs426.png","SevenHD/progresscs/progresscs426_1.png"])
                   self.skinSearchAndReplace.append(["SevenHD/progresscs/progresscs514.png","SevenHD/progresscs/progresscs514_1.png"])
                else:
                   self.skinSearchAndReplace.append(["00fffff4", config.plugins.SevenHD.ProgressCS.value])
                   self.skinSearchAndReplace.append(['picServiceEventProgressbar="SevenHD/progresscs/progresscs52.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progresscs/progresscs362.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progresscs/progresscs426.png"',""])
                   self.skinSearchAndReplace.append(['pixmap="SevenHD/progresscs/progresscs514.png"',""])
                       
                ### ProgressListCS
                if config.plugins.SevenHD.ProgressListCS.value == "progresslistcs":
                   self.skinSearchAndReplace.append(["SevenHD/progresslistcs/progresslistcs52.png","SevenHD/progresslistcs/progresslistcs52_1.png"])
                else:
                   self.skinSearchAndReplace.append(["00fffff5", config.plugins.SevenHD.ProgressListCS.value])
                   self.skinSearchAndReplace.append(['picServiceEventProgressbar="SevenHD/progresslistcs/progresslistcs52.png"',""])

		self.skinSearchAndReplace.append(["buttons_seven_white", config.plugins.SevenHD.ButtonStyle.value])
		self.skinSearchAndReplace.append(["icons_seven_white", config.plugins.SevenHD.IconStyle.value])

		### FrontInfo
		if config.plugins.SevenHD.FrontInfo.value == "db":
		   self.skinSearchAndReplace.append(['<convert type="FrontendInfo">SNR' , '<convert type="FrontendInfo">SNRdB'])

		### Text (running, writing, none)
		if config.plugins.SevenHD.RunningText.value == "writing":
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,startpoint=0,startdelay=2000,steptime=90,wrap=1,always=0,repeat=2,oneshot=1"', 'render="SevenHDEmptyEpg"'])
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,direction=top,startpoint=0,startdelay=2000,steptime=90,wrap=1,always=0,repeat=2,oneshot=1"', 'render="SevenHDEmptyEpg"'])
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,startpoint=0,startdelay=2000,steptime=90,wrap=0,always=0,repeat=2,oneshot=1"', 'render="SevenHDEmptyEpg"'])
		elif config.plugins.SevenHD.RunningText.value == "none":
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,startpoint=0,startdelay=2000,steptime=90,wrap=1,always=0,repeat=2,oneshot=1"', 'render="Label"'])
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,direction=top,startpoint=0,startdelay=2000,steptime=90,wrap=1,always=0,repeat=2,oneshot=1"', 'render="Label"'])
			self.skinSearchAndReplace.append(['render="SevenHDRunningText" options="movetype=running,startpoint=0,startdelay=2000,steptime=90,wrap=0,always=0,repeat=2,oneshot=1"', 'render="Label"'])
		
		self.skinSearchAndReplace.append(["startdelay=2000", "startdelay=%s" % str(int(config.plugins.SevenHD.Startdelay.value) * 1000)])
		
		self.skinSearchAndReplace.append(["steptime=90", "steptime=%s" % str(config.plugins.SevenHD.Steptime.value)])
			
		if not config.plugins.SevenHD.SelectionBorder.value == "none":
			self.selectionbordercolor = config.plugins.SevenHD.SelectionBorder.value
			self.borset = ("borset_" + self.selectionbordercolor + ".png")
			self.skinSearchAndReplace.append(["borset.png", self.borset])
		
		self.analogstylecolor = config.plugins.SevenHD.AnalogStyle.value
		self.analog = ("analog_" + self.analogstylecolor + ".png")
		self.skinSearchAndReplace.append(["analog.png", self.analog])
		
		self.tuner_Count = self.getTunerCount()
		self.debug("verbaute Tuner: " + str(self.tuner_Count))
		
                if str(self.tuner_Count) == str('1'):
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/b_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/b_off.png"'])
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/c_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/c_off.png"'])
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/d_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/d_off.png"'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerB -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerB -->'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerC -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerC -->'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerD -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerD -->'])
		if str(self.tuner_Count) == str('2'):
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/c_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/c_off.png"'])
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/d_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/d_off.png"'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerC -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerC -->'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerD -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerD -->'])
                if str(self.tuner_Count) == str('3'):
		   self.skinSearchAndReplace.append(['<ePixmap pixmap="SevenHD/buttons/d_off.png"', '<!-- ePixmap pixmap="SevenHD/buttons/d_off.png"'])
		   self.skinSearchAndReplace.append(['size="32,32" zPosition="1" alphatest="blend" /> <!-- TunerD -->', 'size="32,32" zPosition="1" alphatest="blend" / --> <!-- TunerD -->'])
		
		
		### Menu (Logo)
		if  config.plugins.SevenHD.Logo.value == "menu-icons1":
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_nologo" />', '<panel name="template_menu_main_logo" />'])
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_button_nologo" />', '<panel name="template_menu_main_button_logo" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_nologo" />', '<panel name="template_title_main_logo" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_button_nologo" />', '<panel name="template_title_main_button_logo" />'])
		elif  config.plugins.SevenHD.Logo.value == "menu-icons2":
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_nologo" />', '<panel name="template_menu_main_logo2" />'])
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_button_nologo" />', '<panel name="template_menu_main_button_logo2" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_nologo" />', '<panel name="template_title_main_logo2" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_button_nologo" />', '<panel name="template_title_main_button_logo2" />'])
		elif  config.plugins.SevenHD.Logo.value == "menu-icons3":
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_nologo" />', '<panel name="template_menu_main_logo3" />'])
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_button_nologo" />', '<panel name="template_menu_main_button_logo3" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_nologo" />', '<panel name="template_title_main_logo3" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_button_nologo" />', '<panel name="template_title_main_button_logo3" />'])
		elif  config.plugins.SevenHD.Logo.value == "menu-icons4":
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_nologo" />', '<panel name="template_menu_main_logo4" />'])
			self.skinSearchAndReplace.append(['<panel name="template_menu_main_button_nologo" />', '<panel name="template_menu_main_button_logo4" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_nologo" />', '<panel name="template_title_main_logo4" />'])
			self.skinSearchAndReplace.append(['<panel name="template_title_main_button_nologo" />', '<panel name="template_title_main_button_logo4" />'])
			
		#Debug Screen Names in Skins
                if config.plugins.SevenHD.debug_screen_names.value:
                   self.skinSearchAndReplace.append(['<!--<eLabel backgroundColor="SevenFontBackgroundLeft" font="Regular;13" foregroundColor="red"', '<eLabel backgroundColor="SevenFontBackgroundLeft" font="Regular;15" foregroundColor="red"'])
		   self.skinSearchAndReplace.append(['position="50,13" size="500,16" halign="left" valign="center" transparent="1" />-->', 'position="50,13" size="500,19" halign="left" valign="top" transparent="1" />'])
				
                ### Header
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.Header.value + "-begin" + XML)
		if not config.plugins.SevenHD.SelectionBorder.value == "none":
			self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.Header.value + "-middle" + XML)
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.Header.value + "-end" + XML)
                self.debug(MAIN_DATA_PATH + 'header' + XML)
                
                ### Volume
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.VolumeStyle.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.VolumeStyle.value + XML)	
                
                ###ChannelSelection
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ChannelSelectionStyle.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ChannelSelectionStyle.value + XML)    
                
                ###Infobar_main
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-main.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-main.xml")       
                
                ###Channelname Infobar
                if config.plugins.SevenHD.InfobarChannelName.value == "none":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarChannelName.value + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarChannelName.value + XML) 
                if config.plugins.SevenHD.InfobarChannelName.value == "-ICN":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICN.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICN.xml")    
                if config.plugins.SevenHD.InfobarChannelName.value == "-ICNumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNumber.xml") 
                if config.plugins.SevenHD.InfobarChannelName.value == "-ICNameandNumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNameandNumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNameandNumber.xml")
                if config.plugins.SevenHD.InfobarChannelName.value == "-fanart":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanart.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanart.xml")
                if config.plugins.SevenHD.InfobarChannelName.value == "-fanartname":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartname.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartname.xml")
                if config.plugins.SevenHD.InfobarChannelName.value == "-fanartnumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartnumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartnumber.xml")
                if config.plugins.SevenHD.InfobarChannelName.value == "-fanartnamenumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartnamenumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-fanartnamenumber.xml")
                if config.plugins.SevenHD.InfobarChannelName.value == "-thumb":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumb.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumb.xml") 
                if config.plugins.SevenHD.InfobarChannelName.value == "-thumbname":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbname.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbname.xml") 
                if config.plugins.SevenHD.InfobarChannelName.value == "-thumbnumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbnumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbnumber.xml")    
                if config.plugins.SevenHD.InfobarChannelName.value == "-thumbnamenumber":
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbnamenumber.xml")
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-thumbnamenumber.xml")    
                
                ###ecm-info
                if config.plugins.SevenHD.InfobarStyle.value != 'infobar-style-xpicon9':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ECMInfo.value + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ECMInfo.value + XML)        
                
                ###clock-style xml Infobar
                if config.plugins.SevenHD.ClockStyle.value == 'clock-weather':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                elif config.plugins.SevenHD.ClockStyle.value == 'clock-icon':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                elif config.plugins.SevenHD.ClockStyle.value == 'clock-weather-meteo':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                elif config.plugins.SevenHD.ClockStyle.value == 'clock-android':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                else:
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + XML)
                
                ###sat-info
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.SatInfo.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.SatInfo.value + XML)        
                
                ###sys-info
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.SysInfo.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.SysInfo.value + XML)        
                
                ###weather-style_1 Infobar
                if config.plugins.SevenHD.WeatherStyle_1.value != 'none':
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_1.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_1.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                else:
                   self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_1.value + XML)
                   self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_1.value + XML)      
                
                ###weather-style_2 Infobar
                   if config.plugins.SevenHD.WeatherStyle_2.value != 'none':
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   else:
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + XML) 
                
                ###Infobar_middle
                self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-middle.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-middle.xml")         
                
                ###clock-style xml 2nd Infobar
                if not config.plugins.SevenHD.SIB.value in ('-minitv2','-right','-picon','-double'):
                   if config.plugins.SevenHD.ClockStyle.value == 'clock-weather':
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   elif config.plugins.SevenHD.ClockStyle.value == 'clock-icon':
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   elif config.plugins.SevenHD.ClockStyle.value == 'clock-weather-meteo':
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   elif config.plugins.SevenHD.ClockStyle.value == 'clock-android':
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                   else:
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ClockStyle.value + XML)       
                
                ###Channelname 2nd Infobar
                if not config.plugins.SevenHD.SIB.value in ('-minitv2','-right','-picon'):
                   if config.plugins.SevenHD.SIBChannelName.value == "none":
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.SIBChannelName.value + XML)
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarChannelName.value + XML) 
                   if config.plugins.SevenHD.SIBChannelName.value == "-ICN":
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICN.xml")
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICN.xml")    
                   if config.plugins.SevenHD.SIBChannelName.value == "-ICNumber":
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNumber.xml")
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNumber.xml") 
                   if config.plugins.SevenHD.SIBChannelName.value == "-ICNameandNumber":
                      self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNameandNumber.xml")
                      self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + "-ICNameandNumber.xml")
                
                ###weather-style 2nd Infobar
                if config.plugins.SevenHD.InfobarStyle.value == 'infobar-style-xpicon8':
                   if not config.plugins.SevenHD.SIB.value in ('-minitv2','-right','-picon'):
                      if config.plugins.SevenHD.WeatherStyle_2.value != 'none':
                         self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                         self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + str(config.plugins.SevenHD.weather_server.value) + XML)
                      else:
                         self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + XML)
                         self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.WeatherStyle_2.value + XML)
                
                ###ecm-info
                if config.plugins.SevenHD.InfobarStyle.value == 'infobar-style-xpicon8' or config.plugins.SevenHD.InfobarStyle.value != 'infobar-style-xpicon9':
                   if not config.plugins.SevenHD.SIB.value in ('-minitv2','-right','-picon'):
                          self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.ECMInfo.value + XML)
                          self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.ECMInfo.value + XML)        
                
                ###Infobar_end
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + config.plugins.SevenHD.SIB.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.InfobarStyle.value + config.plugins.SevenHD.SIB.value + XML)       
		
                ###Main XML
		self.appendSkinFile(MAIN_DATA_PATH + "main.xml")
                self.debug(MAIN_DATA_PATH + "main.xml")       
                
                ###Plugins XML
		self.appendSkinFile(MAIN_DATA_PATH + "plugins.xml")
                self.debug(MAIN_DATA_PATH + "plugins.xml")        
                
                #EMCSTYLE
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EMCStyle.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EMCStyle.value + XML)        
                
                ###EMCMedia_main
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EMCMedia.value + "-main.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EMCMedia.value + "-main.xml")       
				
                ###picon
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EMCPicon.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EMCPicon.value + XML)        
				
                ###EMCMedia_end
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EMCMedia.value + "-end.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EMCMedia.value + "-end.xml")       
                
                #MOVIESELECTIONSTYLE
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.MovieSelectionStyle.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.MovieSelectionStyle.value + XML)        
                 
                ###MoviePlayer_main
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayer.value + "-main.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayer.value + "-main.xml")       
                
                ###picon
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayerCover.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayerCover.value + XML)        
                
                ###MoviePlayer_end
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayer.value + "-end.xml")
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.MoviePlayer.value + "-end.xml")       
                
                #NumberZapExtStyle
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.NumberZapExt.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.NumberZapExt.value + XML)       
                
                #MSNWeatherPlugin
		if fileExists(PLUGIN_PATH + "Extensions/WeatherPlugin/plugin.pyo"):
			self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.MSNWeather.value + XML)
			self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.MSNWeather.value + XML)         
               
                ###cooltv
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.CoolTVGuide.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.CoolTVGuide.value + XML)      
                
                ###eventview
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EventView.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EventView.value + XML)      
                
                ###epgselection
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.EPGSelection.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.EPGSelection.value + XML)      
                
                ###timeredit
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.TimerEdit.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.TimerEdit.value + XML)      
                
                ###custom-main XML
		self.appendSkinFile(MAIN_DATA_PATH + config.plugins.SevenHD.Image.value + XML)
                self.debug(MAIN_DATA_PATH + config.plugins.SevenHD.Image.value + XML)        
                
                ###skin-user
		if config.plugins.SevenHD.use_skin_parts.value != 'none':
                   if config.plugins.SevenHD.use_skin_parts.value == 'skin_user':
                      try:
		         self.appendSkinFile(MAIN_DATA_PATH + "skin-user.xml")
		      except:
		         pass
                   else:
		       try:
                          list_dir = os.listdir(MAIN_USER_PATH)
                          for part in list_dir:
                             if part.endswith('.part'): 
                                self.appendSkinFile(MAIN_USER_PATH + part)
                       except:
		           pass
		           
                ###skin-end
		self.appendSkinFile(MAIN_DATA_PATH + "skin-end.xml")
                self.debug(MAIN_DATA_PATH + "skin-end.xml")       
                
                try:
                   with open(FILE, 'r') as oldFile:
                        old_skin = oldFile.readlines()
                   for old_res in old_skin:
                       if 'resolution bpp="32" xres="' in old_res:
                          old_skin_resolution = re.search('resolution bpp="32" xres="(.+?)" yres="(.+?)"', str(old_res)).groups(1)
                          break
                   old_resolution = old_skin_resolution[0]
                except:
                   old_resolution = '1280'
                
                self.debug('old Skin xRes: ' + str(old_resolution))
                
                if str(old_resolution) == str('1280'):
                   config.plugins.SevenHD.old_skin_mode.value = '1'
                elif str(old_resolution) == str('1920'):
                   config.plugins.SevenHD.old_skin_mode.value = '2'
                elif str(old_resolution) == str('3840'):
                   config.plugins.SevenHD.old_skin_mode.value = '3'
                elif str(old_resolution) == str('4096'):
                   config.plugins.SevenHD.old_skin_mode.value = '4'
                elif str(old_resolution) == str('7680'):
                   config.plugins.SevenHD.old_skin_mode.value = '5'
                elif str(old_resolution) == str('8192'):
                   config.plugins.SevenHD.old_skin_mode.value = '6'
                else: #unknow UserResolution
                   config.plugins.SevenHD.old_skin_mode.value = '7'
                config.plugins.SevenHD.old_skin_mode.save()
                
                #skin/root
                self.debug('Old Skin Resolution: ' + str(config.plugins.SevenHD.old_skin_mode.value) + ' New Skin Resolution: ' + str(config.plugins.SevenHD.skin_mode.value))
                self.debug('DownLoad Path: ' + str(self.server_dir))
                
                if str(config.plugins.SevenHD.skin_mode.value) != str(config.plugins.SevenHD.old_skin_mode.value) or fileExists(PLUGIN_PATH + 'Extensions/SevenHD/firststart'):
                   self.debug('Remove SevenHD Root')
                   self.unpack()
                   
                   if fileExists(PLUGIN_PATH + 'Extensions/SevenHD/firststart'):
                      remove(PLUGIN_PATH + 'Extensions/SevenHD/firststart')
                                  
                self.debug('try open: ' + TMPFILE)
                xFile = open(TMPFILE, "w")
                for xx in self.skin_lines:
                    xFile.writelines(xx)
                xFile.close()
                self.debug('close: ' + TMPFILE)

                Instance = ChangeSkin(self.session)
                
                if fileExists(TMPFILE):
                   if fileExists(FILE):
                      move(TMPFILE, FILE)
                      self.debug('mv : ' + TMPFILE + ' to ' + FILE + "\n")
                   else:
                      rename(TMPFILE, FILE)
                      self.debug('rename : ' + TMPFILE + ' to ' + FILE + "\n")
		
                # user_font
                if fileExists(MAIN_USER_PATH + 'user_font.txt'):
                   os.system('python /usr/lib/enigma2/python/Plugins/Extensions/SevenHD/ChangeFont.py %s' % str(self.value))
                
                self.debug('Console')	
		
                #DOWNLOADS	
                download_list = ['buttons', 'vkeys', 'WetterIcons', 'clock', 'volume', 'icons', 'progress', 'progressvol', 'progressib', 'progresscs', 'progresslistcs', 'menu-icons']
                
                for entrie in download_list:
                       
                       if entrie == 'buttons':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz(entrie, config.plugins.SevenHD.ButtonStyle.value)
                       elif entrie == 'vkeys':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/buttons/vkey*")
                          self.download_tgz('buttons', entrie)
                       elif entrie == 'WetterIcons' and (config.plugins.SevenHD.WeatherStyle_1.value != 'none' or config.plugins.SevenHD.WeatherStyle_2.value != 'none'):
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('weather', 'weather' + config.plugins.SevenHD.weather_server.value)
                       elif entrie == 'clock' and config.plugins.SevenHD.ClockStyle.value in 'clock-analog clock-android clock-weather clock-icon clock-flip':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          if config.plugins.SevenHD.ClockStyle.value == 'clock-weather':  # !! clock-weather <-> weather_xxx
                             self.download_tgz('weather', 'weather' + config.plugins.SevenHD.weather_server.value)
                          elif config.plugins.SevenHD.ClockStyle.value == 'clock-icon':  # !! clock-weather <-> weather_xxx
                             self.download_tgz('weather', 'weather' + config.plugins.SevenHD.weather_server.value)
                          elif config.plugins.SevenHD.ClockStyle.value == 'clock-android':   
                             self.download_tgz(entrie, config.plugins.SevenHD.ClockStyle.value + config.plugins.SevenHD.weather_server.value)
                          else:
                             self.download_tgz(entrie, config.plugins.SevenHD.ClockStyle.value)
                       elif entrie == 'volume' and config.plugins.SevenHD.VolumeStyle.value == 'volumestyle-center':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz(entrie, config.plugins.SevenHD.VolumeStyle.value)
                       elif entrie == 'icons':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz(entrie, config.plugins.SevenHD.IconStyle.value)
                       elif config.plugins.SevenHD.Progress.value == "progress" and entrie == 'progress':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('progress', config.plugins.SevenHD.Progress.value)
                       elif config.plugins.SevenHD.ProgressVol.value == "progressvol" and entrie == 'progressvol':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('progress', config.plugins.SevenHD.ProgressVol.value)
                       elif config.plugins.SevenHD.ProgressIB.value == "progressib" and entrie == 'progressib':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('progress', config.plugins.SevenHD.ProgressIB.value)
                       elif config.plugins.SevenHD.ProgressCS.value == "progresscs" and entrie == 'progresscs':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('progress', config.plugins.SevenHD.ProgressCS.value)
                       elif config.plugins.SevenHD.ProgressListCS.value == "progresslistcs" and entrie == 'progresslistcs':
                          os.system("rm -rf /usr/share/enigma2/SevenHD/%s/*.*; rm -rf /usr/share/enigma2/SevenHD/%s" % (str(entrie), str(entrie)))
                          self.download_tgz('progress', config.plugins.SevenHD.ProgressListCS.value)
                       elif entrie == 'menu-icons' and config.plugins.SevenHD.Logo.value != "menu-icons0":
                          os.system("rm -rf /usr/share/enigma2/SevenHD/buttons/menu-icons*")
                          self.download_tgz('menu-icons', entrie)
                       
                
                if config.plugins.SevenHD.skin_mode.value == '1' or '2' or '3':
                   #background only in HD Mode
		   eConsole().ePopen("rm -rf /usr/share/enigma2/SevenHD/back/*.*; rm -rf /usr/share/enigma2/SevenHD/back")
                
                   if self.BackgroundLeft.startswith('back'):
		      self.download_tgz('back', str(self.BackgroundLeft))
                   if self.BackgroundRight.startswith('back'):
                      self.download_tgz('back', str(self.BackgroundRight))
		   if self.BackgroundIB1.startswith('back'):
		      self.download_tgz('back', str(self.BackgroundIB1))
		   if self.BackgroundIB2.startswith('back'):
		      self.download_tgz('back', str(self.BackgroundIB2))
		   if self.ChannelBack1.startswith('back'):
		      self.download_tgz('back', str(self.ChannelBack1))
		   if self.ChannelBack2.startswith('back'):
		      self.download_tgz('back', str(self.ChannelBack2))
                   if self.ChannelBack3.startswith('back'):
		      self.download_tgz('back', str(self.ChannelBack3))
                
                if fileExists(PLUGIN_PATH + "Extensions/WeatherPlugin/plugin.pyo") and config.plugins.SevenHD.MSNWeather.value == 'msn-icon':
                   self.download_tgz('msn', 'msn-icon')
                
                if config.plugins.SevenHD.use_alba_skin.value == True and os.path.isdir(PLUGIN_PATH + "Extensions/Albatros") :
                   #if not fileExists(PLUGIN_PATH + "/Extensions/Albatros/skin/haupt_Screen.xml"):
                      url = DOWNLOAD_URL + 'Plugins/Albatros.tar.gz'
                      self.debug('URL: ' + url)
                      res = requests.request('get', url)
                   
                      tar_gz = open('/tmp/Albatros.tar.gz','w')
                      tar_gz.write(res.content)
                      tar_gz.close()
        
                      sub = subprocess.Popen("tar xf /tmp/Albatros.tar.gz -C /usr/lib/enigma2/python/Plugins/Extensions/Alabtros", shell=True)
                      sub.wait()
        
                      remove('/tmp/Albatros.tar.gz')
                
                
                if config.plugins.SevenHD.use_mp_skin.value == True and os.path.isdir(PLUGIN_PATH + "Extensions/MediaPortal") :
                   #if not fileExists(PLUGIN_PATH + "/Extensions/MediaPortal/skins_1080/SevenHD/skin.xml"):
                      url = DOWNLOAD_URL + 'Plugins/MediaPortal.tar.gz'
                      self.debug('URL: ' + url)
                      res = requests.request('get', url)
                   
                      tar_gz = open('/tmp/MediaPortal.tar.gz','w')
                      tar_gz.write(res.content)
                      tar_gz.close()
        
                      sub = subprocess.Popen("tar xf /tmp/MediaPortal.tar.gz -C /usr/lib/enigma2/python/Plugins/Extensions/MediaPortal", shell=True)
                      sub.wait()
        
                      remove('/tmp/MediaPortal.tar.gz')
                
                self.debug('download tgz complett')
                
                self.makeGradientBackgrounds()
                self.debug('png generation complete')
                
                self.skin_ok = True
        except:
           config.plugins.SevenHD.debug.setValue(True)
           self.debug('Error creating Skin!')
           self.skin_ok = False
           
        self.makeGradientBackgrounds()
        self.debug('png generation complete')
                
        if self.skin_ok:   
           self.reboot(_("GUI needs a restart to download files and apply a new skin.\nDo you want to Restart the GUI now?"))
        else:
           self.session.open(MessageBox, _("Error creating Skin, contact Kraven Team\nand send /tmp/kraven_debug.log for help!"), MessageBox.TYPE_ERROR)
           
    def unpack(self):
        os.system("rm -rf /usr/share/enigma2/SevenHD/*; rm -rf /usr/share/enigma2/SevenHD")
        
        url = DOWNLOAD_URL + self.server_dir + '/SevenHD.tar.gz'
        self.debug('URL: ' + url)
        res = requests.request('get', url)
        
        tar_gz = open('/tmp/SevenHD.tar.gz','w')
        tar_gz.write(res.content)
        tar_gz.close()
        
        sub = subprocess.Popen("tar xf /tmp/SevenHD.tar.gz -C /usr/share/enigma2/", shell=True)
        sub.wait()
        
        remove('/tmp/SevenHD.tar.gz')

    def download_tgz(self, who, what):
        
        url = DOWNLOAD_URL + self.server_dir + '/' + who + '/' + what + '.tar.gz'
        res = requests.request('get', url)
        
        tar_gz = open('/tmp/%s.tar.gz' % what,'w')
        tar_gz.write(res.content)
        tar_gz.close()
        
        sub = subprocess.Popen("tar xf /tmp/%s.tar.gz -C /usr/share/enigma2/SevenHD/" % str(what), shell=True)
        sub.wait()
        os.remove('/tmp/%s.tar.gz' % str(what))
        
    def appendSkinFile(self, appendFileName, skinPartSearchAndReplace=None):
        """
        add skin file to main skin content

        appendFileName:
        xml skin-part to add

        skinPartSearchAndReplace:
        (optional) a list of search and replace arrays. first element, search, second for replace
        """
        
        skFile = open(appendFileName, "r")
        file_lines = skFile.readlines()
        skFile.close()

        tmpSearchAndReplace = []

        if skinPartSearchAndReplace is not None:
           tmpSearchAndReplace = self.skinSearchAndReplace + skinPartSearchAndReplace
        else:
           tmpSearchAndReplace = self.skinSearchAndReplace

        for skinLine in file_lines:
            for item in tmpSearchAndReplace:
                skinLine = skinLine.replace(item[0], item[1])
            self.skin_lines.append(skinLine)
    
    def getTunerCount(self):
        '''
        get tuner count
        :return:
        '''
        tunerCount = nimmanager.getSlotCount()

        tunerCount = max(1, tunerCount)
        tunerCount = min(6, tunerCount)

        return tunerCount
          
    def showInfo(self):
        options = []
        options.extend(((_("Thanks to"), boundFunction(self.send_to_msg_box, "http://www.gigablue-support.org/")),))
        if config.plugins.SevenHD.debug.value:
           options.extend(((_("Show Debug Log"), boundFunction(self.show_log)),))
        
        if not fileExists(PLUGIN_PATH + "/Extensions/EnhancedMovieCenter/plugin.pyo"):
           options.extend(((_("Install EnhancedMovieCenter?"), boundFunction(self.Open_Setup, "enigma2-plugin-extensions-enhancedmoviecenter")),))
        
        if config.plugins.SevenHD.NumberZapExtImport.value:
           if fileExists(PLUGIN_PATH + "SystemPlugins/NumberZapExt/NumberZapExt.pyo"):
              options.extend(((_("Open NumberZapExt Setup"), boundFunction(self.Open_NumberExt)),))
           else:
              options.extend(((_("Install NumberZapExt?"), boundFunction(self.Open_Setup, "enigma2-plugin-systemplugins-extnumberzap")),))
        else:
           options.extend(((_("Install NumberZapExt?"), boundFunction(self.Open_Setup, "enigma2-plugin-systemplugins-extnumberzap")),))
        
        if not fileExists(PLUGIN_PATH + "/Extensions/CoolTVGuide/plugin.pyo"):
           options.extend(((_("Install CoolTVGuide?"), boundFunction(self.Open_Setup, "enigma2-plugin-extensions-cooltvguide")),))
        
        if not fileExists("/etc/enigma2/SystemFont"):
           options.extend(((_("Install SystemFonts"), boundFunction(self.install_systemfonts)),))
        else:
           options.extend(((_("Refresh SystemFonts"), boundFunction(self.install_systemfonts)),))
        
        if fileExists(MAIN_USER_PATH + "user_font.txt"):
           options.extend(((_("Reset UserFont Height"), boundFunction(self.reset_font_height)),))   
        
        options.extend(((_("Share my Skin"), boundFunction(self.Share_Skin)),))
        options.extend(((_("ChangeLog"), boundFunction(self.ChangeLog)),))
        options.extend(((_("About Team"), boundFunction(self.send_to_msg_box, "Team Kraven\n\TBX, stony272, thomele, Philipswalther, xc3\xb6rlgrey, and Apachi 70")),))
        
        if fileExists(FILE):
           options.extend(((_("About Skin"), boundFunction(self.About)),))
        
        options.extend(((_("Version"), boundFunction(self.do_version)),))
        
        if fileExists(PLUGIN_PATH + "SystemPlugins/MPHelp/plugin.pyo"):
           options.extend(((_("FAQ"), boundFunction(self.show_faq)),))
        else:
           options.extend(((_("FAQ"), boundFunction(self.send_to_msg_box, "No MPHelp Plugin installed")),))
        
        self.session.openWithCallback(self.menuCallback, ChoiceBox,list = options)
            
    def menuCallback(self, ret):
        ret and ret[1]()
    
    def reset_font_height(self):
        os.system('rm -f ' + MAIN_USER_PATH + 'user_font.txt')
        self.session.open(MessageBox,_('user_font.txt removed'), MessageBox.TYPE_INFO, timeout = 5)
        
    def show_faq(self):
        if fileExists(resolveFilename(SCOPE_PLUGINS, "Extensions/SevenHD/faq/faq_%s.xml" % str(config.plugins.SevenHD.faq_language.value))):
           from Plugins.SystemPlugins.MPHelp import PluginHelp, XMLHelpReader
           reader = XMLHelpReader(resolveFilename(SCOPE_PLUGINS, "Extensions/SevenHD/faq/faq_%s.xml" % str(config.plugins.SevenHD.faq_language.value)))
           Faq = PluginHelp(*reader)
           Faq.open(self.session)
        else:
           self.session.open(MessageBox,_('The FAQ is not in your Language available.'), MessageBox.TYPE_INFO, timeout = 5)
           
    def install_systemfonts(self):
        ttf_dir = os.popen('find / -name *.ttf').read().split('\n')
        for ttf in ttf_dir:
            if fileExists(ttf):               
               if not ttf.startswith(MAIN_SKIN_PATH + 'fonts'):
                  copy(str(ttf),MAIN_SKIN_PATH + 'fonts')
        
        otf_dir = os.popen('find / -name *.otf').read().split('\n')
        for otf in otf_dir:
            if fileExists(otf):
               if not otf.startswith(MAIN_SKIN_PATH + 'fonts'):
                  copy(str(otf),MAIN_SKIN_PATH + 'fonts') 
                    
        os.system('touch /etc/enigma2/SystemFont')
        config.plugins.SevenHD.systemfonts.value = True
        config.plugins.SevenHD.systemfonts.save()
        
        self.session.open(MessageBox,_('!! Reboot Gui !!\nAnd on the next PluginStart you can use all SystemFonts'), MessageBox.TYPE_INFO)
        
    def do_version(self):
        config.plugins.SevenHD.version.setValue(str(version))
        config.plugins.SevenHD.version.save()
        self.session.open(MessageBox,_('Youre Version is %s' % str(config.plugins.SevenHD.version.getValue())), MessageBox.TYPE_INFO, timeout = 5)
        
    def About(self):
        with open(FILE, 'r') as xFile:
             self.lines = xFile.readlines()
             resolution = re.search('resolution bpp="32" xres="(.+?)" yres="(.+?)"', str(self.lines)).groups(1)
        
        screen_count = 0
        font_count = 0
        if fileExists("/tmp/about_skin.txt"):
           remove('/tmp/about_skin.txt')
        f = open('/tmp/about_skin.txt', 'a+')
        for screens in self.lines:
            if '<screen' in screens and 'name="' in screens and not 'template' in screens:
               screen_count += 1
               name = re.search('screen.*name="(.*?)"', str(screens)).groups(1)
               f.write(str(name[0]) + '\n')
            if '<font ' in screens:
               font_count += 1
        f.write('\nScreens are skinned:\t' + str(screen_count) + '\nResolution is:\t' + resolution[0]+ 'x' + resolution[1] + '\nUsed Fonts:\t\t' + str(font_count) + '\n')
        f.close()
        self.session.open(Console, _("About Skin"), cmdlist=[("cat /tmp/about_skin.txt")])
    
    def ChangeLog(self):                          
	res = requests.request('get', DOWNLOAD_UPDATE_URL + 'SevenHDChangeLog.txt')
        self.session.open(Console, _("Show Debug Log"), cmdlist=[("echo '%s'" % res.text)])
        
    def send_to_msg_box(self, my_msg):
        self.session.open(MessageBox,_('%s' % str(my_msg)), MessageBox.TYPE_INFO)
    
    def show_log(self):
        if fileExists("/tmp/kraven_debug.txt"):
           self.session.open(Console, _("Show Debug Log"), cmdlist=[("cat /tmp/kraven_debug.txt")])
    
    def Share_Skin(self):
        answer = []
        answer.extend(((_("Share my Skin Config"), boundFunction(self.Open_Skin_Config, "share")),))
        answer.extend(((_("Load shared Skin Config"), boundFunction(self.Open_Skin_Config, "load")),))
        self.session.openWithCallback(self.menuCallback, ChoiceBox,list = answer)
    
    def Open_Skin_Config(self, what):
        do_skin = ShareSkinSettings()
        if what == 'share':
           answer = do_skin.share()
        else:
           answer = do_skin.load()
        
        self.debug(str(answer) + '\n')
        
        if what == 'share':
           if answer:
              self.session.open(MessageBox,_('Youre Skin Config is ready to share.\nLook in /tmp for youre Skin File.'), MessageBox.TYPE_INFO, timeout = 5)
           else:
              self.session.open(MessageBox,_('Anything goes wrong.'), MessageBox.TYPE_INFO, timeout = 5)
        else:
           if answer:
              self.save()
              self.session.open(MessageBox,_('New Skin Config is load.'), MessageBox.TYPE_INFO, timeout = 5)
           else:
              self.session.open(MessageBox,_('Skin Config is wrong.'), MessageBox.TYPE_INFO, timeout = 5)
              
    def Open_Setup(self, what):
        self.reboot("GUI needs a restart after download Plugin.\nDo you want to Restart the GUI now?")
        self.session.open(Console, _("Install Plugin") , cmdlist=[("opkg install %s" % what)])
    
    def Open_NumberExt(self): 
        self.session.open(NumberZapExtSetupScreen, ACTIONLIST)
    
    def reboot(self, message = None):
        self.debug('Reboot\n')
        if message is None:
           message = _("Do you really want to reboot now?")
        
        configfile.save()
        restartbox = self.session.openWithCallback(self.restartGUI, MessageBox, message, MessageBox.TYPE_YESNO)
        restartbox.setTitle(_("Restart GUI"))

    def restartGUI(self, answer):
        if answer is True:
            config.skin.primary_skin.setValue("SevenHD/skin.xml")
            config.skin.save()
            self.session.open(TryQuitMainloop, 3)
        else:
            self.close()

    def exit(self):
        self["menuList"].onSelectionChanged.remove(self.__selectionChanged)
        self.close()

    def __selectionChanged(self):
        self.ShowPicture()
        
    def debug(self, what, error=None):
        if config.plugins.SevenHD.msgdebug.value:
           try:
              self.session.open(MessageBox, _('[PluginScreen]\n' + str(what)), MessageBox.TYPE_INFO)
           except:
              pass
           
        if config.plugins.SevenHD.debug.value:
           f = open('/tmp/kraven_debug.txt', 'a+')
           if error != None:
              f.write('[PluginScreen]' + str(what) + ' error: ' + str(error) + '\n')
           else:
              f.write('[PluginScreen]' + str(what) + '\n')
           f.close()
           
    def makeGradientBackgrounds(self):

        if config.plugins.SevenHD.skin_mode.value=="1":
            width=1280
            height=720
            iboneheights=[
                ("sysinfo_1",142),
                ("ibtop_1",74),
                ("sibleft_1",440),
                ("ibone_1",206),
                ("weatherbig_1",118),
                ("sibleftmetrix_1",670),
                ("sibleftdouble_1",710)
                ]
            ibtwoheights=[
                ("sibtop_1",40),
                ("sibtopbig_1",74),
                ("sibright_1",420),
                ("sibrightmetrix_1",620),
                ("sibrightdouble_1",710)
                ]
            csleftheights=[
                ("cssmall_1",132),
                ("csleft_1",720)
                ]
            csmiddleheights=[
                ("csmiddle_1",708),
                ]
            csrightheights=[
                ("cstop_1",60),
                ("csrightsmall_1",564),
                ("csright_1",720)
                ]
            menurightheights=[
                ("menutop_1",60),
                ("menuright_1",708),
                ("menurightsmall_1",564)
                ]
            menumainheights=[
                ("menuplayer_1",108),
                ("menuplayersmall_1",54),
                ("menuquick_1",272),
                ("menusmall_1",132),
                ("menumain_1",720)
                ]
        elif config.plugins.SevenHD.skin_mode.value=="2":
            width=1920
            height=1080
            iboneheights=[
                ("sysinfo_1",213),
                ("ibtop_1",111),
                ("sibleft_1",660),
                ("ibone_1",309),
                ("weatherbig_1",177),
                ("sibleftmetrix_1",1005),
                ("sibleftdouble_1",1065)
                ]
            ibtwoheights=[
                ("sibtop_1",60),
                ("sibtopbig_1",111),
                ("sibright_1",630),
                ("sibrightmetrix_1",930),
                ("sibrightdouble_1",1065)
                ]
            csleftheights=[
                ("cssmall_1",198),
                ("csleft_1",1080)
                ]
            csmiddleheights=[
                ("csmiddle_1",1062),
                ]
            csrightheights=[
                ("cstop_1",90),
                ("csrightsmall_1",846),
                ("csright_1",1080)
                ]
            menurightheights=[
                ("menutop_1",90),
                ("menuright_1",1062),
                ("menurightsmall_1",846)
                ]
            menumainheights=[
                ("menuplayer_1",162),
                ("menuplayersmall_1",81),
                ("menuquick_1",408),
                ("menusmall_1",198),
                ("menumain_1",1080)
                ]
        elif config.plugins.SevenHD.skin_mode.value=="3":
            width=3840
            height=2160
            iboneheights=[
                ("sysinfo_1",426),
                ("ibtop_1",222),
                ("sibleft_1",1320),
                ("ibone_1",618),
                ("weatherbig_1",354),
                ("sibleftmetrix_1",2010),
                ("sibleftdouble_1",2130)
                ]
            ibtwoheights=[
                ("sibtop_1",120),
                ("sibtopbig_1",222),
                ("sibright_1",1260),
                ("sibrightmetrix_1",1860),
                ("sibrightdouble_1",2130)
                ]
            csleftheights=[
                ("cssmall_1",396),
                ("csleft_1",2160)
                ]
            csmiddleheights=[
                ("csmiddle_1",2124),
                ]
            csrightheights=[
                ("cstop_1",180),
                ("csrightsmall_1",1692),
                ("csright_1",2130)
                ]
            menurightheights=[
                ("menutop_1",180),
                ("menuright_1",2124),
                ("menurightsmall_1",1692)
                ]
            menumainheights=[
                ("menuplayer_1",324),
                ("menuplayersmall_1",162),
                ("menuquick_1",816),
                ("menusmall_1",396),
                ("menumain_1",2130)
                ]

        if config.plugins.SevenHD.BackgroundLeft.value=="back_gradient_main":
            for pair in menumainheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientMenuTop.value,config.plugins.SevenHD.GradientMenuBottom.value,config.plugins.SevenHD.BackgroundLeftColorTrans.value)
        if config.plugins.SevenHD.BackgroundRight.value=="back_gradient_right":
            for pair in menurightheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientMenuRightTop.value,config.plugins.SevenHD.GradientMenuRightBottom.value,config.plugins.SevenHD.BackgroundRightColorTrans.value)
        if config.plugins.SevenHD.BackgroundIB1.value=="back_gradient_ib1":
            for pair in iboneheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientIB1Top.value,config.plugins.SevenHD.GradientIB1Bottom.value,config.plugins.SevenHD.IB1ColorTrans.value)
        if config.plugins.SevenHD.BackgroundIB2.value=="back_gradient_ib2":
            for pair in ibtwoheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientIB2Top.value,config.plugins.SevenHD.GradientIB2Bottom.value,config.plugins.SevenHD.IB2ColorTrans.value)
        if config.plugins.SevenHD.ChannelBack1.value=="back_gradient_csleft":
            for pair in csleftheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientCSLeftTop.value,config.plugins.SevenHD.GradientCSLeftBottom.value,config.plugins.SevenHD.CSLeftColorTrans.value)
        if config.plugins.SevenHD.ChannelBack3.value=="back_gradient_csmiddle":
            for pair in csmiddleheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientCSMiddleTop.value,config.plugins.SevenHD.GradientCSMiddleBottom.value,config.plugins.SevenHD.CSMiddleColorTrans.value)
        if config.plugins.SevenHD.ChannelBack2.value=="back_gradient_csright":
            for pair in csrightheights:
                self.makeGradientPng(pair[0],width,pair[1],config.plugins.SevenHD.GradientCSRightTop.value,config.plugins.SevenHD.GradientCSRightBottom.value,config.plugins.SevenHD.CSRightColorTrans.value)

    def makeGradientPng(self,name,width,height,color1,color2,trans):

        path="/usr/share/enigma2/SevenHD/back/"
        if not os.path.exists(path):
            os.makedirs(path)
    
        width=int(width)
        height=int(height)
        
        color1=color1[-6:]
        r1=int(color1[0:2],16)
        g1=int(color1[2:4],16)
        b1=int(color1[4:6],16)

        color2=color2[-6:]
        r2=int(color2[0:2],16)
        g2=int(color2[2:4],16)
        b2=int(color2[4:6],16)

        trans=255-int(trans,16)

        gradient=Image.new("RGBA",(1,height))
        for pos in range(0,height):
            p=pos/float(height)
            r=r2*p+r1*(1-p)
            g=g2*p+g1*(1-p)
            b=b2*p+b1*(1-p)
            gradient.putpixel((0,pos),(int(r),int(g),int(b),int(trans)))
        gradient=gradient.resize((width,height))
        gradient.save(path+name+".png")

################################################################################        
def main(session, **kwargs):
        if fileExists("/tmp/kraven_debug.txt"):
           remove('/tmp/kraven_debug.txt')
           
        updateInstance = None
        session.open(SevenHD)
        
        if config.plugins.SevenHD.AutoUpdatePluginStart.value or config.plugins.SevenHD.AutoUpdate.value:
           global updateInstance
           if updateInstance is None:
              updateInstance = Update(session)

def Plugins(**kwargs):
	screenwidth = getDesktop(0).size().width()
	if screenwidth and screenwidth == 1920:
		return [PluginDescriptor(name="SevenHD", description=_("Configuration tool for SevenHD"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='pluginfhd.png', fnc=main)]
	else:
		return [PluginDescriptor(name="SevenHD", description=_("Configuration tool for SevenHD"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main)]
