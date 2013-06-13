print('procedure Get xml')
import codecs
import os

'''
//create table
if object_id('tmpReportStat') is not null
	drop table tmpReportStat
go

create table tmpReportStat(
	ReportID	bigint			NOT NULL,
	SQLProcName varchar(128)	NOT NULL,
	DateTime	datetime 
)
go
'''

class GetXML(object):
#	def __init__(self, arg):
#		self.arg = arg
	folders = [	 
				'C:\Projects\coda\Directory'
			   ,'C:\Projects\coda\Warehouse' 
			   ,'C:\Projects\coda\Directory\ReportPredefined' 
	]

	procedures_custom = [
'''		 'JournalWMSIn_BuildMoveOrder'
		,'JournalWMSIn_BuildMoveOrder_Z'
		,'JournalWMSIn_BuildRegisterIn'				#copy
		,'JournalWMSIn_BuildRest' 					#copy
		,'JournalWMSIn_BuildRestShort'
		,'JournalWMSOut_BuildRegisterOut'   '''
		 'ReportCustomPrint_GetContractComission' 	#copy
		,'ReportCustomPrint_GetNotArchivedDocs'
		,'ReportCustomPrint_GetEmployeeSheet'
		,'ReportCustomPrint_GetExpeditorDayTicket'
		,'ReportCustomPrint_GetExpeditorTickets'
		,'ReportCustomPrint_GetInventoryBookkeper'
		,'ReportCustomPrint_GetInventoryStore'
		,'ReportCustomPrint_GetItemRests'
		,'ReportCustomPrint_GetMutualPayment'
		,'ReportCustomPrint_GetNotArchivedDocs'
		,'ReportCustomPrint_GetStoreTickets'
		,'ReportCustomPrint_GetVehicleAccounting'
		,'ReportCustomPrint_GetContractComissionExpeditor'	#- no param ReportID
	]

	procedures_custom2 = [
		 'ReportPredefined_GetCustomerSaldoPrint'
	]

	procedures_builders = [
		 'JournalBuy_Build'
		,'JournalBuy_BuildRet'
		,'JournalCashdesk_BuildCashorder'
		,'JournalClaim_BuildClaim'
		,'JournalClaim_BuildUnpaidInvoiceClaim'
		,'JournalGroup_BuildDelivery'
		,'JournalGroup_BuildDeliveryAttachments'
		,'JournalGroup_BuildMapLoading'
		,'JournalGroup_BuildOperation'
		,'JournalSale_BuildInvoice'
		,'JournalSale_BuildInvoice_CF'
		,'JournalSale_BuildInvoiceOtherFirm'
		,'JournalSale_BuildOrderMova'
		,'JournalSale_BuildInvoiceRet'
		,'JournalStore_BuildDocMove'
		,'JournalTotalTax_BuildTotalTax'
		,'JournalTTN_BuildTTN'
		,'JournalVehicle_BuildDocVehicle'
		,'JournalWMSIn_Build'
		,'JournalWMSIn_BuildWithSource_DocStoreMove'
		,'JournalWMSIn_BuildWithSource'
		,'JournalWMSIn_BuildWithSourceDiscard'
		,'JournalWMSMove_BuildWithSource'
		,'JournalWMSMove_BuildWithSource_InvoiceOrder'
		,'JournalWMSOther_BuildActRepacking'
		,'JournalWMSOther_BuildWithSource'
		,'JournalWMSOut_BuildWithSource'
		,'JournalWMSOut_BuildWithSource_OrderShipment'
		,'JournalWMSTTN_BuildWMSTTN'
	]

#########################################################################

	def GetProcName(self, name):
		return 'PROCEDURE(%s)' % (name)

	def GetProcName2(self, name):
		return 'PROCEDURE (%s)' % (name)

	def GetProcStartPoint(self):
		return 'begin try'

	def GetLoggingTxt(self, procname):
		return '''    declare @isLogging bit = (select cast(Value as bit) from Settings where Name = 'StartReportLog');
    if @isLogging = 1 begin
	
        if object_id('tmpReportStat') is not null
            insert into tmpReportStat 
                values(%s, '%s', getdate());

    end;
''' % ('@ReportID' if procname in self.procedures_builders else '1', procname)

	#for delete added text
	def GetLogginTxt_Start(self):
		return '    declare @isLogging bit'

