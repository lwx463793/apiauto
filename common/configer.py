import os
import configparser
from common.constant import CONF_DIR


conf_path = os.path.join(CONF_DIR, "env.ini")


class Config(configparser.ConfigParser):#继承父类的方法

    def __init__(self, file_path=None):
        #super().__init__(),是调用父类的构造方法
        super().__init__()
        self.file = file_path
        # 没有指定配置文件就按环境配置执行
        if not self.file:
            self.read(conf_path, encoding="utf8")
            #取到env_switch
            env_switch = self.getint("env", "switch")
            if env_switch == 0:
                env = "dev"
            elif env_switch == 1:
                env = "test"
            elif env_switch == 2:
                env = "uat"
            else:
                raise ValueError("config read error")
            self.file = os.path.join(CONF_DIR, "config_{}.ini".format(env))
        self.read(self.file, encoding='utf8')

    def get_conf(self, section, *options, model="str") -> dict:
        """
        查询指定section中部分options
        :param section: section -> str
        :param options: options不定长参数, 可输入多个值, 可不输 -> tuple
        :param model: 返回值的类型(str, int, float, bool) -> str
        :return: 返回查询到的值 -> dict
        """
        op_list = []
        if options:
            for option in options:
                if model == "str":
                    res = self.get(section, option)
                elif model == "int":
                    res = self.getint(section, option)
                elif model == "float":
                    res = self.getfloat(section, option)
                elif model == "bool":
                    res = self.getboolean(section, option)
                else:
                    res = None
                op_list.append(res)
            options_list = dict(zip(options, op_list))
        else:
            options_list = dict(self.items(section))
        return options_list

    def set_conf(self, section, **options) -> None:
        """
        写入section和options
        :param section: 若无该section则创建该section -> str
        :param options: 不定长参数 -> dict
        :return:  None
        """
        for option, value in options.items():
            if self.has_section(section):
                self.set(section, option, value)
            else:
                self.add_section(section)
                self.set(section, option, value)
        with open(self.file, "w+") as f:
            self.write(f)

    def del_conf(self, section, *options) -> None:
        """
        删除section或options
        :param section: 指定的section -> str
        :param options: 指定的options, 不定长参数, 可输多个参数, 可不输 -> tuple
        :return: None
        """
        if options:
            for i in options:
                self.remove_option(section, i)
        else:
            self.remove_section(section)
        with open(self.file, "w+") as f:
            self.write(f)


conf = Config()

if __name__ == '__main__':
    print(conf.get_conf("sexual_distinction", "sexual_1", "sexual_2"))
