# Stub to load the data
stub.DiD <- "region_level_cumulative"

########################################
### Seattle and WA Separate Summary Statistics###
########################################

# Wage bins to be used (note "12" means "jobs paying <= $12.99")

# Read file 
df <- read.dta13(paste0(path.to.data,stub.DiD,".dta", collapse = "")) %>%
  mutate(seattle = ifelse(region0 == 1, 1, 0)) %>%  
  filter(yearquarter > 20141 & yearquarter < 20164)
