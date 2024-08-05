´´´shell
$ python --version
Python 3.12.4
´´´

´´´shell
$ python3 -m pip --version
pip 23.2.1 from /usr/lib/python3.12/site-packages/pip (python 3.12)
´´´

´´´shell
python3 -m venv virtualEnv
´´´

´´´shell
source virtualEnv/bin/activate
´´´

´´´shell
pip install pyodbc
´´´

´´´shell
python3 -m pip install -r requirements.txt
pip install -r packages.txt
´´´

´´´shell
pip list
´´´

[Install the Microsoft ODBC driver for SQL Server (Linux)](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)
´´´shell
#RHEL 9
curl https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo

sudo yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
sudo ACCEPT_EULA=Y yum install -y msodbcsql18
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
´´´

´´´shell
deactivate
´´´
