
# coding: utf-8

# In[2]:

import csv


# In[9]:

ctry = """Afghanistan,AFG
Africa,AFR
Albania,ALB
Algeria,DZA
American Samoa,ASM
Andorra,AND
Angola,AGO
Antigua and Barbuda,ATG
Arab World,ARB
Argentina,ARG
Armenia,ARM
Aruba,ABW
Australia,AUS
Austria,AUT
Azerbaijan,AZE
Bahamas, The,BHS
Bahrain,BHR
Bangladesh,BGD
Barbados,BRB
Belarus,BLR
Belgium,BEL
Belize,BLZ
Benin,BEN
Bermuda,BMU
Bhutan,BTN
Bolivia,BOL
Bosnia and Herzegovina,BIH
Botswana,BWA
Brazil,BRA
Brunei Darussalam,BRN
Bulgaria,BGR
Burkina Faso,BFA
Burundi,BDI
Cabo Verde,CPV
Cambodia,KHM
Cameroon,CMR
Canada,CAN
Caribbean small states,CSS
Cayman Islands,CYM
Central African Republic,CAF
Chad,TCD
Channel Islands,CHI
Chile,CHL
China,CHN
Colombia,COL
Comoros,COM
Congo, Dem. Rep.,COD
Congo, Rep.,COG
Costa Rica,CRI
Cote d'Ivoire,CIV
Croatia,HRV
Cuba,CUB
Curacao,CUW
Cyprus,CYP
Czech Republic,CZE
Denmark,DNK
Djibouti,DJI
Dominican Republic,DOM
Dominica,DMA
East Asia & Pacific (all income levels),EAS
East Asia & Pacific (developing only),EAP
East Asia and the Pacific (IFC classification),CEA
Ecuador,ECU
Egypt, Arab Rep.,EGY
El Salvador,SLV
Equatorial Guinea,GNQ
Eritrea,ERI
Estonia,EST
Ethiopia,ETH
Euro area,EMU
Europe & Central Asia (all income levels),ECS
Europe & Central Asia (developing only),ECA
Europe and Central Asia (IFC classification),CEU
European Union,EUU
Faeroe Islands,FRO
Fiji,FJI
Finland,FIN
France,FRA
French Polynesia,PYF
Gabon,GAB
Gambia, The,GMB
Georgia,GEO
Germany,DEU
Ghana,GHA
Greece,GRC
Greenland,GRL
Grenada,GRD
Guam,GUM
Guatemala,GTM
Guinea-Bissau,GNB
Guinea,GIN
Guyana,GUY
Haiti,HTI
Heavily indebted poor countries (HIPC),HPC
High income: nonOECD,NOC
High income: OECD,OEC
High income,HIC
Honduras,HND
Hong Kong SAR, China,HKG
Hungary,HUN
Iceland,ISL
India,IND
Indonesia,IDN
Iran, Islamic Rep.,IRN
Iraq,IRQ
Ireland,IRL
Isle of Man,IMN
Israel,ISR
Italy,ITA
Jamaica,JAM
Japan,JPN
Jordan,JOR
Kazakhstan,KAZ
Kenya,KEN
Kiribati,KIR
Korea, Dem. Rep.,PRK
Korea, Rep.,KOR
Kosovo,KSV
Kuwait,KWT
Kyrgyz Republic,KGZ
Lao PDR,LAO
Latin America & Caribbean (all income levels),LCN
Latin America & Caribbean (developing only),LAC
Latin America and the Caribbean (IFC classification),CLA
Latvia,LVA
Least developed countries: UN classification,LDC
Lebanon,LBN
Lesotho,LSO
Liberia,LBR
Libya,LBY
Liechtenstein,LIE
Lithuania,LTU
Low & middle income,LMY
Low income,LIC
Lower middle income,LMC
Luxembourg,LUX
Macao SAR, China,MAC
Macedonia, FYR,MKD
Madagascar,MDG
Malawi,MWI
Malaysia,MYS
Maldives,MDV
Mali,MLI
Malta,MLT
Marshall Islands,MHL
Mauritania,MRT
Mauritius,MUS
Mexico,MEX
Micronesia, Fed. Sts.,FSM
Middle East & North Africa (all income levels),MEA
Middle East & North Africa (developing only),MNA
Middle East and North Africa (IFC classification),CME
Middle income,MIC
Moldova,MDA
Monaco,MCO
Mongolia,MNG
Montenegro,MNE
Morocco,MAR
Mozambique,MOZ
Myanmar,MMR
Namibia,NAM
Nepal,NPL
Netherlands,NLD
New Caledonia,NCL
New Zealand,NZL
Nicaragua,NIC
Nigeria,NGA
Niger,NER
North Africa,NAF
North America,NAC
Northern Mariana Islands,MNP
Norway,NOR
OECD members,OED
Oman,OMN
Other small states,OSS
Pacific island small states,PSS
Pakistan,PAK
Palau,PLW
Panama,PAN
Papua New Guinea,PNG
Paraguay,PRY
Peru,PER
Philippines,PHL
Poland,POL
Portugal,PRT
Puerto Rico,PRI
Qatar,QAT
Romania,ROU
Russian Federation,RUS
Rwanda,RWA
Samoa,WSM
San Marino,SMR
Sao Tome and Principe,STP
Saudi Arabia,SAU
Senegal,SEN
Serbia,SRB
Seychelles,SYC
Sierra Leone,SLE
Singapore,SGP
Sint Maarten (Dutch part),SXM
Slovak Republic,SVK
Slovenia,SVN
Small states,SST
Solomon Islands,SLB
Somalia,SOM
South Africa,ZAF
South Asia (IFC classification),CSA
South Asia,SAS
South Sudan,SSD
Spain,ESP
Sri Lanka,LKA
St. Kitts and Nevis,KNA
St. Lucia,LCA
St. Martin (French part),MAF
St. Vincent and the Grenadines,VCT
Sub-Saharan Africa (all income levels),SSF
Sub-Saharan Africa (developing only),SSA
Sub-Saharan Africa (IFC classification),CAA
Sub-Saharan Africa excluding South Africa and Nigeria,XZN
Sub-Saharan Africa excluding South Africa,SXZ
Sudan,SDN
Suriname,SUR
Swaziland,SWZ
Sweden,SWE
Switzerland,CHE
Syrian Arab Republic,SYR
Tajikistan,TJK
Tanzania,TZA
Thailand,THA
Timor-Leste,TLS
Togo,TGO
Tonga,TON
Trinidad and Tobago,TTO
Tunisia,TUN
Turkey,TUR
Turkmenistan,TKM
Turks and Caicos Islands,TCA
Tuvalu,TUV
Uganda,UGA
Ukraine,UKR
United Arab Emirates,ARE
United Kingdom,GBR
United States,USA
Upper middle income,UMC
Uruguay,URY
Uzbekistan,UZB
Vanuatu,VUT
Venezuela, RB,VEN
Vietnam,VNM
Virgin Islands (U.S.),VIR
West Bank and Gaza,PSE
World,WLD
Yemen, Rep.,YEM
Zambia,ZMB
Zimbabwe,ZWE"""


# In[11]:

with open('countries.csv','w') as f:
    f.write(ctry)


# In[12]:


# In[14]:

indic = """Access to electricity (% of population),EG_ELC_ACCS_ZS
Adjusted net national income (annual % growth),NY_ADJ_NNTY_KD_ZG
Adjusted net national income (constant 2000 US$),NY_ADJ_NNTY_KD
Adjusted net national income (current US$),NY_ADJ_NNTY_CD
Adjusted net savings, excluding particulate emission damage (% of GNI),NY_ADJ_SVNX_GN_ZS
Adjusted net savings, excluding particulate emission damage (current US$),NY_ADJ_SVNX_CD
Adjusted net savings, including particulate emission damage (% of GNI),NY_ADJ_SVNG_GN_ZS
Adjusted net savings, including particulate emission damage (current US$),NY_ADJ_SVNG_CD
Adjusted savings: carbon dioxide damage (% of GNI),NY_ADJ_DCO2_GN_ZS
Adjusted savings: carbon dioxide damage (current US$),NY_ADJ_DCO2_CD
Adjusted savings: consumption of fixed capital (% of GNI),NY_ADJ_DKAP_GN_ZS
Adjusted savings: consumption of fixed capital (current US$),NY_ADJ_DKAP_CD
Adjusted savings: education expenditure (% of GNI),NY_ADJ_AEDU_GN_ZS
Adjusted savings: education expenditure (current US$),NY_ADJ_AEDU_CD
Adjusted savings: energy depletion (% of GNI),NY_ADJ_DNGY_GN_ZS
Adjusted savings: energy depletion (current US$),NY_ADJ_DNGY_CD
Adjusted savings: gross savings (% of GNI),NY_ADJ_ICTR_GN_ZS
Adjusted savings: mineral depletion (% of GNI),NY_ADJ_DMIN_GN_ZS
Adjusted savings: mineral depletion (current US$),NY_ADJ_DMIN_CD
Adjusted savings: natural resources depletion (% of GNI),NY_ADJ_DRES_GN_ZS
Adjusted savings: net forest depletion (% of GNI),NY_ADJ_DFOR_GN_ZS
Adjusted savings: net forest depletion (current US$),NY_ADJ_DFOR_CD
Adjusted savings: net national savings (% of GNI),NY_ADJ_NNAT_GN_ZS
Adjusted savings: net national savings (current US$),NY_ADJ_NNAT_CD
Adjusted savings: particulate emission damage (% of GNI),NY_ADJ_DPEM_GN_ZS
Adjusted savings: particulate emission damage (current US$),NY_ADJ_DPEM_CD
Adolescent fertility rate (births per 1,000 women ages 15-19),SP_ADO_TFRT
Age dependency ratio (% of working-age population),SP_POP_DPND
Age dependency ratio, old (% of working-age population),SP_POP_DPND_OL
Age dependency ratio, young (% of working-age population),SP_POP_DPND_YG
Agricultural irrigated land (% of total agricultural land),AG_LND_IRIG_AG_ZS
Agricultural land (% of land area),AG_LND_AGRI_ZS
Agricultural land (sq. km),AG_LND_AGRI_K2
Agricultural machinery, tractors,AG_AGR_TRAC_NO
Agricultural machinery, tractors per 100 sq. km of arable land,AG_LND_TRAC_ZS
Agricultural methane emissions (% of total),EN_ATM_METH_AG_ZS
Agricultural methane emissions (thousand metric tons of CO2 equivalent),EN_ATM_METH_AG_KT_CE
Agricultural nitrous oxide emissions (% of total),EN_ATM_NOXE_AG_ZS
Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent),EN_ATM_NOXE_AG_KT_CE
Agricultural raw materials exports (% of merchandise exports),TX_VAL_AGRI_ZS_UN
Agricultural raw materials imports (% of merchandise imports),TM_VAL_AGRI_ZS_UN
Agriculture value added per worker (constant 2000 US$),EA_PRD_AGRI_KD
Agriculture, value added (% of GDP),NV_AGR_TOTL_ZS
Agriculture, value added (annual % growth),NV_AGR_TOTL_KD_ZG
Agriculture, value added (constant 2000 US$),NV_AGR_TOTL_KD
Agriculture, value added (constant LCU),NV_AGR_TOTL_KN
Agriculture, value added (current LCU),NV_AGR_TOTL_CN
Agriculture, value added (current US$),NV_AGR_TOTL_CD
Air transport, freight (million ton-km),IS_AIR_GOOD_MT_K1
Air transport, passengers carried,IS_AIR_PSGR
Air transport, registered carrier departures worldwide,IS_AIR_DPRT
Alternative and nuclear energy (% of total energy use),EG_USE_COMM_CL_ZS
Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal),ER_H2O_FWAG_ZS
Annual freshwater withdrawals, domestic (% of total freshwater withdrawal),ER_H2O_FWDM_ZS
Annual freshwater withdrawals, industry (% of total freshwater withdrawal),ER_H2O_FWIN_ZS
Annual freshwater withdrawals, total (% of internal resources),ER_H2O_FWTL_ZS
Annual freshwater withdrawals, total (billion cubic meters),ER_H2O_FWTL_K3
Antiretroviral therapy coverage (% of people with advanced HIV infection),SH_HIV_ARTC_ZS
Arable land (% of land area),AG_LND_ARBL_ZS
Arable land (hectares per person),AG_LND_ARBL_HA_PC
Arable land (hectares),AG_LND_ARBL_HA
ARI treatment (% of children under 5 taken to a health provider),SH_STA_ARIC_ZS
Armed forces personnel (% of total labor force),MS_MIL_TOTL_TF_ZS
Armed forces personnel, total,MS_MIL_TOTL_P1
Arms exports (constant 1990 US$),MS_MIL_XPRT_KD
Arms imports (constant 1990 US$),MS_MIL_MPRT_KD
Automated teller machines (ATMs) (per 100,000 adults),FB_ATM_TOTL_P5
Average number of times firms spent in meetings with tax officials,IC_TAX_METG
Average precipitation in depth (mm per year),AG_LND_PRCP_MM
Average time to clear exports through customs (days),IC_CUS_DURS_EX
Bank capital to assets ratio (%),FB_BNK_CAPA_ZS
Bank liquid reserves to bank assets ratio (%),FD_RES_LIQU_AS_ZS
Bank nonperforming loans to total gross loans (%),FB_AST_NPER_ZS
Battle-related deaths (number of people),VC_BTL_DETH
Binding coverage, all products (%),TM_TAX_MRCH_BC_ZS
Binding coverage, manufactured products (%),TM_TAX_MANF_BC_ZS
Binding coverage, primary products (%),TM_TAX_TCOM_BC_ZS
Bird species, threatened,EN_BIR_THRD_NO
Birth rate, crude (per 1,000 people),SP_DYN_CBRT_IN
Births attended by skilled health staff (% of total),SH_STA_BRTC_ZS
Borrowers from commercial banks (per 1,000 adults),FB_CBK_BRWR_P3
Bound rate, simple mean, all products (%),TM_TAX_MRCH_BR_ZS
Bound rate, simple mean, manufactured products (%),TM_TAX_MANF_BR_ZS
Bound rate, simple mean, primary products (%),TM_TAX_TCOM_BR_ZS
Broad money (% of GDP),FM_LBL_BMNY_GD_ZS
Broad money (current LCU),FM_LBL_BMNY_CN
Broad money growth (annual %),FM_LBL_BMNY_ZG
Broad money to total reserves ratio,FM_LBL_BMNY_IR_ZS
Burden of customs procedure, WEF (1=extremely inefficient to 7=extremely efficient),IQ_WEF_CUST_XQ
Business extent of disclosure index (0=less disclosure to 10=more disclosure),IC_BUS_DISC_XQ
Cash surplus/deficit (% of GDP),GC_BAL_CASH_GD_ZS
Cash surplus/deficit (current LCU),GC_BAL_CASH_CN
Central government debt, total (% of GDP),GC_DOD_TOTL_GD_ZS
Central government debt, total (current LCU),GC_DOD_TOTL_CN
Cereal production (metric tons),AG_PRD_CREL_MT
Cereal yield (kg per hectare),AG_YLD_CREL_KG
Changes in inventories (constant LCU),NE_GDI_STKB_KN
Changes in inventories (current LCU),NE_GDI_STKB_CN
Changes in inventories (current US$),NE_GDI_STKB_CD
Changes in net reserves (BoP, current US$),BN_RES_INCL_CD
Chemicals (% of value added in manufacturing),NV_MNF_CHEM_ZS_UN
Child employment in agriculture (% of economically active children ages 7-14),SL_AGR_0714_ZS
Child employment in agriculture, female (% of female economically active children ages 7-14),SL_AGR_0714_FE_ZS
Child employment in agriculture, male (% of male economically active children ages 7-14),SL_AGR_0714_MA_ZS
Child employment in manufacturing (% of economically active children ages 7-14),SL_MNF_0714_ZS
Child employment in manufacturing, female (% of female economically active children ages 7-14),SL_MNF_0714_FE_ZS
Child employment in manufacturing, male (% of male economically active children ages 7-14),SL_MNF_0714_MA_ZS
Child employment in services (% of economically active children ages 7-14),SL_SRV_0714_ZS
Child employment in services, female (% of female economically active children ages 7-14),SL_SRV_0714_FE_ZS
Child employment in services, male (% of male economically active children ages 7-14),SL_SRV_0714_MA_ZS
Children (0-14) living with HIV,SH_HIV_0014
Children out of school, primary,SE_PRM_UNER
Children out of school, primary, female,SE_PRM_UNER_FE
Children out of school, primary, male,SE_PRM_UNER_MA
Children with fever receiving antimalarial drugs (% of children under age 5 with fever),SH_MLR_TRET_ZS
Claims on central government (annual growth as % of broad money),FM_AST_CGOV_ZG_M3
Claims on central government, etc. (% GDP),FS_AST_CGOV_GD_ZS
Claims on other sectors of the domestic economy (% of GDP),FS_AST_DOMO_GD_ZS
Claims on other sectors of the domestic economy (annual growth as % of broad money),FM_AST_DOMO_ZG_M3
Claims on private sector (annual growth as % of broad money),FM_AST_PRVT_ZG_M3
CO2 emissions (kg per 2000 US$ of GDP),EN_ATM_CO2E_KD_GD
CO2 emissions (kg per 2005 PPP $ of GDP),EN_ATM_CO2E_PP_GD_KD
CO2 emissions (kg per PPP $ of GDP),EN_ATM_CO2E_PP_GD
CO2 emissions (kt),EN_ATM_CO2E_KT
CO2 emissions (metric tons per capita),EN_ATM_CO2E_PC
CO2 emissions from electricity and heat production, total (% of total fuel combustion),EN_CO2_ETOT_ZS
CO2 emissions from electricity and heat production, total (million metric tons),EN_CO2_ETOT_MT
CO2 emissions from gaseous fuel consumption (% of total) ,EN_ATM_CO2E_GF_ZS
CO2 emissions from gaseous fuel consumption (kt) ,EN_ATM_CO2E_GF_KT
CO2 emissions from liquid fuel consumption (% of total) ,EN_ATM_CO2E_LF_ZS
CO2 emissions from liquid fuel consumption (kt) ,EN_ATM_CO2E_LF_KT
CO2 emissions from manufacturing industries and construction (% of total fuel combustion),EN_CO2_MANF_ZS
CO2 emissions from manufacturing industries and construction (million metric tons),EN_CO2_MANF_MT
CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion),EN_CO2_OTHX_ZS
CO2 emissions from other sectors, excluding residential buildings and commercial and public services (million metric tons),EN_CO2_OTHX_MT
CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion),EN_CO2_BLDG_ZS
CO2 emissions from residential buildings and commercial and public services (million metric tons),EN_CO2_BLDG_MT
CO2 emissions from solid fuel consumption (% of total),EN_ATM_CO2E_SF_ZS
CO2 emissions from solid fuel consumption (kt) ,EN_ATM_CO2E_SF_KT
CO2 emissions from transport (% of total fuel combustion),EN_CO2_TRAN_ZS
CO2 emissions from transport (million metric tons),EN_CO2_TRAN_MT
CO2 intensity (kg per kg of oil equivalent energy use),EN_ATM_CO2E_EG_ZS
Coal rents (% of GDP),NY_GDP_COAL_RT_ZS
Combustible renewables and waste (% of total energy),EG_USE_CRNW_ZS
Combustible renewables and waste (metric tons of oil equivalent),EG_USE_CRNW_KT_OE
Commercial bank branches (per 100,000 adults),FB_CBK_BRCH_P5
Commercial banks and other lending (PPG + PNG) (NFL, current US$),DT_NFL_PCBO_CD
Commercial service exports (current US$),TX_VAL_SERV_CD_WT
Commercial service imports (current US$),TM_VAL_SERV_CD_WT
Communications, computer, etc. (% of service exports, BoP),BX_GSR_CMCP_ZS
Communications, computer, etc. (% of service imports, BoP),BM_GSR_CMCP_ZS
Community health workers (per 1,000 people),SH_MED_CMHW_P3
Compensation of employees (% of expense),GC_XPN_COMP_ZS
Compensation of employees (current LCU),GC_XPN_COMP_CN
Completeness of birth registration (%),SP_REG_BRTH_ZS
Completeness of birth registration, rural (%),SP_REG_BRTH_RU_ZS
Completeness of birth registration, urban (%),SP_REG_BRTH_UR_ZS
Completeness of infant death reporting (% of reported infant deaths to estimated infant deaths),SP_DTH_INFR_ZS
Completeness of total death reporting (% of reported total deaths to estimated total deaths),SP_DTH_REPT_ZS
Computer, communications and other services (% of commercial service exports),TX_VAL_OTHR_ZS_WT
Computer, communications and other services (% of commercial service imports),TM_VAL_OTHR_ZS_WT
Condom use, population ages 15-24, female (% of females ages 15-24),SH_CON_1524_FE_ZS
Condom use, population ages 15-24, male (% of males ages 15-24),SH_CON_1524_MA_ZS
Consumer price index (2005 = 100),FP_CPI_TOTL
Consumption of iodized salt (% of households),SN_ITK_SALT_ZS
Container port traffic (TEU: 20 foot equivalent units),IS_SHP_GOOD_TU
Contraceptive prevalence (% of women ages 15-49),SP_DYN_CONU_ZS
Contributing family workers, female (% of females employed),SL_FAM_WORK_FE_ZS
Contributing family workers, male (% of males employed),SL_FAM_WORK_MA_ZS
Contributing family workers, total (% of total employed),SL_FAM_WORK_ZS
Cost of business start-up procedures (% of GNI per capita),IC_REG_COST_PC_ZS
Cost to export (US$ per container),IC_EXP_COST_CD
Cost to import (US$ per container),IC_IMP_COST_CD
CPIA building human resources rating (1=low to 6=high),IQ_CPA_HRES_XQ
CPIA business regulatory environment rating (1=low to 6=high),IQ_CPA_BREG_XQ
CPIA debt policy rating (1=low to 6=high),IQ_CPA_DEBT_XQ
CPIA economic management cluster average (1=low to 6=high),IQ_CPA_ECON_XQ
CPIA efficiency of revenue mobilization rating (1=low to 6=high),IQ_CPA_REVN_XQ
CPIA equity of public resource use rating (1=low to 6=high),IQ_CPA_PRES_XQ
CPIA financial sector rating (1=low to 6=high),IQ_CPA_FINS_XQ
CPIA fiscal policy rating (1=low to 6=high),IQ_CPA_FISP_XQ
CPIA gender equality rating (1=low to 6=high),IQ_CPA_GNDR_XQ
CPIA macroeconomic management rating (1=low to 6=high),IQ_CPA_MACR_XQ
CPIA policies for social inclusion/equity cluster average (1=low to 6=high),IQ_CPA_SOCI_XQ
CPIA policy and institutions for environmental sustainability rating (1=low to 6=high),IQ_CPA_ENVR_XQ
CPIA property rights and rule-based governance rating (1=low to 6=high),IQ_CPA_PROP_XQ
CPIA public sector management and institutions cluster average (1=low to 6=high),IQ_CPA_PUBS_XQ
CPIA quality of budgetary and financial management rating (1=low to 6=high),IQ_CPA_FINQ_XQ
CPIA quality of public administration rating (1=low to 6=high),IQ_CPA_PADM_XQ
CPIA social protection rating (1=low to 6=high),IQ_CPA_PROT_XQ
CPIA structural policies cluster average (1=low to 6=high),IQ_CPA_STRC_XQ
CPIA trade rating (1=low to 6=high),IQ_CPA_TRAD_XQ
CPIA transparency, accountability, and corruption in the public sector rating (1=low to 6=high),IQ_CPA_TRAN_XQ
Credit depth of information index (0=low to 6=high),IC_CRD_INFO_XQ
Crop production index (2004-2006 = 100),AG_PRD_CROP_XD
Current account balance (% of GDP),BN_CAB_XOKA_GD_ZS
Current account balance (BoP, current US$),BN_CAB_XOKA_CD
Current transfers, receipts (BoP, current US$),BX_TRF_CURR_CD
Customs and other import duties (% of tax revenue),GC_TAX_IMPT_ZS
Customs and other import duties (current LCU),GC_TAX_IMPT_CN
Daily newspapers (per 1,000 people),IT_PRT_NEWS_P3
Death rate, crude (per 1,000 people),SP_DYN_CDRT_IN
Debt service (PPG and IMF only, % of exports, excluding workers' remittances),DT_TDS_DPPF_XP_ZS
Debt service on external debt, public and publicly guaranteed (PPG) (TDS, current US$),DT_TDS_DPPG_CD
Debt service on external debt, total (TDS, current US$),DT_TDS_DECT_CD
DEC alternative conversion factor (LCU per US$),PA_NUS_ATLS
Delay in obtaining an electrical connection (days),IC_ELC_DURS
Deposit interest rate (%),FR_INR_DPST
Depositors with commercial banks (per 1,000 adults),FB_CBK_DPTR_P3
Depth of hunger (kilocalories per person per day),SN_ITK_DPTH
Diarrhea treatment (% of children under 5 receiving oral rehydration and continued feeding),SH_STA_ORCF_ZS
Disaster risk reduction progress score (1-5 scale; 5=best),EN_CLC_DRSK_XQ
Discrepancy in expenditure estimate of GDP (constant LCU),NY_GDP_DISC_KN
Discrepancy in expenditure estimate of GDP (current LCU),NY_GDP_DISC_CN
Documents to export (number),IC_EXP_DOCS
Documents to import (number),IC_IMP_DOCS
Domestic credit provided by banking sector (% of GDP),FS_AST_DOMS_GD_ZS
Domestic credit to private sector (% of GDP),FS_AST_PRVT_GD_ZS
Droughts, floods, extreme temperatures (% of population, average 1990-2009),EN_CLC_MDAT_ZS
Ease of doing business index (1=most business-friendly regulations),IC_BUS_EASE_XQ
Economically active children, female (% of female children ages 7-14),SL_TLF_0714_FE_ZS
Economically active children, male (% of male children ages 7-14),SL_TLF_0714_MA_ZS
Economically active children, study and work (% of economically active children, ages 7-14),SL_TLF_0714_SW_ZS
Economically active children, study and work, female (% of female economically active children, ages 7-14),SL_TLF_0714_SW_FE_ZS
Economically active children, study and work, male (% of male economically active children, ages 7-14),SL_TLF_0714_SW_MA_ZS
Economically active children, total (% of children ages 7-14),SL_TLF_0714_ZS
Economically active children, work only (% of economically active children, ages 7-14),SL_TLF_0714_WK_ZS
Economically active children, work only, female (% of female economically active children, ages 7-14),SL_TLF_0714_WK_FE_ZS
Economically active children, work only, male (% of male economically active children, ages 7-14),SL_TLF_0714_WK_MA_ZS
Electric power consumption (kWh per capita),EG_USE_ELEC_KH_PC
Electric power consumption (kWh),EG_USE_ELEC_KH
Electric power transmission and distribution losses (% of output),EG_ELC_LOSS_ZS
Electric power transmission and distribution losses (kWh),EG_ELC_LOSS_KH
Electricity production (kWh),EG_ELC_PROD_KH
Electricity production from coal sources (% of total),EG_ELC_COAL_ZS
Electricity production from coal sources (kWh),EG_ELC_COAL_KH
Electricity production from hydroelectric sources (% of total),EG_ELC_HYRO_ZS
Electricity production from hydroelectric sources (kWh),EG_ELC_HYRO_KH
Electricity production from natural gas sources (% of total),EG_ELC_NGAS_ZS
Electricity production from natural gas sources (kWh),EG_ELC_NGAS_KH
Electricity production from nuclear sources (% of total),EG_ELC_NUCL_ZS
Electricity production from nuclear sources (kWh),EG_ELC_NUCL_KH
Electricity production from oil sources (% of total),EG_ELC_PETR_ZS
Electricity production from oil sources (kWh),EG_ELC_PETR_KH
Electricity production from oil, gas and coal sources (% of total),EG_ELC_FOSL_ZS
Electricity production from renewable sources (kWh),EG_ELC_RNEW_KH
Electricity production from renewable sources, excluding hydroelectric (% of total),EG_ELC_RNWX_ZS
Electricity production from renewable sources, excluding hydroelectric (kWh),EG_ELC_RNWX_KH
Emigration rate of tertiary educated (% of total tertiary educated population),SM_EMI_TERT_ZS
Employees, agriculture, female (% of female employment),SL_AGR_EMPL_FE_ZS
Employees, agriculture, male (% of male employment),SL_AGR_EMPL_MA_ZS
Employees, industry, female (% of female employment),SL_IND_EMPL_FE_ZS
Employees, industry, male (% of male employment),SL_IND_EMPL_MA_ZS
Employees, services, female (% of female employment),SL_SRV_EMPL_FE_ZS
Employees, services, male (% of male employment),SL_SRV_EMPL_MA_ZS
Employers, female (% of employment),SL_EMP_MPYR_FE_ZS
Employers, male (% of employment),SL_EMP_MPYR_MA_ZS
Employers, total (% of employment),SL_EMP_MPYR_ZS
Employment in agriculture (% of total employment),SL_AGR_EMPL_ZS
Employment in industry (% of total employment),SL_IND_EMPL_ZS
Employment in services (% of total employment),SL_SRV_EMPL_ZS
Employment to population ratio, 15+, female (%),SL_EMP_TOTL_SP_FE_ZS
Employment to population ratio, 15+, male (%),SL_EMP_TOTL_SP_MA_ZS
Employment to population ratio, 15+, total (%),SL_EMP_TOTL_SP_ZS
Employment to population ratio, ages 15-24, female (%),SL_EMP_1524_SP_FE_ZS
Employment to population ratio, ages 15-24, male (%),SL_EMP_1524_SP_MA_ZS
Employment to population ratio, ages 15-24, total (%),SL_EMP_1524_SP_ZS
Energy imports, net (% of energy use),EG_IMP_CONS_ZS
Energy production (kt of oil equivalent),EG_EGY_PROD_KT_OE
Energy related methane emissions (% of total),EN_ATM_METH_EG_ZS
Energy use (kg of oil equivalent per capita),EG_USE_PCAP_KG_OE
Energy use (kg of oil equivalent) per $1,000 GDP (constant 2005 PPP),EG_USE_COMM_GD_PP_KD
Energy use (kt of oil equivalent),EG_USE_COMM_KT_OE
Exclusive breastfeeding (% of children under 6 months),SH_STA_BFED_ZS
Expenditure per student, primary (% of GDP per capita),SE_XPD_PRIM_PC_ZS
Expenditure per student, secondary (% of GDP per capita),SE_XPD_SECO_PC_ZS
Expenditure per student, tertiary (% of GDP per capita),SE_XPD_TERT_PC_ZS
Expense (% of GDP),GC_XPN_TOTL_GD_ZS
Expense (current LCU),GC_XPN_TOTL_CN
Export value index (2000 = 100),TX_VAL_MRCH_XD_WD
Export volume index (2000 = 100),TX_QTY_MRCH_XD_WD
Exports as a capacity to import (constant LCU),NY_EXP_CAPM_KN
Exports of goods and services (% of GDP),NE_EXP_GNFS_ZS
Exports of goods and services (annual % growth),NE_EXP_GNFS_KD_ZG
Exports of goods and services (BoP, current US$),BX_GSR_GNFS_CD
Exports of goods and services (constant 2000 US$),NE_EXP_GNFS_KD
Exports of goods and services (constant LCU),NE_EXP_GNFS_KN
Exports of goods and services (current LCU),NE_EXP_GNFS_CN
Exports of goods and services (current US$),NE_EXP_GNFS_CD
Exports of goods, services and income (BoP, current US$),BX_GSR_TOTL_CD
External balance on goods and services (% of GDP),NE_RSB_GNFS_ZS
External balance on goods and services (constant LCU),NE_RSB_GNFS_KN
External balance on goods and services (current LCU),NE_RSB_GNFS_CN
External balance on goods and services (current US$),NE_RSB_GNFS_CD
External debt stocks (% of GNI),DT_DOD_DECT_GN_ZS
External debt stocks, long-term (DOD, current US$),DT_DOD_DLXF_CD
External debt stocks, private nonguaranteed (PNG) (DOD, current US$),DT_DOD_DPNG_CD
External debt stocks, public and publicly guaranteed (PPG) (DOD, current US$),DT_DOD_DPPG_CD
External debt stocks, short-term (DOD, current US$),DT_DOD_DSTC_CD
External debt stocks, total (DOD, current US$),DT_DOD_DECT_CD
External resources for health (% of total expenditure on health),SH_XPD_EXTR_ZS
Female headed households (% of households with a female head),SP_HOU_FEMA_ZS
Female legistlators, senior officials and managers (% of total),SG_GEN_LSOM_ZS
Fertility rate, total (births per woman),SP_DYN_TFRT_IN
Fertilizer consumption (% of fertilizer production),AG_CON_FERT_PT_ZS
Fertilizer consumption (kilograms per hectare of arable land),AG_CON_FERT_ZS
Final consumption expenditure (constant 2000 US$),NE_CON_TOTL_KD
Final consumption expenditure (constant LCU),NE_CON_TOTL_KN
Final consumption expenditure (current LCU),NE_CON_TOTL_CN
Final consumption expenditure (current US$),NE_CON_TOTL_CD
Final consumption expenditure, etc. (% of GDP),NE_CON_TETC_ZS
Final consumption expenditure, etc. (annual % growth),NE_CON_TETC_KD_ZG
Final consumption expenditure, etc. (constant 2000 US$),NE_CON_TETC_KD
Final consumption expenditure, etc. (constant LCU),NE_CON_TETC_KN
Final consumption expenditure, etc. (current LCU),NE_CON_TETC_CN
Final consumption expenditure, etc. (current US$),NE_CON_TETC_CD
Firing cost (weeks of wages),IC_EMP_FIRE_WK
Firms expected to give gifts in meetings with tax officials (% of firms),IC_TAX_GIFT_ZS
Firms formally registered when operations started (% of firms),IC_FRM_FREG_ZS
Firms offering formal training (% of firms),IC_FRM_TRNG_ZS
Firms that do not report all sales for tax purposes (% of firms),IC_FRM_INFM_ZS
Firms using banks to finance investment (% of firms),IC_FRM_BNKS_ZS
Firms with female participation in ownership (% of firms),IC_FRM_FEMO_ZS
Fish species, threatened,EN_FSH_THRD_NO
Fixed broadband Internet subscribers,IT_NET_BBND
Fixed broadband Internet subscribers (per 100 people),IT_NET_BBND_P2
Food exports (% of merchandise exports),TX_VAL_FOOD_ZS_UN
Food imports (% of merchandise imports),TM_VAL_FOOD_ZS_UN
Food production index (2004-2006 = 100),AG_PRD_FOOD_XD
Food, beverages and tobacco (% of value added in manufacturing),NV_MNF_FBTO_ZS_UN
Foreign direct investment, net (BoP, current US$),BN_KLT_DINV_CD
Foreign direct investment, net inflows (% of GDP),BX_KLT_DINV_WD_GD_ZS
Foreign direct investment, net inflows (BoP, current US$),BX_KLT_DINV_CD_WD
Foreign direct investment, net outflows (% of GDP),BM_KLT_DINV_GD_ZS
Forest area (% of land area),AG_LND_FRST_ZS
Forest area (sq. km),AG_LND_FRST_K2
Forest rents (% of GDP),NY_GDP_FRST_RT_ZS
Fossil fuel energy consumption (% of total),EG_USE_COMM_FO_ZS
Fuel exports (% of merchandise exports),TX_VAL_FUEL_ZS_UN
Fuel imports (% of merchandise imports),TM_VAL_FUEL_ZS_UN
GDP (constant 2000 US$),NY_GDP_MKTP_KD
GDP (constant LCU),NY_GDP_MKTP_KN
GDP (current LCU),NY_GDP_MKTP_CN
GDP (current US$),NY_GDP_MKTP_CD
GDP deflator (base year varies by country),NY_GDP_DEFL_ZS
GDP growth (annual %),NY_GDP_MKTP_KD_ZG
GDP per capita (constant 2000 US$),NY_GDP_PCAP_KD
GDP per capita (constant LCU),NY_GDP_PCAP_KN
GDP per capita (current US$),NY_GDP_PCAP_CD
GDP per capita growth (annual %),NY_GDP_PCAP_KD_ZG
GDP per capita, PPP (constant 2005 international $),NY_GDP_PCAP_PP_KD
GDP per capita, PPP (current international $),NY_GDP_PCAP_PP_CD
GDP per person employed (constant 1990 PPP $),SL_GDP_PCAP_EM_KD
GDP per unit of energy use (constant 2005 PPP $ per kg of oil equivalent),EG_GDP_PUSE_KO_PP_KD
GDP per unit of energy use (PPP $ per kg of oil equivalent),EG_GDP_PUSE_KO_PP
GDP, PPP (constant 2005 international $),NY_GDP_MKTP_PP_KD
GDP, PPP (current international $),NY_GDP_MKTP_PP_CD
GEF benefits index for biodiversity (0 = no biodiversity potential to 100 = maximum),ER_BDV_TOTL_XQ
General government final consumption expenditure (% of GDP),NE_CON_GOVT_ZS
General government final consumption expenditure (annual % growth),NE_CON_GOVT_KD_ZG
General government final consumption expenditure (constant 2000 US$),NE_CON_GOVT_KD
General government final consumption expenditure (constant LCU),NE_CON_GOVT_KN
General government final consumption expenditure (current LCU),NE_CON_GOVT_CN
General government final consumption expenditure (current US$),NE_CON_GOVT_CD
GHG net emissions/removals by LUCF (Mt of CO2 equivalent),EN_CLC_GHGR_MT_CE
GINI index,SI_POV_GINI
GNI (constant 2000 US$),NY_GNP_MKTP_KD
GNI (constant LCU),NY_GNP_MKTP_KN
GNI (current LCU),NY_GNP_MKTP_CN
GNI (current US$),NY_GNP_MKTP_CD
GNI growth (annual %),NY_GNP_MKTP_KD_ZG
GNI per capita (constant 2000 US$),NY_GNP_PCAP_KD
GNI per capita (constant LCU),NY_GNP_PCAP_KN
GNI per capita growth (annual %),NY_GNP_PCAP_KD_ZG
GNI per capita, Atlas method (current US$),NY_GNP_PCAP_CD
GNI per capita, PPP (current international $),NY_GNP_PCAP_PP_CD
GNI, Atlas method (current US$),NY_GNP_ATLS_CD
GNI, PPP (current international $),NY_GNP_MKTP_PP_CD
Goods and services expense (% of expense),GC_XPN_GSRV_ZS
Goods and services expense (current LCU),GC_XPN_GSRV_CN
Goods exports (BoP, current US$),BX_GSR_MRCH_CD
Goods imports (BoP, current US$),BM_GSR_MRCH_CD
Grants and other revenue (% of revenue),GC_REV_GOTR_ZS
Grants and other revenue (current LCU),GC_REV_GOTR_CN
Grants, excluding technical cooperation (BoP, current US$),BX_GRT_EXTA_CD_WD
Gross capital formation (% of GDP),NE_GDI_TOTL_ZS
Gross capital formation (annual % growth),NE_GDI_TOTL_KD_ZG
Gross capital formation (constant 2000 US$),NE_GDI_TOTL_KD
Gross capital formation (constant LCU),NE_GDI_TOTL_KN
Gross capital formation (current LCU),NE_GDI_TOTL_CN
Gross capital formation (current US$),NE_GDI_TOTL_CD
Gross domestic income (constant 2000 US$),NY_GDY_TOTL_KD
Gross domestic income (constant LCU),NY_GDY_TOTL_KN
Gross domestic savings (% of GDP),NY_GDS_TOTL_ZS
Gross domestic savings (constant LCU),NY_GDS_TOTL_KN
Gross domestic savings (current LCU),NY_GDS_TOTL_CN
Gross domestic savings (current US$),NY_GDS_TOTL_CD
Gross fixed capital formation (% of GDP),NE_GDI_FTOT_ZS
Gross fixed capital formation (annual % growth),NE_GDI_FTOT_KD_ZG
Gross fixed capital formation (constant 2000 US$),NE_GDI_FTOT_KD
Gross fixed capital formation (constant LCU),NE_GDI_FTOT_KN
Gross fixed capital formation (current LCU),NE_GDI_FTOT_CN
Gross fixed capital formation (current US$),NE_GDI_FTOT_CD
Gross fixed capital formation, private sector (% of GDP),NE_GDI_FPRV_ZS
Gross fixed capital formation, private sector (current LCU),NE_GDI_FPRV_CN
Gross intake rate in grade 1, female (% of relevant age group),SE_PRM_GINT_FE_ZS
Gross intake rate in grade 1, male (% of relevant age group),SE_PRM_GINT_MA_ZS
Gross intake rate in grade 1, total (% of relevant age group),SE_PRM_GINT_ZS
Gross national expenditure (% of GDP),NE_DAB_TOTL_ZS
Gross national expenditure (constant 2000 US$),NE_DAB_TOTL_KD
Gross national expenditure (constant LCU),NE_DAB_TOTL_KN
Gross national expenditure (current LCU),NE_DAB_TOTL_CN
Gross national expenditure (current US$),NE_DAB_TOTL_CD
Gross national expenditure deflator (base year varies by country),NE_DAB_DEFL_ZS
Gross national income (constant LCU),NY_GNY_TOTL_KN
Gross savings (% of GDP),NY_GNS_ICTR_ZS
Gross savings (% of GNI),NY_GNS_ICTR_GN_ZS
Gross savings (current LCU),NY_GNS_ICTR_CN
Gross savings (current US$),NY_GNS_ICTR_CD
Gross value added at factor cost (constant 2000 US$),NY_GDP_FCST_KD
Gross value added at factor cost (constant LCU),NY_GDP_FCST_KN
Gross value added at factor cost (current LCU),NY_GDP_FCST_CN
Gross value added at factor cost (current US$),NY_GDP_FCST_CD
Health expenditure per capita (current US$),SH_XPD_PCAP
Health expenditure per capita, PPP (constant 2005 international $),SH_XPD_PCAP_PP_KD
Health expenditure, private (% of GDP),SH_XPD_PRIV_ZS
Health expenditure, private (% of total health expenditure),SH_XPD_PRIV
Health expenditure, public (% of GDP),SH_XPD_PUBL_ZS
Health expenditure, public (% of government expenditure),SH_XPD_PUBL_GX_ZS
Health expenditure, public (% of total health expenditure),SH_XPD_PUBL
Health expenditure, total (% of GDP),SH_XPD_TOTL_ZS
HFC gas emissions (thousand metric tons of CO2 equivalent),EN_ATM_HFCG_KT_CE
High-technology exports (% of manufactured exports),TX_VAL_TECH_MF_ZS
High-technology exports (current US$),TX_VAL_TECH_CD
Hospital beds (per 1,000 people),SH_MED_BEDS_ZS
Household final consumption expenditure (annual % growth),NE_CON_PRVT_KD_ZG
Household final consumption expenditure (constant 2000 US$),NE_CON_PRVT_KD
Household final consumption expenditure (constant LCU),NE_CON_PRVT_KN
Household final consumption expenditure (current LCU),NE_CON_PRVT_CN
Household final consumption expenditure (current US$),NE_CON_PRVT_CD
Household final consumption expenditure per capita (constant 2000 US$),NE_CON_PRVT_PC_KD
Household final consumption expenditure per capita growth (annual %),NE_CON_PRVT_PC_KD_ZG
Household final consumption expenditure, etc. (% of GDP),NE_CON_PETC_ZS
Household final consumption expenditure, etc. (annual % growth),NE_CON_PETC_KD_ZG
Household final consumption expenditure, etc. (constant 2000 US$),NE_CON_PETC_KD
Household final consumption expenditure, etc. (constant LCU),NE_CON_PETC_KN
Household final consumption expenditure, etc. (current LCU),NE_CON_PETC_CN
Household final consumption expenditure, etc. (current US$),NE_CON_PETC_CD
Household final consumption expenditure, PPP (constant 2005 international $),NE_CON_PRVT_PP_KD
Household final consumption expenditure, PPP (current international $),NE_CON_PRVT_PP_CD
IBRD loans and IDA credits (DOD, current US$),DT_DOD_MWBG_CD
ICT goods exports (% of total goods exports),TX_VAL_ICTG_ZS_UN
ICT goods imports (% total goods imports),TM_VAL_ICTG_ZS_UN
ICT service exports (% of service exports, BoP),BX_GSR_CCIS_ZS
ICT service exports (BoP, current US$),BX_GSR_CCIS_CD
IDA resource allocation index (1=low to 6=high),IQ_CPA_IRAI_XQ
Immunization, DPT (% of children ages 12-23 months),SH_IMM_IDPT
Immunization, measles (% of children ages 12-23 months),SH_IMM_MEAS
Import value index (2000 = 100),TM_VAL_MRCH_XD_WD
Import volume index (2000 = 100),TM_QTY_MRCH_XD_WD
Imports of goods and services (% of GDP),NE_IMP_GNFS_ZS
Imports of goods and services (annual % growth),NE_IMP_GNFS_KD_ZG
Imports of goods and services (BoP, current US$),BM_GSR_GNFS_CD
Imports of goods and services (constant 2000 US$),NE_IMP_GNFS_KD
Imports of goods and services (constant LCU),NE_IMP_GNFS_KN
Imports of goods and services (current LCU),NE_IMP_GNFS_CN
Imports of goods and services (current US$),NE_IMP_GNFS_CD
Imports of goods, services and income (BoP, current US$),BM_GSR_TOTL_CD
Improved sanitation facilities (% of population with access),SH_STA_ACSN
Improved sanitation facilities, rural (% of rural population with access),SH_STA_ACSN_RU
Improved sanitation facilities, urban (% of urban population with access),SH_STA_ACSN_UR
Improved water source (% of population with access),SH_H2O_SAFE_ZS
Improved water source, rural (% of rural population with access),SH_H2O_SAFE_RU_ZS
Improved water source, urban (% of urban population with access),SH_H2O_SAFE_UR_ZS
Incidence of tuberculosis (per 100,000 people),SH_TBS_INCD
Income payments (BoP, current US$),BM_GSR_FCTY_CD
Income receipts (BoP, current US$),BX_GSR_FCTY_CD
Income share held by fourth 20%,SI_DST_04TH_20
Income share held by highest 10%,SI_DST_10TH_10
Income share held by highest 20%,SI_DST_05TH_20
Income share held by lowest 10%,SI_DST_FRST_10
Income share held by lowest 20%,SI_DST_FRST_20
Income share held by second 20%,SI_DST_02ND_20
Income share held by third 20%,SI_DST_03RD_20
Industrial nitrous oxide emissions (thousand metric tons of CO2 equivalent),EN_ATM_NOXE_IN_KT_CE
Industry, value added (% of GDP),NV_IND_TOTL_ZS
Industry, value added (annual % growth),NV_IND_TOTL_KD_ZG
Industry, value added (constant 2000 US$),NV_IND_TOTL_KD
Industry, value added (constant LCU),NV_IND_TOTL_KN
Industry, value added (current LCU),NV_IND_TOTL_CN
Industry, value added (current US$),NV_IND_TOTL_CD
Inflation, consumer prices (annual %),FP_CPI_TOTL_ZG
Inflation, GDP deflator (annual %),NY_GDP_DEFL_KD_ZG
Informal payments to public officials (% of firms),IC_FRM_CORR_ZS
Insurance and financial services (% of commercial service exports),TX_VAL_INSF_ZS_WT
Insurance and financial services (% of commercial service imports),TM_VAL_INSF_ZS_WT
Insurance and financial services (% of service exports, BoP),BX_GSR_INSF_ZS
Insurance and financial services (% of service imports, BoP),BM_GSR_INSF_ZS
Intentional homicides (per 100,000 people),VC_IHR_PSRC_P5
Interest payments (% of expense),GC_XPN_INTP_ZS
Interest payments (% of revenue),GC_XPN_INTP_RV_ZS
Interest payments (current LCU),GC_XPN_INTP_CN
Interest rate spread (lending rate minus deposit rate, %),FR_INR_LNDP
Internally displaced persons (number, high estimate),VC_IDP_TOTL_HE
Internally displaced persons (number, low estimate),VC_IDP_TOTL_LE
International migrant stock (% of population),SM_POP_TOTL_ZS
International migrant stock, total,SM_POP_TOTL
International tourism, expenditures (% of total imports),ST_INT_XPND_MP_ZS
International tourism, expenditures (current US$),ST_INT_XPND_CD
International tourism, expenditures for passenger transport items (current US$),ST_INT_TRNX_CD
International tourism, expenditures for travel items (current US$),ST_INT_TVLX_CD
International tourism, number of arrivals,ST_INT_ARVL
International tourism, number of departures,ST_INT_DPRT
International tourism, receipts (% of total exports),ST_INT_RCPT_XP_ZS
International tourism, receipts (current US$),ST_INT_RCPT_CD
International tourism, receipts for passenger transport items (current US$),ST_INT_TRNR_CD
International tourism, receipts for travel items (current US$),ST_INT_TVLR_CD
Internet users,IT_NET_USER
Internet users (per 100 people),IT_NET_USER_P2
Investment in energy with private participation (current US$),IE_PPI_ENGY_CD
Investment in telecoms with private participation (current US$),IE_PPI_TELE_CD
Investment in transport with private participation (current US$),IE_PPI_TRAN_CD
Investment in water and sanitation with private participation (current US$),IE_PPI_WATR_CD
ISO certification ownership (% of firms),IC_FRM_ISOC_ZS
Labor force participation rate, female (% of female population ages 15-64),SL_TLF_ACTI_FE_ZS
Labor force participation rate, male (% of male population ages 15-64),SL_TLF_ACTI_MA_ZS
Labor force participation rate, total (% of total population ages 15-64),SL_TLF_ACTI_ZS
Labor force with primary education (% of total),SL_TLF_PRIM_ZS
Labor force with primary education, female (% of female labor force),SL_TLF_PRIM_FE_ZS
Labor force with primary education, male (% of male labor force),SL_TLF_PRIM_MA_ZS
Labor force with secondary education (% of total),SL_TLF_SECO_ZS
Labor force with secondary education, female (% of female labor force),SL_TLF_SECO_FE_ZS
Labor force with secondary education, male (% of male labor force),SL_TLF_SECO_MA_ZS
Labor force with tertiary education (% of total),SL_TLF_TERT_ZS
Labor force with tertiary education, female (% of female labor force),SL_TLF_TERT_FE_ZS
Labor force with tertiary education, male (% of male labor force),SL_TLF_TERT_MA_ZS
Labor force, female (% of total labor force),SL_TLF_TOTL_FE_ZS
Labor force, total,SL_TLF_TOTL_IN
Labor participation rate, female (% of female population ages 15+),SL_TLF_CACT_FE_ZS
Labor participation rate, male (% of male population ages 15+),SL_TLF_CACT_MA_ZS
Labor participation rate, total (% of total population ages 15+),SL_TLF_CACT_ZS
Labor tax and contributions (% of commercial profits),IC_TAX_LABR_CP_ZS
Land area (sq. km),AG_LND_TOTL_K2
Land area where elevation is below 5 meters (% of total land area),AG_LND_EL5M_ZS
Land under cereal production (hectares),AG_LND_CREL_HA
Lead time to export, median case (days),LP_EXP_DURS_MD
Lead time to import, median case (days),LP_IMP_DURS_MD
Lending interest rate (%),FR_INR_LEND
Life expectancy at birth, female (years),SP_DYN_LE00_FE_IN
Life expectancy at birth, male (years),SP_DYN_LE00_MA_IN
Life expectancy at birth, total (years),SP_DYN_LE00_IN
Lifetime risk of maternal death (%),SH_MMR_RISK_ZS
Lifetime risk of maternal death (1 in: rate varies by country),SH_MMR_RISK
Liner shipping connectivity index (maximum value in 2004 = 100),IS_SHP_GCNW_XQ
Liquid liabilities (M3) as % of GDP,FS_LBL_LIQU_GD_ZS
Listed domestic companies, total,CM_MKT_LDOM_NO
Literacy rate, adult female (% of females ages 15 and above),SE_ADT_LITR_FE_ZS
Literacy rate, adult male (% of males ages 15 and above),SE_ADT_LITR_MA_ZS
Literacy rate, adult total (% of people ages 15 and above),SE_ADT_LITR_ZS
Literacy rate, youth female (% of females ages 15-24),SE_ADT_1524_LT_FE_ZS
Literacy rate, youth male (% of males ages 15-24),SE_ADT_1524_LT_MA_ZS
Literacy rate, youth total (% of people ages 15-24),SE_ADT_1524_LT_ZS
Livestock production index (2004-2006 = 100),AG_PRD_LVSK_XD
Logistics performance index: Ability to track and trace consignments (1=low to 5=high),LP_LPI_TRAC_XQ
Logistics performance index: Competence and quality of logistics services (1=low to 5=high),LP_LPI_LOGS_XQ
Logistics performance index: Ease of arranging competitively priced shipments (1=low to 5=high),LP_LPI_ITRN_XQ
Logistics performance index: Efficiency of customs clearance process (1=low to 5=high),LP_LPI_CUST_XQ
Logistics performance index: Frequency with which shipments reach consignee within scheduled or expected time (1=low to 5=high),LP_LPI_TIME_XQ
Logistics performance index: Overall (1=low to 5=high),LP_LPI_OVRL_XQ
Logistics performance index: Quality of trade and transport-related infrastructure (1=low to 5=high),LP_LPI_INFR_XQ
Long-term unemployment (% of total unemployment),SL_UEM_LTRM_ZS
Long-term unemployment, female (% of female unemployment),SL_UEM_LTRM_FE_ZS
Long-term unemployment, male (% of male unemployment),SL_UEM_LTRM_MA_ZS
Losses due to theft, robbery, vandalism, and arson (% sales),IC_FRM_CRIM_ZS
Low-birthweight babies (% of births),SH_STA_BRTW_ZS
Machinery and transport equipment (% of value added in manufacturing),NV_MNF_MTRN_ZS_UN
Malnutrition prevalence, height for age (% of children under 5),SH_STA_STNT_ZS
Malnutrition prevalence, weight for age (% of children under 5),SH_STA_MALN_ZS
Mammal species, threatened,EN_MAM_THRD_NO
Management time dealing with officials (% of management time),IC_GOV_DURS_ZS
Manufactures exports (% of merchandise exports),TX_VAL_MANF_ZS_UN
Manufactures imports (% of merchandise imports),TM_VAL_MANF_ZS_UN
Manufacturing, value added (% of GDP),NV_IND_MANF_ZS
Manufacturing, value added (annual % growth),NV_IND_MANF_KD_ZG
Manufacturing, value added (constant 2000 US$),NV_IND_MANF_KD
Manufacturing, value added (constant LCU),NV_IND_MANF_KN
Manufacturing, value added (current LCU),NV_IND_MANF_CN
Manufacturing, value added (current US$),NV_IND_MANF_CD
Marine protected areas (% of territorial waters),ER_MRN_PTMR_ZS
Market capitalization of listed companies (% of GDP),CM_MKT_LCAP_GD_ZS
Market capitalization of listed companies (current US$),CM_MKT_LCAP_CD
Maternal mortality ratio (modeled estimate, per 100,000 live births),SH_STA_MMRT
Maternal mortality ratio (national estimate, per 100,000 live births),SH_STA_MMRT_NE
Merchandise exports (current US$),TX_VAL_MRCH_CD_WT
Merchandise exports by the reporting economy (current US$),TX_VAL_MRCH_WL_CD
Merchandise exports by the reporting economy, residual (% of total merchandise exports),TX_VAL_MRCH_RS_ZS
Merchandise exports to developing economies in East Asia & Pacific (% of total merchandise exports),TX_VAL_MRCH_R1_ZS
Merchandise exports to developing economies in Europe & Central Asia (% of total merchandise exports),TX_VAL_MRCH_R2_ZS
Merchandise exports to developing economies in Latin America & the Caribbean (% of total merchandise exports),TX_VAL_MRCH_R3_ZS
Merchandise exports to developing economies in Middle East & North Africa (% of total merchandise exports),TX_VAL_MRCH_R4_ZS
Merchandise exports to developing economies in South Asia (% of total merchandise exports),TX_VAL_MRCH_R5_ZS
Merchandise exports to developing economies in Sub-Saharan Africa (% of total merchandise exports),TX_VAL_MRCH_R6_ZS
Merchandise exports to developing economies outside region (% of total merchandise exports),TX_VAL_MRCH_OR_ZS
Merchandise exports to developing economies within region (% of total merchandise exports),TX_VAL_MRCH_WR_ZS
Merchandise exports to economies in the Arab World (% of total merchandise exports),TX_VAL_MRCH_AL_ZS
Merchandise exports to high-income economies (% of total merchandise exports),TX_VAL_MRCH_HI_ZS
Merchandise imports (current US$),TM_VAL_MRCH_CD_WT
Merchandise imports by the reporting economy (current US$),TM_VAL_MRCH_WL_CD
Merchandise imports by the reporting economy, residual (% of total merchandise imports),TM_VAL_MRCH_RS_ZS
Merchandise imports from developing economies in East Asia & Pacific (% of total merchandise imports),TM_VAL_MRCH_R1_ZS
Merchandise imports from developing economies in Europe & Central Asia (% of total merchandise imports),TM_VAL_MRCH_R2_ZS
Merchandise imports from developing economies in Latin America & the Caribbean (% of total merchandise imports),TM_VAL_MRCH_R3_ZS
Merchandise imports from developing economies in Middle East & North Africa (% of total merchandise imports),TM_VAL_MRCH_R4_ZS
Merchandise imports from developing economies in South Asia (% of total merchandise imports),TM_VAL_MRCH_R5_ZS
Merchandise imports from developing economies in Sub-Saharan Africa (% of total merchandise imports),TM_VAL_MRCH_R6_ZS
Merchandise imports from developing economies outside region (% of total merchandise imports),TM_VAL_MRCH_OR_ZS
Merchandise imports from developing economies within region (% of total merchandise imports),TM_VAL_MRCH_WR_ZS
Merchandise imports from economies in the Arab World (% of total merchandise imports),TM_VAL_MRCH_AL_ZS
Merchandise imports from high-income economies (% of total merchandise imports),TM_VAL_MRCH_HI_ZS
Merchandise trade (% of GDP),TG_VAL_TOTL_GD_ZS
Methane emissions (kt of CO2 equivalent),EN_ATM_METH_KT_CE
Methane emissions in energy sector (thousand metric tons of CO2 equivalent),EN_ATM_METH_EG_KT_CE
Military expenditure (% of central government expenditure),MS_MIL_XPND_ZS
Military expenditure (% of GDP),MS_MIL_XPND_GD_ZS
Military expenditure (current LCU),MS_MIL_XPND_CN
Mineral rents (% of GDP),NY_GDP_MINR_RT_ZS
Mobile cellular subscriptions,IT_CEL_SETS
Mobile cellular subscriptions (per 100 people),IT_CEL_SETS_P2
Money (current LCU),FM_LBL_MONY_CN
Money and quasi money (M2) (current LCU),FM_LBL_MQMY_CN
Money and quasi money (M2) as % of GDP,FM_LBL_MQMY_GD_ZS
Money and quasi money (M2) to total reserves ratio,FM_LBL_MQMY_IR_ZS
Money and quasi money growth (annual %),FM_LBL_MQMY_ZG
Mortality rate, adult, female (per 1,000 female adults),SP_DYN_AMRT_FE
Mortality rate, adult, male (per 1,000 male adults),SP_DYN_AMRT_MA
Mortality rate, female child (per 1,000 female children age one),SH_DYN_CHLD_FE
Mortality rate, infant (per 1,000 live births),SP_DYN_IMRT_IN
Mortality rate, male child (per 1,000 male children age one),SH_DYN_CHLD_MA
Mortality rate, neonatal (per 1,000 live births),SH_DYN_NMRT
Mortality rate, under-5 (per 1,000 live births),SH_DYN_MORT
Motor vehicles (per 1,000 people),IS_VEH_NVEH_P3
Multilateral debt service (% of public and publicly guaranteed debt service),DT_TDS_MLAT_PG_ZS
Multilateral debt service (TDS, current US$),DT_TDS_MLAT_CD
Natural gas rents (% of GDP),NY_GDP_NGAS_RT_ZS
Net barter terms of trade index (2000 = 100),TT_PRI_MRCH_XD_WD
Net bilateral aid flows from DAC donors, Australia (current US$),DC_DAC_AUSL_CD
Net bilateral aid flows from DAC donors, Austria (current US$),DC_DAC_AUTL_CD
Net bilateral aid flows from DAC donors, Belgium (current US$),DC_DAC_BELL_CD
Net bilateral aid flows from DAC donors, Canada (current US$),DC_DAC_CANL_CD
Net bilateral aid flows from DAC donors, Denmark (current US$),DC_DAC_DNKL_CD
Net bilateral aid flows from DAC donors, European Union institutions (current US$),DC_DAC_CECL_CD
Net bilateral aid flows from DAC donors, Finland (current US$),DC_DAC_FINL_CD
Net bilateral aid flows from DAC donors, France (current US$),DC_DAC_FRAL_CD
Net bilateral aid flows from DAC donors, Germany (current US$),DC_DAC_DEUL_CD
Net bilateral aid flows from DAC donors, Greece (current US$),DC_DAC_GRCL_CD
Net bilateral aid flows from DAC donors, Ireland (current US$),DC_DAC_IRLL_CD
Net bilateral aid flows from DAC donors, Italy (current US$),DC_DAC_ITAL_CD
Net bilateral aid flows from DAC donors, Japan (current US$),DC_DAC_JPNL_CD
Net bilateral aid flows from DAC donors, Korea, Rep. (current US$),DC_DAC_KORL_CD
Net bilateral aid flows from DAC donors, Luxembourg (current US$),DC_DAC_LUXL_CD
Net bilateral aid flows from DAC donors, Netherlands (current US$),DC_DAC_NLDL_CD
Net bilateral aid flows from DAC donors, New Zealand (current US$),DC_DAC_NZLL_CD
Net bilateral aid flows from DAC donors, Norway (current US$),DC_DAC_NORL_CD
Net bilateral aid flows from DAC donors, Portugal (current US$),DC_DAC_PRTL_CD
Net bilateral aid flows from DAC donors, Spain (current US$),DC_DAC_ESPL_CD
Net bilateral aid flows from DAC donors, Sweden (current US$),DC_DAC_SWEL_CD
Net bilateral aid flows from DAC donors, Switzerland (current US$),DC_DAC_CHEL_CD
Net bilateral aid flows from DAC donors, Total (current US$),DC_DAC_TOTL_CD
Net bilateral aid flows from DAC donors, United Kingdom (current US$),DC_DAC_GBRL_CD
Net bilateral aid flows from DAC donors, United States (current US$),DC_DAC_USAL_CD
Net capital account (BoP, current US$),BN_TRF_KOGT_CD
Net current transfers (BoP, current US$),BN_TRF_CURR_CD
Net current transfers from abroad (constant LCU),NY_TRF_NCTR_KN
Net current transfers from abroad (current LCU),NY_TRF_NCTR_CN
Net current transfers from abroad (current US$),NY_TRF_NCTR_CD
Net domestic credit (current LCU),FM_AST_DOMS_CN
Net errors and omissions, adjusted (BoP, current US$),BN_KAC_EOMS_CD
Net financial flows, bilateral (NFL, current US$),DT_NFL_BLAT_CD
Net financial flows, IBRD (NFL, current US$),DT_NFL_MIBR_CD
Net financial flows, IDA (NFL, current US$),DT_NFL_MIDA_CD
Net financial flows, IMF concessional (NFL, current US$),DT_NFL_IMFC_CD
Net financial flows, IMF nonconcessional (NFL, current US$),DT_NFL_IMFN_CD
Net financial flows, multilateral (NFL, current US$),DT_NFL_MLAT_CD
Net financial flows, others (NFL, current US$),DT_NFL_MOTH_CD
Net financial flows, RDB concessional (NFL, current US$),DT_NFL_RDBC_CD
Net financial flows, RDB nonconcessional (NFL, current US$),DT_NFL_RDBN_CD
Net foreign assets (current LCU),FM_AST_NFRG_CN
Net income (BoP, current US$),BN_GSR_FCTY_CD
Net income from abroad (constant LCU),NY_GSR_NFCY_KN
Net income from abroad (current LCU),NY_GSR_NFCY_CN
Net income from abroad (current US$),NY_GSR_NFCY_CD
Net incurrence of liabilities, domestic (% of GDP),GC_FIN_DOMS_GD_ZS
Net incurrence of liabilities, domestic (current LCU),GC_FIN_DOMS_CN
Net incurrence of liabilities, foreign (% of GDP),GC_FIN_FRGN_GD_ZS
Net incurrence of liabilities, foreign (current LCU),GC_FIN_FRGN_CN
Net intake rate in grade 1 (% of official school-age population),SE_PRM_NINT_ZS
Net intake rate in grade 1, female (% of official school-age population),SE_PRM_NINT_FE_ZS
Net intake rate in grade 1, male (% of official school-age population),SE_PRM_NINT_MA_ZS
Net migration,SM_POP_NETM
Net ODA received (% of central government expense),DT_ODA_ODAT_XP_ZS
Net ODA received (% of GNI),DT_ODA_ODAT_GN_ZS
Net ODA received (% of gross capital formation),DT_ODA_ODAT_GI_ZS
Net ODA received (% of imports of goods and services),DT_ODA_ODAT_MP_ZS
Net ODA received per capita (current US$),DT_ODA_ODAT_PC_ZS
Net official aid received (constant 2010 US$),DT_ODA_OATL_KD
Net official aid received (current US$),DT_ODA_OATL_CD
Net official development assistance and official aid received (constant 2010 US$),DT_ODA_ALLD_KD
Net official development assistance and official aid received (current US$),DT_ODA_ALLD_CD
Net official development assistance received (constant 2010 US$),DT_ODA_ODAT_KD
Net official development assistance received (current US$),DT_ODA_ODAT_CD
Net official flows from UN agencies, IAEA (current US$),DT_NFL_IAEA_CD
Net official flows from UN agencies, IFAD (current US$),DT_NFL_IFAD_CD
Net official flows from UN agencies, UNAIDS (current US$),DT_NFL_UNAI_CD
Net official flows from UN agencies, UNDP (current US$),DT_NFL_UNDP_CD
Net official flows from UN agencies, UNECE (current US$),DT_NFL_UNEC_CD
Net official flows from UN agencies, UNFPA (current US$),DT_NFL_UNFP_CD
Net official flows from UN agencies, UNHCR (current US$),DT_NFL_UNCR_CD
Net official flows from UN agencies, UNICEF (current US$),DT_NFL_UNCF_CD
Net official flows from UN agencies, UNPBF (current US$),DT_NFL_UNPB_CD
Net official flows from UN agencies, UNRWA (current US$),DT_NFL_UNRW_CD
Net official flows from UN agencies, UNTA (current US$),DT_NFL_UNTA_CD
Net official flows from UN agencies, WFP (current US$),DT_NFL_WFPG_CD
Net official flows from UN agencies, WHO (current US$),DT_NFL_WHOL_CD
Net taxes on products (constant LCU),NY_TAX_NIND_KN
Net taxes on products (current LCU),NY_TAX_NIND_CN
Net taxes on products (current US$),NY_TAX_NIND_CD
Net trade in goods (BoP, current US$),BN_GSR_MRCH_CD
Net trade in goods and services (BoP, current US$),BN_GSR_GNFS_CD
New business density (new registrations per 1,000 people ages 15-64),IC_BUS_NDNS_ZS
New businesses registered (number),IC_BUS_NREG
Newborns protected against tetanus (%),SH_VAC_TTNS_ZS
Nitrous oxide emissions (thousand metric tons of CO2 equivalent),EN_ATM_NOXE_KT_CE
Nitrous oxide emissions in energy sector (thousand metric tons of CO2 equivalent),EN_ATM_NOXE_EG_KT_CE
Nitrous oxide emissions in industrial and energy processes (% of total nitrous oxide emissions),EN_ATM_NOXE_EI_ZS
Notified cases of malaria (per 100,000 people),SH_MLR_INCD
Number of maternal deaths,SH_MMR_DTHS
Nurses and midwives (per 1,000 people),SH_MED_NUMW_P3
Official exchange rate (LCU per US$, period average),PA_NUS_FCRF
Oil rents (% of GDP),NY_GDP_PETR_RT_ZS
Ores and metals exports (% of merchandise exports),TX_VAL_MMTL_ZS_UN
Ores and metals imports (% of merchandise imports),TM_VAL_MMTL_ZS_UN
Organic water pollutant (BOD) emissions (kg per day per worker),EE_BOD_WRKR_KG
Organic water pollutant (BOD) emissions (kg per day),EE_BOD_TOTL_KG
Other expense (% of expense),GC_XPN_OTHR_ZS
Other expense (current LCU),GC_XPN_OTHR_CN
Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent),EN_ATM_GHGO_KT_CE
Other manufacturing (% of value added in manufacturing),NV_MNF_OTHR_ZS_UN
Other taxes (% of revenue),GC_TAX_OTHR_RV_ZS
Other taxes (current LCU),GC_TAX_OTHR_CN
Other taxes payable by businesses (% of commercial profits),IC_TAX_OTHR_CP_ZS
Out-of-pocket health expenditure (% of private expenditure on health),SH_XPD_OOPC_ZS
Out-of-pocket health expenditure (% of total expenditure on health),SH_XPD_OOPC_TO_ZS
Outpatient visits per capita ,SH_VST_OUTP
Part time employment, female (% of total female employment),SL_TLF_PART_FE_ZS
Part time employment, female (% of total part time employment),SL_TLF_PART_TL_FE_ZS
Part time employment, male (% of total male employment),SL_TLF_PART_MA_ZS
Part time employment, total (% of total employment),SL_TLF_PART_ZS
Passenger cars (per 1,000 people),IS_VEH_PCAR_P3
Patent applications, nonresidents,IP_PAT_NRES
Patent applications, residents,IP_PAT_RESD
Permanent cropland (% of land area),AG_LND_CROP_ZS
Persistence to grade 5, female (% of cohort),SE_PRM_PRS5_FE_ZS
Persistence to grade 5, male (% of cohort),SE_PRM_PRS5_MA_ZS
Persistence to grade 5, total (% of cohort),SE_PRM_PRS5_ZS
Persistence to last grade of primary, female (% of cohort),SE_PRM_PRSL_FE_ZS
Persistence to last grade of primary, male (% of cohort),SE_PRM_PRSL_MA_ZS
Persistence to last grade of primary, total (% of cohort),SE_PRM_PRSL_ZS
PFC gas emissions (thousand metric tons of CO2 equivalent),EN_ATM_PFCG_KT_CE
Physicians (per 1,000 people),SH_MED_PHYS_ZS
Plant species (higher), threatened,EN_HPT_THRD_NO
PM10, country level (micrograms per cubic meter),EN_ATM_PM10_MC_M3
Point-of-sale terminals (per 100,000 adults),FB_POS_TOTL_P5
Population ages 0-14 (% of total),SP_POP_0014_TO_ZS
Population ages 15-64 (% of total),SP_POP_1564_TO_ZS
Population ages 65 and above (% of total),SP_POP_65UP_TO_ZS
Population density (people per sq. km of land area),EN_POP_DNST
Population growth (annual %),SP_POP_GROW
Population in largest city,EN_URB_LCTY
Population in the largest city (% of urban population),EN_URB_LCTY_UR_ZS
Population in urban agglomerations of more than 1 million,EN_URB_MCTY
Population in urban agglomerations of more than 1 million (% of total population),EN_URB_MCTY_TL_ZS
Population living in areas where elevation is below 5 meters (% of total population),EN_POP_EL5M_ZS
Population, female (% of total),SP_POP_TOTL_FE_ZS
Population, total,SP_POP_TOTL
Portfolio equity, net inflows (BoP, current US$),BX_PEF_TOTL_CD_WD
Portfolio investment, bonds (PPG + PNG) (NFL, current US$),DT_NFL_BOND_CD
Portfolio investment, excluding LCFAR (BoP, current US$),BN_KLT_PTXL_CD
Poverty gap at $1.25 a day (PPP) (%),SI_POV_GAPS
Poverty gap at $2 a day (PPP) (%),SI_POV_GAP2
Poverty gap at national poverty line (%),SI_POV_NAGP
Poverty gap at rural poverty line (%),SI_POV_RUGP
Poverty gap at urban poverty line (%),SI_POV_URGP
Poverty headcount ratio at $1.25 a day (PPP) (% of population),SI_POV_DDAY
Poverty headcount ratio at $2 a day (PPP) (% of population),SI_POV_2DAY
Poverty headcount ratio at national poverty line (% of population),SI_POV_NAHC
Poverty headcount ratio at rural poverty line (% of rural population),SI_POV_RUHC
Poverty headcount ratio at urban poverty line (% of urban population),SI_POV_URHC
Power outages in firms in a typical month (number),IC_ELC_OUTG
PPP conversion factor (GDP) to market exchange rate ratio,PA_NUS_PPPC_RF
PPP conversion factor, GDP (LCU per international $),PA_NUS_PPP
PPP conversion factor, private consumption (LCU per international $),PA_NUS_PRVT_PP
Pregnant women receiving prenatal care (%),SH_STA_ANVC_ZS
Presence of peace keepers (number of troops, police, and military observers in mandate),VC_PKP_TOTL_UN
Present value of external debt (% of exports of goods, services and income),DT_DOD_PVLX_EX_ZS
Present value of external debt (% of GNI),DT_DOD_PVLX_GN_ZS
Present value of external debt (current US$),DT_DOD_PVLX_CD
Prevalence of anemia among pregnant women (%),SH_PRG_ANEM
Prevalence of HIV, female (% ages 15-24),SH_HIV_1524_FE_ZS
Prevalence of HIV, male (% ages 15-24),SH_HIV_1524_MA_ZS
Prevalence of HIV, total (% of population ages 15-49),SH_DYN_AIDS_ZS
Prevalence of overweight (% of children under 5),SH_STA_OWGH_ZS
Prevalence of undernourishment (% of population),SN_ITK_DEFC_ZS
Prevalence of wasting (% of children under 5),SH_STA_WAST_ZS
Primary completion rate, female (% of relevant age group),SE_PRM_CMPT_FE_ZS
Primary completion rate, male (% of relevant age group),SE_PRM_CMPT_MA_ZS
Primary completion rate, total (% of relevant age group),SE_PRM_CMPT_ZS
Primary education, duration (years),SE_PRM_DURS
Primary education, pupils,SE_PRM_ENRL
Primary education, pupils (% female),SE_PRM_ENRL_FE_ZS
Primary education, teachers,SE_PRM_TCHR
Primary education, teachers (% female),SE_PRM_TCHR_FE_ZS
Primary school starting age (years),SE_PRM_AGES
Private capital flows, total (% of GDP),BN_KLT_PRVT_GD_ZS
Private capital flows, total (BoP, current US$),BN_KLT_PRVT_CD
Private credit bureau coverage (% of adults),IC_CRD_PRVT_ZS
Private current transfers, payments (BoP, current US$),BM_TRF_PRVT_CD
Procedures to build a warehouse (number),IC_WRH_PROC
Procedures to enforce a contract (number),IC_LGL_PROC
Procedures to register property (number),IC_PRP_PROC
Profit tax (% of commercial profits),IC_TAX_PRFT_CP_ZS
Progression to secondary school (%),SE_SEC_PROG_ZS
Progression to secondary school, female (%),SE_SEC_PROG_FE_ZS
Progression to secondary school, male (%),SE_SEC_PROG_MA_ZS
Proportion of seats held by women in national parliaments (%),SG_GEN_PARL_ZS
Public and publicly guaranteed debt service (% of exports, excluding workers' remittances),DT_TDS_DPPG_XP_ZS
Public and publicly guaranteed debt service (% of GNI),DT_TDS_DPPG_GN_ZS
Public credit registry coverage (% of adults),IC_CRD_PUBL_ZS
Public spending on education, total (% of GDP),SE_XPD_TOTL_GD_ZS
Public spending on education, total (% of government expenditure),SE_XPD_TOTL_GB_ZS
Pump price for diesel fuel (US$ per liter),EP_PMP_DESL_CD
Pump price for gasoline (US$ per liter),EP_PMP_SGAS_CD
Pupil-teacher ratio, primary,SE_PRM_ENRL_TC_ZS
Pupil-teacher ratio, secondary,SE_SEC_ENRL_TC_ZS
Quality of port infrastructure, WEF (1=extremely underdeveloped to 7=well developed and efficient by international standards),IQ_WEF_PORT_XQ
Quasi money (current LCU),FM_LBL_QMNY_CN
Quasi-liquid liabilities (% of GDP),FS_LBL_QLIQ_GD_ZS
Rail lines (total route-km),IS_RRS_TOTL_KM
Railways, goods transported (million ton-km),IS_RRS_GOOD_MT_K6
Railways, passengers carried (million passenger-km),IS_RRS_PASG_KM
Ratio of female to male labor force participation rate (%),SL_TLF_CACT_FM_ZS
Ratio of female to male primary enrollment (%),SE_ENR_PRIM_FM_ZS
Ratio of female to male secondary enrollment (%),SE_ENR_SECO_FM_ZS
Ratio of female to male tertiary enrollment (%),SE_ENR_TERT_FM_ZS
Ratio of girls to boys in primary and secondary education (%),SE_ENR_PRSC_FM_ZS
Ratio of young literate females to males (% ages 15-24),SE_ADT_1524_LT_FM_ZS
Real effective exchange rate index (2005 = 100),PX_REX_REER
Real interest rate (%),FR_INR_RINR
Refugee population by country or territory of asylum,SM_POP_REFG
Refugee population by country or territory of origin,SM_POP_REFG_OR
Renewable internal freshwater resources per capita (cubic meters),ER_H2O_INTR_PC
Renewable internal freshwater resources, total (billion cubic meters),ER_H2O_INTR_K3
Repeaters, primary, female (% of female enrollment),SE_PRM_REPT_FE_ZS
Repeaters, primary, male (% of male enrollment),SE_PRM_REPT_MA_ZS
Repeaters, primary, total (% of total enrollment),SE_PRM_REPT_ZS
Repeaters, secondary, female (% of female enrollment),SE_SEC_REPT_FE_ZS
Repeaters, secondary, male (% of male enrollment),SE_SEC_REPT_MA_ZS
Repeaters, secondary, total (% of total enrollment),SE_SEC_REPT_ZS
Research and development expenditure (% of GDP),GB_XPD_RSDV_GD_ZS
Researchers in R&D (per million people),SP_POP_SCIE_RD_P6
Revenue, excluding grants (% of GDP),GC_REV_XGRT_GD_ZS
Revenue, excluding grants (current LCU),GC_REV_XGRT_CN
Risk premium on lending (prime rate minus treasury bill rate, %),FR_INR_RISK
Road density (km of road per 100 sq. km of land area),IS_ROD_DNST_K2
Road sector diesel fuel consumption (kt of oil equivalent),IS_ROD_DESL_KT
Road sector diesel fuel consumption per capita (kg of oil equivalent),IS_ROD_DESL_PC
Road sector energy consumption (% of total energy consumption),IS_ROD_ENGY_ZS
Road sector energy consumption (kt of oil equivalent),IS_ROD_ENGY_KT
Road sector energy consumption per capita (kg of oil equivalent),IS_ROD_ENGY_PC
Road sector gasoline fuel consumption (kt of oil equivalent),IS_ROD_SGAS_KT
Road sector gasoline fuel consumption per capita (kg of oil equivalent),IS_ROD_SGAS_PC
Roads, goods transported (million ton-km),IS_ROD_GOOD_MT_K6
Roads, passengers carried (million passenger-km),IS_ROD_PSGR_K6
Roads, paved (% of total roads),IS_ROD_PAVE_ZS
Roads, total network (km),IS_ROD_TOTL_KM
Royalty and license fees, payments (BoP, current US$),BM_GSR_ROYL_CD
Royalty and license fees, receipts (BoP, current US$),BX_GSR_ROYL_CD
Rural population,SP_RUR_TOTL
Rural population (% of total population),SP_RUR_TOTL_ZS
Rural population growth (annual %),SP_RUR_TOTL_ZG
S&P Global Equity Indices (annual % change),CM_MKT_INDX_ZG
School enrollment, preprimary (% gross),SE_PRE_ENRR
School enrollment, preprimary, female (% gross),SE_PRE_ENRR_FE
School enrollment, preprimary, male (% gross),SE_PRE_ENRR_MA
School enrollment, primary (% gross),SE_PRM_ENRR
School enrollment, primary (% net),SE_PRM_NENR
School enrollment, primary, female (% gross),SE_PRM_ENRR_FE
School enrollment, primary, female (% net),SE_PRM_NENR_FE
School enrollment, primary, male (% gross),SE_PRM_ENRR_MA
School enrollment, primary, male (% net),SE_PRM_NENR_MA
School enrollment, primary, private (% of total primary),SE_PRM_PRIV_ZS
School enrollment, secondary (% gross),SE_SEC_ENRR
School enrollment, secondary (% net),SE_SEC_NENR
School enrollment, secondary, female (% gross),SE_SEC_ENRR_FE
School enrollment, secondary, female (% net),SE_SEC_NENR_FE
School enrollment, secondary, male (% gross),SE_SEC_ENRR_MA
School enrollment, secondary, male (% net),SE_SEC_NENR_MA
School enrollment, secondary, private (% of total secondary),SE_SEC_PRIV_ZS
School enrollment, tertiary (% gross),SE_TER_ENRR
School enrollment, tertiary, female (% gross),SE_TER_ENRR_FE
School enrollment, tertiary, male (% gross),SE_TER_ENRR_MA
Scientific and technical journal articles,IP_JRN_ARTC_SC
Secondary education, duration (years),SE_SEC_DURS
Secondary education, general pupils,SE_SEC_ENRL_GC
Secondary education, general pupils (% female),SE_SEC_ENRL_GC_FE_ZS
Secondary education, pupils,SE_SEC_ENRL
Secondary education, pupils (% female),SE_SEC_ENRL_FE_ZS
Secondary education, teachers,SE_SEC_TCHR
Secondary education, teachers (% female),SE_SEC_TCHR_FE_ZS
Secondary education, teachers, female,SE_SEC_TCHR_FE
Secondary education, vocational pupils,SE_SEC_ENRL_VO
Secondary education, vocational pupils (% female),SE_SEC_ENRL_VO_FE_ZS
Secondary school starting age (years),SE_SEC_AGES
Secure Internet servers,IT_NET_SECR
Secure Internet servers (per 1 million people),IT_NET_SECR_P6
Self-employed, female (% of females employed),SL_EMP_SELF_FE_ZS
Self-employed, male (% of males employed),SL_EMP_SELF_MA_ZS
Self-employed, total (% of total employed),SL_EMP_SELF_ZS
Service exports (BoP, current US$),BX_GSR_NFSV_CD
Service imports (BoP, current US$),BM_GSR_NFSV_CD
Services, etc., value added (% of GDP),NV_SRV_TETC_ZS
Services, etc., value added (annual % growth),NV_SRV_TETC_KD_ZG
Services, etc., value added (constant 2000 US$),NV_SRV_TETC_KD
Services, etc., value added (constant LCU),NV_SRV_TETC_KN
Services, etc., value added (current LCU),NV_SRV_TETC_CN
Services, etc., value added (current US$),NV_SRV_TETC_CD
SF6 gas emissions (thousand metric tons of CO2 equivalent),EN_ATM_SF6G_KT_CE
Share of tariff lines with international peaks, all products (%),TM_TAX_MRCH_IP_ZS
Share of tariff lines with international peaks, manufactured products (%),TM_TAX_MANF_IP_ZS
Share of tariff lines with international peaks, primary products (%),TM_TAX_TCOM_IP_ZS
Share of tariff lines with specific rates, all products (%),TM_TAX_MRCH_SR_ZS
Share of tariff lines with specific rates, manufactured products (%),TM_TAX_MANF_SR_ZS
Share of tariff lines with specific rates, primary products (%),TM_TAX_TCOM_SR_ZS
Share of women employed in the nonagricultural sector (% of total nonagricultural employment),SL_EMP_INSV_FE_ZS
Short-term debt (% of exports of goods, services and income),DT_DOD_DSTC_XP_ZS
Short-term debt (% of total external debt),DT_DOD_DSTC_ZS
Short-term debt (% of total reserves),DT_DOD_DSTC_IR_ZS
Smoking prevalence, females (% of adults),SH_PRV_SMOK_FE
Smoking prevalence, males (% of adults),SH_PRV_SMOK_MA
Social contributions (% of revenue),GC_REV_SOCL_ZS
Social contributions (current LCU),GC_REV_SOCL_CN
Start-up procedures to register a business (number),IC_REG_PROC
Stocks traded, total value (% of GDP),CM_MKT_TRAD_GD_ZS
Stocks traded, total value (current US$),CM_MKT_TRAD_CD
Stocks traded, turnover ratio (%),CM_MKT_TRNR
Strength of legal rights index (0=weak to 10=strong),IC_LGL_CRED_XQ
Subsidies and other transfers (% of expense),GC_XPN_TRFT_ZS
Subsidies and other transfers (current LCU),GC_XPN_TRFT_CN
Surface area (sq. km),AG_SRF_TOTL_K2
Survival to age 65, female (% of cohort),SP_DYN_TO65_FE_ZS
Survival to age 65, male (% of cohort),SP_DYN_TO65_MA_ZS
Tariff rate, applied, simple mean, all products (%),TM_TAX_MRCH_SM_AR_ZS
Tariff rate, applied, simple mean, manufactured products (%),TM_TAX_MANF_SM_AR_ZS
Tariff rate, applied, simple mean, primary products (%),TM_TAX_TCOM_SM_AR_ZS
Tariff rate, applied, weighted mean, all products (%),TM_TAX_MRCH_WM_AR_ZS
Tariff rate, applied, weighted mean, manufactured products (%),TM_TAX_MANF_WM_AR_ZS
Tariff rate, applied, weighted mean, primary products (%),TM_TAX_TCOM_WM_AR_ZS
Tariff rate, most favored nation, simple mean, all products (%),TM_TAX_MRCH_SM_FN_ZS
Tariff rate, most favored nation, simple mean, manufactured products (%),TM_TAX_MANF_SM_FN_ZS
Tariff rate, most favored nation, simple mean, primary products (%),TM_TAX_TCOM_SM_FN_ZS
Tariff rate, most favored nation, weighted mean, all products (%),TM_TAX_MRCH_WM_FN_ZS
Tariff rate, most favored nation, weighted mean, manufactured products (%),TM_TAX_MANF_WM_FN_ZS
Tariff rate, most favored nation, weighted mean, primary products (%),TM_TAX_TCOM_WM_FN_ZS
Tax payments (number),IC_TAX_PAYM
Tax revenue (% of GDP),GC_TAX_TOTL_GD_ZS
Tax revenue (current LCU),GC_TAX_TOTL_CN
Taxes on exports (% of tax revenue),GC_TAX_EXPT_ZS
Taxes on exports (current LCU),GC_TAX_EXPT_CN
Taxes on goods and services (% of revenue),GC_TAX_GSRV_RV_ZS
Taxes on goods and services (% value added of industry and services),GC_TAX_GSRV_VA_ZS
Taxes on goods and services (current LCU),GC_TAX_GSRV_CN
Taxes on income, profits and capital gains (% of revenue),GC_TAX_YPKG_RV_ZS
Taxes on income, profits and capital gains (% of total taxes),GC_TAX_YPKG_ZS
Taxes on income, profits and capital gains (current LCU),GC_TAX_YPKG_CN
Taxes on international trade (% of revenue),GC_TAX_INTT_RV_ZS
Taxes on international trade (current LCU),GC_TAX_INTT_CN
Technical cooperation grants (BoP, current US$),BX_GRT_TECH_CD_WD
Technicians in R&D (per million people),SP_POP_TECH_RD_P6
Teenage mothers (% of women ages 15-19 who have had children or are currently pregnant),SP_MTR_1519_ZS
Telephone lines,IT_MLT_MAIN
Telephone lines (per 100 people),IT_MLT_MAIN_P2
Terms of trade adjustment (constant LCU),NY_TTF_GNFS_KN
Terrestrial and marine protected areas (% of total territorial area),ER_PTD_TOTL_ZS
Terrestrial protected areas (% of total land area),ER_LND_PTLD_ZS
Tertiary education, teachers (% female),SE_TER_TCHR_FE_ZS
Textiles and clothing (% of value added in manufacturing),NV_MNF_TXTL_ZS_UN
Time required to build a warehouse (days),IC_WRH_DURS
Time required to enforce a contract (days),IC_LGL_DURS
Time required to get electricity (days),IC_ELC_TIME
Time required to obtain an operating license (days),IC_FRM_DURS
Time required to register property (days),IC_PRP_DURS
Time required to start a business (days),IC_REG_DURS
Time to export (days),IC_EXP_DURS
Time to import (days),IC_IMP_DURS
Time to prepare and pay taxes (hours),IC_TAX_DURS
Time to resolve insolvency (years),IC_ISV_DURS
Total debt service (% of exports of goods, services and income),DT_TDS_DECT_EX_ZS
Total debt service (% of GNI),DT_TDS_DECT_GN_ZS
Total enrollment, primary (% net),SE_PRM_TENR
Total enrollment, primary, female (% net),SE_PRM_TENR_FE
Total enrollment, primary, male (% net),SE_PRM_TENR_MA
Total natural resources rents (% of GDP),NY_GDP_TOTL_RT_ZS
Total reserves (% of total external debt),FI_RES_TOTL_DT_ZS
Total reserves (includes gold, current US$),FI_RES_TOTL_CD
Total reserves in months of imports,FI_RES_TOTL_MO
Total reserves minus gold (current US$),FI_RES_XGLD_CD
Total tax rate (% of commercial profits),IC_TAX_TOTL_CP_ZS
Trade (% of GDP),NE_TRD_GNFS_ZS
Trade in services (% of GDP),BG_GSR_NFSV_GD_ZS
Trademark applications, aggregate direct,IP_TMK_AGGD
Trademark applications, direct nonresident,IP_TMK_NRES
Trademark applications, direct resident,IP_TMK_RESD
Trademark applications, Madrid,IP_TMK_MDRD
Trademark applications, total,IP_TMK_TOTL
Trained teachers in primary education (% of total teachers),SE_PRM_TCAQ_ZS
Trained teachers in primary education, female (% of female teachers),SE_PRM_TCAQ_FE_ZS
Trained teachers in primary education, male (% of male teachers),SE_PRM_TCAQ_MA_ZS
Transport services (% of commercial service exports),TX_VAL_TRAN_ZS_WT
Transport services (% of commercial service imports),TM_VAL_TRAN_ZS_WT
Transport services (% of service exports, BoP),BX_GSR_TRAN_ZS
Transport services (% of service imports, BoP),BM_GSR_TRAN_ZS
Travel services (% of commercial service exports),TX_VAL_TRVL_ZS_WT
Travel services (% of commercial service imports),TM_VAL_TRVL_ZS_WT
Travel services (% of service exports, BoP),BX_GSR_TRVL_ZS
Travel services (% of service imports, BoP),BM_GSR_TRVL_ZS
Tuberculosis case detection rate (%, all forms),SH_TBS_DTEC_ZS
Tuberculosis treatment success rate (% of registered cases),SH_TBS_CURE_ZS
Unemployment with primary education (% of total unemployment),SL_UEM_PRIM_ZS
Unemployment with primary education, female (% of female unemployment),SL_UEM_PRIM_FE_ZS
Unemployment with primary education, male (% of male unemployment),SL_UEM_PRIM_MA_ZS
Unemployment with secondary education (% of total unemployment),SL_UEM_SECO_ZS
Unemployment with secondary education, female (% of female unemployment),SL_UEM_SECO_FE_ZS
Unemployment with secondary education, male (% of male unemployment),SL_UEM_SECO_MA_ZS
Unemployment with tertiary education (% of total unemployment),SL_UEM_TERT_ZS
Unemployment with tertiary education, female (% of female unemployment),SL_UEM_TERT_FE_ZS
Unemployment with tertiary education, male (% of male unemployment),SL_UEM_TERT_MA_ZS
Unemployment, female (% of female labor force),SL_UEM_TOTL_FE_ZS
Unemployment, male (% of male labor force),SL_UEM_TOTL_MA_ZS
Unemployment, total (% of total labor force),SL_UEM_TOTL_ZS
Unemployment, youth female (% of female labor force ages 15-24),SL_UEM_1524_FE_ZS
Unemployment, youth male (% of male labor force ages 15-24),SL_UEM_1524_MA_ZS
Unemployment, youth total (% of total labor force ages 15-24),SL_UEM_1524_ZS
Unmet need for contraception (% of married women ages 15-49),SP_UWT_TFRT
Urban population,SP_URB_TOTL
Urban population (% of total),SP_URB_TOTL_IN_ZS
Urban population growth (annual %),SP_URB_GROW
Use of IMF credit (DOD, current US$),DT_DOD_DIMF_CD
Use of insecticide-treated bed nets (% of under-5 population),SH_MLR_NETS_ZS
Value lost due to electrical outages (% of sales),IC_FRM_OUTG_ZS
Vehicles (per km of road),IS_VEH_ROAD_K1
Vitamin A supplementation coverage rate (% of children ages 6-59 months),SN_ITK_VITA_ZS
Vulnerable employment, female (% of female employment),SL_EMP_VULN_FE_ZS
Vulnerable employment, male (% of male employment),SL_EMP_VULN_MA_ZS
Vulnerable employment, total (% of total employment),SL_EMP_VULN_ZS
Wage and salaried workers, female (% of females employed),SL_EMP_WORK_FE_ZS
Wage and salaried workers, total (% of total employed),SL_EMP_WORK_ZS
Wage and salary workers, male (% of males employed),SL_EMP_WORK_MA_ZS
Wanted fertility rate (births per woman),SP_DYN_WFRT
Water pollution, chemical industry (% of total BOD emissions),EE_BOD_CHEM_ZS
Water pollution, clay and glass industry (% of total BOD emissions),EE_BOD_CGLS_ZS
Water pollution, food industry (% of total BOD emissions),EE_BOD_FOOD_ZS
Water pollution, metal industry (% of total BOD emissions),EE_BOD_MTAL_ZS
Water pollution, other industry (% of total BOD emissions),EE_BOD_OTHR_ZS
Water pollution, paper and pulp industry (% of total BOD emissions),EE_BOD_PAPR_ZS
Water pollution, textile industry (% of total BOD emissions),EE_BOD_TXTL_ZS
Water pollution, wood industry (% of total BOD emissions),EE_BOD_WOOD_ZS
Water productivity, total (constant 2000 US$ GDP per cubic meter of total freshwater withdrawal),ER_GDP_FWTL_M3_KD
Wholesale price index (2005 = 100),FP_WPI_TOTL
Women's share of population ages 15+ living with HIV (%),SH_DYN_AIDS_FE_ZS
Workers' remittances and compensation of employees, paid (current US$),BM_TRF_PWKR_CD_DT
Workers' remittances and compensation of employees, received (% of GDP),BX_TRF_PWKR_DT_GD_ZS
Workers' remittances and compensation of employees, received (current US$),BX_TRF_PWKR_CD_DT
Workers' remittances, receipts (BoP, current US$),BX_TRF_PWKR_CD"""


# In[15]:

with open('indicators.csv','w') as f:
    f.write(indic)


# In[16]:



# In[ ]:




# In[ ]:



