create table chapter1
(
    id                int unsigned not null primary key,
    xinxichenshuzhe   varchar(100),
    yuhuanzheguanxi   varchar(100),
    xinxikekaochengdu varchar(100),
    xingming          varchar(100),
    xingbie           int,
    chushengriqi      date,
    nianling          varchar(100),
    minzu             int,
    shenfenzhenghao   varchar(100),
    xuexing           int,
    jiatingzhuzhi     varchar(100),
    gudingdianhua     varchar(100),
    shouji1           varchar(100),
    shouji2           varchar(100),
    zhiye             int,
    jiaoyuchengdu     int,
    feiyongleibie     int
) character set = utf8;

create table chapter2
(
    id                                   int unsigned not null primary key,
    tangniaobingbingshi                  varchar(100),
    danbainiao                           varchar(100),
    xuejiganshenggao                     varchar(100),
    hebingqitajibing                     varchar(100),
    guominshi                            varchar(100),
    jiazushi                             varchar(100),
    tangniaobingqitabingfazhengqingkuang varchar(100)
) character set = utf8;

create table chapter3
(
    id                      int unsigned not null primary key,
    yinshixiguanzhiqian     varchar(100),
    rizhishuliangzhiqian    varchar(100),
    yundongxiguanzhiqian    int,
    zhouyundongliangzhiqian varchar(100),
    yinshixiguanzuijin      varchar(100),
    rizhishuliangzuijin     varchar(100),
    yundongxiguanzuijin     int,
    zhouyundongliangzuijin  varchar(100),
    kaishixiyannianling     varchar(100),
    xiyanliang              varchar(100),
    jieyannianling          varchar(100),
    kaishiyinjiunianling    varchar(100),
    yinjiuliang             varchar(100),
    jiejiunianling          varchar(100)
) character set = utf8;

create table chapter5
(
    id                       int unsigned not null primary key,
    juandaifali              int,
    shaoqilanyan             int,
    yizihan                  int,
    touyunmuxuan             int,
    jingshaosedan            int,
    yangankouke              int,
    mujingganse              int,
    wuxinfanre               int,
    chaoredaohan             int,
    weihanzhileng            int,
    dabiantangxi             int,
    yeniaopinduo             int,
    yanhouzhongtong          int,
    xinxiongfanre            int,
    pifucuochuanghuojiezhong int,
    xiaobianhuangchi         int,
    parehanchu               int,
    kexilengyin              int,
    kouzhongchouhui          int,
    duoshiyiji               int,
    dabianganjie             int,
    kouganbuyuyin            int,
    kouganzhanni             int,
    dabianzhannibushuang     int,
    muchichiduo              int,
    kouku                    int,
    jizaoyinu                int,
    qingxuyiyu               int,
    xiongxiezhangmanxitaixi  int,
    shenzhongkunjuan         int,
    pifusaoyang              int,
    eryinshiyang             int,
    guanfupiman              int,
    shishaooue               int,
    dingweicitong，yejianjiazhong int,
    jifujiacuo               int,
    zhitimamu                int,
    yaojitengtong            int,
    chigaofatuo              int,
    ermingerlong             int
) character set = utf8;

create table chapter6
(
    id                       int unsigned not null primary key,
    miansecangbaihuoweihuang int,
    mianseliheihuohuian      int,
    mianhongchi              int,
    mianrumengyou            int,
    chunjiasedan             int,
    kouchunshezi，huozian、yuban、shexiamaizinuzhang int,
    mianzufuzhong            int,
    shexiang                 varchar(100),
    maixiang                 varchar(100),
    tiwen                    varchar(100),
    maibo                    varchar(100),
    huxi                     varchar(100),
    xueya                    varchar(100),
    tizhong                  varchar(100),
    shengao                  varchar(100),
    BMIzhi                   varchar(100),
    yaowei                   varchar(100)
) character set = utf8;

