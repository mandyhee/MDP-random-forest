# MDP-random-forest
This is for University of Michigan Multidisciplinary Design Program Machine Learning Lab (Dr. Jay Guo). 
Two random forest model example:  
1. Toy example using UCI chronic kidney disease data. 
2. University of Michigan DataDirect Precision Health database (Yottabyte Research Cloud).
  * script: `random_forest_ybrc.py` (including data manipulation and model building)
  * results: `Random Forest Final Report.pdf`, `Random Forest Final Presentation.pdf`

Python Library used: `pandas`, `sklearn`. 

SQL code to extract data from U of M DataDirect Precision Health database.   
`\copy (select a.encounterid, a.termnamemapped, b.result_name, b.value   
from diagnoses as a join labresults as b 
on a.encounterid = b.encounterid   
where a.termnamemapped = ‘Neop, mlig, soft tissue NOS’ and (b.result_name = ‘ALBUMIN LEVEL’ or b.result_name = ‘CALCIUM LEVEL’ or b.result_name = ‘CHOLESTEROL’ or b.result_name = ‘PROTEIN LEVEL’ or b.result_name = ‘Hemoglobin’) limit 5000) TO ‘C:\Users\uniquname\Desktop\data_TS_5000.csv’ CSV HEADER;`  


`\copy (select a.encounterid, a.termnamemapped, b.result_name, b.value from diagnoses as a join labresults as b  
on a.encounterid = b.encounterid   
where a.termnamemapped = ‘Multiple sclerosis’ and (b.result_name = ‘ALBUMIN LEVEL’ or b.result_name = ‘CALCIUM LEVEL’ or b.result_name = ‘CHOLESTEROL’ or b.result_name = ‘PROTEIN LEVEL’ or b.result_name = ‘Hemoglobin’) limit 5000​) TO ‘C:\Users\uniqname\Desktop\data_MS_5000.csv’ CSV HEADER;`
