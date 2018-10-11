# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo

HOST = 'localhost'
USER = 'liyuhuang'
PASSWORD = '123456'
CHARSET = 'utf8'
DB_DEV = 'db_dev'
DB_ENGINE = 'InnoDB'

TB_FUNDAMENTAL_BASIC_INFO = 'tb_fundamental_basic_info'
TB_FUNDAMENTAL_REPORT = 'tb_fundamental_report'
TB_FUNDAMENTAL_PROFIT = 'tb_fundamental_profit'
TB_FUNDAMENTAL_OPERATION = 'tb_fundamental_operation'
TB_FUNDAMENTAL_GROWTH = 'tb_fundamental_growth'
TB_FUNDAMENTAL_DEBT = 'tb_fundamental_debt'
TB_FUNDAMENTAL_CASH_FLOW = 'tb_fundamental_cash_flow'

TB_TRADE_HISTORY_SECURITY = 'tb_trade_history_security__%s'
TB_TRADE_HISTORY_INDEX = 'tb_trade_history_index_%s'
TB_TRADE_TICK = 'tb_trade_tick_%s'
TB_TRADE_BIG_DEAL = 'tb_trade_big_deal_%s'

TB_CLASSIFY_INDUSTRY = 'tb_classify_industry'
TB_CLASSIFY_CONCEPT = 'tb_classify_concept'
TB_CLASSIFY_AREA = 'tb_classify_area'
TB_CLASSIFY_SME = 'tb_classify_sme'
TB_CLASSIFY_GEM = 'tb_classify_gem'
TB_CLASSIFY_ST = 'tb_classify_st'
TB_CLASSIFY_HS300 = 'tb_classify_hs300'
TB_CLASSIFY_SZ50 = 'tb_classify_sz50'
TB_CLASSIFY_ZZ500 = 'tb_classify_zz500'
TB_CLASSIFY_TERMINATED = 'tb_classify_terminated'
TB_CLASSIFY_SUSPENDED = 'tb_classify_suspended'

TB_MACRO_DEPOSIT_RATE = 'tb_macro_deposit_rate'
TB_MACRO_LOAN_RATE = 'tb_macro_loan_rate'
TB_MACRO_RRR = 'tb_macro_rrr'
TB_MACRO_MONEY_SUPPLY = 'tb_macro_money_supply'
TB_MACRO_MONEY_SUPPLY_BAL = 'tb_macro_money_supply_bal'
TB_MACRO_GDP = 'tb_macro_gdp'
TB_MACRO_GDP_QUARTER = 'tb_macro_gdp_quarter'
TB_MACRO_GDP_FOR = 'tb_macro_gdp_for'
TB_MACRO_GDP_PULL = 'tb_macro_gdp_pull'
TB_MACRO_GDP_CONTRIBUTION = 'tb_macro_gdp_contribution'
TB_MACRO_CPI = 'tb_macro_cpi'
TB_MACRO_PPI = 'tb_macro_ppi'

TB_REFERENCE_DIVIDE = 'tb_reference_divide'
TB_REFERENCE_FORECAST = 'tb_reference_forecast'
TB_REFERENCE_RESTRICTED_SHARE = 'tb_reference_restricted_share'
TB_REFERENCE_FUND_HOLDING = 'tb_reference_fund_holding'
TB_REFERENCE_NEW_SECURITY = 'tb_reference_new_security'
TB_REFERENCE_TRADE_MARGIN_SH = 'tb_reference_trade_margin_sh'
TB_REFERENCE_TRADE_MARGIN_DETAIL_SH = 'tb_reference_trade_margin_detail_sh'
TB_REFERENCE_TRADE_MARGIN_SZ = 'tb_reference_trade_margin_sz'
TB_REFERENCE_TRADE_MARGIN_DETAIL_SZ = 'tb_reference_trade_margin_detail_sz'

TB_SHIBOR = 'tb_shibor'
TB_SHIBOR_QUOTE = 'tb_shibor_quote'
TB_SHIBOR_MA = 'tb_shibor_ma'
TB_SHIBOR_LPR = 'tb_shibor_lpr'
TB_SHIBOR_LPR_MA = 'tb_shibor_lpr_ma'

TB_RANK_TOP = 'tb_rank_top'
TB_RANK_STATIC = 'tb_rank_static'
TB_RANK_BROKER_STATIC = 'tb_rank_broker_static'
TB_RANK_INSTITUTION_STATIC = 'tb_rank_institution_static'
TB_RANK_INSTITUTION_TRADE_DETAIL = 'tb_rank_institution_trade_detail'

TB_SOCIAL_NEWS = 'tb_social_news'
TB_SOCIAL_NOTICE = 'tb_social_notice'
TB_SOCIAL_SINA_GUBA = 'tb_social_sina_guba'


