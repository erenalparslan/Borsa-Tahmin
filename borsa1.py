import yfinance as yf

# Borsa İstanbul'daki tüm hisselerin listesi
hisseler = ["A1CAP.IS", "ACSEL.IS", "ADEL.IS", "ADESE.IS", "ADGYO.IS", "AEFES.IS", "AFYON.IS", "AGESA.IS", "AGHOL.IS", "AGYO.IS", "AHGAZ.IS", "AKBNK.IS", "AKCNS.IS", "AKENR.IS", "AKFGY.IS", "AKFYE.IS",
            "AKGRT.IS", "AKMGY.IS", "AKSA.IS", "AKSEN.IS", "AKSGY.IS", "AKSUE.IS", "AKYHO.IS", "ALARK.IS", "ALBRK.IS", "ALCAR.IS", "ALCAR.IS", "ALCTL.IS", "ALFAS.IS", "ALGYO.IS", "ALKA.IS", "ALKIM.IS",
            "ALMAD.IS", "ANELE.IS", "ANGEN.IS", "ANHYT.IS", "ANSGR.IS", "ARASE.IS", "ARCLK.IS", "ARDYZ.IS", "ARENA.IS", "ARSAN.IS", "ARZUM.IS", "ASELS.IS", "ASGYO.IS", "ASTOR.IS", "ASUZU.IS", "ATAGY.IS",
            "ATAKP.IS", "ATATP.IS", "ATEKS.IS", "ATLAS.IS", "ATSYH.IS", "AVGYO.IS", "AVHOL.IS", "AVOD.IS", "AVTUR.IS", "AYCES.IS", "AYDEM.IS", "AYEN.IS", "AYES.IS", "AYGAZ.IS", "AZTEK.IS", "BAGFS.IS",
            "BAKAB.IS", "BALAT.IS", "BANVT.IS", "BARMA.IS", "BASCM.IS", "BASGZ.IS", "BAYRK.IS", "BERA.IS", "BEYAZ.IS", "BFREN.IS", "BIENY.IS", "BIGCH.IS", "BIMAS.IS", "BIOEN.IS", "BIZIM.IS", "BJKAS.IS",
            "BLCYT.IS", "BMSCH.IS", "BMSTL.IS", "BNTAS.IS", "BOBET.IS", "BOSSA.IS", "BRISA.IS", "BRKO.IS", "BRKSN.IS", "BRKVY.IS", "BRLSM.IS", "BRMEN.IS", "BRSAN.IS", "BRYAT.IS", "BSOKE.IS", "BTCIM.IS",
            "BUCIM.IS", "BURCE.IS", "BURVA.IS", "BVSAN.IS", "BYDNR.IS", "CANTE.IS", "CASA.IS", "CCOLA.IS", "CELHA.IS", "CEMAS.IS", "CEMTS.IS", "CEOEM.IS", "CIMSA.IS", "CLEBI.IS", "CMBTN.IS", "CMENT.IS",
            "CONSE.IS", "COSMO.IS", "CRDFA.IS", "CRFSA.IS", "CUSAN.IS", "CVKMD.IS", "CWENE.IS", "DAGHL.IS", "DAGI.IS","DAPGM.IS", "DARDL.IS", "DENGE.IS", "DERHL.IS", "DERIM.IS", "DESA.IS", "DESPC.IS",
            "DEVA.IS", "DGATE.IS", "DGGYO.IS", "DGNMO.IS","DIRIT.IS", "DITAS.IS", "DJIST.IS", "DMRGD.IS", "DMSAS.IS", "DNISI.IS", "DOAS.IS", "DOBUR.IS", "DOCO.IS", "DOGUB.IS", "DOHOL.IS", "DOKTA.IS",
            "DURDO.IS", "DYOBY.IS", "DZGYO.IS", "EBEBK.IS", "ECILC.IS", "ECZYT.IS", "EDATA.IS", "EDIP.IS", "EGEEN.IS", "EGEPO.IS", "EGGUB.IS", "EGPRO.IS", "EGSER.IS", "EKGYO.IS", "EKIZ.IS", "EKSUN.IS",
            "ELITE.IS", "EMKEL.IS", "EMNIS.IS", "ENERY.IS", "ENJSA.IS", "ENKAI.IS", "ENSRI.IS", "EPLAS.IS", "ERBOS.IS", "ERCB.IS", "EREGL.IS", "ERSU.IS", "ESCAR.IS", "ESCOM.IS", "ESEN.IS", "ETILR.IS",
            "ETYAT.IS", "EUHOL.IS", "EUKYO.IS", "EUPWR.IS", "EUREN.IS", "EUYO.IS", "EYGYO.IS", "FADE.IS", "FENER.IS", "FLAP.IS", "FMIZP.IS", "FONET.IS", "FORMT.IS", "FORTE.IS", "FRIGO.IS", "FROTO.IS",
            "FZLGY.IS", "GARAN.IS", "GARFA.IS", "GEDIK.IS", "GEDZA.IS", "GENIL.IS", "GENTS.IS", "GEREL.IS", "GESAN.IS", "GIPTA.IS", "GLBMD.IS", "GLCVY.IS", "GLDTR.IS", "GLRYH.IS", "GLYHO.IS", "GMSTR.IS",
            "GMTAS.IS", "GOKNR.IS", "GOLTS.IS", "GOODY.IS", "GOZDE.IS", "GRNYO.IS", "GRSEL.IS", "GRTRK.IS", "GSDDE.IS", "GSDHO.IS", "GSRAY.IS", "GUBRF.IS", "GWIND.IS", "GZNMI.IS", "HALKB.IS", "HATEK.IS",
            "HATSN.IS", "HDFGS.IS", "HEDEF.IS", "HEKTS.IS", "HKTM.IS", "HLGYO.IS", "HTTBT.IS", "HUBVC.IS", "HUNER.IS", "HURGZ.IS", "ICBCT.IS", "ICUGS.IS", "IDEAS.IS", "IDGYO.IS", "IEYHO.IS", "IHAAS.IS",
            "IHEVA.IS", "IHGZT.IS", "IHLAS.IS", "IHLGM.IS", "IHYAY.IS", "IMASM.IS", "INDES.IS", "INFO.IS", "INGRM.IS", "INTEM.IS", "INVEO.IS", "INVES.IS", "IPEKE.IS", "ISATR.IS", "ISBIR.IS", "ISBTR.IS",
            "ISCTR.IS", "ISDMR.IS", "ISFIN.IS", "ISGSY.IS", "ISGYO.IS", "ISIST.IS", "ISKPL.IS", "ISKUR.IS","ISMEN.IS", "ISSEN.IS", "ISYAT.IS", "IZENR.IS", "IZFAS.IS", "IZINV.IS", "IZMDC.IS", "JANTS.IS",
            "KAPLM.IS", "KAREL.IS", "KARSN.IS", "KARTN.IS", "KARYE.IS", "KATMR.IS", "KAYSE.IS", "KCAER.IS", "KCHOL.IS", "KENT.IS", "KERVN.IS", "KERVT.IS", "KFEIN.IS", "KGYO.IS", "KIMMR.IS", "KLGYO.IS",
            "KLKIM.IS", "KLMSN.IS", "KLNMA.IS", "KLRHO.IS", "KLSER.IS", "KLSYN.IS", "KMPUR.IS", "KNFRT.IS", "KONKA.IS", "KONTR.IS", "KONYA.IS", "KOPOL.IS", "KORDS.IS", "KOZAA.IS", "KOZAL.IS", "KRDMA.IS",
            "KRDMB.IS", "KRDMD.IS", "KRGYO.IS", "KRONT.IS", "KRPLS.IS", "KRSTL.IS", "KRTEK.IS", "KRVGD.IS", "KSTUR.IS", "KTLEV.IS", "KTSKR.IS", "KUTPO.IS", "KUVVA.IS", "KUYAS.IS", "KZBGY.IS","KZGYO.IS",
            "LIDER.IS", "LIDFA.IS", "LINK.IS", "LKMNH.IS", "LOGO.IS", "LUKSK.IS", "MAALT.IS", "MACKO.IS", "MAGEN.IS", "MAKIM.IS", "MAKTK.IS", "MANAS.IS", "MARKA.IS", "MARTI.IS", "MAVI.IS", "MEDTR.IS",
            "MEGAP.IS", "MEPET.IS", "MERCN.IS", "MERIT.IS", "MERKO.IS", "METRO.IS", "METUR.IS", "MGROS.IS", "MIATK.IS", "MIPAZ.IS", "MMCAS.IS", "MNDRS.IS", "MNDTR.IS", "MOBTL.IS", "MPARK.IS", "MRGYO.IS",
            "MRSHL.IS", "MSGYO.IS", "MTRKS.IS", "MTRYO.IS", "MZHLD.IS", "NATEN.IS", "NETAS.IS", "NIBAS.IS", "NTGAZ.IS", "NTHOL.IS", "NUGYO.IS", "NUHCM.IS", "OBASE.IS", "ODAS.IS", "OFSYM.IS", "ONCSM.IS",
            "ORCAY.IS", "ORGE.IS", "ORMA.IS", "OSMEN.IS", "OSTIM.IS", "OTKAR.IS", "OTTO.IS", "OYAKC.IS", "OYAYO.IS", "OYLUM.IS", "OYYAT.IS", "OZGYO.IS", "OZKGY.IS", "OZRDN.IS", "OZSUB.IS", "PAGYO.IS",
            "PAMEL.IS", "PAPIL.IS", "PARSN.IS", "PASEU.IS", "PCILT.IS", "PEGYO.IS", "PEKGY.IS", "PENGD.IS", "PENTA.IS", "PETKM.IS", "PETUN.IS", "PGSUS.IS", "PINSU.IS", "PKART.IS", "PKENT.IS", "PLTUR.IS",
            "PNLSN.IS", "PNSUT.IS", "POLHO.IS", "POLTK.IS", "PRDGS.IS", "PRKAB.IS", "PRKME.IS", "PRZMA.IS", "PSDTC.IS", "PSGYO.IS", "QNBFB.IS", "QNBFL.IS", "QUAGR.IS", "RALYH.IS", "RAYSG.IS", "REEDR.IS",
            "RNPOL.IS", "RODRG.IS", "RTALB.IS", "RUBNS.IS", "RYGYO.IS", "RYSAS.IS", "SAFKR.IS", "SAHOL.IS", "SAMAT.IS", "SANEL.IS", "SANFM.IS", "SANKO.IS", "SARKY.IS", "SASA.IS", "SAYAS.IS", "SDTTR.IS",
            "SEGYO.IS", "SEKFK.IS", "SEKUR.IS", "SELEC.IS", "SELGD.IS", "SELVA.IS", "SEYKM.IS", "SILVR.IS", "SISE.IS", "SKBNK.IS", "SKTAS.IS", "SMART.IS", "SMRTG.IS", "SNGYO.IS", "SNICA.IS", "SNKRN.IS",
            "SNPAM.IS", "SODSN.IS", "SOKE.IS", "SOKM.IS", "SONME.IS", "SRVGY.IS", "SUMAS.IS", "SUNTK.IS", "SUWEN.IS", "TARKM.IS", "TATEN.IS", "TATGD.IS", "TAVHL.IS", "TBORG.IS", "TCELL.IS", "TDGYO.IS",
            "TEKTU.IS", "TERA.IS", "TETMT.IS", "TEZOL.IS", "TGSAS.IS", "THYAO.IS", "TKFEN.IS", "TKNSA.IS", "TLMAN.IS", "TMPOL.IS", "TMSN.IS", "TNZTP.IS", "TOASO.IS", "TRCAS.IS", "TRGYO.IS", "TRILC.IS",
            "TSGYO.IS", "TSKB.IS", "TSPOR.IS", "TTKOM.IS", "TTRAK.IS", "TUCLK.IS", "TUKAS.IS", "TUPRS.IS", "TUREX.IS", "TURGG.IS", "TURSG.IS", "UFUK.IS", "ULAS.IS", "ULKER.IS", "ULUFA.IS", "ULUSE.IS",
            "ULUUN.IS", "UMPAS.IS", "UNLU.IS", "USAK.IS", "USDTR.IS", "UZERB.IS", "VAKBN.IS", "VAKFN.IS", "VAKKO.IS", "VANGD.IS", "VBTYZ.IS", "VERTU.IS", "VERUS.IS", "VESBE.IS", "VESTL.IS", "VKFYO.IS",
            "VKGYO.IS", "VKING.IS", "X030S.IS", "X100S.IS", "XBANA.IS","XBANK.IS", "XBLSM.IS", "XELKT.IS", "XFINK.IS", "XGIDA.IS", "XGMYO.IS", "XHARZ.IS", "XHOLD.IS", "XILTM.IS", "XINSA.IS", "XKAGT.IS",
            "XKMYA.IS", "XKOBI.IS", "XKURY.IS", "XMADN.IS", "XMANA.IS", "XMESY.IS", "XSADA.IS", "XSANK.IS", "XSANT.IS", "XSBAL.IS", "XSBUR.IS", "XSDNZ.IS", "XSGRT.IS", "XSIST.IS", "XSIZM.IS", "XSKAY.IS",
            "XSKOC.IS", "XSKON.IS", "XSPOR.IS", "XSTKR.IS", "XTAST.IS", "XTCRT.IS", "XTEKS.IS", "XTM25.IS", "XTMTU.IS", "XTRZM.IS", "XTUMY.IS", "XU030.IS", "XU050.IS", "XU100.IS", "XUHIZ.IS", "XULAS.IS",
            "XUMAL.IS","XUSIN.IS", "XUSRD.IS", "XUTEK.IS", "XUTUM.IS", "XYLDZ.IS", "XYORT.IS", "XYUZO.IS", "YAPRK.IS", "YATAS.IS", "YAYLA.IS", "YBTAS.IS", "YEOTK.IS", "YESIL.IS", "YGGYO.IS", "YGYO.IS",
            "YKBNK.IS", "YKSLN.IS", "YONGA.IS", "YUNSA.IS", "YYAPI.IS", "YYLGD.IS", "Z30EA.IS", "Z30KE.IS", "Z30KP.IS", "ZEDUR.IS", "ZELOT.IS", "ZGOLD.IS", "ZOREN.IS", "ZPBDL.IS", "ZPLIB.IS", "ZPT10.IS",
            "ZPX30.IS", "ZRE20.IS", "ZRGYO.IS", "ZTM15.IS"]

