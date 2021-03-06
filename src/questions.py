chapters = {
    "chapter1": [
        {"field": "xinxichenshuzhe", "type": 0, "zh-cn": "信息陈述者"},
        {"field": "yuhuanzheguanxi", "type": 0, "zh-cn": "与患者关系"},
        {"field": "xinxikekaochengdu", "type": 0, "zh-cn": "信息可靠程度"},
        {"field": "xingming", "type": 0, "zh-cn": "姓名"},
        {"field": "xingbie", "type": 1, "zh-cn": "性别", "items": ["男", "女"]},
#        {"field": "chushengriqi", "type": 3, "zh-cn": "出生日期（无需填写）"},
#        {"field": "nianling", "type": 6, "zh-cn": "年龄（无需填写）", "id": "nianling"},
        {"field": "minzu", "type": 1, "zh-cn": "民族", "items": ["汉", "其他"]},
        # {"field": "shenfenzhenghao", "type": 0, "zh-cn": "身份证号（无需填写）"},
        {"field": "xuexing", "type": 1, "zh-cn": "血型", "items": ["A型", "B型", "AB型", "O型", "不详"]},
        {"field": "jiatingzhuzhi", "type": 0, "zh-cn": "家庭住址"},
        {"field": "gudingdianhua", "type": 0, "zh-cn": "固定电话"},
        {"field": "shouji1", "type": 4, "zh-cn": "手机1"},
        {"field": "shouji2", "type": 4, "zh-cn": "手机2"},
        {"field": "zhiye", "type": 1, "zh-cn": "职业", "items": ["农民", "工人", "学生", "个体", "行政", "职员", "离退休", "无业", "其他"]},
        {"field": "jiaoyuchengdu", "type": 1, "zh-cn": "教育程度", "items": ["本科及以上", "大专", "高中或职高", "初中", "小学", "文盲或半文盲"]},
        {"field": "feiyongleibie", "type": 1, "zh-cn": "费用类别", "items": ["医保", "工费", "农村合作医疗", "自费", "商业保险", "其他"]}
    ],
    "chapter2": [
        {"field": "tangniaobingbingshi", "type": 4, "zh-cn": "糖尿病病史"},
        {"field": "danbainiao", "type": 4, "zh-cn": "蛋白尿(月)"},
        {"field": "xuejiganshenggao", "type": 4, "zh-cn": "血肌酐升高(月)"},
        {"field": "hebingqitajibing", "type": 2, "zh-cn": "糖尿病病史",
         "items": ["高血压", "高血脂症", "高尿酸血症", "脂肪肝", "冠心病", "急性心血管时间", "脑血管病"]},
        {"field": "guominshi", "type": 0, "zh-cn": "过敏史"},
        {"field": "jiazushi", "type": 2, "zh-cn": "家族史", "items": ["糖尿病", "高血压", "冠心病", "心脑血管病"]},
        {"field": "tangniaobingqitabingfazhengqingkuang", "type": 2, "zh-cn": "糖尿病其他并发症情况",
         "items": ["糖尿病视网膜病变", "糖尿病周围神经病变", "糖尿病动脉粥样硬化", "糖尿病足"]}
    ],
    "chapter3": [
        {"field": "yinshixiguanzhiqian", "type": 2, "zh-cn": "饮食习惯(出现蛋白尿前5~10年)",
         "items": ["偏肉食", "偏素食", "喜辛辣", "喜油腻", "喜甜食", "无偏嗜"]},
        {"field": "rizhishuliangzhiqian", "type": 4, "zh-cn": "日主食量(出现蛋白尿前5~10年, 两)"},
        {"field": "yundongxiguanzhiqian", "type": 1, "zh-cn": "运动习惯(出现蛋白尿前5~10年)",
         "items": ["基本无运动", "低强度运动(如散步)", "中等强度运动(如慢跑)", "高强度运动(如打球)"]},
        {"field": "zhouyundongliangzhiqian", "type": 4, "zh-cn": "周运动量(出现蛋白尿前5~10年)"},
        {"field": "yinshixiguanzuijin", "type": 2, "zh-cn": "饮食习惯(最近)",
         "items": ["偏肉食", "偏素食", "喜辛辣", "喜油腻", "喜甜食", "无偏嗜"]},
        {"field": "rizhishuliangzuijin", "type": 4, "zh-cn": "日主食量(最近, 两)"},
        {"field": "yundongxiguanzuijin", "type": 1, "zh-cn": "运动习惯(最近)",
         "items": ["基本无运动", "低强度运动(如散步)", "中等强度运动(如慢跑)", "高强度运动(如打球)"]},
        {"field": "zhouyundongliangzuijin", "type": 4, "zh-cn": "周运动量(最近)"},
        {"field": "kaishixiyannianling", "type": 0, "zh-cn": "开始吸烟年龄"},
        {"field": "xiyanliang", "type": 0, "zh-cn": "吸烟量(支/天)"},
        {"field": "jieyannianling", "type": 0, "zh-cn": "戒烟年龄"},
        {"field": "kaishiyinjiunianling", "type": 0, "zh-cn": "开始饮酒年龄"},
        {"field": "yinjiuliang", "type": 0, "zh-cn": "饮酒量(ml/天)"},
        {"field": "jiejiunianling", "type": 0, "zh-cn": "戒酒年龄"},
        ],
    "chapter4": [

    ],
    "chapter5": [
        {"field": "juandaifali", "type": 1, "zh-cn": "倦怠乏力",
         "items": ["无", "偶感疲乏，程度轻微，不耐劳力，可坚持轻体力劳动", "偶感疲乏，程度轻微，不耐劳力，可坚持轻体力劳动", "休息亦感疲乏无力，持续出现，不能坚持日常活动"]},
        {"field": "shaoqilanyan", "type": 1, "zh-cn": "少气懒言",
         "items": ["无", "活动后气短，平素懒于多言", "安静时也时有气短，懒于言语", "安静时持续气短，语声低微，言语无力"]},
        {"field": "yizihan", "type": 1, "zh-cn": "易自汗",
         "items": ["无", "安静略有汗出，动则汗出增多", "安静时即有明显汗出，动则多汗", "安静时即汗多，活动则大汗欲脱"]},
        {"field": "touyunmuxuan", "type": 1, "zh-cn": "头晕目眩",
         "items": ["无", "不因猛然起立，有时发生", "不因猛然起立，经常发生", "不因猛然起立，反复发作，不易缓解"]},
        {"field": "jingshaosedan", "type": 1, "zh-cn": "经少色淡",
         "items": ["无", "经量偏少，经色较淡", "月经量少，月经色淡", "经量少甚或闭经，经色极淡"]},
        {"field": "yangankouke", "type": 1, "zh-cn": "咽干口渴",
         "items": ["无", "偶有", "咽干口渴喜饮", "咽干口渴多饮"]},
        {"field": "mujingganse", "type": 1, "zh-cn": "目睛干涩",
         "items": ["无", "双目少津，视物易疲劳", "双目干涩不爽，视物常模糊", "双目干燥，昏暗不明"]},
        {"field": "wuxinfanre", "type": 1, "zh-cn": "五心烦热",
         "items": ["无", "偶有手足心热，或兼轻微心烦", "时时手足心热，或兼明显心烦", "双目干燥，昏暗不明"]},
        {"field": "chaoredaohan", "type": 1, "zh-cn": "潮热盗汗", "items": ["无", "偶有头部潮热盗汗", "胸背潮热,夜间常有盗汗", "周身潮热,每晚必有盗汗"]},
        {"field": "weihanzhileng", "type": 1, "zh-cn": "畏寒肢冷",
         "items": ["无", "全身略感畏寒，肢体偏凉", "全身明显畏寒，肢体冷凉", "全身特别畏寒，肢冷如冰"]},
        {"field": "dabiantangxi", "type": 1, "zh-cn": "大便溏稀",
         "items": ["无", "大便不成形，每日一次", "大便稀软，每日2-3次", "大便稀软，每日3次以上"]},
        {"field": "yeniaopinduo", "type": 1, "zh-cn": "夜尿频多",
         "items": ["无", "夜尿略显频多，每夜2次", "夜尿频而量多，每夜2-3次", "夜尿频而量多，每夜3次以上"]},
        {"field": "yanhouzhongtong", "type": 1, "zh-cn": "咽喉肿痛", "items": ["无", "偶有轻微疼痛", "时有疼痛不适", "经常持续疼痛，难以缓解"]},
        {"field": "xinxiongfanre", "type": 1, "zh-cn": "心胸烦热", "items": ["无", "略有心中烦热", "常有心胸烦热", "心胸烦热尤甚"]},
        {"field": "pifucuochuanghuojiezhong", "type": 1, "zh-cn": "皮肤痤疮或疖肿",
         "items": ["无", "皮肤浅表红肿热痛，疖肿小而数目 少", "皮肤浅表红肿热痛，疖肿略大而多", "皮肤浅表红肿热痛，疖肿大而数目多"]},
        {"field": "xiaobianhuangchi", "type": 1, "zh-cn": "小便黄赤", "items": ["无", "尿黄", "尿黄量少", "尿黄量少涩痛"]},
        {"field": "parehanchu", "type": 1, "zh-cn": "怕热汗出", "items": ["无", "偏怕热，略喜汗出", "怕热，时有汗出", "特别怕热，时时 汗出"]},
        {"field": "kexilengyin", "type": 1, "zh-cn": "渴喜冷饮",
         "items": ["无", "口略干，饮水量稍增，喜冷饮", "口燥咽干，饮水量较以 往增加半倍以上，喜冷饮", "终日口燥咽干，饮水量较以往增加1倍以上，嗜冷饮"]},
        {"field": "kouzhongchouhui", "type": 1, "zh-cn": "口中臭秽", "items": ["无", "自觉有口臭", "旁人可闻及", "口中尿臭味，令人难近"]},
        {"field": "duoshiyiji", "type": 1, "zh-cn": "多食易饥",
         "items": ["无", "饥饿感较平时有所增加，食量增加1/2以下", "每于食后2小时即有饥饿感，食量增加1/2以上1倍以下", "整日有饥饿感，食量增加1倍以上"]},
        {"field": "dabianganjie", "type": 1, "zh-cn": "大便干结",
         "items": ["无", "大便干燥，排出硬而费力", "大便硬结，2-3天1行", "大 便硬结，3天以上一行"]},
        {"field": "kouganbuyuyin", "type": 1, "zh-cn": "口干不欲饮",
         "items": ["无", "口干不欲饮，但欲漱水", "口干不欲饮，饮后无反应", "口干不欲饮，饮后恶心"]},
        {"field": "kouganzhanni", "type": 1, "zh-cn": "口干粘腻", "items": ["无", "偶有", "时有", "终日"]},
        {"field": "dabianzhannibushuang", "type": 1, "zh-cn": "大便粘腻不爽", "items": ["无", "大便略粘腻", "大便粘腻", "大便粘腻不爽"]},
        {"field": "muchichiduo", "type": 1, "zh-cn": "目赤眵多", "items": ["无", "偶有", "时有", "经常发生"]},
        {"field": "kouku", "type": 1, "zh-cn": "口苦", "items": ["无", "晨起口苦，或口中微苦", "口苦不知食味", "口苦而涩"]},
        {"field": "jizaoyinu", "type": 1, "zh-cn": "急躁易怒", "items": ["无", "偶有", "时有发生，脾气暴躁", "经常发生，情绪急躁"]},
        {"field": "qingxuyiyu", "type": 1, "zh-cn": "情绪抑郁",
         "items": ["无", "无明显诱因，有时发生", "无明显诱因情绪低落，经常容易发生", "无明显诱因，特别容易发生，难以自控"]},
        {"field": "xiongxiezhangmanxitaixi", "type": 1, "zh-cn": "胸胁胀满喜太息",
         "items": ["无", "胸胁稍有胀满，可自行缓解", "胸胁 胀满明显，太息则舒，部分影响生活", "胸胁胀满，持续不能缓解，影响工作和休息"]},
        {"field": "shenzhongkunjuan", "type": 1, "zh-cn": "身重困倦",
         "items": ["无", "仅有困重感，尚未碍及活动", "肢体沉重，活动费力", "肢体沉重如裹，活动困难影响日常生活"]},
        {"field": "pifusaoyang", "type": 1, "zh-cn": "皮肤瘙痒",
         "items": ["无", "皮肤偶有局限性瘙痒", "皮肤时有不同部位瘙痒", "皮肤时有多部位瘙痒，难以忍受"]},
        {"field": "eryinshiyang", "type": 1, "zh-cn": "二阴湿痒", "items": ["无", "偶有", "有时发生，可以忍受", "终日潮湿，瘙痒难忍"]},
        {"field": "guanfupiman", "type": 1, "zh-cn": "脘腹痞满", "items": ["无", "脘腹偶有不舒", "脘腹时有痞满", "脘腹持续痞塞不通"]},
        {"field": "shishaooue", "type": 1, "zh-cn": "食少呕恶",
         "items": ["无", "饮食稍减，偶有恶心", "饮食明显减少，时有恶心，偶有呕吐", "近于不能进食，时时恶心，时有呕吐"]},
        {"field": "dingweicitong，yejianjiazhong", "type": 1, "zh-cn": "定位刺痛，夜间加重",
         "items": ["无", "偶有某部位局限性刺痛", "时有不同部位刺痛", "多部位持续刺痛"]},
        {"field": "jifujiacuo", "type": 1, "zh-cn": "肌肤甲错",
         "items": ["无", "肌肤局限性粗糙、干燥，欠润泽", "肌肤不同部位粗糙、干燥、角化、脱屑", "肌肤广泛性粗糙、干燥、角化、脱屑"]},
        {"field": "zhitimamu", "type": 1, "zh-cn": "肢体麻木", "items": ["无", "手足麻木", "四肢麻木，感觉减退", "四肢麻木无知觉"]},
        {"field": "yaojitengtong", "type": 1, "zh-cn": "腰脊疼痛", "items": ["无", "疼痛隐隐，偶有发作", "疼痛较重，转侧不利", "疼痛剧烈，难以忍受"]},
        {"field": "chigaofatuo", "type": 1, "zh-cn": "齿稿发脱", "items": ["无", "牙齿松动或少量脱发", "牙齿少数脱落或大量脱发", "牙齿多数脱落或头发稀少"]},
        {"field": "ermingerlong", "type": 1, "zh-cn": "耳鸣耳聋",
         "items": ["无", "耳鸣轻微，偶尔出现，数秒即逝，不影响听力", "耳鸣较重，经常出现，持续数分钟，轻度影响听力", "耳鸣如蝉，如火车声，持续不已，听力中度减退"]}

    ],
    "chapter6": [
        {"field": "miansecangbaihuoweihuang", "type": 1, "zh-cn": "面色苍白或萎黄",
         "items": ["无", "面色淡白，无光泽", "面色淡白，无血色或萎黄", "面色苍白无血色，或萎黄兼虚肿"]},
        {"field": "mianseliheihuohuian", "type": 1, "zh-cn": "面色黧黑或晦暗",
         "items": ["无", "面部呈现淡黧黑（晦暗）色", "面部呈现 黧黑(晦暗)色", "面部呈现深黧黑（晦暗）色"]},
        {"field": "mianhongchi", "type": 1, "zh-cn": "面红赤", "items": ["无", "面微红赤", "面赤明显", "面赤如妆"]},
        {"field": "mianrumengyou", "type": 1, "zh-cn": "面如蒙油", "items": ["无", "轻度", "明显", "重度"]},
        {"field": "chunjiasedan", "type": 1, "zh-cn": "唇甲色淡", "items": ["无", "唇甲干涩，欠红润", "唇甲干涩，色淡白无光泽", "唇甲 干涩，苍白无光泽"]},
        {"field": "kouchunshezi，huozian、yuban、shexiamaizinuzhang", "type": 1, "zh-cn": "口唇舌紫，或紫暗、瘀斑、舌下脉紫努张",
         "items": ["无", "口唇舌略暗，可见少量瘀点，舌下脉络略紫", "口唇舌紫暗，可见较多瘀点、瘀斑，舌下脉络青紫", "口唇舌明显紫暗， 满布瘀点、瘀斑，舌下脉络青紫努张"]},
        {"field": "mianzufuzhong", "type": 1, "zh-cn": "面足浮肿",
         "items": ["无", "眼睑、足踝轻度浮肿", "颜面、下肢明显浮肿", "颜面、下肢浮肿严重，或有胸腹水"]},
        {"field": "shexiang", "type": 5, "zh-cn": "舌象",
         "items": ["舌体胖有齿痕", "舌淡胖苔润", "舌质淡白无泽", "舌红而少苔", "舌红苔黄", "舌边有浊沫", "舌红苔黄腻", "苔腻", "其他"]},
        {"field": "maixiang", "type": 5, "zh-cn": "脉象",
         "items": ["脉细数", "脉滑数", "脉弦数", "脉数或洪大", "脉弱无力", "脉细弱", "脉沉迟", "脉涩或结代", "其他"]},
        {"field": "tiwen", "type": 4, "zh-cn": "体温(℃)"},
        {"field": "maibo", "type": 4, "zh-cn": "脉搏(次/分)"},
        {"field": "huxi", "type": 4, "zh-cn": "呼吸（次/分)"},
        {"field": "xueya", "type": 0, "zh-cn": "血压（mmHg)"},
        {"field": "tizhong", "type": 6, "zh-cn": "体重(kg)", "id": "tizhong"},
        {"field": "shengao", "type": 6, "zh-cn": "身高(cm)", "id": "shengao"},
        {"field": "BMIzhi", "type": 6, "zh-cn": "BMI(kg/m2)", "id": "BMIzhi"},
        {"field": "yaowei", "type": 4, "zh-cn": "腰围(肋骨下缘与髂嵴连线中点的腹部周径)(cm)"},
    ],
    "chapter7": [
        {"field": "xiehongdanbai", "type": 8, "zh-cn": "血红蛋白(g/dl)"},
        {"field": "hongxibaoxue", "type": 8, "zh-cn": "血常规红细胞(×10^12/L)"},
        {"field": "hongxibaoyaji", "type": 8, "zh-cn": "红细胞压积(%)"},
        {"field": "baixibaoxue", "type": 8, "zh-cn": "血常规白细胞(×10^9/L)"},
        {"field": "xiexiaoban", "type": 8, "zh-cn": "血小板(×10^9/L)"},
        {"field": "zhongxinglixibao", "type": 8, "zh-cn": "中性粒细胞(×10^9/L)"},
        {"field": "niaodanbai", "type": 8, "zh-cn": "尿蛋白(g/L)"},
        {"field": "guanxing", "type": 8, "zh-cn": "管型(/LPF)"},
        {"field": "hongxibaoniao", "type": 8, "zh-cn": "尿常规红细胞(/HPF)"},
        {"field": "baixibaoniao", "type": 8, "zh-cn": "尿常规白细胞(/HPF)"},
        {"field": "K", "type": 8, "zh-cn": "K+(mmol/L)"},
        {"field": "Ca2", "type": 8, "zh-cn": "Ca2+(mmol/L)"},
        {"field": "P3", "type": 8, "zh-cn": "P3+(mmol/L)"},
        {"field": "CO2CP", "type": 8, "zh-cn": "CO2CP(mmol/L)"},
        {"field": "GLU", "type": 8, "zh-cn": "GLU(mmol/L)"},
        {"field": "BUN", "type": 8, "zh-cn": "BUN(mmol/l)"},
        {"field": "Scr", "type": 8, "zh-cn": "Scr(umol/l)"},
        {"field": "UA", "type": 8, "zh-cn": "UA(umol/l)"},
        {"field": "TP", "type": 8, "zh-cn": "TP(g/L)"},
        {"field": "Alb", "type": 8, "zh-cn": "Alb(g/L)"},
        {"field": "ALT", "type": 8, "zh-cn": "ALT(IU/L)"},
        {"field": "AST", "type": 8, "zh-cn": "AST(IU/L)"},
        {"field": "GammaGT", "type": 8, "zh-cn": "γ-GT(IU/L)"},
        {"field": "ALP", "type": 8, "zh-cn": "ALP(IU/L)"},
        {"field": "TBIL", "type": 8, "zh-cn": "TBIL(umol/l)"},
        {"field": "CHO", "type": 8, "zh-cn": "CHO(mmol/l)"},
        {"field": "TG", "type": 8, "zh-cn": "TG(mmol/l)"},
        {"field": "LDL", "type": 8, "zh-cn": "LDL(mmol/l)"},
        {"field": "INS", "type": 8, "zh-cn": "INS(IU/L)"},
        {"field": "Ctai", "type": 8, "zh-cn": "C肽(IU/L)"},
        {"field": "eGFR", "type": 7, "zh-cn": "eGFR(ml/(min·1.73m2))", "id": "eGFR"},
        {"field": "niaobaidanbaijihang", "type": 8, "zh-cn": "尿白蛋白/肌酐(mg/g)"},
        {"field": "xiaoshiniaoweiliangbaidanbaipaixielv", "type": 8, "zh-cn": "24小时尿微量白蛋白排泄率(mg)"},
        {"field": "xiaoshiniaodanbaidingliang", "type": 8, "zh-cn": "24小时尿蛋白定量(mg)"},
        {"field": "niaoliang", "type": 8, "zh-cn": "尿量(ml)"},
        {"field": "yaowei", "type": 8, "zh-cn": "腰围(肋骨下缘与髂嵴连线中点的腹部周径)(cm)"},
        {"field": "tanghuaxuehongdanbai", "type": 8, "zh-cn": "糖化血红蛋白(%)"},
        {"field": "xindiantu", "type": 8, "zh-cn": "心电图"},
        {"field": "chaoshengxindong", "type": 8, "zh-cn": "超声心动"},
        {"field": "zuoxinshishexuefenshu", "type": 8, "zh-cn": "左心室射血分数(%)"},
        {"field": "jingdongmaiBchao", "type": 8, "zh-cn": "颈动脉B超"},
        {"field": "jingneizhongmohouduzuo", "type": 8, "zh-cn": "颈内中膜厚度左(mm)"},
        {"field": "jingneizhongmohouduyou", "type": 8, "zh-cn": "颈内中膜厚度右(mm)"},
        {"field": "yandijiancha", "type": 8, "zh-cn": "眼底检查"},
        {"field": "ectjiancha", "type": 8, "zh-cn": "ect检查"},
        {"field": "zhaopianlujing", "type":9, "zh-cn": "实验室照片路径(无用)"},
    ],
    "chapter8": [
        {"field": "yinshixiguanzuijin", "type": 2, "zh-cn": "饮食习惯(最近)",
         "items": ["偏肉食", "偏素食", "喜辛辣", "喜油腻", "喜甜食", "无偏嗜"]},
        {"field": "rizhishuliangzuijin", "type": 4, "zh-cn": "日主食量(最近, 两)"},
        {"field": "yundongxiguanzuijin", "type": 1, "zh-cn": "运动习惯(最近)",
         "items": ["基本无运动", "低强度运动(如散步)", "中等强度运动(如慢跑)", "高强度运动(如打球)"]},
        {"field": "zhouyundongliangzuijin", "type": 4, "zh-cn": "周运动量(最近)"},
    ],
    "chapter9": [

    ]

}
#                 1           2           3             4          5        6         7          8            9
chapter_name = ["基本情况", "病史情况", "生活习惯情况", "请勿点击", "症状", "体征", "实验室检查", "生活习惯情况", "中医处方记录"]

# survey_info = [
#     [1, 2, 3, 4, 5, 6, 7],
#     [8, 9, 4, 5, 6, 7],
#     [8, 9, 4, 5, 6, 7],
#     [8, 9, 4, 5, 6, 7],
# ]

# 更改survey_info 为一个矩阵每次显示所有信息
survey_info = [[1, 2, 3, 5, 6, 7]]