#########################################################################

	def Parse_Delete(self, procedures):
		for proc in procedures:
			if proc.find('_') > 0:
				for folder in self.folders:

					if proc not in self.procedures_custom2: 
						filename = proc[0:proc.index('_')] + '.sql'
					else:
						filename = proc[proc.index('_') + 1:] + '.sql' #because file name not equel to proc beginning

					fullpath = os.path.join(folder, filename)

					if os.path.exists(fullpath) == True:
						
						self.AddCmdFileLine(fullpath)
						print filename + ' ' + self.GetProcName(proc)
						
						stream = codecs.open(fullpath, 'r', 'cp1251')
						txt = stream.read()
						stream.close()

						index = txt.index(self.GetProcName(proc)) if self.GetProcName(proc) in txt else txt.index(self.GetProcName2(proc))

						procTxt = txt[index:]
						procTxt = procTxt[:procTxt.index('end try')]

						#Check if not already parse
						if procTxt.find('StartReportLog') > 0:

							indexStartCut = index + procTxt.index(self.GetLogginTxt_Start())
							procTxt = txt[:indexStartCut] + txt[indexStartCut + len(self.GetLoggingTxt(proc)) + 1:]

							stream = codecs.open(fullpath, 'w', 'cp1251')
							stream.seek(0)
							stream.write(procTxt)
							stream.close()
			else:
				raise Exception('cant find symbol _ in procudure name')


#########################################################################

	def Parse_Add(self, procedures):
		txt_for_compile = ''
		for proc in procedures:
			if proc.find('_') > 0:
				for folder in self.folders:

					if proc not in self.procedures_custom2: 
						filename = proc[0:proc.index('_')] + '.sql'
					else:
						filename = proc[proc.index('_') + 1:] + '.sql' #because file name not equel to proc beginning

					fullpath = os.path.join(folder, filename)

					if os.path.exists(fullpath) == True:
						
						self.AddCmdFileLine(fullpath)
						print filename + ' ' + self.GetProcName(proc)
						
						stream = codecs.open(fullpath, 'r', 'cp1251')
						txt = stream.read()
						stream.close()

						index = txt.index(self.GetProcName(proc)) if self.GetProcName(proc) in txt else txt.index(self.GetProcName2(proc))
						procTxt = txt[index:]
						procTxt = procTxt[:procTxt.index('end try')]

						#Check if not already parse
						if procTxt.find('StartReportLog') < 0:
							length = index + txt[index:].index(self.GetProcStartPoint()) + len(self.GetProcStartPoint())

							stream = codecs.open(fullpath, 'w', 'cp1251')
							stream.seek(0)
							stream.write(txt[:length])
							stream.seek(length)
							stream.write('\n')
							stream.write('\n')
							stream.write(self.GetLoggingTxt(proc))
							stream.seek(length + len(self.GetLoggingTxt(proc)) + 1)
							stream.write(txt[length:])
							stream.close()
			else:
				raise Exception('cant find symbol _ in procudure name')

######################################################################### 

	cmdFileName = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'CompileFileForLoggingPrintReports.cmd')

	def CreateCmdFileHeader(self, server = 'kib17', database = 'coda_dev'):
		header = '''echo off 

SET SERVER=%s 
SET DATABASE=%s 
SET DB_EDIT=PRODUCTION.CODA 

''' % (server, database)
		stream = codecs.open(self.cmdFileName, 'w', 'cp1251')
		stream.write(header)
		stream.close()

	cmdline = lambda self, s: 'echo y | call c:\\bin\\csql25.cmd ' + s + '  %SERVER% %DATABASE% /DCOMPILE_PROC /DDB_NAME#%DB_EDIT%'

	def AddCmdFileLine(self, filename):
		line = self.cmdline(filename)
		stream = codecs.open(self.cmdFileName, 'r', 'cp1251')
		txt = stream.read()
		stream.close()

		if line not in txt:
			stream = codecs.open(self.cmdFileName, 'a', 'cp1251')
			stream.write(line + '\n')
			stream.close()

#########################################################################

	def Start_Add(self):
		self.CreateCmdFileHeader()
		self.Parse_Add(self.procedures_builders)
		self.Parse_Add(self.procedures_custom)
		self.Parse_Add(self.procedures_custom2)

	def Start_Delete(self):
		self.CreateCmdFileHeader()
		self.Parse_Delete(self.procedures_builders)
		self.Parse_Delete(self.procedures_custom)
		self.Parse_Delete(self.procedures_custom2)		

#########################################################################

c = GetXML()
c.Start_Add()
#c.Start_Delete()
