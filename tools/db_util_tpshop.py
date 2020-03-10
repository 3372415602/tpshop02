# 1. 导包
import pymysql


# 2. 新建数据库工具类
class DBUtilTpshop:
    # 定义 连接对象
    __conn = None
    # 定义 游标对象
    __cursor = None

    # 1. 获取连接对象方法
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.Connect(host="localhost",
                                         user="root",
                                         password="root",
                                         database="tpshop2.0",
                                         port=3306,
                                         charset="utf8")
        return cls.__conn

    # 2. 获取游标对象方法
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 3. 执行sql语句方法（业务方法）
    @classmethod
    def exe_sql(cls, sql):
        try:
            # 1. 获取游标对象
            cursor = cls.__get_cursor()
            # 2. 执行sql语句
            num = cursor.execute(sql)
            # 3. 判断是查询
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            # 4. 否则
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响的行数
                return num
        except:
            # 回滚
            cls.__conn.rollback()
            # 抛异常
            raise
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()

    # 4. 关闭游标对象方法
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 5. 关闭连接对象方法
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None
