
# attribute 'age' numeric
# attribute 'bp'  numeric
#' attribute 'sg' {1.005,1.010,1.015,1.020,1.025}
#' attribute 'al' {0,1,2,3,4,5}  
#' attribute 'su' {0,1,2,3,4,5}  
#' attribute 'rbc' {normal,abnormal}
#' attribute 'pc' {normal,abnormal} 
#' attribute 'pcc' {present,notpresent}
#' attribute 'ba' {present,notpresent}
#' attribute 'bgr'  numeric
#' attribute 'bu' numeric
#' attribute 'sc' numeric
#' attribute 'sod' numeric
#' attribute 'pot' numeric
#' attribute 'hemo' numeric
#' attribute 'pcv' numeric
#' attribute 'wbcc' numeric
#' attribute 'rbcc' numeric
#' attribute 'htn' {yes,no}
#' attribute 'dm' {yes,no}
#' attribute 'cad' {yes,no}
#' attribute 'appet' {good,poor}
#' attribute 'pe' {yes,no} 
#' attribute 'ane' {yes,no}
#' attribute 'class' {ckd,notckd}
#' 
#' age		-	age	
#' bp		-	blood pressure
#' sg		-	specific gravity
#' al		-   	albumin
#' su		-	sugar
#' rbc		-	red blood cells
#' pc		-	pus cell
#' pcc		-	pus cell clumps
#' ba		-	bacteria
#' bgr		-	blood glucose random
#' bu		-	blood urea
#' sc		-	serum creatinine
#' sod		-	sodium
#' pot		-	potassium
#' hemo		-	hemoglobin
#' pcv		-	packed cell volume
#' wc		-	white blood cell count
#' rc		-	red blood cell count
#' htn		-	hypertension
#' dm		-	diabetes mellitus
#' cad		-	coronary artery disease
#' appet		-	appetite
#' pe		-	pedal edema
#' ane		-	anemia
#' class		-	class	


data = read.delim("kidney.txt", header = FALSE, sep = ",", dec = ".")
colnames(data) = c('age', 'blood pressure', 'specific gravity', 'albumin', 'sugar', 'rbc', 'pus cell', 
                   'pus cell clumps', 'bacteric', 'blood glucose random', 'blood urea', 'serum creatinine',
                   'sodium', 'potassium', 'hemoglobin', 'packed cell volume', 'wbc count', 'rbc count', 
                   'hypertension', 'diabetes mellitus', 'coronary artery disease', 'appetite', 'pedal edema', 
                   'anemia', 'class')

# convert yes = 1, no = 1
# convert abnormal = 1, normal = 0
# convert present = 1, notpresent = 0
# convert "ckd" ,"ckd\t" = 1,  "notckd" "no" = 0, ""  = NA  
data[data == "?"] = NA
data[data == ""] = NA
data[data == "yes"] = 1
data[data == " yes"] = 1
data[data == "\tno"] = 0
data[data == "\tyes"] = 1

data[data == "no"] = 0
data[data == "abnormal"] = 1
data[data == "normal"] = 0
data[data == "present"] = 1
data[data == "notpresent"] = 0
data[data == "ckd"] = 1
data[data == "ckd\t"] = 1
data[data == "notckd"] = 0
data[data == "no"] = 0
data[data == "poor"] = 0
data[data == "good"] = 1


data = read.csv("kidney.csv", header = TRUE, sep = ",")

write.table(data, "~/Desktop/kidney.csv", sep = ",",row.names = FALSE, col.names = TRUE)







