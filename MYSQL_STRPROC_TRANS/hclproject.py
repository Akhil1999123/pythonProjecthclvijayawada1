from hcl_database_connectivity import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")
            self.cursor.stored_results()


        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass

b1=Booking()
b1.connect("localhost","root","9494564496","mysql")
sts=b1.available_seats()
seat_avl={}
seat_avl['train_name']=sts[0]
seat_avl['train_number']=sts[1]
print(seat_avl)