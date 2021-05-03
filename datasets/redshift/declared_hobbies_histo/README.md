# crm.sps_sport_practices_h

## Description

Declared sport history table.
A view is available to test the data : cds.sps_sport_practices_h

## Columns

| Name | Type | Nullable | Parents | Comment | Completeness* |
| ---- | ---- | -------- | ------- | ------- | ------------ |
| member_id | varchar(50) | false | crm.d_customers.member_id | customer unique id | 100 % |
| personne_id | varchar(50) | false | crm.d_customers.personne_id | "old" customer unique id | 100 % |
| id_sport | integer not null | true |  | "old sport id" (only available for testing, will be deleted.) | 100 % |
| sport_id_sdd | varchar(50) | false | ods.dds_sport_translation.sport_id_sdd | new sport id, go to ods.dds_sport_translation to get sport label | 100 % |
| sport_id_group_sdd | varchar(355) | false |  | new sport id group | 100 % |
| created_at | timestamp without time zone | false |  | time at which the declaration was made | 72 % |
| creation_app_id | varchar(50) | false | | the app used to create the declaration | 72 % |
| updated_at | timestamp without time zone | true |  | time at which the declaration was updated | 72,5 % |
| updated_app_id | varchar(50) | true |  | the app used to update the declaration | 72,5 % |
| start_date | timestamp | false |  | The earliest date the customer declared this sport | 100 % |
| end_date | timestamp | false |  | The date the customer unchecked this sport | 100 % |
| status | numeric(1) | false |  | =1 if the member is active in this sport, =0 if he is not active anymore | 100 % |
| flag_origin | char(3) | false |  | Allow you to know if the data comes from the old referential (MYD) or from the new declared sport module (SPP) | 100 % |
| rs_technical_date | timestamp without time zone | false | | time at which this refresh was updated in our cool table | 100 % |
| rs_technical_flow | varchar(50) | false |  | technical information about the user who updated the table | 100 % |

*Completeness : Percentage of non-null (and non-empty) values

## DistKey : member_id 

## SortKey : start_date, end_date

## Relations

| Table | Column | info |
| ---- | ---- | ---------- |
| cds.d_customers | member_id | informations about our customers |
| ods.dds_sport_translation | sport_id_sdd | Use a filter like "t.locale = 'en'" to find the proper translation |

## S3 Infos

**Prod**  
Bucket : discovery-crm  
Path : crm/sps_sport_practices_h/  
Format : Parquet  
Partition key : sport_id_group_sdd

**PreProd**  
Bucket : preprod-discovery-crm  
Path : crm/sps_sport_practices_h/  
Format : Parquet  
Partition key : sport_id_group_sdd

You will have to ask the rights to access this bucket/path using discovery offering.

## General Documentation

Wiki DKT : https://wiki.decathlon.net/display/DATA/Sport+Practices 