# Değerlendirmelere göre uygun olan hisseleri saklayacağımız liste
uygun_hisseler = []

for hisse in hisseler:
    # Hisse bilgilerini çekiyoruz
    bilgi = yf.Ticker(hisse).info
    # F/K (Fiyat/Kazanç) oranını kontrol ediyoruz. F/K oranı şirketin hisse fiyatıyla hisse başına düşen kârını gösterir.
    if 'forwardPE' in bilgi and bilgi['forwardPE'] < 6:
        # FD/FAVÖK (Firma Değeri/Vergi öncesi kâr) oranını kontrol ediyoruz. FD/FAVÖK oranı net kar kaleminin öngörülmesine yardımcı olur.
        if 'enterpriseToEbitda' in bilgi and 0 < bilgi['enterpriseToEbitda'] < 10:
            #FD/Satış (Firma Değeri/Satış) oranını kontrol ediyoruz. FD/Satış oranı Şirket değerinin satışlara göre oranını belirler.
            if 'enterpriseToRevenue' in bilgi and bilgi['enterpriseToRevenue'] > 2:
                #PD/DD (Piyasa Değeri/Defter Değeri) oranını kontrol ediyoruz. PD/DD oranı ne ölçüde primli/iskontolu olduğunu saptamak için kullanılmaktadır.
                if 'priceToBook' in bilgi and bilgi['priceToBook'] >= 1:
                    uygun_hisseler.append(hisse)

# Sonuçları yazdırıyoruz
print("Mali teknik tablosuna göre alınabilecek olan hisseler:")
for hisse in uygun_hisseler:
    bilgi = yf.Ticker(hisse).info
    forwardPe = bilgi["forwardPE"]
    enterpriseEbitda = bilgi["enterpriseToEbitda"]
    enterpriseRenenue = bilgi["enterpriseToRevenue"]
    priceBook = bilgi["priceToBook"]
    marketOpen = bilgi["regularMarketOpen"]
    print("Hisse:", hisse, "\n", "F/K değeri:", forwardPe, "\n", "FD/FAVÖK değeri:", enterpriseEbitda, "\n", "FD/Satış değeri:", enterpriseRenenue, "\n", "PD/DD değeri:", priceBook, "\n", "Güncel Hisse değeri:", marketOpen)
    print("YTD.\n")
    #print("F/K değeri: ", forwardPe, "\n")
    #print("FD/FAVÖK değeri: ", enterpriseEbitda, "\n")
    #print("FD/Satış değeri: ", enterpriseRenenue, "\n")
    #print("PD/DD değeri: ", priceBook, "\n")
    #print("Güncel Hisse değeri: ", marketOpen, "\n")