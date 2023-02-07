from mysql.connector import Error
from hcl_database_connectivity import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        custid=2
        sql="delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something is goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
obj=HclPythonTransaction()
obj.connect("localhost","root","9494564496","mysql")
obj.execute_transaction_query()