echo off 

SET SERVER=kib17 
SET DATABASE=coda_dev 
SET DB_EDIT=PRODUCTION.CODA 

echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalBuy.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalCashdesk.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalClaim.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalGroup.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalSale.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalStore.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalTotalTax.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalTTN.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\JournalVehicle.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Warehouse\JournalWMSIn.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Warehouse\JournalWMSMove.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Warehouse\JournalWMSOther.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Warehouse\JournalWMSOut.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Warehouse\JournalWMSTTN.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\ReportCustomPrint.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
echo y | call c:\bin\csql25.cmd C:\Projects\coda\Directory\ReportPredefined\GetCustomerSaldoPrint.sql  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%
