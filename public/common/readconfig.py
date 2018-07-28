# -*- coding:utf-8 -*-
import codecs
import configparser
class ReadConfig:
    #专门读取配置文件,.ini文件格式
    def __init__(self, filename):
        configpath = filename
        fd = open(configpath)
        data = fd.read()
        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    #param:env[projectConfig]
    #param:nameproject_path
    def getValue(self,env,name):
        return self.cf.get(env, name)


















