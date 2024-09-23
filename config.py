bist_tickers = ["A1CAP","ACSEL","ADEL","ADESE","ADGYO","AEFES","AFYON","AGESA","AGHOL","AGROT","AGYO","AHGAZ","AKBNK","AKCNS","AKENR","AKFGY","AKFYE","AKGRT","AKMGY",
              "AKSA","AKSEN","AKSGY","AKSUE","AKSUE","AKYHO","ALARK","ALBRK","ALCAR","ALCTL","ALFAS","ALGYO","ALKA","ALKIM","ALMAD","ANELE","ANGEN","ANHYT",
              "ANSGR","ARASE","ARCLK","ARDYZ","ARENA","ARSAN","ARZUM","ASELS","ASGYO","ASTOR","ASUZU","ATAGY","ATAKP","ATATP","ATEKS","ATLAS","ATSYH","AVGYO","AVHOL",
              "AVOD","AVPGY","AVTUR","AYCES","AYDEM","AYEN","AYES","AYGAZ","AZTEK","BAGFS","BAKAB","BALAT","BANVT","BARMA","BASCM","BASGZ","BAYRK","BEGYO","BERA","BEYAZ",
              "BFREN","BIENY","BIGCH","BIMAS","BINHO","BIOEN","BIZIM","BJKAS","BLCYT","BMSCH","BMSTL","BNTAS","BOBET","BORLS","BOSSA","BRISA","BRKO","BRKSN","BRKVY","BRLSM",
              "BRMEN","BRSAN","BRYAT","BSOKE","BTCIM","BUCIM","BURCE","BURVA","BVSAN","BYDNR","CANTE","CASA","CATES","CCOLA","CELHA","CELHA","CEMAS","CEMTS","CEOEM","CIMSA",
              "CLEBI","CMBTN","CMENT","CONSE","COSMO","CRDFA","CRFSA","CUSAN","CVKMD","CWENE","DAGHL","DAGI","DAPGM","DARDL","DENGE","DERHL","DERIM","DESA","DESPC","DEVA",
              "DGATE","DGGYO","DGNMO","DIRIT","DITAS","DMRGD","DMSAS","DNISI","DOAS","DOBUR","DOCO","DOFER","DOGUB","DOHOL","DOKTA","DURDO","DYOBY","DZGYO","EBEBK","ECILC",
              "ECZYT","EDATA","EDIP","EGEEN","EGEPO","EGGUB","EGPRO","EGSER","EKGYO","EKIZ","EKOS","EKSUN","ELITE","EMKEL","EMNIS","ENERY","ENJSA","ENKAI","ENSRI","EPLAS",
              "ERBOS","ERCB","EREGL","ERSU","ESCAR","ESCOM","ESEN","ETILR","ETYAT","EUHOL","EUKYO","EUPWR","EUREN","EUYO","EYGYO","FADE","FENER","FLAP","FMIZP","FONET",
              "FORMT","FORTE","FRIGO","FROTO","FZLGY","GARAN","GARFA","GEDIK","GEDZA","GENIL","GENTS","GEREL","GESAN","GIPTA","GLBMD","GLCVY","GLRYH","GLYHO","GMTAS",
              "GOKNR","GOLTS","GOODY","GOZDE","GRNYO","GRSEL","GRTRK","GSDDE","GSDHO","GSRAY","GUBRF","GWIND","GZNMI","HALKB","HATEK","HATSN","HDFGS","HEDEF","HEKTS",
              "HKTM","HLGYO","HTTBT","HUBVC","HUNER","HURGZ","ICBCT","ICUGS","IDEAS","IDGYO","IEYHO","IHAAS","IHEVA","IHGZT","IHLAS","IHLGM","IHYAY","IMASM","INDES",
              "INFO","INGRM","INTEM","INVEO","INVES","IPEKE","ISATR","ISBIR","ISBTR","ISCTR","ISDMR","ISFIN","ISGSY","ISGYO","ISKPL","ISKUR","ISMEN","ISSEN","ISYAT",
              "IZENR","IZFAS","IZINV","IZMDC","JANTS","KAPLM","KAREL","KARSN","KARTN","KARYE","KATMR","KAYSE","KBORU","KCAER","KCHOL","KENT","KERVN","KERVT","KFEIN",
              "KGYO","KIMMR","KLGYO","KLKIM","KLMSN","KLNMA","KLRHO","KLSER","KLSYN","KMPUR","KNFRT","KONKA","KONTR","KONYA","KOPOL","KORDS","KOZAA","KOZAL","KRDMA",
              "KRDMB","KRDMD","KRGYO","KRONT","KRPLS","KRSTL","KRTEK","KRVGD","KSTUR","KTLEV","KTSKR","KUTPO","KUVVA","KUYAS","KZBGY","KZGYO","LIDER","LIDFA","LINK",
              "LKMNH","LOGO","LRSHO","LUKSK","MAALT","MACKO","MAGEN","MAKIM","MAKTK","MANAS","MARBL","MARKA","MARTI","MAVI","MEDTR","MEGAP","MEGMT","MEKAG","MEPET",
              "MERCN","MERIT","MERKO","METRO","METUR","MGROS","MHRGY","MIATK","MIPAZ","MMCAS","MNDRS","MNDTR","MOBTL","MPARK","MRGYO","MRSHL","MSGYO","MTRKS","MTRYO",
              "MZHLD","NATEN","NETAS","NIBAS","NTGAZ","NTHOL","NUGYO","NUHCM","OBASE","ODAS","OFSYM","ONCSM","ORCAY","ORGE","ORMA","OSMEN","OSTIM","OTKAR","OTTO","OYAKC",
              "OYAYO","OYLUM","OYYAT","OZGYO","OZKGY","OZRDN","OZSUB","PAGYO","PAMEL","PAPIL","PARSN","PASEU","PCILT","PEGYO","PEKGY","PENGD","PENTA","PETKM","PETUN","PGSUS",
              "PINSU","PKART","PKENT","PLTUR","PNLSN","PNSUT","POLHO","POLTK","PRDGS","PRKAB","PRKME","PRZMA","PSDTC","PSGYO","QNBFB","QNBFL","QUAGR","RALYH","RAYSG","REEDR",
              "RNPOL","RODRG","ROYAL","RTALB","RUBNS","RYGYO","RYSAS","SAFKR","SAHOL","SAMAT","SANEL","SANFM","SANKO","SARKY","SASA","SAYAS","SDTTR","SEGYO","SEKFK","SEKUR",
              "SEKUR","SELEC","SELGD","SELVA","SEYKM","SILVR","SISE","SKBNK","SKTAS","SKYMD","SMART","SMRTG","SNGYO","SNICA","SNKRN","SNPAM","SODSN","SOKE","SOKM","SONME",
              "SRVGY","SUMAS","SUNTK","SURGY","SUWEN","TABGD","TARKM","TATEN","TATGD","TAVHL","TBORG","TCELL","TDGYO","TEKTU","TERA","TETMT","TEZOL","TGSAS","THYAO","TKFEN",
              "TKNSA","TLMAN","TMPOL","TMSN","TNZTP","TOASO","TRCAS","TRGYO","TRILC","TSGYO","TSKB","TSPOR","TSPOR","TTKOM","TTRAK","TUCLK","TUKAS","TUPRS","TUREX","TURGG",
              "TURSG","UFUK","ULAS","ULKER","ULUFA","ULUSE","ULUUN","UMPAS","UNLU","USAK","UZERB","VAKBN","VAKFN","VAKKO","VANGD","VBTYZ","VERTU","VERUS","VESBE","VESTL",
              "VKFYO","VKGYO","VKING","VRGYO","YAPRK","YATAS","YAYLA","YBTAS","YEOTK","YESIL","YGGYO","YGYO","YKBNK","YKSLN","YONGA","YUNSA","YYAPI","YYLGD","ZEDUR","ZOREN","ZRGYO"]  # BIST hisselerini buraya ekle