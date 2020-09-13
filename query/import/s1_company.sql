INSERT INTO ig_test.company (company_name) 
VALUES({})
ON CONFLICT (company_name)
DO NOTHING
;