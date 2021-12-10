create table chapter1
(
    id int unsigned not null primary key,
    xinxichenshuzhe varchar(100),
    yuhuanzheguanxi varchar(100),
    xinxikekaochengdu varchar(100),
    xingming varchar(100),
    xingbie int,
    chushengriqi date,
    nianling varchar(100),
    minzu int,
    shenfenzhenghao varchar(100),
    xuexing int,
    jiatingzhuzhi varchar(100),
    gudingdianhua varchar(100),
    shouji1 varchar(100),
    shouji2 varchar(100),
    zhiye int,
    jiaoyuchengdu int,
    feiyongleibie int,
    jiazushi varchar(100)
) character set = utf8;

create table suifang
(
    id int unsigned not null auto_increment primary key, -- 表示一条随访记录
    name varchar(100) not null,
    id_number varchar(100) not null,
    sequence int not null, -- 第几次随访
    time_stamp TIMESTAMP
)character set = utf8;

create table usr
(
    user_id varchar(100) not null primary key, -- 表示一条随访记录
    user_name varchar(100) not null,
    user_phone varchar(100) not null unique,
    user_sex varchar(100),
    user_age int,
    user_height int,
    user_weight int,
    user_bmi float,
    user_group varchar(100),
    user_photo blob
)character set = utf8;