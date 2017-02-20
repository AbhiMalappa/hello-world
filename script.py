data sa_data;
set sa.sa;
censored = 0;
if tt1st_purch > 0 then censored = 1;
run;
