/****** Script for SelectTopNRows command from SSMS  ******/
use ERPTESTJAV
go

SELECT [Id]
      ,[Name]
      ,[Datetime_Hired]
      ,[Department_Id]
      ,[Job_Id]
  FROM [ERPTESTJAV].[dbo].[HiredEmployees]

/*
SELECT TOP (1000) [Id]
      ,[Job]
FROM [ERPTESTJAV].[dbo].[Jobs]

SELECT TOP (1000) [Id]
      ,[Department]
  FROM [ERPTESTJAV].[dbo].[Departments]
*/

/*
truncate table HiredEmployees
delete from Jobs
delete from Departments
*/

----

--Resultado #1
Select * 
from dbo.vwEmployeesHiredByQuarter
where Year_Hired = 2021
Order by Year_Hired, Department, Job

--Resultado #2
Select * 
from dbo.vwEmployeesHiredByDeparments_Year
where Year_Hired = 2021
and TotHiresXDep_Year >	AvgYear
Order by Year_Hired, TotHiresXDep_Year desc


