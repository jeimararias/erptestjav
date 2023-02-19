/****** Script for SelectTopNRows command from SSMS  ******/
SELECT Id, [Name], Replace(convert(varchar,getdate(),111),'/','-')+'T'+convert(varchar,Datetime_Hired, 108)+'z' Datetime_Hired, Department_Id, Job_Id
FROM dbo.HiredEmployees

Select convert(varchar,getdate(),108)  --102, 111, 

---
Select * from vwEmployees


select Name, [Red], [Green], [Blue]
from
(
select *
from cte
) as src
pivot 
(
  max(Value)
  for color IN ([Red], [Green], [Blue])
) as Dtpivot;


select Department,	Job, [Q1], [Q2, [Q3], [Q4]
from
(
	Select
		Year_Hired, Department,	Job, Quarter_Hired, count(*) TotRecords
	from vwEmployees
	where Year_Hired = 2021
	group by Year_Hired, Department, Job, Quarter_Hired
) as src
pivot 
(
  count(1) 
  --TotRecords
  for Quarter_Hired IN ([Q1], [Q2, [Q3], [Q4])
) as Dtpivot;


Select
	Year_Hired, Department,	Job, Quarter_Hired, count(1) TotRecords
from vwEmployees
where Year_Hired = 2021
--and Job like '%Recruiting Manager%'
group by Year_Hired, Department,	Job, Quarter_Hired
order by Year_Hired, Department,	Job, Quarter_Hired

---
SELECT
	Year_Hired,	Department,	Job,	Isnull(Q1,0) Q1, Isnull(Q2,0) Q2,	Isnull(Q3,0) Q3,	Isnull(Q4,0) Q4
FROM
	(Select
		Year_Hired, Department,	Job, Quarter_Hired, count(1) TotRecords
	from vwEmployees
	group by Year_Hired, Department,	Job, Quarter_Hired
	) AS SourceTable PIVOT(sum([TotRecords]) FOR [Quarter_Hired] IN ([Q1], [Q2], [Q3], [Q4])) AS PivotTable
where Year_Hired = 2022;



	Select
		* --Year_Hired, Department,	Job, Quarter_Hired, count(1) TotRecords
	from vwEmployees
	where Year_Hired = 2021
	and Department = 'Human Resources'
	and Job = 'Account Coordinator'
	--group by Year_Hired, Department,	Job, Quarter_Hired

Year_Hired	Department	Job	Q1	Q2	Q3	Q4
2021	Engineering	Account Coordinator	NULL	1	1	NULL
2021	Human Resources	Account Coordinator	1	2	NULL	NULL


Select * 
from dbo.vwEmployeesHiredByQuarter
where Year_Hired = 2021
Order by Year_Hired, Department, Job

Select THxD.Year_Hired,	THxD.Department_Id, THxD.Department, THxD.TotHiresXDep_Year, TotC.AvgYear, TotC.TotYear
from
	(Select
		Year_Hired, Department_Id, Department, count(1) TotHiresXDep_Year
	from vwEmployees
	Group by Year_Hired, Department_Id, Department) THxD
Inner Join
	(Select TD.Year_Hired, avg(TotRecords) AvgYear, sum(TotRecords) TotYear
	from
		(Select
			Year_Hired, Department_Id, count(1) TotRecords
		from vwEmployees
		Group by Year_Hired, Department_Id) TD
	group by TD.Year_Hired) TotC On TotC.Year_Hired = THxD.Year_Hired