sql_create_tb_fundamental_basic_info = '''
DROP TABLE IF EXISTS tb_fundamental_basic_info;
CREATE TABLE tb_fundamental_basic_info (
    c_code VARCHAR(10) PRIMARY KEY NOT NULL COMMENT 'Security code 代码',
    c_name VARCHAR(20) NOT NULL COMMENT 'Security name 名称',
    c_industry VARCHAR(40) COMMENT 'Security industry 领域',
    c_area VARCHAR(20) COMMENT 'Security area 区域',
    c_pe DOUBLE COMMENT 'Security PE 市盈率',
    c_circulating_cap DOUBLE COMMENT 'Security circulating capitalization, (100 million RMB Yuan) 流通股本',
    c_total_cap DOUBLE COMMENT 'Security total capitalization (100 million RMB Yuan) 总股本',
    c_total_assets DOUBLE COMMENT 'Security total assets (10 thousand RMB Yuan) 总资产',
    c_liquid_assets DOUBLE COMMENT 'Security liquid assets (10 thousand RMB Yuan) 流动资产',
    c_fixed_assets DOUBLE  COMMENT 'Security fixed assets (10 thousand RMB Yuan) 固定资产',
    c_reserved DOUBLE COMMENT 'Security reserved fund (10 thousand RMB Yuan) 公积金',
    c_rps DOUBLE COMMENT 'Security reserved fund per share (RMB Yuan) 每股公积金',
    c_eps VARCHAR(20) COMMENT 'Security Earning Per Share (RMB Yuan) 每股收益',
    c_bvps DOUBLE COMMENT 'Security Book Value Per Share (RMB Yuan) 每股净资产',
    c_pb DOUBLE  COMMENT 'Security Price To Book Ratio 市净率',
    c_ipo_date BIGINT COMMENT 'Security IPO date 上市日期',
    c_up DOUBLE COMMENT 'Security undistributed profit 未分配利润',
    c_upps DOUBLE COMMENT 'Security undistributed profit per share(RMB Yuan) 每股未分配利润',
    c_revenue_yoy DOUBLE COMMENT 'Security revenue increase rate YOY 收入同比',
    c_profit_yoy DOUBLE COMMENT 'Security profit increase rate YOY 利润同比',
    c_gpr DOUBLE COMMENT 'Security gross profit rate 毛利率',
    c_npr DOUBLE COMMENT 'Security net profit rate 净利润率',
    c_shareholders BIGINT COMMENT 'Number of shareholders 股东人数'
)
ENGINE=InnoDB DEFAULT CHARSET=utf8
COMMENT = 'Basic info of all securities';
'''

sql_update_tb_fundamental_basic_info = '''
INSERT INTO tb_fundamental_basic_info (
    c_code, c_name, c_industry, c_area, c_pe, c_circulating_cap, c_total_cap, c_total_assets,
    c_liquid_assets, c_fixed_assets, c_reserved, c_rps, c_eps, c_bvps, c_pb, c_ipo_date,
    c_up, c_upps, c_revenue_yoy, c_profit_yoy, c_gpr, c_npr, c_shareholders
)
VALUES (
    '%s', '%s', '%s', '%s', %lf, %lf, %lf, %lf,
    %lf, %lf, %lf, %lf, '%s', %lf, %lf, %d,
    %lf, %lf, %lf, %lf, %lf, %lf, %d
)'''


sql_create_tb_fundamental_report = '''
DROP TABLE IF EXISTS tb_fundamental_report;
CREATE TABLE tb_fundamental_report (
    c_report_quarter VARCHAR(10) NOT NULL COMMENT 'Security report quarter 报告季度',
    c_code VARCHAR(10) NOT NULL COMMENT 'Security code 代码',
    c_name VARCHAR(20) NOT NULL COMMENT 'Security name 名称',
    c_eps DOUBLE COMMENT 'Security Earn Per Share 每股收益',
    c_eps_yoy DOUBLE COMMENT 'Security Earn Per Share YOY 每股收益同比（%）',
    c_bvps DOUBLE COMMENT 'Security Book Value Per Share (RMB Yuan) 每股净资产',
    c_roe DOUBLE COMMENT 'Security Rate of Return on Common Stockholders’ Equity 净资产收益率（%）',
    c_cfps DOUBLE COMMENT 'Security Cash Flow Per Share 每股现金流',
    c_np DOUBLE  COMMENT 'Security Net Profit (RMB Yuan) 净利润（万元）',
    c_profit_yoy DOUBLE  COMMENT 'Security Net Profit YOY 净利润同比（%）',
    c_distribute VARCHAR(40) COMMENT 'Security distribute 分配方案',
    c_publish_date VARCHAR(10) COMMENT 'Security report date 报告发布日期'
)
ENGINE=InnoDB DEFAULT CHARSET=utf8
COMMENT = 'Report info of all securities';
'''
# ALTER TABLE tb_fundamental_report ADD CONSTRAINT pk_name PRIMARY KEY(c_report_quarter, c_code)


sql_update_tb_fundamental_report = '''
INSERT INTO tb_fundamental_report (
    c_report_quarter, c_code, c_name, c_eps, c_eps_yoy, c_bvps, c_roe,
    c_cfps, c_np, c_profit_yoy, c_distribute, c_publish_date
)
VALUES (
    '%s', '%s', '%s', %lf, %lf, %lf, %lf,
    %lf, %lf, %lf, '%s' ,'%s'
)'''



