import mimetypes
import pymysql
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("application/javascript", ".js", True)

#pymysql.install_as_MySQLdb()

pymysql.install_as_MySQLdb()