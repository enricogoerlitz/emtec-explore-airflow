CREATE SCHEMA gold_pr;


CREATE OR REPLACE MATERIALIZED VIEW gold_pr.DimUsers AS
SELECT
	id
	,name
FROM silver_projecttool.users;


CREATE MATERIALIZED VIEW gold_pr.DimProjects AS
SELECT
	p.id
	,p.projectname
	,p.description
	,p.hourly_rate
	,p.businesspartner_id
	,bp.name AS businesspartner_name
FROM silver_projecttool.projects p
LEFT JOIN silver_projecttool.businesspartners bp
ON p.businesspartner_id = bp.id
WITH DATA;


CREATE MATERIALIZED VIEW gold_pr.FactProjecttimes AS
SELECT
	pt.id
	,pt.user_id
	,pt.project_id
	,pt.hours
	,p.hourly_rate
	,(pt.hours * p.hourly_rate) AS expected_revenue
	,pt.comment
FROM silver_projecttool.projecttimes pt
LEFT JOIN silver_projecttool.projects p
ON pt.project_id = p.id
WITH DATA;


-- REPORT


SELECT
	p.projectname
	,u.name AS username
	,SUM(pt.hours) AS workinghours
	,SUM(pt.expected_revenue) AS expected_revenue_total
FROM gold_pr.FactProjecttimes pt
LEFT JOIN gold_pr.DimUsers u
ON pt.user_id = u.id
LEFT JOIN gold_pr.DimProjects p
ON pt.project_id = p.id
GROUP BY p.projectname, u.name
ORDER BY p.projectname, expected_revenue_total DESC;