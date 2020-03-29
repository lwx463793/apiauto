import pymysql



class MySqlData:

    def __int__(self,host,user, password,
                 database, port=0,
                 charset='utf-8'):
        # 连接到数据库
        self.con =pymysql.Connect(host=host, user=user,
                                  password=password,
                                  database=database,
                                  port=port,
                                  charset='utf-8')
        #创键游标
        self.cur = self.con.cursor()

    #返回第一条数据
    def find_one(self,sql):
        #执行sql
        self.cur.execute(sql)
        #刷新
        self.con.commit()
        #返回一个元组形式
        return self.cur.fetchone()

    #返回所有查询的数据
    def find_all(self,sql):
        #执行sql
        self.cur.execute(sql)
        #刷新
        self.con.commit()
        #返回一个元组形式
        return self.cur.fetchone()

    def close(self):
        """断开连接"""
        self.cur.close()
        self.con.close()