create table chapter7
(
    id                                   int unsigned not null primary key,
    xiehongdanbai                        varchar(100),
    hongxibaoxue                         varchar(100),
    hongxibaoyaji                        varchar(100),
    baixibaoxue                          varchar(100),
    xiexiaoban                           varchar(100),
    zhongxinglixibao                     varchar(100),
    niaodanbai                           varchar(100),
    guanxing                             varchar(100),
    hongxibaoniao                        varchar(100),
    baixibaoniao                         varchar(100),
    K                                    varchar(100),
    Ca2                                  varchar(100),
    P3                                   varchar(100),
    CO2CP                                varchar(100),
    GLU                                  varchar(100),
    BUN                                  varchar(100),
    Scr                                  varchar(100),
    UA                                   varchar(100),
    TP                                   varchar(100),
    Alb                                  varchar(100),
    ALT                                  varchar(100),
    AST                                  varchar(100),
    GammaGT                              varchar(100),
    ALP                                  varchar(100),
    TBIL                                 varchar(100),
    CHO                                  varchar(100),
    TG                                   varchar(100),
    LDL                                  varchar(100),
    INS                                  varchar(100),
    Ctai                                 varchar(100),
    eGFR                                 varchar(100),
    niaobaidanbaijihang                  varchar(100),
    xiaoshiniaoweiliangbaidanbaipaixielv varchar(100),
    xiaoshiniaodanbaidingliang           varchar(100),
    niaoliang                            varchar(100),
    yaowei                               varchar(100),
    tanghuaxuehongdanbai                 varchar(100),
    xindiantu                            varchar(100),
    chaoshengxindong                     varchar(100),
    zuoxinshishexuefenshu                varchar(100),
    jingdongmaiBchao                     varchar(100),
    jingneizhongmohouduzuo               varchar(100),
    jingneizhongmohouduyou               varchar(100),
    yandijiancha                         varchar(100),
    ectjiancha                           varchar(100),
    zhaopianlujing                       varchar(100)
) character set = utf8;

create table chapter8
(
    id                     int unsigned not null primary key,
    yinshixiguanzuijin     varchar(100),
    rizhishuliangzuijin    varchar(100),
    yundongxiguanzuijin    int,
    zhouyundongliangzuijin varchar(100)
) character set = utf8;

create table suifang
(
    id           int unsigned not null auto_increment primary key, -- 表示一条随访记录
    name         varchar(100) not null,
    id_number    varchar(100) not null,
    phone        varchar(100) not null,
    sequence     int          not null,                            -- 第几次随访
    tag          varchar(100) not null,
    time_stamp   TIMESTAMP,
    docter_name  varchar(100),
    docter_phone varchar(100)
)character set = utf8;

create table patient
(
    user_id     int not null auto_increment primary key,
    user_name   varchar(100),
    user_phone  varchar(100) unique,
    user_passwd varchar(100),
    user_sex    varchar(100),
    user_age    int,
    user_height int,
    user_weight int,
    user_bmi    float,
    user_group  varchar(100),
    user_photo  mediumblob

) character set = utf8;

create table login
(
    user_phone varchar(100) unique

) character set = utf8;

create table feed
(
    feed_id             int not null auto_increment primary key,
    feed_title          varchar(100),
    feed_description    varchar(100),
    feed_file_timestamp int

) character set = utf8;

/* create table diagnosis
(
    user_id int not null auto_increment primary key,
    user_name varchar(100),
    user_phone varchar(100),
    user_sex varchar(100),
    user_age int,
    user_height int,
    user_weight int,
    user_bmi float,
    user_group varchar(100),
    user_photo mediumblob

) character set = utf8; */

create table blood_sugar
(
    blood_sugar_id     int not null auto_increment primary key,
    blood_sugar_phone  varchar(100),
    blood_sugar_time   timestamp,
    blood_sugar_number int
) character set = utf8;

create table docter
(
    docter_name  varchar(100) not null,
    docter_phone varchar(100) not null,
    time_stamp   TIMESTAMP
)

